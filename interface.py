import tkinter as tk
from tkinter import ttk, messagebox
import funcoes

# ==========================================
# AÇÕES DO SISTEMA
# ==========================================


def mudar_pagina(titulo_pagina, nome):
    titulo_pagina.config(text=nome)


def cadastrar_item(entrada_id, entrada_nome, entrada_preco, tabela_cardapio):
    id_produto = entrada_id.get().strip()
    nome = entrada_nome.get().strip()
    preco = entrada_preco.get().strip()

    if not id_produto or not nome or not preco:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    if not funcoes.verificar_preco(preco):
        messagebox.showwarning(
            "Preço inválido", "Digite um preço numérico maior que zero."
        )
        return

    if not id_produto.isdigit() or int(id_produto) <= 0:
        messagebox.showwarning(
            "ID inválido", "O ID deve ser um número inteiro positivo."
        )
        return

    for item in tabela_cardapio.get_children():
        dados = tabela_cardapio.item(item, "values")

        if int(dados[0]) == int(id_produto):
            messagebox.showwarning("ID duplicado", "Já existe um produto com esse ID.")
            return

    tabela_cardapio.insert("", "end", values=(id_produto, nome, preco))

    entrada_id.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)


def remover_item(tabela_cardapio):
    selecionados = tabela_cardapio.selection()

    if not selecionados:
        messagebox.showwarning("Atenção", "Selecione um produto para remover.")
        return

    item = selecionados[0]
    dados = tabela_cardapio.item(item, "values")

    confirmar = messagebox.askyesno(
        "Confirmar remoção", f"Deseja remover o produto {dados[1]}?"
    )

    if confirmar:
        tabela_cardapio.delete(item)


# ==========================================
# COMPONENTES REUTILIZÁVEIS
# ==========================================


def criar_botao_menu(menu_lateral, texto, comando):
    botao = tk.Button(
        menu_lateral,
        text=texto,
        command=comando,
        bg="#374151",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        cursor="hand2",
        anchor="w",
        padx=15,
    )

    botao.pack(fill="x", padx=15, pady=5, ipady=10)

    return botao


def criar_campo(frame, texto, coluna, peso):
    label = tk.Label(frame, text=texto, bg="white", fg="#374151", font=("Segoe UI", 10))
    label.grid(row=0, column=coluna, sticky="w")

    entrada = tk.Entry(frame, font=("Segoe UI", 11), relief="solid", bd=1)
    entrada.grid(
        row=1, column=coluna, sticky="ew", padx=(0, 10) if coluna < 2 else 0, ipady=7
    )

    frame.columnconfigure(coluna, weight=peso)

    return entrada


# ==========================================
# CONSTRUÇÃO DA INTERFACE
# ==========================================


def criar_menu_lateral(janela):
    menu_lateral = tk.Frame(janela, bg="#1F2937", width=230)
    menu_lateral.pack(side="left", fill="y")
    menu_lateral.pack_propagate(False)

    titulo_menu = tk.Label(
        menu_lateral,
        text="Sistema de Restaurante",
        bg="#1F2937",
        fg="white",
        font=("Segoe UI Semibold", 13),
    )
    titulo_menu.pack(pady=(30, 40))

    botoes = {}

    for nome in ("Cardápio", "Pedidos", "Cozinha", "Histórico"):
        botoes[nome] = criar_botao_menu(menu_lateral, nome, None)

    return botoes


def criar_area_principal(janela):
    area_principal = tk.Frame(janela, bg="#F3F4F6")
    area_principal.pack(side="left", fill="both", expand=True)

    titulo_pagina = tk.Label(
        area_principal,
        text="Cardápio",
        bg="#F3F4F6",
        fg="#111827",
        font=("Segoe UI Semibold", 24),
    )
    titulo_pagina.pack(anchor="w", padx=35, pady=(30, 10))

    return area_principal, titulo_pagina


def criar_formulario_cadastro(area_principal):
    frame_cadastro = tk.Frame(area_principal, bg="white", padx=25, pady=20)
    frame_cadastro.pack(fill="x", padx=35, pady=20)

    titulo_cadastro = tk.Label(
        frame_cadastro,
        text="Cadastrar produto",
        bg="white",
        fg="#111827",
        font=("Segoe UI Semibold", 15),
    )
    titulo_cadastro.pack(anchor="w", pady=(0, 20))

    frame_campos = tk.Frame(frame_cadastro, bg="white")
    frame_campos.pack(fill="x")

    entrada_id = criar_campo(frame_campos, "ID", 0, 1)
    entrada_nome = criar_campo(frame_campos, "Nome", 1, 3)
    entrada_preco = criar_campo(frame_campos, "Preço", 2, 1)

    botao_cadastrar = tk.Button(
        frame_cadastro,
        text="Cadastrar item",
        bg="#2563EB",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        cursor="hand2",
        padx=20,
        pady=10,
    )
    botao_cadastrar.pack(anchor="e", pady=(20, 0))

    return botao_cadastrar, entrada_id, entrada_nome, entrada_preco


def criar_tabela_cardapio(area_principal):
    frame_cardapio = tk.Frame(area_principal, bg="white", padx=25, pady=20)
    frame_cardapio.pack(fill="both", expand=True, padx=35, pady=(0, 20))

    frame_cabecalho = tk.Frame(frame_cardapio, bg="white")
    frame_cabecalho.pack(fill="x", pady=(0, 20))

    titulo_lista = tk.Label(
        frame_cabecalho,
        text="Itens do cardápio",
        bg="white",
        fg="#111827",
        font=("Segoe UI Semibold", 15),
    )
    titulo_lista.pack(side="left")

    tabela_cardapio = ttk.Treeview(
        frame_cardapio, columns=("id", "nome", "preco"), show="headings"
    )

    tabela_cardapio.heading("id", text="ID")
    tabela_cardapio.heading("nome", text="Nome")
    tabela_cardapio.heading("preco", text="Preço")

    tabela_cardapio.column("id", width=80, anchor="center")
    tabela_cardapio.column("nome", width=300)
    tabela_cardapio.column("preco", width=120, anchor="center")

    botao_remover = tk.Button(
        frame_cabecalho,
        text="Remover selecionado",
        bg="#FEE2E2",
        fg="#991B1B",
        font=("Segoe UI", 10),
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=8,
        command=lambda: remover_item(tabela_cardapio),
    )
    botao_remover.pack(side="right")

    tabela_cardapio.pack(fill="both", expand=True)

    return tabela_cardapio


# ==========================================
# INICIALIZAÇÃO
# ==========================================


def iniciar_interface():
    janela = tk.Tk()

    janela.title("Sistema de Restaurante")
    janela.geometry("1100x700")
    janela.minsize(900, 600)
    janela.configure(bg="#F3F4F6")

    botoes_menu = criar_menu_lateral(janela)

    area_principal, titulo_pagina = criar_area_principal(janela)

    for nome, botao in botoes_menu.items():
        botao.config(command=lambda pagina=nome: mudar_pagina(titulo_pagina, pagina))

    botao_cadastrar, entrada_id, entrada_nome, entrada_preco = (
        criar_formulario_cadastro(area_principal)
    )

    tabela_cardapio = criar_tabela_cardapio(area_principal)

    botao_cadastrar.config(
        command=lambda: cadastrar_item(
            entrada_id, entrada_nome, entrada_preco, tabela_cardapio
        )
    )

    janela.mainloop()


if __name__ == "__main__":
    iniciar_interface()
