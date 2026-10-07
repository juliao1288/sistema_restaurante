# 🍔 FastBite CLI — Sistema de Gerenciamento de Restaurante

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Estrutura de Dados](https://img.shields.io/badge/Estruturas_de_Dados-Fila_e_Pilha-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

O **FastBite CLI** é uma aplicação interativa via linha de comando (Terminal) desenvolvida para gerenciar o fluxo operacional de um restaurante. O sistema combina o cadastro dinâmico de cardápios com a gestão da fila de produção da cozinha e um histórico auditável de ações com suporte a desfecho de operações.

---

## 📌 Funcionalidades Principais

- 📋 **Gestão de Cardápio:** Cadastrar itens com ID sequencial dinâmico, preço validado e remoção por ID.
- 🛎️ **Fila da Cozinha (FIFO):** Processamento de pedidos por ordem de entrada no restaurante[cite: 5, 7, 8].
- ↺ **Controlo de Histórico & Undo (LIFO):** Desfaz a última ação realizada (lançamento de pedido ou atendimento) reordenando a fila automaticamente[cite: 5, 6, 8].
- 🔍 **Visualização Não-Destrutiva:** Consulta ao cardápio, à fila de espera e ao histórico sem alterar a ordem das estruturas de dados.

---

## 🛠️ Arquitetura e Estrutura do Projeto

O projeto adota uma arquitetura modularizada em Python:

```text
.
├── main.py        # Ponto de entrada da aplicação e menu interativo (CLI)
├── funcoes.py     # Lógica de negócio e manipulação dos requisitos
├── fila.py        # Implementação customizada da classe Fila (FIFO)
└── pilha.py       # Implementação customizada da classe Pilha (LIFO)
