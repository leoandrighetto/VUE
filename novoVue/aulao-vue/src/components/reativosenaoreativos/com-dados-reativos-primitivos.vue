<template>
    <div>
        
        <h1>Componente com Dados Reativos Primitivos</h1>
        <p>
            Nome da Pessoa: {{ nome }} | Idade: {{ idade }}
        </p>
        <button @click="fazerAniversario()">Fazer aniversário</button>
        <button @click="mudarNome()">Mudar Nome</button>

    </div>

</template>

<script setup>
//é preciso declarar que a variavel que eu quero mudar pode variar de valor 
import { ref } from 'vue'

const nome = ref('Leonardo')
const idade = ref(27)




function fazerAniversario() {
    idade.value += 1
}

function mudarNome() {
    nome.value = "LeoLeo"
}
</script>

<style scoped>
div {
    background-color: rgb(22, 48, 194);
    margin: 30px;
    text-align: center;
    padding: 20px;
    border-radius: 20px;
}

div:hover {
    background-color: rgb(88, 88, 248);

}

button{
    background-color: rgb(10,69,4);
    color: white;
    padding: 10px 20px;
    font-weight: bold;
    margin: 5px 10px;
    border-radius: 5px;
    border: none;
}
button:hover{
    background-color: rgb(5,102,28);
}

</style>