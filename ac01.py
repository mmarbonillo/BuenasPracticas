# Implemente un programa que lea el contenido del fichero y realice los siguientes cálculos:
# ● ¿Qué mes se ha gastado más?
# ● ¿Qué mes se ha ahorrado más?
# ● ¿Cuál es la media de gastos al año?
# ● ¿Cuál ha sido el gasto total a lo largo del año?
# ● ¿Cuáles han sido los ingresos totales a lo largo del año?
# ● Opcional: Realice una gráfica de la evolución de ingresos a lo largo del año .
# APARTADO 2:
# Haciendo uso de excepciones, haga las siguientes comprobaciones:
# ● Compruebe que el fichero existe y que tiene 12 columnas, una para cada mes del año.
# ● Para cada mes compruebe que hay contenido.
# ● Compruebe que todos los datos son correctos. De no haber un dato correcto, el programa debe saber actuar en consecuencia y continuar con su ejecución.

from asyncio.windows_events import NULL
import pandas as pd

MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

df = NULL

try:
    df = pd.read_csv('finanzas20202.csv')
    df = pd.DataFrame(df)
    describe = df.describe()
except :
    print('El archivo no existe')

# COMPROBAR COLUMNAS
cols = []
if df is not NULL:
    cols = df.columns
    cols = cols[0].split('\t')
print(cols)
assert len(cols) != 12, "El número de columnas no es correcto"

# for column in df:
#     col = df[column]
#     print(f'{column} : {col}')

# columna5 = df.iloc[:, 4] # RECOJO LA COLUMNA
# columna5EnLista = columna5.tolist() # LA PASO A LISTA

# # RECORRO LA LISTA PARA COMPROBAR CADA ELEMENTO
# for i in range(0, len(columna5EnLista)):
#     columna5EnLista[i] = float(columna5EnLista[i])

# # PASO LA LISTA A DATAFRAME
# columna5 = pd.DataFrame(data = columna5EnLista)

# # LE ASIGNO EL DATAFRAME A LA COLUMNA
# df['Volumen'] = columna5


# columnas = df.columns

# print(columnas)

# data = df.to_json(orient = "index")
# data = json.loads(data)
# describe = df.describe().to_json(orient = "index")