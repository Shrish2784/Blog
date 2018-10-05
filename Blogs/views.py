from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from Blogs import models
from Blogs import forms


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class PostUserListView(LoginRequiredMixin, ListView):
    model = models.Post
    template_name = 'post_user_list.html'

    def get_queryset(self):
        return models.Post.objects.filter(author=self.request.user).order_by('-publish_date')

class ProfileDetailView(DetailView):
    model = User
    template_name = 'Blogs/user_detail.html'
    # context_object_name = 'user'

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    form_class = forms.PostForm
    model = models.Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login/'
    redirect_field_name = 'Blogs/post_list.html'
    form_class = forms.PostForm
    model = models.Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy('Blogs:post_list')

class DraftListView(LoginRequiredMixin, ListView):
    template_name = 'post_drafts_list.html'
    login_url = 'login/'
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publish_date__isnull=True).filter(author=self.request.user).order_by('-create_date')

###########################
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('Blogs:post_list')
    else:
        form = forms.CommentForm()
        context_dict = {
            'form': form
        }
        return render(request, 'Blogs/comment_form.html', context=context_dict)

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.approve()
    return redirect('Blogs:post_list')

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('Blogs:post_list')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.publish()
    return redirect('Blogs:post_list')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.save().username
            password = form.clean_password2()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/signup.html', context={'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', context={'form':form})
