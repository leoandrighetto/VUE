<template>
    <div>
        <div class="card">
            Nome: {{ product.name }}
            <div>
                Preço: {{ product.price }}
            </div>
            <div style="text-align: right;">
            <button @click="addCarrinho(product)"> Adicionar ao Carrinho </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useStore } from 'vuex';

const store = useStore()

defineProps({
    product: Object
})

function addCarrinho(product) {
    store.commit("setCarrinho", product)
    store.commit("setTotal", product.price)

}



</script>

<style scoped>
.card {
    background-color: antiquewhite;
    padding: 10px;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-size: 15pt;
    margin-bottom: 15px;


}
</style>