<script setup>

//imports
import { ref, watch } from 'vue';
import Teclado from './Teclado.vue';

//propriedades
const props = defineProps({ palavra: String, reiniciarPalavra: Boolean, reiniciarTeclado: Boolean })

//emits
const emits = defineEmits(["onTentarLetra"])

//constantes e variáveis
const palavra = ref(props.palavra.split("").map((v, id) => { return { id, encontrada: false, valor: v } }))
const vogais = "AEIOU".split("");
const consoantes = "BCDFGHJKLMNPQRSTVWXYZ".split("");

//referencias de estado
const encontradas = ref(0);


//funções
function validarLetra(letra) {
    
    palavra.value.filter((v) => {
        if (v.valor === letra) {
            v.encontrada = true
            encontradas.value += 1
            return v.valor
        }
    })

    if (encontradas.value > 0) {
        emits("onTentarLetra", encontradas.value);
        encontradas.value = 0;

    } else {
        emits("onTentarLetra", "errou")
    }
}

//watchs
watch(() => props.reiniciarPalavra, (v) => {
    if (v) {
        palavra.value = props.palavra.split("").map((v, id) => { return { id, encontrada: false, valor: v } })
    }
}, { immediate: true })
</script>

<template>
    <div class="conteiner_principal">
        <div class="forca">
            <div class="palavra" v-for="letra in palavra">
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
    justify-content: center;
    align-items: center;
    height: 30vh;
    margin-top: 100px;
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
