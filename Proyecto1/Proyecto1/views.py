from django.http import HttpResponse
import datetime
from django.template import Template, Context
"""

"""
def saludo(request):
    doc_externo = open('plantilla1.html') # no es la forma mas elegante de hacerlo en django
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
    # Esta es una funcion vista
    # Devuelve una respuesta donde aparece este texto

def dame_fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = f"""<html>
    <body>
    <h1>
    Fecha y hora actual: {fecha_actual}
    </h1>
    </body>
    </html>
    """ # codigo html muy falopa

    return HttpResponse(documento)

def calcula_edad(request, edad, ano):
    #edadActual = 29
    periodo = ano - datetime.date.today().year  # 
    edadFutura = edad + periodo
    documento = f"""<html>
    <body>
    <h2>
    Tu edad en {ano} será {edadFutura}
    </h2>
    </body>
    </html>"""

    return HttpResponse(documento)
