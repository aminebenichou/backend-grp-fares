from django.shortcuts import render, HttpResponse, redirect
from .models import Note
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

def home(request):

    if request.method == 'POST':
        query = request.POST.get('query')
        return redirect(f"search/{query}")


    notes = Note.objects.all()
    result = []
    if len(notes) == 0:
        return HttpResponse("No Notes Available")
    else:
        for note in notes:
            result.append(note)  
        if request.user != None:
            username=request.user

        print(username)
        context={
            'notes': result,
            'message':'hello world',
            'username': username,
            'islogged':True
        }
        return render(request, 'index.html', context)

def create_note(request):
    notes = Note.objects.all()
    title = request.POST.get('title')
    content = request.POST.get('content')
    

    notes.create(title=title, content=content)

    return redirect(home)

def delete_note(request, id:int):
    note= Note.objects.get(id=id)
    note.delete()

    return redirect(home)

def search_view(request, query:str):
    notes= Note.objects.filter(title=query)
    return render(request, 'index.html', {'notes':notes})


def edit_note(request, id:int):
    # Get (getting data from db)
    note = Note.objects.get(id=id)
    
    if request.method == 'GET':
        context = {
            'note':note
        }
        return render(request, 'edit.html', context)
    
    # POST (sending data to db)
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        note.title=title
        note.content=content
        note.save()

        return redirect(home)
    
def sign_in(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect(home)
        else:
            return render(request, 'signin.html')
        
    
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        return redirect(sign_in)
    
def signout(request):
    logout(request)
    return redirect(sign_in)