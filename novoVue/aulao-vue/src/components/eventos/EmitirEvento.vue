<template>

    <div>
        <h1>Componente que emite evento</h1>
        <p>{{ item }} | {{ preco.toFixed(2) }}</p>
        <br>
        <button @click="adicionar">Adicionar Ao Carrinho</button>
    </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
    item: String,
    preco: Number
})

const emit = defineEmits(["adicionado"])

function adicionar(){
    emit("adicionado", props.preco)
}



</script>

<style scoped>
div{
    background-color: rgb(22, 48, 194);
    margin: 30px;
    padding: 20px;
    border-radius: 20px;
    font-size: 5pt;
}

button{

    font-size: 5pt;
}

</style>