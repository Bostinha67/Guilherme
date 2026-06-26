import tkinter as tk
from tkinter import ttk

class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações principais da janela
        self.title("Interface de Busca")
        self.geometry("800x600")
        self.configure(bg="#ffffff")
        self.minsize(400, 300) # Tamanho mínimo para manter a responsividade
        
        # Container principal centralizado (Responsividade)
        # Usando place com relx=0.5 e rely=0.5 para manter sempre no centro
        main_frame = tk.Frame(self, bg="#ffffff")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # --- Título (Estilo Google com letras coloridas) ---
        title_frame = tk.Frame(main_frame, bg="#ffffff")
        title_frame.pack(pady=(0, 30))
        
        # Cores inspiradas no Google
        colors = ["#4285F4", "#EA4335", "#FBBC05", "#4285F4", "#34A853", "#EA4335", "#FBBC05", "#4285F4","#4285F4", "#EA4335", "#FBBC05", "#4285F4", "#34A853", "#EA4335", "#FBBC05", "#4285F4","#4285F4", "#EA4335"]
        text = "Femboy"
        
        for i, char in enumerate(text):
            tk.Label(title_frame, text=char, font=("Arial", 56, "bold"), fg=colors[i], bg="#ffffff").pack(side="left")
            
        # --- Barra de Pesquisa ---
        # Frame para simular a borda arredondada/destacada da barra de pesquisa
        search_frame = tk.Frame(main_frame, bg="#ffffff", bd=1, relief="solid", highlightbackground="#dfe1e5", highlightthickness=1)
        search_frame.pack(ipadx=10, ipady=5, fill="x")
        
        # Ícone de lupa (usando emoji/caractere unicode)
        search_icon = tk.Label(search_frame, text="🔍", bg="#ffffff", font=("Segoe UI Emoji", 14), fg="#9aa0a6")
        search_icon.pack(side="left", padx=(10, 5))
        
        # Entrada de texto (Entry)
        self.placeholder_text = " Qual seria sua duvida?"
        self.search_var = tk.StringVar()
        
        self.search_entry = tk.Entry(
            search_frame, 
            textvariable=self.search_var,
            font=("Arial", 14), 
            width=50, 
            bd=0, 
            bg="#ffffff",
            fg="grey",
            highlightthickness=0
        )
        self.search_entry.pack(side="left", padx=5, pady=5)
        self.search_entry.insert(0, self.placeholder_text)
        
        # Ícone de microfone (decorativo)
        mic_icon = tk.Label(search_frame, text="ᯓ ✈︎ ▌ ▌", bg="#ffffff", font=("Segoe UI Emoji", 14))
        mic_icon.pack(side="right", padx=(5, 10))
        
        # Eventos para o placeholder (comportamento de clicar e sumir o texto)
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.bind("<Return>", self.perform_search)
        
        # --- Botões ---
        buttons_frame = tk.Frame(main_frame, bg="#ffffff")
        buttons_frame.pack(pady=30)
        
        search_button = tk.Button(
            buttons_frame, 
            text="final da copa do mundo! clica aqui", 
            font=("Arial", 11),
            bg="#f8f9fa",
            fg="#3c4043",
            relief="flat",
            activebackground="#e8eaed",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.perform_search
        )
        search_button.pack(side="left", padx=10)
        
        feeling_lucky_button = tk.Button(
            buttons_frame, 
            text="Neymar bate em robinhojr? veja o caso", 
            font=("Arial", 11),
            bg="#f8f9fa",
            fg="#3c4043",
            relief="flat",
            activebackground="#e8eaed",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        feeling_lucky_button.pack(side="left", padx=10)

    def on_entry_click(self, event):
        """Remove o texto de placeholder quando a barra recebe foco."""
        if self.search_entry.get() == self.placeholder_text:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg="black")

    def on_focus_out(self, event):
        """Adiciona o texto de placeholder quando a barra perde foco e está vazia."""
        if self.search_entry.get() == "":
            self.search_entry.insert(0, self.placeholder_text)
            self.search_entry.config(fg="grey")

    def perform_search(self, event=None):
        """Função que simula a ação de busca."""
        query = self.search_entry.get()
        if query and query != self.placeholder_text:
            print(f"Buscando por: {query}")
            # Aqui você pode adicionar a lógica real de busca, 
            # como abrir o navegador ou fazer uma requisição API.

if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()
