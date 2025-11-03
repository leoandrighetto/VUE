<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import AppProdutcs from './components/Products/AppProdutcs.vue';


const store = useStore()
const count = computed(() => store.state.count);

const newUser = {
  first_name: 'Millena',
  last_name: 'Andrighetto Linhares'
}


</script>

<template>
  <div >
  <AppProdutcs/>
  </div>

<!-- 
  <button @click="store.commit('decrementCount')">Diminuir</button>

  <br>
  <p>{{ count }}</p>
  <br>
  <button @click="store.commit('incrementCount')">Adicionar</button>
  <br>
  <br>
  <button @click="save(newUser)"> Save User </button>
  <br>
  <p></p>
  {{ console.log(store.state.user) }} -->

</template>