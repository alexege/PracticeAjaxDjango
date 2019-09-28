from django.shortcuts import render, HttpResponse, redirect
from .models import Note
def index(request):
    context = {
        "all_notes" : Note.objects.all(),
    }
    return render(request, "learnAjaxApp/index.html", context)

def note(request):
    if request.method == 'POST':
        print(request.POST)
        Note.objects.create(title=request.POST['note-title'])

    context = {
        'all_notes' : Note.objects.all()
    }
    return render(request, "learnAjaxApp/notes_index.html", context)