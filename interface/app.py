import tkinter as tk

from .componentes import criar_botao_menu
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

def iniciar_interface(cardapio):
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

    tabela_cardapio = criar_tabela_cardapio(area_principal, cardapio)
    atualizar_cardapio(tabela_cardapio, cardapio)

    botao_cadastrar.config(
        command=lambda: cadastrar_item(
            entrada_id, entrada_nome, entrada_preco, tabela_cardapio, cardapio
        )
    )

    janela.mainloop()