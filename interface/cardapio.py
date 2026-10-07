import tkinter as tk
from tkinter import ttk, messagebox

import funcoes
from .componentes import criar_campo


def cadastrar_item(entrada_id, entrada_nome, entrada_preco, tabela_cardapio, cardapio):
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

    for produto in cardapio:
        if produto["id"] == int(id_produto):
            messagebox.showwarning("ID duplicado", "Já existe um produto com esse ID.")
            return

    produto = funcoes.cadastrar_item(
        int(id_produto), nome, float(preco.replace(",", "."))
    )

    cardapio.append(produto)

    atualizar_cardapio(tabela_cardapio, cardapio)

    entrada_id.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)


def remover_item(tabela_cardapio, cardapio):
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
        id_produto = int(dados[0])

        if funcoes.remover_item(cardapio, id_produto):
            atualizar_cardapio(tabela_cardapio, cardapio)


def atualizar_cardapio(tabela_cardapio, cardapio):
    for item in tabela_cardapio.get_children():
        tabela_cardapio.delete(item)

    for produto in cardapio:
        tabela_cardapio.insert(
            "", "end", values=(produto["id"], produto["nome"], produto["preco"])
        )

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


def criar_tabela_cardapio(area_principal, cardapio):
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
        command=lambda: remover_item(tabela_cardapio, cardapio),
    )
    botao_remover.pack(side="right")

    tabela_cardapio.pack(fill="both", expand=True)

    return tabela_cardapio