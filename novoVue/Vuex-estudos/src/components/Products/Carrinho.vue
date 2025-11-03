<template>
    <div>
        <div>
            Nome: {{ product.name }}
            <div>
                Preço: {{ product.price }}
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

</script>

<style scoped>
.card {
    background-color: rgb(255, 188, 112);
    padding: 2px;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-size: 07pt;
    margin-bottom: 15px;

}
</style>