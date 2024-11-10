from extranjeria import *

def test_lee_datos_extranjeria(ruta):
    res = lee_datos_extranjeria(ruta)
    print(res)

def test_numero_nacionalidades_distintas(registros):
    res = numero_nacionalidades_distintas(registros)
    print(res)

def test_secciones_distritos_con_extranjeros_nacionalidades(registros,  paises):
    res = secciones_distritos_con_extranjeros_nacionalidades(registros,  paises)
    print(res)

def test_total_extranjeros_por_pais(registros):
    ers = total_extranjeros_por_pais(registros)
    print(ers)

def test_top_n_extranjeria(registros,  n):
    res = top_n_extranjeria(registros,  n)
    print(res)

def test_barrio_mas_multicultural(registros):
    res = barrio_mas_multicultural(registros)
    print(res)

def test_barrio_con_mas_extranjeros(registros, tipo):
    res = barrio_con_mas_extranjeros(registros, tipo)
    print(res)

def test_pais_mas_representado_por_distrito(registros):
    res = pais_mas_representado_por_distrito(registros)
    print(res)

if __name__ == '__main__':
    #test_lee_datos_extranjeria('data/extranjeriaSevilla.csv')
    registros = lee_datos_extranjeria('data/extranjeriaSevilla.csv')
    #test_numero_nacionalidades_distintas(registros)
    #test_secciones_distritos_con_extranjeros_nacionalidades(registros, 'ALEMANIA')
    #test_total_extranjeros_por_pais(registros)
    #test_top_n_extranjeria(registros, 5)
    #test_barrio_mas_multicultural(registros)
    #test_barrio_con_mas_extranjeros(registros, 'Mujeres')
    test_pais_mas_representado_por_distrito(registros)
