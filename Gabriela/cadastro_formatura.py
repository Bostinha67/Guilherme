import tkinter as tk
from tkinter import ttk, messagebox

class AppFormatura(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Sistema de Cadastro - Formatura")
        self.geometry("900x650")
        self.configure(bg="#0D1117") # Fundo escuro tecnológico (estilo GitHub Dark)
        self.resizable(False, False)
        
        # Paleta de Cores (Tecnológica / Neon)
        self.bg_color = "#0D1117"
        self.fg_color = "#FFFFFF"
        self.accent_color = "#00E5FF" # Ciano Neon
        self.input_bg = "#161B22"
        self.border_color = "#30363D"
        self.text_muted = "#8B949E"
        
        # Configuração de Estilo do ttk (para o Combobox)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", 
                        fieldbackground=self.input_bg, 
                        background=self.bg_color,
                        foreground=self.fg_color,
                        bordercolor=self.border_color,
                        arrowcolor=self.accent_color,
                        padding=5)
                        
        self.create_widgets()

    def create_widgets(self):
        # --- CABEÇALHO ---
        header_frame = tk.Frame(self, bg=self.bg_color)
        header_frame.pack(fill="x", pady=(50, 30))
        
        # Efeito de texto espaçado
        title = tk.Label(header_frame, text="S I S T E M A   D E   A C E S S O", 
                         font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg=self.accent_color)
        title.pack()
        
        subtitle = tk.Label(header_frame, text="CADASTRO DE CONVIDADOS", 
                            font=("Segoe UI", 32, "bold"), bg=self.bg_color, fg=self.fg_color)
        subtitle.pack()

        # Linha decorativa
        separator = tk.Frame(header_frame, bg=self.accent_color, height=2, width=100)
        separator.pack(pady=(10, 0))

        # --- FORMULÁRIO ---
        form_frame = tk.Frame(self, bg=self.bg_color)
        form_frame.pack(expand=True, fill="both", padx=120, pady=10)
        
        # Função auxiliar para criar inputs padronizados
        def create_input(parent, label_text, row, col, width=30):
            lbl = tk.Label(parent, text=label_text, font=("Segoe UI", 10, "bold"), bg=self.bg_color, fg=self.text_muted)
            lbl.grid(row=row, column=col, sticky="w", pady=(15, 0), padx=15)
            
            # Campo de entrada
            entry = tk.Entry(parent, font=("Segoe UI", 13), bg=self.input_bg, fg=self.fg_color, 
                             insertbackground=self.accent_color, relief="flat", width=width,
                             highlightthickness=1, highlightbackground=self.border_color, highlightcolor=self.accent_color)
            entry.grid(row=row+1, column=col, sticky="we", pady=(5, 5), padx=15, ipady=8)
            return entry
            
        self.ent_nome = create_input(form_frame, "NOME COMPLETO", 0, 0, width=35)
        self.ent_cpf = create_input(form_frame, "CPF / DOCUMENTO", 0, 1, width=25)
        
        self.ent_email = create_input(form_frame, "E-MAIL", 2, 0, width=35)
        self.ent_telefone = create_input(form_frame, "TELEFONE", 2, 1, width=25)
        
        # Tipo de Ingresso
        lbl_tipo = tk.Label(form_frame, text="TIPO DE CONVITE", font=("Segoe UI", 10, "bold"), bg=self.bg_color, fg=self.text_muted)
        lbl_tipo.grid(row=4, column=0, sticky="w", pady=(15, 0), padx=15)
        
        self.combo_tipo = ttk.Combobox(form_frame, values=["Pista / Padrão", "VIP", "Mesa Premium", "Camarote"], 
                                       font=("Segoe UI", 12), state="readonly")
        self.combo_tipo.grid(row=5, column=0, sticky="we", pady=(5, 5), padx=15)
        self.combo_tipo.set("Pista / Padrão")

        # Configuração das cores do menu dropdown do Combobox
        self.option_add('*TCombobox*Listbox.font', ("Segoe UI", 12))
        self.option_add('*TCombobox*Listbox.background', self.input_bg)
        self.option_add('*TCombobox*Listbox.foreground', self.fg_color)
        self.option_add('*TCombobox*Listbox.selectBackground', self.accent_color)
        self.option_add('*TCombobox*Listbox.selectForeground', "#000000")
        
        # Configurar grid
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)
        
        # --- BOTÃO E STATUS ---
        btn_frame = tk.Frame(self, bg=self.bg_color)
        btn_frame.pack(fill="x", pady=(20, 50))
        
        # Efeitos de Hover no botão
        def on_enter(e):
            self.btn_cadastrar.config(bg="#00B3CC", fg="#000000")
            
        def on_leave(e):
            self.btn_cadastrar.config(bg=self.accent_color, fg="#000000")

        self.btn_cadastrar = tk.Button(btn_frame, text="CADASTRAR CONVIDADO", font=("Segoe UI", 12, "bold"), 
                                       bg=self.accent_color, fg="#000000", activebackground="#00B3CC", activeforeground="#000000",
                                       relief="flat", cursor="hand2", command=self.cadastrar)
        self.btn_cadastrar.pack(ipady=12, ipadx=50)
        
        self.btn_cadastrar.bind("<Enter>", on_enter)
        self.btn_cadastrar.bind("<Leave>", on_leave)

        # Label de Status
        self.status_lbl = tk.Label(self, text="", font=("Segoe UI", 11), bg=self.bg_color, fg=self.accent_color)
        self.status_lbl.pack(pady=(10, 0))

    def cadastrar(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        email = self.ent_email.get()
        tipo = self.combo_tipo.get()
        
        if not nome or not cpf:
            messagebox.showwarning("Atenção", "Os campos Nome e CPF são obrigatórios!", parent=self)
            return
            
        # Simulação de carregamento / cadastro
        self.status_lbl.config(text=f"Processando...", fg=self.fg_color)
        self.update()
        self.after(500) # delay de 500ms
        
        self.status_lbl.config(text=f"✓ Sucesso! Acesso {tipo} liberado para {nome.split()[0]}.", fg=self.accent_color)
        
        # Limpar campos
        self.ent_nome.delete(0, tk.END)
        self.ent_cpf.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        self.ent_telefone.delete(0, tk.END)
        self.combo_tipo.set("Pista / Padrão")
        self.ent_nome.focus()

if __name__ == "__main__":
    app = AppFormatura()
    app.mainloop()
