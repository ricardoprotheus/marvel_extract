import hashlib
# import json
import os
from time import time

import requests

''' função para gerar hash md5 necessário para autenticação
conforme instruções disponíveis na documentação da API da Marvel '''


def criar_hash():
    ts = int(time())
    pvt = os.getenv('PVT_KEY')
    apikey = os.getenv('API_KEY')

    to_encode = str(ts) + pvt + apikey

    hash_marvel = hashlib.md5(to_encode.encode()).hexdigest()

    return ts, apikey, hash_marvel


''' função responsável por gerar conexão com API e receber dados
retornando uma lista de listas '''


def conectar_dados(count_offset):
    info_hash = criar_hash()

    params = {
        "offset": count_offset,
        "limit": 100,
        "ts": info_hash[0],
        "apikey": info_hash[1],
        "hash": info_hash[2]
    }

    resp = requests.get('https://gateway.marvel.com:443/v1/public/characters', params)
    return resp.json()['data']['results'], resp.json()['data']['total'], resp.json()['data']['count']


''' função responsável pela paginação dentro da API e entrega
 da lista onde iremos iterar '''


def coletar_dados(starts_in):
    count_offset = starts_in
    resp_test = [0, 0, 1]
    lst_heroes = []
    while resp_test[2] > 0:
        if resp_test[2] == 1:
            resp_test = conectar_dados(count_offset)
            lst_heroes = resp_test[0]
            count_offset += 100
            print(f'Foram coletados {resp_test[2]} resultados.')
        else:
            resp_test = conectar_dados(count_offset)
            lst_heroes = lst_heroes + resp_test[0]
            count_offset += 100
            print(f'Foram coletados {resp_test[2]} resultados.')
    return lst_heroes


''' função responsável por criar lista contendo as informações de cada herói
que será utilizada para gerar um DataFrame '''


def criar_lista_herois(starts_in=0):
    lst_heroes = coletar_dados(starts_in)
    print(type(lst_heroes))
    heroes = []
    for item in lst_heroes:
        heroes.append([
            item['id'],
            item['name'],
            item['description'],
            item['comics']['available'],
            item['series']['available'],
            item['stories']['available'],
            item['events']['available']
        ])
    return heroes
