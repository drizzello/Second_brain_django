<script setup>
import { ref, computed } from 'vue'
import Home from './Home.vue'
import Operations from './Operations.vue'

const NotFound = {
  template: '<h1>Page not found</h1>'
}

const routes = {
  '/': Home,
  '/operations': Operations
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>

<template>
  <a href="#/">Home</a> |
  <a href="#/operations">Operations</a>
  <component :is="currentView" />
</template>
