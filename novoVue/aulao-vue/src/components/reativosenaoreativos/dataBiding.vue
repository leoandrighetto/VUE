<template>
    <div class="componente">
        <h1>Componente com Data Binding</h1>
        <p>{{ valor }}</p>


                    <!-- oneway datab biding (seta unidirecional)
                    <input type="text" v-bind:value="valor"></input> -->


                    <!-- twoway data biding, 
                    o valor da variavel (valor) é passado para o input,
                    e depois atualizado
                    conforme a atualização NO input -->

                    
                    <!-- SEM ATALHOS -->
                    <!-- <input type="text" 
                    v-bind:value="valor" 
                    v-on:input="(e)=> valor = e.target.value"></input> -->


                    <!-- COM ATALHOS | SEM OTIMIZAÇÃO -->
                    <!-- <input type="text" 
                            :value="valor" 
                            @input="(e)=> valor = e.target.value"></input> -->


        <!-- MODO MAIS OTIMIZADO -->
        <input type="text" v-model="valor"></input>

    </div>
</template>

<script setup>

import { ref } from 'vue';
const valor = ref("Vue é top!")

</script>

<style scoped>

div{
    text-align: center;
    background-color: rgb(22, 48, 194);
    padding: 10px;
    margin: 30px;
    border-radius: 20px;

    
}

div:hover{
    background-color: rgb(88, 88, 248);
    }

</style>