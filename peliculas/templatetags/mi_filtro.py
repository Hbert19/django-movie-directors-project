from django import template

register = template.Library()

@register.filter(name='formatear_tiempo')
def formatear_tiempo(tiempo):
    duracion = str(tiempo)[1:2] + "h" + str(tiempo)[2:5] + "m"
    duracion_formateada = duracion.replace(':', ' ')
    return duracion_formateada