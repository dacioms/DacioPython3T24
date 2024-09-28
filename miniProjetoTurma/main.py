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
        


from view import *
from calculos import *


lista_alunos = []


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



def main():
    while True:
        continua = menu()
        if not continua:
            break
        
if __name__ == "__main__":
    main()