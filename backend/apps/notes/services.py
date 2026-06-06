from openai import OpenAI
from pydantic import BaseModel
from apps.accounts.models import User
from apps.notes.models import Tags, Note
from django.conf import settings

DEBUG = True

class NoteTaggingResult(BaseModel):
    tag: Tags

def tag_note(note_title: str, note_content: str) -> Tags:
    client = OpenAI(api_key=settings.OPENAI_KEY)
    if DEBUG == True:
        return Tags.STUDY.value
    response =  client.responses.parse(
        model="gpt-5.5",
        input=[
            {"role": "system", "content": "Extract the tag from note context."},
            {
                "role": "user",
                "content": f"{note_title, note_content}",
            },
        ],
        text_format=NoteTaggingResult,
    )
    return response.output_parsed.tag

def create_note(*, user: User, title: str, content: str) -> Note:
    tag = tag_note(title, content)

    return Note.objects.create(
        owner=user,
        title=title,
        content=content,
        tag=tag,
    )