from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from .models import module as Module
from .models import comment as Comment
from .models import Tag as Tag
from .forms import ModuleForm, CommentForm,TagForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import requires_csrf_token, csrf_protect

@csrf_protect
def loginUser(request):
    page ='login'
    if request.user.is_authenticated:
        return redirect('modules')

    if request.method =='POST' :
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
          login(request,user)
          return redirect('modules')
        else:
            print(request, 'Username OR password is incorrect')
    return render(request, 'modules/login_register.html')

def registerUser(request):
    page ='register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request,'User account was created')

            login(request,user)
            return redirect('modules')

        else:
         pass
    context ={'page': page,'form': form}
    return render(request,'modules/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect ('login')


def modules(request):
    modules = Module.objects.all()
    context = {'modules' :modules}
    return render(request, 'modules/modules.html', context)

def comments(request):
    comments = Comment.objects.all()
    context = {'comments':comments}
    return render(request,'modules/comment.html', context)

def tags(request):
    tags=Tag.objects.all()
    context = {'tags':tags}
    return render(request,'modules/tags.html',context)
    
   


def module(request,pk):
    moduleObj = Module.objects.get(id=pk)
    return render(request, 'modules/single-module.html', {'module':moduleObj})

def createModule(request):
    form = ModuleForm()

    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modules')
    context = {'form' : form}
    return render(request, "modules/module_form.html", context)

def updateEvent(request) :
    event = Module.objects.get(id=request.user.id)
    form =EventForm(instance=event)

    if request.method == "POST":
        form =ModuleForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'members/upcoming_events.html', context)


def update_user(request):

current_user = User.objects.get(id=request.user.id)
form = Signupform(request.POST or None, instance=current_user)
if form.is_valid():
form.save()
login(request, profile)




@requires_csrf_token   
def deleteModule(request,pk) :
    mod = Module.objects.get(id=pk)
    if request.method == "POST":
        mod.delete()
        return redirect('modules')
    context = {'object':mod}
    return render(request, 'modules/delete_template.html', context)

def createComment(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments')
    context = {'form': form}
    return render(request, "modules/comment_form.html", context)

def updateComment(request,pk):
    com= Comment.objects.get(id=pk)
    form= CommentForm(instance=com)

    if request.method == 'POST':
        form=TagForm(request.POST, instance=com)
        if form.is_valid():
            form.save()
            return redirect('modules')
    
    context = {'form': form}
    return render(request,'modules/comment_form.html', context)



@requires_csrf_token   
def deleteComment(request,pk) :
    com = Comment.objects.get(id=pk)
    if request.method == "POST":
        com.delete()
        return redirect('comments')
    context = {'object':com}
    return render(request, 'modules/delete_template.html', context)

   
def createTag(request):
    form = TagForm()

    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags')

    context = {'form': form}
    return render(request, "modules/tag_form.html", context)

def updateTag(request, pk):
    tag= Tag.objects.get(id=pk)
    form= TagForm(instance=tag)

    if request.method == 'POST':
        form=TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('modules')
    
    context = {'form': form}
    return render(request,'modules/tag_form.html', context)

@requires_csrf_token   
def deleteTag(request,pk) :
    tag = Tag.objects.get(id=pk)
    if request.method == "POST":
        tag.delete()
        return redirect('modules')
    context = {'object':tag}
    return render(request, 'modules/delete_template.html', context)

# Create your views here.
