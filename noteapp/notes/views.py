from django.shortcuts import render, HttpResponse, redirect
from .models import Note
# Create your views here.
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

        context={
            'notes': result,
            'message':'hello world'
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