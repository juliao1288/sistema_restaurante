import tkinter as tk
from tkinter import messagebox

import funcoes
from .componentes import (
    criar_botao_acao, criar_campo, criar_tabela, limpar_tabela, formatar_moeda,
)
from .integracao import executar_funcao


def lancar_pedido(cardapio, cliente, itens, fila_cozinha, pilha_historico, id_pedido):
   
    cliente = cliente.strip()
    if not cliente:
        raise ValueError("Informe o nome do cliente.")
    if not cardapio:
        raise ValueError("O cardápio está vazio. Cadastre um produto primeiro.")
    if not itens:
        raise ValueError("Adicione pelo menos um produto ao pedido.")
    ids_validos = {produto["id"] for produto in cardapio}
    if any(item not in ids_validos for item in itens):
        raise ValueError("Um produto foi removido do cardápio. Atualize o pedido.")

    # Nome, ID de cada item e opção 1 (continuar) ou 2 (encerrar).
    respostas = [cliente]
    for indice, item in enumerate(itens):
        respostas.extend((item, "2" if indice == len(itens) - 1 else "1"))
    pedido, _ = executar_funcao(
        funcoes.cadastrar_pedido, cardapio, id_pedido, respostas=respostas
    )
    if pedido is None:
        raise ValueError("Não foi possível cadastrar o pedido.")
    fila_cozinha.enqueue(pedido)
    funcoes.registrar_historico(pilha_historico, pedido, "lancar")
    return pedido


def criar_pagina_pedidos(area_principal, cardapio, fila_cozinha, pilha_historico):
    pagina = tk.Frame(area_principal, bg="#F3F4F6", padx=24, pady=12)
    itens_selecionados = []
    proximo_id = 1
    produtos_por_linha = {}
    pedido_por_linha = {}

    def rotulo(texto):
        tk.Label(pagina, text=texto, bg="#F3F4F6", fg="#374151",
                 font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(6, 4))

    entrada_cliente = criar_campo(pagina, "Nome do cliente")
    rotulo("Produtos do cardápio")
    lista_produtos = criar_tabela(pagina, ("id", "nome", "preco"), ("ID", "Produto", "Preço"),
                           (60, 280, 100), "extended")

    def atualizar_resumo():
        limpar_tabela(lista_pedido)
        pedido_por_linha.clear()
        total = 0
        for produto in cardapio:
            quantidade = itens_selecionados.count(produto["id"])
            if quantidade:
                subtotal = quantidade * produto["preco"]
                total += subtotal
                linha = lista_pedido.insert("", "end", values=(
                    produto["nome"], quantidade, formatar_moeda(produto["preco"]), formatar_moeda(subtotal)))
                pedido_por_linha[linha] = produto["id"]
        contador.config(text=f"Itens adicionados: {len(itens_selecionados)}")
        total_label.config(text=f"Total: {formatar_moeda(total)}")

    def atualizar_produtos():
        limpar_tabela(lista_produtos)
        produtos_por_linha.clear()
        for produto in cardapio:
            linha = lista_produtos.insert("", "end", values=(
                produto["id"], produto["nome"], formatar_moeda(produto["preco"])))
            produtos_por_linha[linha] = produto["id"]
        # Remove do rascunho somente os produtos que deixaram de existir.
        ids_validos = {produto["id"] for produto in cardapio}
        itens_selecionados[:] = [item for item in itens_selecionados if item in ids_validos]
        atualizar_resumo()

    def adicionar_produtos():
        selecionados = lista_produtos.selection()
        if not selecionados:
            messagebox.showwarning("Atenção", "Selecione um produto para adicionar.", parent=pagina)
            return
        itens_selecionados.extend(produtos_por_linha[linha] for linha in selecionados)
        lista_produtos.selection_remove(*selecionados)
        atualizar_resumo()

    criar_botao_acao(pagina, "+ Adicionar ao pedido", adicionar_produtos, "#2563EB").pack(anchor="e", pady=6)
    rotulo("Resumo do pedido")
    lista_pedido = criar_tabela(pagina, ("nome", "quantidade", "unitario", "subtotal"),
                         ("Produto", "Qtd.", "Valor unitário", "Subtotal"),
                         (250, 60, 120, 120), "browse")

    def remover_produto():
        selecionados = lista_pedido.selection()
        if not selecionados:
            messagebox.showwarning("Atenção", "Selecione um item do pedido.", parent=pagina)
            return
        itens_selecionados.remove(pedido_por_linha[selecionados[0]])
        atualizar_resumo()

    acoes = tk.Frame(pagina, bg="#F3F4F6")
    acoes.pack(fill="x", pady=6)
    criar_botao_acao(acoes, "Remover 1 unidade", remover_produto, "#DC2626").pack(side="left")
    contador = tk.Label(acoes, bg="#F3F4F6", fg="#374151", font=("Segoe UI", 10))
    contador.pack(side="right")
    rodape = tk.Frame(pagina, bg="#F3F4F6")
    rodape.pack(fill="x", pady=(6, 0))
    total_label = tk.Label(rodape, bg="#F3F4F6", fg="#15803D", font=("Segoe UI", 15, "bold"))
    total_label.pack(side="left")

    def finalizar_pedido():
        nonlocal proximo_id
        try:
            pedido = lancar_pedido(cardapio, entrada_cliente.get(), itens_selecionados,
                                  fila_cozinha, pilha_historico, proximo_id)
        except (ValueError, RuntimeError) as erro:
            messagebox.showwarning("Pedido incompleto", str(erro), parent=pagina)
            return
        proximo_id += 1
        itens_selecionados.clear()
        entrada_cliente.delete(0, tk.END)
        atualizar_resumo()
        messagebox.showinfo("Pedido enviado", f"Pedido #{pedido['id']} enviado à cozinha!", parent=pagina)
        entrada_cliente.focus_set()

    criar_botao_acao(rodape, "Finalizar pedido", finalizar_pedido, "#15803D").pack(side="right")
    pagina.atualizar_produtos = atualizar_produtos
    atualizar_produtos()
    return pagina
