import tkinter as tk
from tkinter import messagebox

import funcoes
from .componentes import (
    criar_campo, criar_botao_acao, criar_tabela, limpar_tabela, formatar_moeda,
)


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

    for entrada in (entrada_id, entrada_nome, entrada_preco):
        entrada.delete(0, tk.END)


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
    limpar_tabela(tabela_cardapio)

    for produto in cardapio:
        tabela_cardapio.insert(
            "", "end", values=(produto["id"], produto["nome"],
                                 formatar_moeda(produto["preco"]))
        )

def criar_formulario_cadastro(area_principal):
    frame_cadastro = tk.Frame(area_principal, bg="#F3F4F6", pady=12)
    frame_cadastro.pack(fill="x", padx=24)

    titulo_cadastro = tk.Label(
        frame_cadastro,
        text="Cadastrar produto",
        bg="#F3F4F6",
        fg="#374151",
        font=("Segoe UI", 11, "bold"),
    )
    titulo_cadastro.pack(anchor="w", pady=(0, 8))

    frame_campos = tk.Frame(frame_cadastro, bg="#F3F4F6")
    frame_campos.pack(fill="x")

    entrada_id = criar_campo(frame_campos, "ID", 0, 1)
    entrada_nome = criar_campo(frame_campos, "Nome", 1, 3)
    entrada_preco = criar_campo(frame_campos, "Preço", 2, 1)
    botao_cadastrar = criar_botao_acao(frame_cadastro, texto='Cadastrar item', cor='#2563EB', cor_ativa='#1D4ED8')
    botao_cadastrar.pack(anchor="e", pady=(8, 0))

    return botao_cadastrar, entrada_id, entrada_nome, entrada_preco


def criar_tabela_cardapio(area_principal, cardapio):
    frame_cardapio = tk.Frame(area_principal, bg="#F3F4F6")
    frame_cardapio.pack(fill="both", expand=True, padx=24, pady=(0, 12))

    frame_cabecalho = tk.Frame(frame_cardapio, bg="#F3F4F6")
    frame_cabecalho.pack(fill="x", pady=(0, 8))

    titulo_lista = tk.Label(
        frame_cabecalho,
        text="Itens do cardápio",
        bg="#F3F4F6",
        fg="#374151",
        font=("Segoe UI", 11, "bold"),
    )
    titulo_lista.pack(side="left")

    tabela_cardapio = criar_tabela(
        frame_cardapio, ("id", "nome", "preco"), ("ID", "Produto", "Preço"),
        (80, 300, 120), altura=5
    )

    botao_remover = criar_botao_acao(frame_cabecalho, texto='Remover selecionado', cor='#DC2626', cor_ativa='#B91C1C', comando=lambda: remover_item(tabela_cardapio, cardapio))
    botao_remover.pack(side="right")

    return tabela_cardapio
