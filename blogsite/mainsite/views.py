from django.shortcuts import render, HttpResponse
import json
from .models import BlogPost
# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def Home(request):
    if request.method == 'GET':
        allBlogPosts = BlogPost.objects.all()
        context = {'posts':allBlogPosts}
        return render(request, 'home.html', context)

def uploadContent(request):
    if is_ajax(request) and request.method == 'POST':
        blogContent = request.POST['content']
        blogObj = BlogPost.objects.create(content = blogContent)
        blogObj.save()
        return HttpResponse(json.dumps({'value':True}))

def editContent(request, id):
    if request.method == 'POST' and is_ajax(request):
        try:
            postObj = BlogPost.objects.get(id=id)
            postObj.content = request.POST['content']
            postObj.save()
            return HttpResponse(json.dumps({'value': True}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'value':False}))
def delPost(request, id):
    if request.method == 'POST' and is_ajax(request):
        try:
            obj_ = BlogPost.objects.get(id=id)
            obj_.delete()
            return HttpResponse(json.dumps({'value': True}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'value':False}))
