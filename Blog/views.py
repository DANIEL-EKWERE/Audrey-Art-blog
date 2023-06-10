from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from .forms import *
from django.db.models import Q
from taggit.models import Tag
from django.views.generic.edit import CreateView, UpdateView
from django.http import FileResponse
from django.conf import settings
from django.core.paginator import Paginator
import os
# Create your views here.



def download(request):
    file = os.path.join(settings.BASE_DIR, 'Blog/static/images/portrait toon art.png')
    fileOpened = open(file, 'rb')

    return FileResponse(fileOpened)



class CreatePost(CreateView):

    model = Post
    fields = [
        'image',
        'title',
        'author',
        'body',
        'category',
        'slug',
        'tags',
        'status',
    ]
    

    template_name = 'form_upload.html'
    success_url = '/'


class UpdatePost(UpdateView):
    model = Post
    fields = [
         'image',
        'title',
        'author',
        'body',
        'category',
        'slug',
        'tags',
        'status',
    ]

    
    template_name = 'update_form.html'
    success_url = '/'


from django.contrib.auth import logout , login
def Signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email,password=raw_password)
            login(request,user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html',{'form':form})

class Login(LoginView):
    form_class = MyLoginForm
    template_name = 'login.html'
    success_url = ''
    redirect_field_name = '/'

def Logout(request):
    logout(request)
    return redirect('/')


def PreAnimatedVideos(request,pk):
    anim = pk
    videos = PreAnimatedVid.objects.all()
    page = Paginator(videos, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    return render(request, 'anim_videos.html',{"page":page,"anim":anim})

def home(request):
    posts = Post.objects.filter(status='published')[0:6]
    recent_post = posts[0:6]
    category = Category.objects.all()
    videos = AnimatedVid.objects.all()[0:6]
    return render(request, 'index.html',{'posts':posts, 'recent_post':recent_post, 'category':category, "videos":videos,})

def Video(request,pk):
    key = int(pk)
    vid = AnimatedVid.objects.get(id=key)

    return render(request, 'video.html',{"vid":vid})


def Post_Detail(request,pk):
    post = Post.objects.get(id= pk)
    comments = post.comments.filter(active = True)
    recent_post = Post.objects.filter(status = 'published')[0:3]
    category = Category.objects.all()
    # vid = AnimatedVid.objects.get(id=pk)
    comment_form = CommentForm(data=request.POST)

    if request.method == "POST" and comment_form.is_valid():
        body = comment_form.cleaned_data['body']

        try:
            parent = comment_form.cleaned_data['parent']
        except:
            parent = None

        new_comment = BlogComment(body=body,User=request.user,post=post,parent=parent)
        new_comment.save()

    return render(request, 'post_details.html',{'post':post,'recent_posts':recent_post,
                'categoty':category,'comments':comments,'comment_form':comment_form})

def Search_Result(request):

    if request.method == 'POST':
        Query = request.POST['query']
        posts = Post.published.filter(Q(title__icontains = Query) | Q(tags__name__icontains = Query)).distinct()

        recent_posts = Post.objects.filter(status='published')[0:3]
        return render(request, "search.html",{'posts':posts,"recent_posts":recent_posts,'query':Query})

def categories(request,category):
    cate = category

    print(Post.objects.filter(category__title = category))
    posts = Post.objects.filter(category__title = category)
    page = Paginator(posts, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    recent_posts = Post.objects.filter(status = 'published')[0:3]
    return render(request, 'category.html',{'page':page,'cate':cate,"recent_posts":recent_posts,"posts":posts})




def Update(request,book_id):
    iD = int(book_id)
    try:
        post = Post.objects.get(id = iD)
    except Post.DoesNotExist:
        return redirect('/')
    post_form = CreateBook(request.POST or None, instance = post)
    if post_form.is_valid:
        post_form.save()
        return redirect('/')
    return render(request, 'upload_form.html',{"post_form":post})


def Delete(request , post_id):
    id = int(post_id)
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return redirect('/')
    post.delete()
    return redirect('/')


def About(request):
    return render(request, 'about_us_page.html')


# class Login(LoginView):
#     template_name = 'login.html'
#     form_class = SellerLoginForm
#     next_page = 'sale_center'
   
    
   