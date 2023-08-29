import json
from pathlib import Path

def extract_route(req):
    route = req.split('\n')[0]
    route = route.split(' ')[1][1:]
    return route

def read_file(path):
    file = open(path, mode = 'rb')
    return file.read()

def load_data(file):
    caminho = Path() / 'data' / file
    with open(caminho, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def load_template(file):
    caminho = Path() / 'templates' / file
    with open(caminho, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def add_in_file(dic):
    caminho = Path() / 'data' / 'notes.json'
    with open(caminho,'r') as r:
        data = json.load(r)
    data.append(dic)
    with open(caminho, 'w') as f:
        json.dump(data,f)

def build_response(body='', code=200, reason='OK', headers=''):
    httpv = 'HTTP/1.1'
    response = httpv+' '+str(code)+' '+reason+'\n\n'+body
    if len(headers)>0:
        response = httpv+' '+str(code)+' '+reason+'\n'+headers+'\n\n'+body
    return response.encode()