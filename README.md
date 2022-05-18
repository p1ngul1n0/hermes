<img alt="hermes-logo" align="left" width="300" height="300" src="https://github.com/p1ngul1n0/badges/blob/main/badges/21.png">
<h1>Hermes</h1>

### Uma ferramenta de OSINT para buscar informações por CPF.
> O Hermes 900 Kochav (Star) é um Veículo aéreo não tripulado (VANT) israelense designado para missões táticas. [...] Tem uma autonomia de mais de 30 horas e pode voar a uma altitude de até 30 mil pés (9.100 m), com os principais objetivos de reconhecimento, vigilância e retransmissão de sinal.
</br></br>

## Uso

#### Buscar por CPF
```python
python blackbird.py -cpf XXXXXXXXXXX
```
#### Buscar com modo stealth ativo
```python
python blackbird.py -cpf XXXXXXXXXXX --stealth
```

#### List supportted sites
```python
python hermes.py --list-sites
```

## Sites suportados <a name="social-networks"></a> ![](https://img.shields.io/badge/12--red)
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
12. Situação Cadastral [NÃO FUNCIONAL]
</details>

## Supersonic speed :rocket:
Blackbird sends async HTTP requests, allowing a lot more speed when discovering user accounts.
