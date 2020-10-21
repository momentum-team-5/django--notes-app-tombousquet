from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, mail_admins
from .models import Note
from .forms import NoteForm, ContactForm

def notes_list(request):
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html",
                    {"notes": notes})

def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/notes_detail.html",
                 {"note": note})

def notes_add(request):
    if request.method == "GET":
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect(to="notes/notes_list")
    return render(request, "notes/notes_add.html", {"form": form})   

def notes_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "GET":
        form = NoteForm(instance=note)
    else:
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(to="notes_list")
    return render(request, "notes/notes_edit.html", {"form": form})

def notes_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect(to="notes_list")

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(data.request.POST)
        if form.is_valid():
            send_confirmation = form.cleaned_data['email']
            message_title = form.cleaned_data['title']
            message_body = form.cleaned_data['body']
            send_mail("Message delivered", "Due to COVID-19, message are repsonded to on a monthly basis", recipient_list=[send_confirmation])
            mail_admins(message_title, message_body, fail_silently=True)
            return redirect(to='notes_list')
        return render(request, "contact_us.html", {'form': form})                                                     