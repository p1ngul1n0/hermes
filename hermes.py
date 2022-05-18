import time
from bs4 import BeautifulSoup
import json
import aiohttp
import asyncio
import warnings
import argparse
from colorama import init, Fore
from datetime import datetime

init()

file = open('data.json')
searchData = json.load(file)

warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser()
parser.add_argument('-cpf', action = 'store', dest = 'cpf',
                           required = False,
                           help = 'CPF alvo.')
parser.add_argument('--stealth',action='store_true',help='Busca CPF apenas em sites que não causam alguma ação como envio de e-mails ou SMS.')
arguments = parser.parse_args()

proxy = "http://127.0.0.1:8080"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0"
}

async def findUsername(cpf):
    start_time = time.time()
    timeout = aiohttp.ClientTimeout(total=20)
    
    print (f"{Fore.LIGHTYELLOW_EX}[!] Buscando o CPF '{cpf}' em {len(searchData['sites'])} sites \033[0m")
    if arguments.stealth:
        print (f'{Fore.LIGHTYELLOW_EX}[-] MODO STEALTH ATIVO 🤫 \033[0m')
    async with aiohttp.ClientSession(timeout=timeout) as session:
            tasks = []
            for u in searchData["sites"]:
                task = asyncio.ensure_future(makeRequest(session,u,cpf))
                tasks.append(task)

            results = await asyncio.gather(*tasks)
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print (f"{Fore.LIGHTYELLOW_EX}[!] Busca completa em {round(time.time() - start_time,1)} seconds\033[0m")

async def makeRequest(session,u,cpf):
    url = u["url"].format(cpf=cpf)
    jsonBody = None
    formData = None
    if 'headers' in u:
        headers.update(eval(u['headers']))
    if 'json' in u:
        jsonBody = u['json'].format(cpf=cpf)
        jsonBody = json.loads(jsonBody)
    if 'form' in u:
        formData = u['form'].format(cpf=cpf)
    try:
        if arguments.stealth and u['silent'] == False:
            print (f'{Fore.CYAN}[+] - {u["app"]} não executado pois modo stealth está ativo - {url} \033[0m')
        else:
            async with session.request(u["method"],url,json=jsonBody,data=formData, proxy=proxy,headers=headers, ssl=False) as response:
                responseContent = await response.text()
                
                if 'content-type' in response.headers and "application/json" in response.headers["Content-Type"]:
                    jsonData = await response.json()
                else:
                    soup = BeautifulSoup(responseContent, 'html.parser')
                
                if eval(u["valid"]):
                    print (f'{Fore.LIGHTGREEN_EX}[+] - {u["app"]} conta identificada - {url} [{response.status} {response.reason}]\033[0m')
                    return ({"app": u['app'], "url": url, "error": False, "found": True})
                elif eval(u["error"]):
                    print (f'{Fore.RED}[+] - {u["app"]} erro na consulta - {url} [{response.status} {response.reason}]\033[0m')
                    return ({"app": u['app'], "url": url, "error": True, "found": False})
                else:
                    print (f'[-] - {u["app"]} conta não identificada - {url} [{response.status} {response.reason}]')
                    return ({"app": u['app'], "url": url, "error": False, "found": False})
    except Exception as e:
        print (f'{Fore.RED}[X] - {u["app"]} erro na consulta ({repr(e)}) - {url}')
        return ({"app": u['app'], "url": url, "error":True, "found": False})  
         

if arguments.cpf:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(findUsername(arguments.cpf))   