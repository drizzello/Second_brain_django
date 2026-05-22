from django.shortcuts import get_object_or_404, redirect, render
from backend.apps.notes.models import Note
from backend.apps.accounts.models import User
from backend.apps.notes.services import create_note
from .forms import NoteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request=request, template_name="notes/home.html")

@login_required
def list_notes(request):
    note = Note.objects.filter(owner=request.user)
    ctx = {
        "notes": note
    }
    return render(request=request, template_name="notes/list_notes.html", context=ctx)

@login_required
def note_detail(request, pk):
    nota = get_object_or_404(Note, pk=pk)
    ctx = {
        "note": nota
    }
    return render(request=request, template_name="notes/note_detail.html", context=ctx)

@login_required
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            create_note(
                user=request.user,
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
            )
            messages.add_message(request, messages.SUCCESS ,message="Nota aggiunta con successo")
            return redirect("notes:list")
    else:
        form = NoteForm()

    return render(request, "notes/new_note_form.html", {"form": form})

@login_required
def delete_note(request, pk):
    if request.method == "POST":
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        messages.add_message(request, messages.SUCCESS ,message="Nota eliminata con successo")
        return redirect("notes:home")
    
    return redirect("notes:home")

@login_required
def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save(update_fields=["title", "content"])
            messages.add_message(request, messages.SUCCESS ,message="Nota aggiornata con successo")
            return redirect("notes:home")

    else:
        form = NoteForm(instance=note)

    return render(request, "notes/update_note_form.html", {"form": form, "note": note})
