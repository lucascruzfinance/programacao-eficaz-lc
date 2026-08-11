import json

def load_data(nome_arquivo):
    # Constrói o caminho completo: "static/data/" + nome do arquivo
    caminho = f"static/data/{nome_arquivo}"
    
    # Abre o arquivo em modo leitura ("r" = read)
    arquivo = open(caminho, "r", encoding="utf-8")
    
    # json.load() lê o arquivo e transforma em dicionário Python
    dados = json.load(arquivo)
    
    # Fecha o arquivo
    arquivo.close()
    
    # Devolve o dicionário
    return dados

def load_template(nome_arquivo):
    # Constrói o caminho completo: "static/templates/" + nome do arquivo
    caminho = f"static/templates/{nome_arquivo}"
    
    # Abre o arquivo em modo leitura ("r" = read)
    arquivo = open(caminho, "r", encoding="utf-8")
    
    # Lê todo o conteúdo do arquivo
    conteudo = arquivo.read()
    
    # Fecha o arquivo
    arquivo.close()
    
    # Devolve o conteúdo como string
    return conteudo