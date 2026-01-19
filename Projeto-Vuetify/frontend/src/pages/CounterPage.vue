<template>
  <v-container>
    <v-row>
      <v-col
        class="d-flex flex-column align-center font-weight-semibold text-h2">

      <v-card height="300" width="500" class="d-flex flex-column align-center justify-center text-center">

        <div class="text-light-blue-darken-4">Contador Básico</div>

        <div class="d-flex text-light-blue-darken-4 ga-16 mt-16 align-center font-weight-black text-h3">

          <v-btn @click="count--" class=" text-light-blue-darken-4 border-0 rounded-pill text-h3"  height="70" width="70">-</v-btn>

          <p>{{ count }}</p>

          <v-btn @click="count++" class="text-light-blue-darken-4 border-0 rounded-pill text-h3" height="70" width="70">+</v-btn>

        </div>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";

const count = ref(0);
</script>
