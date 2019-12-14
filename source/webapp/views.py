from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


from webapp.models import Photo, Comment

class IndexView(ListView):
    model = Photo
    template_name = 'index.html'
    context_object_name = 'photos'
    ordering = ['-create_at']


class PhotoView(DetailView):
    template_name = 'photo.html'
    model = Photo
    context_object_name = 'photo'
    ordering = ['-create_at']
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments']= self.object.photo_comments.all().order_by('-create_at')
        return context


class PhotoCreateView( CreateView, LoginRequiredMixin):
    model = Photo
    template_name = 'create.html'
    fields = ('signature', 'photo')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoUpdateView(UpdateView, UserPassesTestMixin):
    model = Photo
    template_name = 'update.html'
    fields = ('signature', 'photo')
    # context_object_name = 'photos'

    def test_func(self):
        photo_pk = self.kwargs.get('pk')
        photo = Photo.objects.get(pk=photo_pk)
        return self.request.user == photo.author or self.request.user.has_perm('webapp.change_photo')

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView, UserPassesTestMixin):
    model = Photo
    template_name = 'delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        photo_pk = self.kwargs.get('pk')
        photo = Photo.objects.get(pk=photo_pk)
        return self.request.user == photo.author or self.request.user.has_perm('webapp.change_photo')