import tkinter as tk
import funcoes

from .pedidos import criar_pagina_pedidos
from .cozinha import criar_pagina_cozinha
from .historico import criar_pagina_historico
from .integracao import executar_funcao
from .componentes import (
    criar_botao_menu, criar_botao_acao, criar_area_texto, atualizar_texto,
)
from .cardapio import (
    criar_formulario_cadastro,
    criar_tabela_cardapio,
    atualizar_cardapio,
    cadastrar_item,
)


def mudar_pagina(titulo_pagina, nome):
    titulo_pagina.config(text=nome)


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


def iniciar_interface(cardapio, fila_cozinha, pilha_historico):
    # Usa as mesmas estruturas criadas no main.
    janela = tk.Tk()

    janela.title("Sistema de Restaurante")
    janela.geometry("1100x700")
    janela.minsize(900, 600)
    janela.configure(bg="#F3F4F6")

    botoes_menu = criar_menu_lateral(janela)

    area_principal, titulo_pagina = criar_area_principal(janela)
    pagina_pedidos = criar_pagina_pedidos(
        area_principal, cardapio, fila_cozinha, pilha_historico
    )

    botao_cadastrar, entrada_id, entrada_nome, entrada_preco = (
        criar_formulario_cadastro(area_principal)
    )

    tabela_cardapio = criar_tabela_cardapio(area_principal, cardapio)
    atualizar_cardapio(tabela_cardapio, cardapio)

    def visualizar_cardapio():
        _, mensagem = executar_funcao(funcoes.visualizar_cardapio, cardapio)
        resumo = tk.Toplevel(janela)
        resumo.title("Cardápio")
        resumo.geometry("600x400")
        texto = criar_area_texto(resumo, padx=16, pady=16)
        atualizar_texto(texto, mensagem)

    criar_botao_acao(area_principal, texto='Ver cardápio completo', comando=visualizar_cardapio, cor='#2563EB').pack(anchor="e", padx=24, pady=(0, 12))
    componentes_cardapio = [
        (componente, componente.pack_info())
        for componente in area_principal.winfo_children()
        if componente not in (titulo_pagina, pagina_pedidos)
    ]
    pagina_cozinha = criar_pagina_cozinha(area_principal, fila_cozinha, pilha_historico)
    pagina_historico = criar_pagina_historico(area_principal, fila_cozinha, pilha_historico)

    def ocultar_paginas():
        for componente in area_principal.winfo_children():
            if componente != titulo_pagina:
                componente.pack_forget()

    paginas = {
        "Pedidos": (pagina_pedidos, pagina_pedidos.atualizar_produtos),
        "Cozinha": (pagina_cozinha, pagina_cozinha.atualizar),
        "Histórico": (pagina_historico, pagina_historico.atualizar),
    }

    def abrir_pagina(nome):
        ocultar_paginas()
        mudar_pagina(titulo_pagina, nome)
        if nome == "Cardápio":
            atualizar_cardapio(tabela_cardapio, cardapio)
            for componente, configuracao in componentes_cardapio:
                componente.pack(**configuracao)
        else:
            pagina, atualizar = paginas[nome]
            atualizar()
            pagina.pack(fill="both", expand=True)

    botao_cadastrar.config(
        command=lambda: cadastrar_item(
            entrada_id, entrada_nome, entrada_preco, tabela_cardapio, cardapio
        )
    )

    for nome, botao in botoes_menu.items():
        botao.config(command=lambda pagina=nome: abrir_pagina(pagina))

    janela.mainloop()
