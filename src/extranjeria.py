from collections import namedtuple
import csv
from collections import defaultdict

RegistroExtranjeria = namedtuple('RegistroExtranjeria', 'distrito,seccion,barrio,pais,hombres,mujeres')

def lee_datos_extranjeria(ruta):
    lista = []
    with open(ruta,encoding='utf-8') as f:
        next(f)
        fichero = csv.reader(f)
        for distrito, seccion, barrio, pais, h, m in fichero:
            distrito = int(distrito)
            seccion = int(seccion)
            barrio = str(barrio)
            pais = str(pais)
            h = int(h)
            m = int(m)
            RegistroExtranjeria = (distrito, seccion, barrio, pais, h, m)
            lista.append(RegistroExtranjeria)
    return lista

def numero_nacionalidades_distintas(registros):
    lis = []
    for distrito, seccion, barrio, pais, h, m in registros:
        if pais not in lis:
            lis.append(pais)
    return len(lis)

def secciones_distritos_con_extranjeros_nacionalidades(registros,  paises):
    lis = []
    for distrito, seccion, barrio, pais, h, m in registros:
        if pais in paises:
            tupla = (distrito, seccion)
            lis.append(tupla)
    lis.sort(key=lambda x:x[0])
    return lis

def total_extranjeros_por_pais(registros):
    dicc = defaultdict(int)
    for distrito, seccion, barrio, pais, h, m in registros:
        dicc[pais] += h+m
    return dicc

def top_n_extranjeria(registros,  n=3):
    registros.sort(key=lambda x:x[3])
    lista = []
    x = 0
    p = 0
    for distrito, seccion, barrio, pais, h, m in registros:
        if p == pais:
            x += h+m
        else:
            tupla = (p,x)
            lista.append(tupla)
            p = pais
            x = h+m
    del lista[0]
    lista.sort(key=lambda x:x[1])
    lista.reverse()
    res = []
    for i in range(0,n):
        res.append(lista[i])
    return res

def barrio_mas_multicultural(registros):
    dicc = defaultdict(int)
    for distrito, seccion, barrio, pais, h, m in registros:
        dicc[barrio] += 1
    lista = list(dicc.items())
    lista.sort(key=lambda x:x[1])
    lista.reverse()
    return lista[0][0]

def barrio_con_mas_extranjeros(registros, tipo=None):
    dicc = defaultdict(int)
    for distrito, seccion, barrio, pais, h, m in registros:
        if tipo == 'Hombres':
            dicc[barrio] += h
        elif tipo == 'Mujeres':
            dicc[barrio] += m
        else:
            dicc[barrio] += h+m
    lista = list(dicc.items())
    lista.sort(key=lambda x:x[1])
    lista.reverse()
    return lista[0][0]

def pais_mas_representado_por_distrito(registros):
    distritos_paises = defaultdict(lambda: defaultdict(int))
    for distrito, seccion, barrio, pais, hombres, mujeres in registros:
        total_personas = hombres + mujeres
        distritos_paises[distrito][pais] += total_personas
    pais_maximo_por_distrito = {}
    for distrito, paises in distritos_paises.items():
        pais_maximo = max(paises, key=paises.get)
        pais_maximo_por_distrito[distrito] = pais_maximo
    return pais_maximo_por_distrito
