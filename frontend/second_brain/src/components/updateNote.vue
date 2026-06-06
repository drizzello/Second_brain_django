<script setup lang="ts">

    import { ref } from 'vue'
    import NotesApiCommon from '../api/notes'

    type Note = {
        id: number,
        title: string,
        content: string
        tag: string
    };
    const props = defineProps<{
        noteToUpdate: Note
    }>();

    const emits = defineEmits(['updateNote', 'updatedNote'])

    const title = ref(props.noteToUpdate.title)
    const content = ref(props.noteToUpdate.content)
    const tag = ref(props.noteToUpdate.tag)
    const note_id = ref(props.noteToUpdate.id)

    function cleanNoteForm() {
        title.value = ""
        content.value = ""
        }

    async function updateNote() {
        let item = {
            id: note_id.value,
            title: title.value,
            content: content.value,
            tag: tag.value
        }
        console.log(item)
        try{
            await NotesApiCommon.updateNote(item)
            emits('updateNote', item)
            cleanNoteForm()
        }
        catch(error){
            console.error(error);
        }
    }

</script>

<template>
<form @submit.prevent="updateNote">
      <p>
        <label for="title">Titolo (required):</label>
        <input type="text" name="title" id="title" v-model="title" required />
      </p>
      <p>
        <label for="content">Content (required):</label>
        <input type="text" name="Content" v-model="content" id="Content" required />
      </p>
      <button type="submit">Invia</button>
</form>
</template>