import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


def criar_botao_acao(frame, texto, comando=None, cor="#2563EB", cor_ativa=None, **opcoes):
    """Cria o botão; cada aba define sua ação e posição."""
    configuracao = dict(fg="white", activeforeground="white",
                        font=("Segoe UI", 10, "bold"), relief="flat",
                        cursor="hand2", padx=14, pady=7)
    configuracao.update(opcoes)
    return tk.Button(frame, text=texto, command=comando, bg=cor,
                     activebackground=cor_ativa or cor, **configuracao)


def criar_botao_menu(menu_lateral, texto, comando):
    botao = criar_botao_acao(
        menu_lateral,
        texto=texto,
        comando=comando,
        cor="#374151",
        font=("Segoe UI", 12, "bold"),
        anchor="w",
        padx=15,
        pady=0,
    )

    botao.pack(fill="x", padx=15, pady=5, ipady=10)

    return botao


def criar_campo(frame, texto, coluna=None, peso=1):
    label = tk.Label(
        frame, text=texto, bg=frame.cget("bg"),
        fg="#374151", font=("Segoe UI", 10, "bold")
    )
    entrada = ttk.Entry(frame, font=("Segoe UI", 11))
    if coluna is None:
        label.pack(anchor="w", pady=(6, 4))
        entrada.pack(fill="x", pady=(0, 8))
    else:
        label.grid(row=0, column=coluna, sticky="w", pady=(0, 5))
        entrada.grid(row=1, column=coluna, sticky="ew",
                     padx=(0, 10) if coluna < 2 else 0, ipady=4)
        frame.columnconfigure(coluna, weight=peso)

    return entrada


def formatar_moeda(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def limpar_tabela(tabela):
    linhas = tabela.get_children()
    if linhas:
        tabela.delete(*linhas)


def criar_tabela(frame, colunas, titulos, larguras, selecao="browse", altura=3):
    """Monta a tabela com cabeçalhos e rolagem vertical."""
    moldura = tk.Frame(frame, bg="white")
    moldura.pack(fill="both", expand=True)
    tabela = ttk.Treeview(moldura, columns=colunas, show="headings",
                         selectmode=selecao, height=altura)
    for coluna, titulo, largura in zip(colunas, titulos, larguras):
        tabela.heading(coluna, text=titulo)
        tabela.column(coluna, width=largura, minwidth=45,
                      anchor="w" if coluna == "nome" else "center")
    barra = ttk.Scrollbar(moldura, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=barra.set)
    barra.pack(side="right", fill="y")
    tabela.pack(side="left", fill="both", expand=True)
    return tabela


def criar_area_texto(frame, **posicao):
    texto = ScrolledText(frame, font=("Consolas", 11), wrap="word", relief="flat")
    texto.pack(fill="both", expand=True, **posicao)
    texto.config(state="disabled")
    return texto


def atualizar_texto(texto, mensagem):
    texto.config(state="normal")
    texto.delete("1.0", tk.END)
    texto.insert("1.0", mensagem)
    texto.config(state="disabled")
