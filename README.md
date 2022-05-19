<img alt="hermes-logo" align="left" width="300" height="300" src="https://github.com/p1ngul1n0/badges/blob/main/badges/21.png">
<h1>Hermes</h1>

### Uma ferramenta de OSINT para buscar informações por CPF.
> O Hermes 900 Kochav (Star) é um Veículo aéreo não tripulado (VANT) israelense designado para missões táticas. [...] Tem uma autonomia de mais de 30 horas e pode voar a uma altitude de até 30 mil pés (9.100 m), com os principais objetivos de reconhecimento, vigilância e retransmissão de sinal.
</br></br></br></br>

## Uso

#### Buscar por CPF
```python
python hermes.py -cpf XXXXXXXXXXX
```
#### Buscar com modo stealth ativo
Realiza a busca apenas em sites que não causam alguma ação como o envio de e-mails ou SMS.
```python
python hermes.py -cpf XXXXXXXXXXX --stealth
```

#### Listar sites suportados
```python
python hermes.py --list-sites
```

## Sites suportados <a name="social-networks"></a> ![](https://img.shields.io/badge/18--red)
<details>
  <summary></summary>
  
1. Serasa
2. Banco Toyota
3. FGV Conhecimento
4. SEBRAE
5. InfoJobs
6. Hospital das Clínicas USP
7. Universidade Anhembi Morumbi
8. Universidade São Judas
9. Universidade UFABC
10. Claretiano - Centro Universitário
11. UNIP
12. QualiCorp
13. 99 Jobs
14. Natura
15. Correios
16. Eventim
17. Ticket360
18. Ingressos Corinthians
</details>

## Velocidade supersônica :rocket:
As requisições HTTP são enviadas de forma assíncrona, permitindo muito mais velocidade durante a varredura pelo CPF.
