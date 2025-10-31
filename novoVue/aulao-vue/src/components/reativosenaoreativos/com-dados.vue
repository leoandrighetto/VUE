<template>
    <div>

        <h1>Componente com dados</h1>
        <p>Nome: {{ produto }} | Código: {{ codigo }}</p>
        <p></p>

    </div>

</template>




//OPTIONS API
// export default{

// data() {
// return{
// produto: 'Caderno',
// codigo: '#321'
// }
// }
// }


             
//COMPOSITION API


<script setup>

const produto = 'Caderno'
const codigo = '#321'

</script>


<style scoped>
div {
    text-align: center;
    border: 2px solid;
    background-color: #050d04;
    border-radius: 15px;
    margin: 30px;
    padding: 10px;


}

p {
    font-size: 15pt;
}

</style>