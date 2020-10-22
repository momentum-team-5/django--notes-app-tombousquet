from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, mail_admins
from .models import Note
from .forms import NoteForm, ContactForm, SearchForm

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

def contact_us(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            send_confirmation = form.cleaned_data['email']
            message_title = form.cleaned_data['title']
            message_body = form.cleaned_data['body']
            send_mail("Message delivered", "Due to COVID-19, message are responded to on a monthly basis", None, recipient_list=[send_confirmation])
            mail_admins(message_title, message_body, fail_silently=True)
        return redirect(to='notes_list')
    return render(request, "notes/contact_us.html", {'form': form})

def notes_search(request):
    if request.method == "GET":
        form = SearchForm()
    else:
        form = SearchForm(data=request.POST)
        if form.is_valid():
            notes = Note.objects.all()
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            order_by = form.cleaned_data['order_by']
            if title:
                title_search_type = form.cleaned_data['title_search_type']
                if title_search_type == "starts with":
                    notes = notes.filter(title__startswith=title)
                elif title_search_type == "includes":
                    notes = notes.filter(title__contains=title)
                else:
                    notes = notes.filter(title__exact=title)
            if body:
                notes = notes.filter(body__contains=body)
                body_search_type = form.cleaned_data['body_search_type']
                if body_search_type == "starts with":
                    notes = notes.filter(body__startswith=body)
                elif body_search_type == "includes":
                    notes = notes.filter(body__contains=body)
                else:
                    notes = notes.filter(body__exact=body)
            notes = notes.order_by(order_by)
            return render(request, "notes/search_results.html", {"notes": notes})
    return render(request, "notes/notes_search.html", {"form": form})                                                                