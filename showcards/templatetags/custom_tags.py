from django import template
from showcards.models import Cards
register = template.Library()

@register.filter(name='getcards')
def getcards(v):
    yo =  Cards.objects.get(id=v).img
    return yo

@register.filter(name='getstatus')
def getcards(v):
    yo =  Cards.objects.get(id=v).status
    return yo
