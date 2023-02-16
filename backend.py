import pandas as pd
import numpy

def get_cursos(data_frame):
    lista_cursos = data_frame["NO_CURSO"]
    lista_cursos = list(dict.fromkeys(lista_cursos))
    lista_cursos.sort()
    lista_cursos.insert(0, "TODOS")

    return lista_cursos


def get_universidades(data_frame):
    lista_universidades = data_frame["SG_IES"]
    lista_universidades = list(dict.fromkeys(lista_universidades))
    nan_index = lista_universidades.index(numpy.nan)
    lista_universidades.pop(85)
    lista_universidades.sort()
    lista_universidades.insert(0, "TODAS")

    return lista_universidades


def rename_columns(data_frame):
    nome_colunas = {"SG_IES": "Sigla",
                    "NO_CAMPUS": "Campus",
                    "NO_MUNICIPIO_CAMPUS": "Município do Campus",
                    "NO_CURSO": "Nome do Curso",
                    "DS_GRAU": "Grau do Curso",
                    "DS_TURNO": "Turno",
                    "DS_MOD_CONCORRENCIA": "Descrição da modalidade",
                    "QT_VAGAS_CONCORRENCIA": "Vagas",
                    "NU_NOTACORTE": "Nota de corte",
                    "QT_INSCRICAO": "Quantidade de inscritos"}
    data_frame.reset_index(inplace=True)
    data_frame.drop("index", axis=1, inplace=True)
    data_frame.rename(columns=nome_colunas, inplace=True)
    return data_frame


def get_possibilidades(data_frame, curso, universidade):
    if universidade != "TODAS" and curso != "TODOS":
        possibilidades = data_frame.loc[data_frame["NO_CURSO"]
                                        == curso].squeeze()
        possibilidades = possibilidades.loc[possibilidades["SG_IES"]
                                            == universidade].squeeze()
        possibilidades = rename_columns(possibilidades)

    elif curso != "TODOS":
        possibilidades = data_frame.loc[data_frame["NO_CURSO"]
                                        == curso].squeeze()
        possibilidades = rename_columns(possibilidades)

    elif universidade != "TODAS":
        possibilidades = data_frame.loc[data_frame["SG_IES"]
                                        == universidade].squeeze()
        possibilidades = rename_columns(possibilidades)

    else:
        possibilidades = None

    return possibilidades


if __name__ == "__main__":
    FILEPATH = "DataBase/inscricoes_e_notas_de_corte_Sisu_2022-1.xlsx"
    df = pd.read_excel(FILEPATH, sheet_name="inscricao_2022_1")
    get_universidades(df)

