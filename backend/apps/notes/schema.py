from ninja import Schema
from .models import Tags

class NoteOut(Schema):
    id: int
    title: str
    content: str
    tag: str

class NoteUpdateIn(Schema):
    title: str
    content: str
    tag: str = Tags.WORK

class NoteCreateIn(Schema):
    title: str
    content: str

class NotFoundSchema(Schema):
    message: str
