<template>
    <div>
        
        <h1>Componente com Dados Reativos NÃO Primitivos</h1>
        <p>
            Nome da Pessoa: {{ pessoa.nome }} | Idade: {{ pessoa.idade }}
        </p>
        <button @click="fazerAniversario()">Fazer aniversário</button>
        <button @click="mudarNome()">Mudar Nome</button>    

    </div>

</template>


<script setup>

import { reactive } from 'vue'

const pessoa = reactive({nome:'Leonardo', idade:27})

function fazerAniversario() {
    pessoa.idade += 1
}

function mudarNome() {
    pessoa.nome = "LeoLeo"
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