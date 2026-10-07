import tkinter as tk


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
    label = tk.Label(
        frame, text=texto, bg="white",
        fg="#374151", font=("Segoe UI", 10)
    )
    label.grid(row=0, column=coluna, sticky="w")

    entrada = tk.Entry(frame, font=("Segoe UI", 11), relief="solid", bd=1)
    entrada.grid(
        row=1, column=coluna, sticky="ew",
        padx=(0, 10) if coluna < 2 else 0,
        ipady=7
    )

    frame.columnconfigure(coluna, weight=peso)

    return entrada