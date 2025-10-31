<!-- para usar renderização condicional é preciso utilizar uma diretiva do vue
 v-if -->

<template>
    <div>
        <h1>Componente com Renderização Condicional</h1>
        <p>Nome: {{ nome }}</p>
        <p v-if="qntcachorros === 0">Não tem cachorros</p>
        <p v-else-if="qntcachorros === 1">Tem um cachorro</p>
        <p v-else>Tem muitos cachorros</p>
    </div>
</template>



<script setup>
import { defineProps } from 'vue';

defineProps({
    nome:String,
    qntcachorros:Number
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

</style>