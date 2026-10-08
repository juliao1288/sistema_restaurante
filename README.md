🍔 FastBite CLI — Sistema de Gerenciamento de Restaurante

!Python !Estruturas de Dados !Status

O FastBite CLI é uma aplicação interativa via linha de comando (Terminal), desenvolvida em Python para gerenciar o fluxo operacional de um restaurante.

O sistema combina o gerenciamento dinâmico do cardápio com o controle de pedidos da cozinha e um histórico de ações, utilizando estruturas de dados como Fila (FIFO) e Pilha (LIFO), além de oferecer suporte ao desfazer de operações.

📌 Funcionalidades Principais
🧾 Gestão de Cardápio: Cadastro, consulta e remoção de itens, com identificadores dinâmicos e validação de preços.
🍲 Fila da Cozinha (FIFO): Organização e processamento dos pedidos por ordem de entrada.
↩️ Histórico e Desfazer (LIFO): Registro de ações e possibilidade de desfazer a última operação, mantendo a consistência das estruturas de dados.
🔍 Visualização Não Destrutiva: Consulta ao cardápio, à fila de pedidos e ao histórico sem alterar sua organização.
🧩 Arquitetura Modular: Separação das responsabilidades em módulos, facilitando a manutenção e a evolução do projeto.
🖥️ Interface de Terminal: Interação com o sistema por meio de menus e opções de gerenciamento.
🛠️ Tecnologias e Estruturas de Dados
Python 3.10+: Linguagem utilizada no desenvolvimento.
Fila (FIFO — First In, First Out): Garante o processamento dos pedidos na ordem de chegada.
Pilha (LIFO — Last In, First Out): Permite controlar o histórico e desfazer a última ação registrada.
Programação Modular: Organização do código em arquivos com responsabilidades específicas.
🏗️ Arquitetura e Estrutura do Projeto

O projeto utiliza uma arquitetura modular em Python, separando a lógica principal, as estruturas de dados e os componentes da interface.

FastBite-CLI/
│
├── interface/
│   ├── __init__.py       # Inicialização do pacote de interface
│   ├── app.py            # Aplicação e fluxo da interface
│   ├── cardapio.py       # Funcionalidades do cardápio
│   ├── componentes.py    # Componentes reutilizáveis da interface
│   ├── cozinha.py        # Operações relacionadas à cozinha
│   ├── historico.py      # Histórico de ações
│   ├── integracao.py     # Integração entre os módulos
│   └── pedidos.py        # Gerenciamento dos pedidos
│
├── .gitignore            # Arquivos ignorados pelo Git
├── README.md             # Documentação do projeto
├── fila.py               # Implementação da estrutura de Fila (FIFO)
├── funcoes.py            # Funções e regras de negócio
├── main.py               # Ponto de entrada da aplicação
└── pilha.py              # Implementação da estrutura de Pilha (LIFO)

⚙️ Como Executar o Projeto
Pré-requisitos
Python 3.10 ou superior.
Git (opcional, para clonar o repositório).
1. Clone o repositório
git clone URL_DO_SEU_REPOSITORIO

2. Acesse a pasta do projeto
cd FastBite-CLI

3. Execute a aplicação
python main.py

Observação: Caso seu ambiente utilize o comando python3, execute python3 main.py.
🧠 Conceitos Aplicados

Este projeto demonstra, na prática, a aplicação de conceitos importantes de programação:

Estruturas de dados lineares.
Manipulação de filas e pilhas.
Modularização e organização de código.
Validação de dados e regras de negócio.
Controle de fluxo por menus interativos.
Registro e reversão de operações.
🎯 Objetivo do Projeto

Desenvolver um sistema de gerenciamento de restaurante que demonstre a aplicação prática de estruturas de dados e boas práticas de organização em Python, simulando operações comuns de um ambiente de atendimento e produção.

📌 Status do Projeto

Concluído — estrutura modular e funcionalidades desenvolvidas conforme a proposta do projeto.

Desenvolvido com 🐍 Python e 🍔 foco em organização, eficiência e aprendizado.
