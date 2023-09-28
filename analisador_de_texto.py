import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import nltk
from nltk.tokenize import sent_tokenize
import re

nltk.download("punkt")

def analisar_texto():
    texto = texto_entrada.get("1.0", "end-1c")  # Obter o texto da entrada

    # Remover vírgulas antes de tokenizar
    texto_sem_virgula = re.sub(r'[^\w\s]', '', texto)

    num_caracteres = len(texto_sem_virgula)
    frases = sent_tokenize(texto)
    num_frases = len(frases)

    resultado.config(text=f"Número de caracteres: {num_caracteres}\nNúmero de frases: {num_frases}")

def salvar_arquivo():
    texto = texto_entrada.get("1.0", "end-1c")
    num_caracteres = resultado.cget("text").split(": ")[1].split("\n")[0]
    num_frases = resultado.cget("text").split(": ")[2]

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    
    if file_path:
        with open(file_path, "w") as file:
            file.write(f"Número de caracteres: {num_caracteres}\nNúmero de frases: {num_frases}\n\n")
            file.write(texto)

# Cria uma janela
window = tk.Tk()
window.title("Analisador de Texto")

# Cria uma área de texto para inserir o texto
texto_entrada = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
texto_entrada.pack(padx=10, pady=10)

# Cria um botão para iniciar a análise
analisar_button = tk.Button(window, text="Analisar Texto", command=analisar_texto)
analisar_button.pack()

# Cria um botão para salvar o texto
salvar_button = tk.Button(window, text="Salvar Arquivo", command=salvar_arquivo)
salvar_button.pack()

# Cria um rótulo para exibir os resultados
resultado = tk.Label(window, text="")
resultado.pack()

# Inicia o loop principal
window.mainloop()
