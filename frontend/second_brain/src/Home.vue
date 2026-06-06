<script setup>
import { ref, onMounted } from 'vue'
import NotesApiCommon from './api/notes'

import ListNotes from './components/listNotes.vue';
import RemoveNote from './components/removeNote.vue';

const itemsList = ref(Array)

onMounted(async () => {
  itemsList.value =  await NotesApiCommon.getNotes()
})

function handleNoteDeleted(deletedId) {
    itemsList.value = itemsList.value.filter(note => note.id !== deletedId)
}

// Questa funzione viene chiamata quando il componente figlio emette 'update-list'
function updateNoteInState(updatedNote) {
    // Troviamo l'indice della nota da aggiornare
    const index = itemsList.value.findIndex(note => note.id === updatedNote.id);
    
    // Se la nota esiste nell'array, la sostituiamo con quella aggiornata
    if (index !== -1) {
        itemsList.value[index] = updatedNote;
    }
}
</script>


<template>
    <ListNotes 
        :items-list="itemsList"
        @update-list="updateNoteInState"/>
    <RemoveNote
        :items-list="itemsList"
        @note-deleted="handleNoteDeleted" />

</template>