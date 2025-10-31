<!-- OBSERVADORES ou Propriedades Assistidas -->

<template>
    <div>

        <h1>Componente com Propriedades Assistidas</h1>
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
import { ref, watch} from 'vue';


const anoNascimento = ref(1998);
const anoAtual = ref(2025);

const idade = ref(0)

// não seria a melhor opção pois o código é mais ou menos o mesmo dentro dos watchSyncEffect
// ele é mais útil em casos onde existem efeitos colaterais, implicando na DOM ou 
// requisição de APIs, por exmeplo

watch(anoAtual, (anoAtual) => {

    idade.value = anoAtual - anoNascimento.value;


})

watch(anoNascimento, (anoNascimento) => {

    idade.value = anoAtual.value - anoNascimento;
    
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

.forms{
    display: flex;
    flex-direction: column;
}
</style>
