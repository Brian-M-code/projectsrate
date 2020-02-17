from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from .models import  Projects,Profile
from django.views.generic import ListView,DetailView


class PostListView(ListView):
    model = Projects
    template_name = 'index.html'
    context_object_name = 'projects'
    ordering = ['-created_date']

class PostDetailView(DetailView):
    model = Projects