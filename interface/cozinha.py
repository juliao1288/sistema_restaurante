import tkinter as tk
from tkinter import messagebox

import funcoes
from .componentes import criar_botao_acao, criar_area_texto, atualizar_texto
from .integracao import executar_funcao


def atender_proximo(fila_cozinha, pilha_historico, confirmar):
    pedido = fila_cozinha.front()
    realizado, mensagem = executar_funcao(
        funcoes.realizar_pedido, pedido, respostas=("1" if confirmar else "2",)
    )
    if realizado:
        fila_cozinha.dequeue()
        funcoes.registrar_historico(pilha_historico, pedido, "atender")
    return realizado, mensagem


def criar_pagina_cozinha(area_principal, fila_cozinha, pilha_historico):
    pagina = tk.Frame(area_principal, bg="#F3F4F6", padx=24, pady=12)
    tk.Label(pagina, text="Pedidos aguardando preparo, na ordem de chegada.",
             bg="#F3F4F6", fg="#374151", font=("Segoe UI", 11)).pack(anchor="w", pady=(0, 12))
    acoes = tk.Frame(pagina, bg="#F3F4F6")
    acoes.pack(fill="x", pady=(0, 12))
    texto = criar_area_texto(pagina)

    def atualizar():
        _, mensagem = executar_funcao(funcoes.visualizar_fila, fila_cozinha)
        atualizar_texto(texto, mensagem)

    def atender():
        pedido = fila_cozinha.front()
        confirmar = False
        if pedido:
            confirmar = messagebox.askyesno(
                "Atender próximo pedido",
                f"Concluir o pedido #{pedido['id']} de {pedido['cliente']}?", parent=pagina)
        realizado, mensagem = atender_proximo(fila_cozinha, pilha_historico, confirmar)
        if realizado:
            messagebox.showinfo("Pedido realizado", "Pedido concluído e registrado no histórico.", parent=pagina)
        elif not pedido:
            messagebox.showinfo("Cozinha", mensagem, parent=pagina)
        atualizar()

    criar_botao_acao(acoes, texto='Atender próximo pedido', comando=atender, cor='#15803D').pack(side="left")
    criar_botao_acao(acoes, texto='Atualizar fila', comando=atualizar, cor='#E5E7EB', fg='#374151').pack(side="right")
    pagina.atualizar = atualizar
    atualizar()
    return pagina
