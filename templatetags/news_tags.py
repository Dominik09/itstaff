from django import template
from django.shortcuts import render_to_response, redirect, get_object_or_404
from sheet.models import Sheet, Comments

register = template.Library()

def sheets(request):
	args = {}
    args['news'] = Sheet.objects.all()
    if request.POST:
        news_form = Sheet.objects.get(pk=args['news'].id)
    return render_to_response('main.html', args)
