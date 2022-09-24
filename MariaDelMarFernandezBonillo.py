
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame()

MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

gastoTotal = 0
ingresoTotal = 0

try:
    df = pd.read_csv('finanzas2020.csv', sep = '\t')
except:
    print('El archivo que intenta leer no existe')

# COMPROBAMOS LAS COLUMNAS
columnas = list(df.columns)
contCols = False

for c in columnas:
    if len(df[c].values) != 0: contCols = True

assert len(columnas) == 12 or columnas == MESES or contCols, "El archivo no tiene contenido en todos los meses del año"

# print(df)
# print(f'RV --> {df.loc[0]}')

for i in range(0, len(df.axes[1])): #COLUMNAS
    mes = MESES[i]
    for x in range(0, len(df.axes[0])): # FILAS
        rv = df.at[x, mes]
        try:
            rv = int(rv)
        except Exception as e:
            # print(f'ERROR --> {e} \nEn el valor --> {rv[i]}')
            # COMPRUEBO SI EL DATO ES UN STRING DE UN STRING Y SI LO ES, ELIMINO LAS COMILLAS SIMPLES Y LO PASO A INT
            coma = "'"
            if rv.find(coma) != -1: 
                rv = int(rv.replace("'", ""))
            else: # SI NO CONSIGUE PASARLO A INT NI TIENE COMILLAS, SE TRATA DE 'bug' O DE 'ups'. EN ESTE CASO LO PONGO A 0
                rv = 0
        df.at[x, mes] = rv
        # APROVECHO ESTE BUCLE PARA CALCULAR EL TOTAL DE GASTOS Y DE INGRESOS DEL AÑO
        if rv < 0: gastoTotal += rv
        else: ingresoTotal += rv


########################## CALCULO DE GASTOS ##########################
suma = df.sum()

maximoGasto = suma.min()
minimoGasto = suma.max()

for x, i in suma.iteritems():
    if i == maximoGasto: maximoGasto = {x: i}
    if i == minimoGasto: minimoGasto = {x: i}


print(f'Máximo gasto --> {list(maximoGasto.keys())[0]}: {list(maximoGasto.values())[0]}')
print(f'Mínimo gasto --> {list(minimoGasto.keys())[0]}: {list(minimoGasto.values())[0]}')
print(f'Media de gastos del año --> {suma.sum() / len(suma)}')
print(f'Gastos totales del año --> {gastoTotal}')
print(f'Ingresos totales del año --> {ingresoTotal}')