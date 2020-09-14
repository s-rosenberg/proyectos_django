from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
"""

"""
def saludo(request):
    #nombre = 'Sebastian' 
    #apellido = 'Rosenberg'
    fecha_actual = datetime.datetime.now()
    comidas = ['pizza', 'pan', 'albondigas', 'arroz']
    #comidas = []
    """
    Esta manera open - close no es la manera optima de cargar plantillas -> consumen recursos
    se utilizan loaders de templates
    Sirve para cargar muchas plantillas
    Decirle a django que todas las plantillas se encuentra en una carpeta en este caso plantillas

    """

    #doc_externo = open('/mnt/4EA83DD1A83DB7F3/python/proyectos_django/Proyecto1/Proyecto1/plantillas/plantilla1.html') # no es la forma mas elegante de hacerlo en django
    #plantilla = Template(doc_externo.read())
    #doc_externo.close()
    
    #doc_externo = loader.get_template('plantilla1.html') # esta bueno porque no hace falta cargar el dir para cada plantilla (esta en settings)
    #contexto = Context({'nombre_persona': 'Sebastián', 'apellido_persona': 'Rosenberg', 'fecha': fecha_actual, 'comidas': comidas}) 
    #documento = doc_externo.render(contexto)
    dict_contexto = {'nombre_persona': 'Sebastián', 'apellido_persona': 'Rosenberg', 'fecha': fecha_actual, 'comidas': comidas}
    #documento = doc_externo.render(dic_contexto) # cuando se utiliza un loader se espera un diccionario para renderizar vs un contexto
    
    return render(request, 'plantilla1.html', dict_contexto)
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

def lorem_ipsum(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "hija1.html", {"dame_fecha": fecha_actual})

def lorem_lorem(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "hija2.html", {"dame_fecha": fecha_actual})
