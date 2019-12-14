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
    context_object_name = 'photo'


class PhotoCreateView( CreateView):
    model = Photo
    template_name = 'create.html'
    fields = ('signature', 'photo')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    # permission_required = 'webapp.add_product', 'webapp.can_have_piece_of_pizza'
    # permission_denied_message = '403 Доступ запрещён!'

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'update.html'
    fields = ('signature', 'photo')
    # context_object_name = 'photos'

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})