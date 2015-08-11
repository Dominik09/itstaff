from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect, get_object_or_404
from sheet.models import Sheet, Comments
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm, AddNewsForm, EditNewsForm
from django.core.context_processors import csrf
from django.contrib import auth
from loginsys.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def sheets(request):
    Total = Sheet.objects.filter().count()
    return render_to_response('sheets.html', {'sheets': Sheet.objects.filter()[Total-3:Total], 'username': auth.get_user(request).username})

def sheet(request, sheet_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['sheet'] = Sheet.objects.get(id=sheet_id)
    args['comments'] = Comments.objects.filter(com_sheet_id=sheet_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('sheet.html', args)

def addlike(request, sheet_id):
    try:
        if sheet_id in request.COOKIES:
            redirect('/')
        else:
            sheet = Sheet.objects.get(id=sheet_id)
            sheet.likes += 1
            sheet.save()
            response = redirect('/')
            response.set_cookie(sheet_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, sheet_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.com_sheet = Sheet.objects.get(id=sheet_id)
            form.save()
            request.session.set_expiry(10)
            request.session['pause'] = True
    return redirect('/sheets/get/%s/' % sheet_id)


# def addnews(request):
#     args = {}
#     args.update(csrf(request))
#     args['form'] = AddNewsForm()
#     if request.method == "POST":
#         news_form = AddNewsForm(request.POST, request.FILES)
#         if news_form.is_valid():
#             sheet = news_form.save()
#             args['sheet'] = Sheet.objects.get(id = sheet.id)
#             return redirect('/sheets/%s/' % args['sheet'].id)
#         else:
#             args['form'] = news_form
#     return render_to_response('addnews.html', args)

def ednews(request, sheet_id):
    args = {}
    args.update(csrf(request))
    args['user'] = User.objects.get(username = request.user)
    args['new'] = get_object_or_404(Sheet, id = sheet_id)
    args['form'] = EditNewsForm(args['new'].__dict__)
    if request.method == "POST":
        news = Sheet.objects.get(id = sheet_id)
        news_edit_form = EditNewsForm(request.POST, request.FILES, instance = news)
        if news_edit_form.is_valid():
            news_edit_form.save()
            return redirect('Get_news', sheet_id = sheet_id)
        else:
            args['form'] = news_edit_form
    return render_to_response('edit_news.html', args)


def news_all(request):
    args = {}
    args['list_news'] = Sheet.objects.all().order_by('-date')
    return render_to_response('list_news.html', args)

class CreateNewsItem(CreateView):
    model = Sheet
    form_class = AddNewsForm
    template_name = 'addnews.html'
    success_url = reverse_lazy('List_news')
addnews = CreateNewsItem.as_view()
