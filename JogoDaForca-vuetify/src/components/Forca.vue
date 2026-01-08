<script setup>
//imports
import { ref, watch } from "vue";
import Teclado from "./Teclado.vue";

//propriedades
const props = defineProps({
  palavra: String,
  reiniciarPalavra: Boolean,
  reiniciarTeclado: Boolean,
});

//emits
const emits = defineEmits(["onTentarLetra"]);

//constantes e variáveis

const palavra = ref(""); //LISTA DE OBJETOS EM QUE CADA OBJETO CONTÉM AS CHAVES ID, ENCONTRADA E VALOR (PARA CADA LETRA DA PALAVRA);

//referencias de estado
const encontradas = ref(0);

function validarVogais(letra) {
  const acentosA = ["Á", "Â", "Ã"];
  const acentosE = ["É", "Ê"];
  const acentosI = ["Í"];
  const acentosO = ["Ó", "Õ", "Ô"];
  const acentosU = ["Ú"];

  function filtrar(lista) {
    let filtro = palavra.value.filter((dadosPalavra) =>
      lista.find((letraAcentos) => {
        if (dadosPalavra.valor === letraAcentos) {
          encontradas.value += 1;
          return (dadosPalavra.encontrada = true);
        }
      })
    );

    return filtro;
  }

  if (letra === "A") {
    let filtro = filtrar(acentosA);
    if (encontradas.value === 0) {
      emits("onTentarLetra", "errou");
    }
    else{
    return filtro;}
  } else if (letra === "E") {
    let filtro = filtrar(acentosE);
    return filtro;
  } else if (letra === "I") {
    let filtro = filtrar(acentosI);
    return filtro;
  } else if (letra === "O") {
    let filtro = filtrar(acentosO);
    return filtro;
  } else if (letra === "U") {
    let filtro = filtrar(acentosU);
    return filtro;
  }
}

//funções
function validarLetra(letra) {
  encontradas.value = 0;
  let filtroVogais = validarVogais(letra);

  let filtroConsoantes = palavra.value.filter((v) => {
    if (v.valor === letra) {
      encontradas.value += 1;
      return (v.encontrada = true);
    }
  });

  if (filtroVogais) {
    console.log("CAIU EM FILTROVOGAIS");
    return;
  }

  if (filtroConsoantes) {
    console.log("CAIU EM CONSOANTES");
    if (encontradas.value > 0) {
      emits("onTentarLetra", encontradas.value);
      encontradas.value = 0;
    } else {
      emits("onTentarLetra", "errou");
    }
  }
}

//watchs
watch(
  () => props.reiniciarPalavra,
  (v) => {
    if (v) {
      palavra.value = props.palavra.split("").map((v, id) => {
        return { id, encontrada: false, valor: v };
      });
    }
  },
  { immediate: true }
);

watch(
  () => props.palavra,
  (v) => {
    if (v != palavra.value) {
      palavra.value = props.palavra.split("").map((v, id) => {
        return { id, encontrada: false, valor: v };
      });
    }
  }
);

watch(
  () => encontradas.value,
  (v) => {
    if (v) {
      return console.log(v);
    }
  },
  { immediate: true }
);
</script>

<template>
  <div class="conteiner_principal">
    <div class="forca">
      <div class="palavra" v-for="letra in palavra" :key="letra.id">
        <span v-if="letra.encontrada">{{ letra.valor }}</span>
        <span v-else> - </span>
      </div>
    </div>
  </div>
  <Teclado @onTeclar="validarLetra" :reiniciarTeclado="reiniciarTeclado" />
</template>

<style scoped>
.conteiner_principal {
  display: flex;
  flex-direction: column;
  justify-content: center;
  justify-items: center;
  align-items: center;
  height: 30vh;
  width: 600px;
  margin-top: 40px;
  gap: 10px;
}

.forca {
  display: flex;
}

.palavra {
  font-size: 50px;
  font-family: Arial, Helvetica, sans-serif;
  padding: 30px;
}
</style>
