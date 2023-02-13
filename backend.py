import pandas as pd

def get_cursos(data_frame):
    lista_cursos = data_frame["NO_CURSO"]
    lista_cursos = list(dict.fromkeys(lista_cursos))
    lista_cursos.sort()
    return lista_cursos

if __name__ == "__main__":
    get_cursos()

def get_possibilidades(data_frame, curso):
    possibilidades = data_frame.loc[data_frame["NO_CURSO"] == curso].squeeze()
    return possibilidades
