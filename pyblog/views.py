from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import post


# Create your views here.
def home(request):
    context = {
        'posts': post.objects.all() #context is a dictionary which has the list of all the posts( which are themselves dictionary )
    }
    #return HttpResponse('<h1>Blog Home</h1>') #heading of webapp
    return render(request,'pyblog/home.html', context)  #using template we need to render
                                                        #context is the third parameter , now posts will be rendered via template home.html

class PostListView(ListView):
    model = post
    template_name = 'pyblog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 4

class UserPostListView(ListView):
    model = post
    template_name = 'pyblog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author = user).order_by('-date')



class PostDetailView(DetailView):
    model = post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request,'pyblog/about.html', {'title':'About'}) #using template we need to render
