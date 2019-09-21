from django.shortcuts import render, HttpResponse, redirect
from .models import Note
def index(request):
    context = {
        "all_notes" : Note.objects.all()
    }
    return render(request, "learnAjaxApp/index.html", context)

def AddNote(request):
    Note.objects.create(title=request.POST['note-title'])
    return redirect("/")