from django.shortcuts import render_to_response, redirect
from django.http import Http404
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth

def template(request):
    view = 'template'
    return render_to_response('myview.html', {'name': view})

def all_article(request):
    return render_to_response('all.html', {'articles': Article.objects.all(),'username': auth.get_user(request).username})

def single_article(request, art_id = 1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id = art_id)
    args['comments'] = Comments.objects.filter(article_id = art_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('single.html', args)

def like(request, art_id):
    try:
        if art_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id = art_id)
            article.likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(art_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def backto(request):
    return redirect('/')

def addcomment(request, art_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.article = Article.objects.get(id = art_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % art_id)