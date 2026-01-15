<script setup>
import beatles from "../assets/beatles.png";
import O_Mundo_de_Beakman from "../assets/O_Mundo_de_Beakman.webp";
</script>
<template>
  <v-layout>
    <v-container>
      <div>
        <v-row class="d-flex align-center justify-center flex-column">
          <p class="text-h3">Bem-Vindo!</p>
          <p class="text-h6">Me chamo Leo Andrighetto</p>
        </v-row>

        <v-row
          class="d-flex align-center justify-center mt-10 ga-4 flex-column text-overline"
        >
          Antes de conhecer minhas habilidades, eis alguns conteúdos que me
          representam:</v-row
        >

        <v-row class="d-flex align-stretch ga-3 justify-center">
          <v-card density="comfortable" elevation="24">
            <v-card-title> The Beatles </v-card-title>
            <v-card-subtitle>Grupo Musical Preferido</v-card-subtitle>
            <v-card-item class="d-flex justify-start">
              <v-img
                class="d-flex align-end"
                cover
                :src="beatles"
              />
              <p class="ma-2">Uma banda que me inspira até hoje</p>
            </v-card-item>
            <v-card-actions>
              <v-btn
                href="https://music.youtube.com/channel/UC2XdaAVUannpujzv32jcouQ"
                target="_blank"
              >
                explorar</v-btn
              >
            </v-card-actions>
          </v-card>

          <v-card density="comfortable" elevation="24">
            <v-card-title> O Mundo de Beakman </v-card-title>
            <v-card-subtitle>Programa de TV retrô preferido</v-card-subtitle>
            <v-card-item>
              <v-img
                height="270"
                cover
                :src="O_Mundo_de_Beakman"
              />

              <p class="ma-2">Um programa que me ensinou a ser curioso</p>
            </v-card-item>

            <v-card-actions class="d-flex align-end">
              <v-btn
                target="_blank"
                href="https://www.youtube.com/watch?v=foZpk8s1a94&list=PL-t1336xq7ymurqPDexSW0k_aL0x0LOV2"
                >explorar</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-row>
      </div>
    </v-container>
  </v-layout>
</template>
