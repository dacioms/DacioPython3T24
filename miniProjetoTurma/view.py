from calculos import calcular_medias
from cadastro import cadastrar_aluno
from main import solicitar_medias, classificar_alunos, lista_alunos

def menu():
    print("Bem vindo ao sistema de cadastro de alunos")
    print("Escolha uma opção")
    print("1 - Cadastrar aluno")
    print("2 - Calcular médias")
    print("3 - Classificar alunos")
    print("4 - Exibir")
    print("5 - Sair")
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        lista_alunos.append(cadastrar_aluno())
        return True
    elif opcao == "2":
        solicitar_medias()
        return True
    elif opcao == "3":
        classificar_alunos()
        return True
    elif opcao == "4":
        print("Até logo!")
        return False
    else:
        print("Opção inválida")
        menu()
        
if __name__ == "__main__":
    menu()