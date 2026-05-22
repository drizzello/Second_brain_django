from ninja import NinjaAPI

from apps.notes.services import create_note
from apps.notes.schema import NoteCreateIn, NoteOut, NotFoundSchema, NoteUpdateIn
from apps.notes.models import Note

api = NinjaAPI()

@api.get("/notes", response=list[NoteOut])
def NoteList(request):
    return Note.objects.filter(owner=request.user)

@api.post("/notes/add", response={201: NoteOut})
def CreateNote(request, payload: NoteCreateIn):
    nota = create_note(
        user=request.user,
        title=payload.title,
        content=payload.content
        )
    return 201, nota

@api.put("/notes/update/{note_id}", response={200: NoteOut, 404: NotFoundSchema})
def UpdateNote(request, note_id: int, data: NoteUpdateIn):
    try:
        note = Note.objects.get(pk=note_id)
        for attribute, value in data.dict().items():
            setattr(note, attribute, value)
        note.save()
        return 200, note
    except Note.DoesNotExist as e:
        return 404, {"message": "Could not find note"}

@api.get("/notes/{note_id}", response={200: NoteOut, 404: NotFoundSchema})
def NoteDetail(request, note_id):
    try: 
        nota = Note.objects.get(pk=note_id)
        return 200, nota
    except Note.DoesNotExist as e:
        return 404, {"message": "could not find note"}
    
@api.delete("/notes/delete/{note_id}", response={200: None, 404: NotFoundSchema})
def delete_track(request, note_id: int):
    try:
        note = Note.objects.get(pk=note_id)
        note.delete()
        return 200
    except Note.DoesNotExist as e:
        return 404, {"message": "Could not find note"}
