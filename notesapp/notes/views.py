from django.shortcuts import render, get_object_or_404
from .models import Note

def notes_list(request):
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html",
                    {"notes": notes})

def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/notes_detail.html",
                 {"note": note})