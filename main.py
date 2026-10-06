# Sistema de Restaurante

import fila
import pilha
import funcoes

def exibir_menu():
    print()
    print("=" * 50)
    print("           RESTAURANTE FASTBITE - CLI")
    print("=" * 50)
    print("--- CARDÁPIO (list) ---")
    print("1. Cadastrar Item no Cardápio")
    print("2. Remover Item do Cardápio")
    print("3. Listar Cardápio\n")
    print("--- COZINHA & PEDIDOS (Fila) ---")
    print("4. Lançar Novo Pedido")
    print("5. Atender Próximo Pedido")
    print("6. Visualizar Fila da Cozinha\n")
    print("--- SISTEMA (Pilha) ---")
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
                # RF-03: Listar Cardápio
                pass

            case "4":
                # RF-04: Lançar Novo Pedido
                pass

            case "5":
                # RF-05: Atender Próximo Pedido
                pass

            case "6":
                # RF-06: Visualizar Fila da Cozinha
                pass

            case "7":
                # Opção 7: Desfazer
                funcoes.desfazer(pilha_historico, fila_cozinha)

            case "8":
                # Opção 8: Visualizar Histórico
                pass

            case "0":
                print("Encerrando o restaurante. Até logo!")
                break

            case _:
                print(" Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
