<template>

    <div>
        <h1>Componente que escuta evento</h1>
        <p>Total: R$ {{ total }}</p>
        <br>

        <div class="lista">
            <emitir-evento item="Violão" :preco='1000' @adicionado="atualizartotal"/>
            <emitir-evento item="Bola" :preco='20' @adicionado="atualizartotal"/>
            <emitir-evento item="PC" :preco='500' @adicionado="atualizartotal" />            
        </div>        
    </div>

</template>

<script setup>
    import EmitirEvento from './EmitirEvento.vue';

    import { ref } from 'vue';
    
    const total = ref(0)

    function atualizartotal(preco){

        const valor = total.value + preco;
        total.value = valor;
    }

</script>

<style scoped> 
div{background-color: rgb(22, 48, 194);
    margin: 0 auto;
    max-width: 1000px;
    text-align: center;
    padding: 20px;
    border-radius: 20px;


}
.lista{
    display: flex;
    justify-content: space-between;
    margin-bottom: auto;
}
</style>