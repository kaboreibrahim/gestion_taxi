import datetime
from django import template

register = template.Library()

@register.filter
def semaine_du_mois(date):
    first_day_of_month = date.replace(day=1)
    return ((date - first_day_of_month).days // 7) + 1
