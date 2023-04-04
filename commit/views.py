from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Version
from .forms import PostForm,UpdatePostForm

def home(request):
    return render(request, 'home.html')
def all_post(request):
    posts=Post.objects.all()
    return render(request, 'all_post.html',  {"posts":posts})
# def view_post(request, id):
#     post=get_object_or_404(Post, id=id)
#     get_post=Post.objects.get(id=id)
#     if request.method == "POST":
#         form=Post(request.POST, instance=post)
#     return render(request, 'view_post.html', {"post":get_post})
def view_post(request, id):
    get_post=Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    versions = post.versions.order_by('-timestamp')
    return render(request, 'view_post.html', {'post': post, 'versions': versions})

def create_post(request):
    if request.method=="POST":
        element=PostForm(request.POST)
        element.save()
    return render(request, 'create_post.html')
# def create_post(sender, instance, created, **kwargs):
#     if created:
#         version = Version(post=instance, desc=instance.desc, version_number=1)
#         version.save()
#     else:
#         latest_version = instance.versions.latest('version_number')
#         if latest_version.content != instance.content:
#             version_number = latest_version.version_number + 1
#             version = Version(post=instance, desc=instance.desc, version_number=version_number)
#             version.save()
#     return render(request, 'create_post.html')
# def update_post(request, id):
#     post=Post.objects.get(id=id)
#     if request.method=="POST":
#         form=Post_version(request.POST, instance=post)
#     return render(request, "update_post.html",{"post":post})
# def update_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     if request.method == 'POST':
#         content = request.POST['content']
#         version_number = post.versions.count() + 1
#         version = Version(post=post, content=content, version_number=version_number)
#         version.save()
#         post.content = content
#         post.save()
#         return redirect('view_post', post_id=id)
#     return render(request, 'update_post.html', {'post': post})
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        version_number = post.versions.count() + 1
        post_version = Version(post=post,version_number=version_number, desc=post.desc)
        post_version.save()
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_post', id=post.id)
    else:
        form = UpdatePostForm(instance=post)
    versions = post.versions.order_by('-timestamp')
    context = {
        'form': form,
        'versions': versions,
    }
    return render(request, 'update_post.html', context)


# def update_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     if request.method == 'POST':
#             form = UpdatePostForm(request.POST, instance=post)
#             if form.is_valid():
#                 title = request.POST['title']
#                 description = request.POST['desc']
#                 post.title = title
#                 post.description = description
#                 post.save()
#                 version_number = post.versions.count() + 1
#                 post_version =Version(post=post, version_number=version_number, desc=description)
#                 post_version.save()
#                 return render(request, 'view_post.html', {'post': post})
#     else:
#         return render(request, 'update_post.html', {'post': post})

# def update_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     versions = post.versions.order_by('-timestamp')

#     if request.method == 'POST':
#         form = UpdatePostForm()(request.POST)
#         if form.is_valid():
#             # Create a new version with the updated content
#             version_number = versions.first().version_number + 1 if versions else 1
#             version = Version(post=post, content=form.cleaned_data['content'], version_number=version_number)
#             version.save()
#             return redirect('post_detail', id=post.id)
#     else:
#         form = PostForm(initial={'desc': post.desc})

#     return render(request, 'update_post.html', {'form': form, 'post': post, 'versions': versions})
