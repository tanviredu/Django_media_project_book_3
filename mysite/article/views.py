## this is the core library
from django.shortcuts import render
from django.http import  HttpResponse
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.template import Context
###

## database model
from .models import  Article
## form
from .forms import ArticleForm
from .forms import UserCreationForm
