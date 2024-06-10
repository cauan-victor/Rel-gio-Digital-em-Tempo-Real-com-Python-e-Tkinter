import tkinter as tk
from time import strftime

# Função para atualizar o tempo
def update_time():
    current_time = strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Configuração da janela principal
root = tk.Tk()
root.title('Relógio em Tempo Real')

# Configuração do rótulo do relógio
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(anchor='center')

# Inicializa a atualização do tempo
update_time()

# Inicia a aplicação
root.mainloop()
