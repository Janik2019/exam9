from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib import messages


from webapp.models import Photo, Comment

class IndexView(ListView):
    model = Photo
    template_name = 'index.html'
    context_object_name = 'photos'
    ordering = ['-create_at']
    #
    # def get_queryset(self):
    #     return Photo.objects.filter(in_order=True)


class PhotoView(DetailView):
    template_name = 'photo.html'
    model = Photo