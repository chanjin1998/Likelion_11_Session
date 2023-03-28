from django.shortcuts import render,get_object_or_404,redirect
# Create your views here.
from .models import Blog
from django.http import HttpResponse

def home(request):
  blogs = Blog.objects.all() #Blog에 있는 객체 전부 가져오기
  return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
  blog = get_object_or_404(Blog, pk=blog_id)
  return render(request,'detail.html',{'blog':blog})

#뒤에 블로그가 위에 블로그 앞에 블로그가 html 블로그
def new(request):
  return render(request,'new.html')

def create(request):
  new_blog = Blog()
  new_blog.title = request.POST['title']
  new_blog.content = request.POST['content']
  new_blog.save()
  return redirect('detail',new_blog.id)