from main import lista_alunos

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
    return dict_aluno
    
    # lista_alunos.append(dict_aluno)
    # print("Aluno cadastrado com sucesso!")
    # # print(lista_alunos)