import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Funções do aplicativo ---

def adicionar_tarefa():
    # Coleta os dados e remove espaços em branco extras
    tarefa = entrada_tarefa.get().strip()
    categoria = combo_categoria.get()

    if tarefa and categoria and categoria != "Escolha uma categoria":
        # Adiciona na lista com um formato mais limpo
        item_formatado = f"{categoria} | {tarefa}"
        listbox_tarefas.insert(tk.END, item_formatado)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Preencha a tarefa e escolha uma categoria válida!")

def remover_tarefa():
    selecionado = listbox_tarefas.curselection()
    if selecionado:
        listbox_tarefas.delete(selecionado)
    else:
        messagebox.showwarning("Aviso", "Selecione uma tarefa na lista para remover!")

def limpar_tudo():
    # Pergunta antes de apagar tudo para evitar acidentes
    if messagebox.askyesno("Confirmar", "Deseja apagar TODAS as tarefas?"):
        listbox_tarefas.delete(0, tk.END)

# --- Configuração Principal (Dark Mode) ---
janela = tk.Tk()
janela.title("⚡ TaskMaster Pro")
janela.geometry("450x580")

# Paleta de Cores Modernas
BG_COLOR = "#1E1E2E" # Fundo Escuro
FG_COLOR = "#CDD6F4" # Texto Claro
ACCENT_COLOR = "#89B4FA" # Azul Destaque
INPUT_BG = "#313244" # Fundo dos inputs
janela.config(bg=BG_COLOR, padx=25, pady=25)

# Fontes
fonte_padrao = ("Segoe UI", 11)
fonte_titulo = ("Segoe UI", 14, "bold")

# Configurando o tema do Combobox (para tirar o visual antigo)
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground=INPUT_BG, background=INPUT_BG, foreground="white", borderwidth=0)

# --- Layout da Interface ---

# Título
tk.Label(janela, text="🚀 Gerenciador de Tarefas", font=fonte_titulo, bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=(0, 15))

# Entrada de Texto
tk.Label(janela, text="Qual é a missão?", font=fonte_padrao, bg=BG_COLOR, fg=FG_COLOR).pack(anchor="w")
entrada_tarefa = tk.Entry(janela, font=fonte_padrao, bg=INPUT_BG, fg="white", insertbackground="white", relief="flat")
entrada_tarefa.pack(fill="x", pady=5, ipady=6) # ipady deixa o campo mais "gordinho"

# Combobox com Emojis
tk.Label(janela, text="Categoria:", font=fonte_padrao, bg=BG_COLOR, fg=FG_COLOR).pack(anchor="w", pady=(10, 0))
categorias_opcoes = ["💻 Trabalho", "📚 Estudos", "🏠 Casa", "🎮 Lazer", "🚨 Urgente"]
combo_categoria = ttk.Combobox(janela, values=categorias_opcoes, state="readonly", font=fonte_padrao, style="TCombobox")
combo_categoria.pack(fill="x", pady=5, ipady=4)
combo_categoria.set("Escolha uma categoria")

# Botão Adicionar (Verde Pastel)
btn_add = tk.Button(janela, text="➕ Adicionar Tarefa", font=("Segoe UI", 11, "bold"), bg="#A6E3A1", fg="#11111B", activebackground="#94E2D5", relief="flat", command=adicionar_tarefa)
btn_add.pack(fill="x", pady=20, ipady=6)

# Título da Lista
tk.Label(janela, text="📋 Minhas Tarefas", font=fonte_titulo, bg=BG_COLOR, fg=ACCENT_COLOR).pack(anchor="w")

# Container da Lista e Scrollbar
frame_lista = tk.Frame(janela, bg=BG_COLOR)
frame_lista.pack(fill="both", expand=True, pady=5)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

# Listbox Estilizado
listbox_tarefas = tk.Listbox(frame_lista, font=fonte_padrao, bg=INPUT_BG, fg="white", selectbackground=ACCENT_COLOR, selectforeground="#11111B", relief="flat", highlightthickness=0, yscrollcommand=scrollbar.set)
listbox_tarefas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox_tarefas.yview)

# Container dos Botões Inferiores
frame_botoes = tk.Frame(janela, bg=BG_COLOR)
frame_botoes.pack(fill="x", pady=(15, 0))

# Botão Remover (Vermelho Pastel)
btn_remover = tk.Button(frame_botoes, text="❌ Remover", font=fonte_padrao, bg="#F38BA8", fg="#11111B", relief="flat", command=remover_tarefa)
btn_remover.pack(side="left", expand=True, fill="x", padx=(0, 5), ipady=4)

# Botão Limpar Tudo (Laranja Pastel)
btn_limpar = tk.Button(frame_botoes, text="🗑️ Limpar Tudo", font=fonte_padrao, bg="#FAB387", fg="#11111B", relief="flat", command=limpar_tudo)
btn_limpar.pack(side="right", expand=True, fill="x", padx=(5, 0), ipady=4)

# Inicia o aplicativo
janela.mainloop()