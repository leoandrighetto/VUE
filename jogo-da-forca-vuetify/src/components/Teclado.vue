<script setup>
import { ref, watch } from "vue";
//imports

//propriedades
const props = defineProps({ reiniciarTeclado: Boolean });

//emits
const emits = defineEmits(["onTeclar"]);

//constantes e variáveis

//estados
const alfabeto = "QWERTYUIOPASDFGHJKLÇZXCVBNM";
const teclado = ref(
  alfabeto.split("").map((v, id) => {
    return { id: id, teclada: false, valor: v };
  })
);

//funções
function teclar(letra) {
  emits("onTeclar", letra.valor);
  return (letra.teclada = true);
}

// //watchs
// watch(() => props.reiniciarTeclado, (v) => {

//     if (v) {
//         console.log(v);
//         teclado.value =  alfabeto.split("").map((v, id) => { return { id: id, teclada: false, valor: v } })
//     }

// }, { immediate: true })
</script>

<template>
  <v-container>
    <v-row>
      <v-col lg="8">

        <v-responsive width="100%"> </v-responsive>

        <div class="d-flex flex-wrap justify-center ga-2">

          <v-btn

            v-for="letra in teclado"
            :key="letra.id"
            :disabled="letra.teclada"
            @click="teclar(letra)"
            color="#01579b"
            text-color="#ffff8d"
            width="40"
            height="64"

            >{{ letra.valor }}
          </v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.tecla {
  font-size: 50px;
  background-color: #01579b;
  color: #ffff8d;
}
</style>
