<!-- 
 Propriedades ou variáveis que dependem de outras propriedades (presentes nos scripts)
são atualizadas automaticamente qunado as dependencias mudam -->

<template>
    <div>

        <h1>Componente com Propriedades Computadas</h1>
        <div class="forms">
        <label>Ano Nascimento: </label>
        <input type="number" v-model="anoNascimento" min="1900" />
        <br>
        <label>Ano Atual: </label>
        <input type="number" v-model="anoAtual" min="2000" />
        </div>

        <p>Idade: {{ idade }}</p>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const anoNascimento = ref(1998);
const anoAtual = ref(2025);
const idade = computed(() => anoAtual.value - anoNascimento.value)

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

.forms{
    display: flex;
    flex-direction: column;
}
</style>
