def calcular_medias(port : list, mat : list, cien : list) -> list:
    '''Função que calcula a média das notas de um aluno
    
    Args:
        port (list): lista de notas do aluno em português
        mat (list): lista de notas do aluno em matemática
        cien (list): lista de notas do aluno em ciências

    return: lista de notas do aluno em português, matemática e ciências
    '''
    media_port = sum(port) / len(port)
    media_mat = sum(mat) / len(mat)
    media_cien = sum(cien) / len(cien)
    return [media_port, media_mat, media_cien]