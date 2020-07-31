# from django.shortcuts import render
# from .models import Blog
# from django.shortcuts import render, get_object_or_404

# def home(request):
#     return render(request, 'home.html')

# def location(request):
#     return render(request, 'location.html')

# def search(request):
#     return render(request, 'search.html')

# def community(request):
#     blog_model = Blog.objects.all()

#     context = {
#         'blog' : blog_model
#     }
#     return render(request, 'community.html', context)

# def community_view(request, blog_id):
#     blog_model = Blog.objects.all()
#     blog = get_object_or_404(Blog, pk=blog_id)
    

#     context = {
#         'blog' : blog,
#         'blog_model' : blog_model
#     }
#     return render(request, 'community_view.html', context)

# def community_delete(request):
#     return render(request, 'community_delete.html')

# def community_reply(request):
#     return render(request, 'community_reply.html')

# def community_update(request):
#     return render(request, 'community_update.html')



# def community_write(request):
#     return render(request, 'community_write.html')

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def location(request):
    return render(request, 'location.html')

def search(request):
    return render(request, 'search.html')

class community(ListView):
    template_name = 'community.html'
    context_object_name = 'blog_list' 
    def get_queryset(self):
        return Blog.objects.all

class community_view(DetailView):
    model = Blog
    template_name = 'community_view.html'
    context_object_name = 'blog'

class community_delete(DeleteView):
    model = Blog
    template_name = 'community_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('community')

class community_update(UpdateView):
    model = Blog
    template_name = 'community_update.html'
    fields = ['title','text']
    success_url = reverse_lazy('community')

class community_write(CreateView):
    model=Blog
    template_name='community_write.html'
    fields=['title','text']

    def form_valid(self,form):
        Blog=form.save(commit=False)
        Blog.author=self.request.user
        Blog.save()

        return HttpResponseRedirect(self.request.POST.get('next','/'))

def comment_write(request, post_pk):
    if request.method == 'POST':
        post=get_object_or_404(Blog, pk=post_pk)
        content=request.POST.get('comment_contents')
        context = {
            'post_pk' : post_pk
        }

        Comment.objects.create(post=post, comment_write=writer,comment_contents=content)
        return HttpResponseRedirect(reverse_lazy('community', context))