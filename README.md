# sistema_restaurante
Sistema de Atendimento de Restaurante, projeto da aula do professor Henrique Shishido, na disciplina Estrutura de Dados.

Glossário da Estrutura:

- Produto: Deve ser armazenado em um dicionário, com as chaves ID(int), nome(str) e preco(float).
- Cardápio: Deve ser do tipo list, contendo um dicionário de cada produto dentro da lista.
  Exemplo de cardápio:
  cardapio = [
    {"id": 1, "nome": "Hambúrguer Clássico", "preco": 25.50},
    {"id": 2, "nome": "Batata Frita Média", "preco": 12.00},
    {"id": 3, "nome": "Refrigerante 350ml", "preco": 6.50}

]
- Registro de Pedido: Deve ser registrado um pedido informando o nome do cliente e o ID dos produtos
- Fila da cozinha: Deve ser do tipo Fila, onde First In, First Out.
- Histórico: Deve ser do tipo Pilha, onde First In, Last Out.
