<template>

    <div>

        <AppProduct 
        v-for="product in store.state.products" 
        :key="product.id" 
        :product="product" />

    </div>

    <div>
        <pre>Lista de Compras:        Subtotal: R$ {{ store.state.total }}</pre>
        <Carrinho v-for="product in store.state.carrinho" :key="product.id" :product="product" />
    </div>


</template>

<script setup>

import { useStore } from 'vuex';
import AppProduct from './AppProduct.vue';
import Carrinho from './Carrinho.vue';

const store = useStore();

</script>
