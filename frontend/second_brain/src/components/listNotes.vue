<script setup>
import {ref} from 'vue'
import UpdateNote from './updateNote.vue';


    const props = defineProps({
        "itemsList":  Array
    })

    const emit = defineEmits(['update-list'])

    const showUpdateForm = ref(false);
    const selectedNote = ref(null)

    function startUpdate(note){
        showUpdateForm.value = !showUpdateForm.value
        selectedNote.value = note
    }

    function handleUpdate(updatedNote){
        emit('update-list', updatedNote)
    
    // Opzionale: chiudi il form e resetta la selezione
    showUpdateForm.value = false;
    selectedNote.value = null;
    }

</script>


<template>
    <h1>List notes</h1>
    <table>
        <thead>
            <tr>
                <th scope="col">Note id</th>
                <th scope="col">Note Title</th>
                <th scope="col">Note Tag</th>
                <th scope="col">Note action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in itemsList" :key="item.title">
                <td>{{item.id}}</td>
                <td>{{item.title}}</td>
                <td>
                {{item.tag}}
                </td>
                <td>
                    <button @click="startUpdate(item)">
                        Update
                    </button>
                </td>
            </tr>
        </tbody>
    </table>

    <UpdateNote @update-note="handleUpdate" :note-to-update="selectedNote" v-if="showUpdateForm"/>


</template>

<style lang="css" scoped>
th,
td {
  border: 1px solid rgb(160 160 160);
  padding: 8px 10px;
}

th[scope="col"] {
  background-color: #505050;
  color: white;
}

th[scope="row"] {
  background-color: #d6ecd4;
}

td {
  text-align: center;
}

tr:nth-of-type(even) {
  background-color: #eeeeee;
}

table {
  border-collapse: collapse;
  border: 2px solid rgb(140 140 140);
  font-family: sans-serif;
  font-size: 0.8rem;
  letter-spacing: 1px;
}

</style>