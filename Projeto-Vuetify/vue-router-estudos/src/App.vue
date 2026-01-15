<template>
  <v-app class="bg-teal-lighten-4">
    <v-app-bar flat position="fixed" class="border-b bg-teal-darken-1">
      <template v-slot:prepend>
        <v-app-bar-nav-icon @click="abrirNavigation"></v-app-bar-nav-icon>
        <v-app-bar-title>App do LeLéo</v-app-bar-title>
      </template>
    </v-app-bar>

    <appNavigation @update:flag="abrirNav = $event" :flag="abrirNav" />

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from "vue";
import AppNavigation from "./components/AppNavigation.vue";

const abrirNav = ref(false);

function abrirNavigation() {
  abrirNav.value = !abrirNav.value;
}
</script>

<!-- 

App.vue é o conteiner principal do projeto inteiro.

-->
