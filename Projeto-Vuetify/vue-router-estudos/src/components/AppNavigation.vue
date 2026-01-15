<template>
  <v-navigation-drawer
    @update:model-value="$emit('update:flag', $event)"
    :model-value="props.flag"
    class="bg-teal-lighten-5"
    elevation="4"
    
  >
    <v-list class="text-medium-emphasis text-h6">
      <v-list-item prepend-icon="mdi-home" to="/">Home</v-list-item>
      <v-list-item prepend-icon="mdi-account" to="/Auth"
        >Autenticação</v-list-item
      >
      <v-list-item prepend-icon="mdi-counter" to="/CounterPage"
        >Contador Básico</v-list-item
      >
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
const props = defineProps({ flag: Boolean });

</script>
