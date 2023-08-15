import json

def extract_route(req):
    route = req.split('\n')[0]
    route = route.split(' ')[1][1:]
    return route

def read_file(path):
    file = open(path, mode = 'rb')
    return file.read()

def load_data(file):
    with open("data/"+file, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def load_template(file):
    with open("templates/"+file, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo