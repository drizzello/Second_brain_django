<script setup>

    import NotesApiCommon from '../api/notes'
    import { ref } from 'vue';

    const props = defineProps({
        "itemsList":  Array
    });
    const emit = defineEmits(['noteDeleted'])

    async function removeNote () {
        if(!selectedNoteId){
            console.log("Nessuna nota selezionata")
            return
        }
        else{
            await NotesApiCommon.deleteNote(selectedNoteId.value)
            emit('noteDeleted', selectedNoteId.value)
        }
    };
    const selectedNoteId = ref(null)

    function openDialog (){
        if (window.confirm("Do you want to delete the note?")) {
            removeNote()
        }
        else{
            console.log("operazione annullata")
        }
    };

</script>

<template>
    <form @submit.prevent="openDialog">
        <select v-model="selectedNoteId">
            <option v-for="item in itemsList" :value="item.id">
                {{ item.title }}
            </option>
        </select>
        <button type="submit">Elimina</button>
    </form>
</template>