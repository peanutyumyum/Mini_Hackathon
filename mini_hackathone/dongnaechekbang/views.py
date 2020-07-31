from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog, Bookstore, Evaluation_about_bookstore, Informations
# import model data
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, 'home.html')

def location(request):
    bookstore_model = Bookstore.objects.all()
    evaluation_about_bookstore_model = Evaluation_about_bookstore.objects.all()
    informations_model = Informations.objects.all()
    # insert model information to use in location.html

    context = {
        'bookstore' : bookstore_model, 
        'evaluation_about_bookstore' : evaluation_about_bookstore_model, 
        'informations' : informations_model, 
    }
    # declare variable
    
    return render(request, 'location.html', context)

def location_bookstore(request, bookstore_id):

    bookstore = get_object_or_404(Bookstore, pk=bookstore_id)
    bookstore_model = Bookstore.objects.all()
    # insert model information to use in location_bookstore.html

    """ city_address_of_bookstore_을지로_model = bookstore_model.filter(city_address_of_bookstore='을지로')
    city_address_of_bookstore_망원동_model = bookstore_model.filter(city_address_of_bookstore='망원동')
    # to list city address of bookstore """
    # 사용 안합니다

    context = {
        'bookstores' : bookstore, 
        'bookstore' : bookstore_model
    }
    # declare variable

    return render(request, 'location_bookstore.html', context)

def search(request):
    return render(request, 'search.html')

def result(request):
    bookstoreinfo = Bookstore.objects.all()
    query = request.GET.get('query','') 
    search_type = request.GET.get('type','')
    if query:
        if search_type == 'all':
            bookstoreinfo = bookstoreinfo.filter(Q(name__icontains=query)| Q(city_address_of_bookstore__icontains=query) | Q(trait__icontains=query)|Q(bookstore_information__icontains=query))
        elif search_type == 'name':
            bookstoreinfo = bookstoreinfo.filter(name__icontains=query)
        elif search_type == 'city_address_of_bookstore':
            bookstoreinfo = bookstoreinfo.filter(city_address_of_bookstore__icontains=query)
        elif search_type == 'trait':
            bookstoreinfo = bookstoreinfo.filter(trait__icontains=query)
        elif search_type == 'bookstore_information':
            bookstoreinfo = bookstoreinfo.filter(bookstore_information__icontains=query)
    return render(request, 'result.html',{'bookstoreinfo':bookstoreinfo , 'query':query})

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