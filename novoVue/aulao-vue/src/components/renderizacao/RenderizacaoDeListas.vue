<template>
    <div>
        <h1>Componente com Renderização de Lista</h1>
        <p>Nome: {{ nome }}</p>
        <p v-show="!cachorros.length">Não tem cachorros</p>

        <ul>
            <li v-for="cachorro in cachorros">Nome: {{ cachorro.nome }} | Idade: {{ cachorro.idade }} </li>
        </ul>


    </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
    nome:String,
    cachorros: Array
})
</script>

<style scoped>

div{
    max-width: 1000px;
    margin: 30px;
    text-align: center;
    padding: 20px;
    background-color: rgb(22, 48, 194);
    border-radius: 20px;
}

ul{
    text-align: left;
}

</style>