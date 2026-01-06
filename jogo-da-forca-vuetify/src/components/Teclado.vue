<script setup>

import { ref, watch } from 'vue';
//imports

//propriedades
const props = defineProps({ reiniciarTeclado: Boolean })

//emits
const emits = defineEmits(["onTeclar"])

//constantes e variáveis

//estados
const alfabeto = "QWERTYUIOPASDFGHJKLÇZXCVBNM";
const teclado = ref(alfabeto.split("").map((v, id) => { return { id: id, teclada: false, valor: v } }));

//funções
function teclar(letra) {
    emits("onTeclar", letra.valor);
    return letra.teclada = true

}

//watchs
watch(() => props.reiniciarTeclado, (v) => {
    if (v) {
        teclado.value =  alfabeto.split("").map((v, id) => { return { id: id, teclada: false, valor: v } })
    }
}, { immediate: true })
</script>

<template>
    <div class="conteiner_principal">
        <div class="conteiner_teclado">
            <div class="teclado" v-for="letra in teclado" :key="letra.id">
                <v-btn :disabled="letra.teclada" @click="teclar(letra)" class="tecla" width="40" height="64">{{
                    letra.valor }}</v-btn>
            </div>
        </div>
    </div>
</template>

<style scoped>
.conteiner_principal {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 110vh;
}

.conteiner_teclado {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    width: 600px;
    gap: 2px;


}

.tecla {
    font-size: 50px;
    background-color: #01579B;
    color: #FFFF8D;
}
</style>