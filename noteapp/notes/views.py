from django.shortcuts import render, HttpResponse, redirect
from .models import Note
# Create your views here.
def home(request):
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
    notes.create(title="adding new note", content="hello 02")

    return redirect(home)

def delete_note(request, id:int):
    note= Note.objects.get(id=id)
    note.delete()

    return redirect(home)