<script setup>

    import { ref } from 'vue'
    import NotesApiCommon from '../api/notes'

    const title = ref("")
    const content = ref("")

    function cleanNoteForm() {
        title.value = ""
        content.value = ""
        }

    async function addNote(note_id) {
        let item = {
            title: title.value,
            content: content.value
        }
        console.log(item)
        try{
            await NotesApiCommon.addNote(item)
            cleanNoteForm()
        }
        catch(error){
            console.error(error);
        }
    }

</script>

<template>
<form @submit.prevent="addNote">
      <p>
        <label for="title">Titolo (required):</label>
        <input type="text" name="title" id="title" :value="title" @input="event => title = event.target.value" required />
      </p>
      <p>
        <label for="content">Content (required):</label>
        <input type="text" name="Content" v-model="content" id="Content" required />
      </p>
      <button type="submit">Invia</button>
</form>
</template>