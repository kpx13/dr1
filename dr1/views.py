# -*- coding: utf-8 -*-

import datetime
from django.core.context_processors import csrf
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from livesettings import config_value

from pages.models import Page
from company.models import Page as CompanyPage
from news.models import Article
from slideshow.models import Slider
from docs.models import Category, DocFile
from news.models import Article

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['docs'] = Category.objects.all()
    c['pages'] = CompanyPage.objects.all()
    c.update(csrf(request))
    
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['slider'] = Slider.objects.filter(show=True)
    c['news'] = Article.objects.all()[:4]
    c['content'] = Page.get_by_slug('home')['content']
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def other_page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()

def company_page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(CompanyPage.get_by_slug(page_name))
        return render_to_response('company.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()


def news_article_page(request, page_name):
    c = get_common_context(request)
    try:
        c['item'] = Article.get_by_slug(page_name)
        c['news'] = Article.objects.all()
        return render_to_response('news_article.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()
    
def news_page(request):
    c = get_common_context(request)
    try:
        c['news'] = Article.objects.all()
        return render_to_response('news.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()
    
def docs_page(request, id=None):
    c = get_common_context(request)
    try:
        c['item'] = Category.objects.get(id=id)
        return render_to_response('docs.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()
    