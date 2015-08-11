from django import template
from django.shortcuts import render_to_response, redirect, get_object_or_404
from sheet.models import Sheet, Comments

register = template.Library()

@register.inclusion_tag('sheets.html', takes_context=True)
def last_sheets(context):
    #import ipdb; ipdb.set_trace()
    Total = Sheet.objects.filter().count()
    context.update({'sheets': Sheet.objects.filter()[Total-3:Total]})
    return context
