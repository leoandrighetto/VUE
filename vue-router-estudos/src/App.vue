<template>
  <v-app class="bg-teal-lighten-4">
    <v-app-bar flat position="fixed" class="border-b bg-teal-darken-1">
      <template v-slot:prepend>
        <v-app-bar-nav-icon @click="abrirNavigation"></v-app-bar-nav-icon>
        <v-app-bar-title>App do LeLéo</v-app-bar-title>
      </template>
    </v-app-bar>

    <v-navigation-drawer v-model="abrirNav" class="bg-teal-lighten-5">
      <v-list class="text-medium-emphasis text-h6">
        <v-list-item prepend-icon="mdi-home" to="Home">Home</v-list-item>
        <v-list-item prepend-icon="mdi-account" to="Auth">Autenticação</v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from "vue";

const abrirNav = ref(false);

function abrirNavigation() {
  abrirNav.value = !abrirNav.value;
}
</script>

<!-- 

App.vue é o conteiner principal do projeto inteiro.

-->
