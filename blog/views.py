# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_list2(request,data):
    return render(request,'blog/post_list2.html',{'data':data})
