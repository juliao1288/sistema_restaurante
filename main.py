# Sistema de Restaurante

import fila
import pilha
import funcoes

def exibir_menu():
    print()
    print("=" * 50)
    print("           RESTAURANTE FASTBITE - CLI")
    print("=" * 50)
    print("--- CARDÁPIO ---")
    print("1. Cadastrar Item no Cardápio")
    print("2. Remover Item do Cardápio")
    print("3. Listar Cardápio\n")
    print("--- COZINHA & PEDIDOS ---")
    print("4. Lançar Novo Pedido")
    print("5. Atender Próximo Pedido")
    print("6. Visualizar Fila da Cozinha\n")
    print("--- SISTEMA ---")
    print("7. Desfazer Última Ação")
    print("8. Visualizar Histórico de Ações")
    print("0. Sair")
    print("=" * 50)
  
def main():
    contagem = 0
    cardapio = []
    fila_cozinha = fila.Fila()
    pilha_historico = pilha.Pilha()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        print()

        match opcao:
            case "1":
                contagem += 1
                id_prod = contagem
                
                nome = input(" Insira o nome do produto: ").strip()
                preco = input(" Insira o preço do produto (Ex: 15.50): ")
        
                while not funcoes.verificar_preco(preco):
                    preco = input(" Tente novamente! Insira somente números maiores que 0: ")
                
                preco_num = float(preco.replace(',', '.'))
          
                produto = funcoes.cadastrar_item(id_prod, nome, preco_num)
                cardapio.append(produto)
                print(f" Item '{nome}' (ID: {id_prod}) cadastrado com sucesso!")
                print(f" Item: {nome} -- ID: {id_prod} -- Cadastro realizado com sucesso!")
              
            case "2":
                if not cardapio:
                    print(" O cardápio está vazio!")
                else:
                    id_input = input(" Insira o ID do produto a remover: ").strip()
                    if id_input.isdigit():
                        removido = funcoes.remover_item(cardapio, int(id_input))
                        if not removido:
                            print(" Produto não encontrado no cardápio!")
                    else:
                        print(" ID inválido! Digite apenas números.")

            case "3":
                print()
                funcoes.visualizar_cardapio(cardapio)
                print()
                
            case "4":
                pedido = funcoes.cadastrar_pedido(cardapio)
                fila_cozinha.enqueue(pedido) 

            case "5":
                primeiro_fila = fila_cozinha.front()
                confirmar_realizacao = funcoes.realizar_pedido(primeiro_fila)
                if confirmar_realizacao == True:
                    fila_cozinha.dequeue()
   
            case "6":
                print()
                funcoes.visualizar_fila(fila_cozinha)
                print()

            case "7":
                print()
                funcoes.desfazer(pilha_historico, fila_cozinha)
                print()

            case "8":
                print()
                funcoes.visualizar_historico(pilha_historico)
                print()

            case "0":
                print("Encerrando o restaurante. Até logo!")
                break

            case _:
                print(" Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
