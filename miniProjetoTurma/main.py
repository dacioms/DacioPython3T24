# cadastro de aluno 

    # dados dos alunos
        # matricula (key)
        # nome
        # Turma
        # 
        # notas
            # portugues; matematica; ciencias;
                # trabalho; teste; prova
    
    # requisitos especificos
        # cadastrar alunos
            # => função que adiciona o dict_aluno à lista_alunos
                # => função que instancia uma classe
            # solicitar os dados ao usuário
                # => função que valida os dados dos alunos
                    # => matricula auto incremental

            
        # calcular a média do aluno
            # => que acessa a lista de notas de cada disciplina de cada aluno
                # => lista de lista com a notas[[#, #, #], [#, #, #], [#, #, #]]
                    # => função que calcula a média recebendo lista de listas de notas
                    # => retorna a lista de média ordenada
                # => adiciona ao dicionádrio do aluno os itens média_portugues, média_matematica, média_ciencias
                
        # classificar aprovado / reprovado (aprov >= 7)
            # => função que verifica se a média do aluno em cada disciplina é maior ou igual a 7
                # se qualquer das disciplinas for menor que 7, o aluno é reprovado
                    # => adiciona ao dicionário do aluno o item aprovado (bool)
                
    
    # requisito geral 
        # interface
            # => terminal
                #opções
                    # cadastrar aluno
                    # calcular médias
                    # classificar alunos
                    # sair
                    
        # estrutura de dados
            # => lista de alunos -> lista_alunos
                # cada aluno é registrado em um dicionario
                    # [{matricula: int , nome: str, turma: str, portugues: [#, #, #]; matematica: [#, #, #]; ciencias: [#, #, #]}, ]
        # 
        
lista_alunos = []
def cadastrar_aluno():
    '''Função que cadastra um aluno'''
    
    dict_aluno = {}
    if lista_alunos == []:
        dict_aluno["matricula"] = 1
    else:
        dict_aluno["matricula"] = lista_alunos[-1]["matricula"] + 1
        
    dict_aluno["nome"] = input("Digite o nome do aluno: ")
    dict_aluno["turma"] = input("Digite a turma do aluno: ")
    
    dict_aluno["portugues"] = [float(input("Digite a nota do trabalho de português: ")), 
                               float(input("Digite a nota do teste de português: ")), 
                               float(input("Digite a nota da prova de português: "))]
    
    dict_aluno["matematica"] = [float(input("Digite a nota do trabalho de matemática: ")), 
                                float(input("Digite a nota do teste de matemática: ")), 
                                float(input("Digite a nota da prova de matemática: "))]
    
    dict_aluno["ciencias"] = [float(input("Digite a nota do trabalho de ciências: ")), 
                              float(input("Digite a nota do teste de ciências: ")), 
                              float(input("Digite a nota da prova de ciências: "))]
    
    lista_alunos.append(dict_aluno)
    print("Aluno cadastrado com sucesso!")
    # print(lista_alunos)

def calcular_medias(port, mat, cien):
    media_port = sum(port) / len(port)
    media_mat = sum(mat) / len(mat)
    media_cien = sum(cien) / len(cien)
    return [media_port, media_mat, media_cien]

def solicitar_medias():
    for aluno in lista_alunos:
        port, mat, cien = aluno["portugues"], aluno["matematica"], aluno["ciencias"]
        medias = calcular_medias(port = port, mat = mat, cien = cien)
        aluno["media_portugues"] = medias[0]
        aluno["media_matematica"] = medias[1]
        aluno["media_ciencias"] = medias[2]
    print('Medias calculadas com sucesso!')


def classificar_alunos():
    for aluno in lista_alunos:

        if "media_portugues" not in aluno.keys() or 'media_matematica' not in aluno.keys() or 'media_ciencias' not in aluno.keys():
            print('É necessário calcular as médias antes de classificar os alunos')
            break
        media_port = aluno["media_portugues"]
        media_mat = aluno["media_matematica"]
        media_cien = aluno["media_ciencias"]
        if media_port >= 7 and media_mat >= 7 and media_cien >= 7:
            aluno["aprovado"] = True
        else:
            aluno["aprovado"] = False
    print('Classificação de alunos concluída!')


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
        cadastrar_aluno()
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
def main():
    while True:
        continua = menu()
        if not continua:
            break
        
if __name__ == "__main__":
    main()