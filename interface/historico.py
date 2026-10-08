import tkinter as tk
from tkinter import messagebox

import funcoes
from .componentes import criar_botao_acao, criar_area_texto, atualizar_texto
from .integracao import executar_funcao


def criar_pagina_historico(area_principal, fila_cozinha, pilha_historico):
    pagina = tk.Frame(area_principal, bg="#F3F4F6", padx=24, pady=12)
    tk.Label(pagina, text="Ações mais recentes primeiro. Desfazer reverte a última ação.",
             bg="#F3F4F6", fg="#374151", font=("Segoe UI", 11)).pack(anchor="w", pady=(0, 12))
    acoes = tk.Frame(pagina, bg="#F3F4F6")
    acoes.pack(fill="x", pady=(0, 12))
    texto = criar_area_texto(pagina)

    def atualizar():
        _, mensagem = executar_funcao(funcoes.visualizar_historico, pilha_historico)
        atualizar_texto(texto, mensagem)

    def desfazer():
        if not pilha_historico.isEmpty() and not messagebox.askyesno(
                "Desfazer última ação", "Deseja reverter a última ação?", parent=pagina):
            return
        _, mensagem = executar_funcao(funcoes.desfazer, pilha_historico, fila_cozinha)
        atualizar()
        messagebox.showinfo("Histórico", mensagem, parent=pagina)

    criar_botao_acao(acoes, texto='Desfazer última ação', comando=desfazer, cor='#DC2626').pack(side="left")
    criar_botao_acao(acoes, texto='Atualizar histórico', comando=atualizar, cor='#E5E7EB', fg='#374151').pack(side="right")
    pagina.atualizar = atualizar
    atualizar()
    return pagina
