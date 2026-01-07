<script setup>
import JogoDaForca from "./components/JogoDaForca.vue";

import { ref, onMounted } from "vue";
//constantes e variáveis

const palavrasFaceis = [
  "CASA",
  "GATO",
  "BOLA",
  "PATO",
  "MESA",
  "FLOR",
  "UVA",
  "BOLO",
  "FACA",
  "COPO",
  "SAPATO",
  "LIVRO",
  "CARRO",
  "JANELA",
  "PORTA",
  "CHAVE",
  "LUZ",
  "AMIGO",
  "CACHORRO",
  "FOGO",
];

const palavrasMedias = [
  "BANANA",
  "JARDIM",
  "AMIGOS",
  "ESCOLA",
  "CANETA",
  "AVIAO",
  "NAVIO",
  "MORANGO",
  "CAVALO",
  "PEIXES",
  "TELEFONE",
  "CADEIRA",
  "CAMISA",
  "TRAVESSE",
  "CHAPÉU",
  "MONTANHA",
  "PRAIA",
  "FLORESTA",
  "ROUPA",
  "VENTILAR",
];

const palavrasDificeis = [
  "COMPUTADOR",
  "BICICLETA",
  "DINHEIRO",
  "FELICIDADE",
  "SABORES",
  "RELÓGIO",
  "ABACAXI",
  "CHOCOLATE",
  "VENTILADOR",
  "REFRIGERAR",
  "MICROONDAS",
  "PROFESSOR",
  "TELEVISÃO",
  "NOTEBOOK",
  "RESTAURANTE",
  "AUTOMÓVEL",
  "LANCHONETE",
  "FOTOGRAFIA",
  "CADERNO",
  "TELEFONEMA",
];

const dicasFaceis = [
  "Lugar onde você mora",
  "Animal que mia",
  "Objeto usado para jogar",
  "Ave que grasna",
  "Móvel para refeições",
  "Planta colorida",
  "Fruta roxa",
  "Doce assado",
  "Utensílio para cortar",
  "Recipiente para líquidos",
  "Calçado para os pés",
  "Objeto para ler",
  "Veículo de quatro rodas",
  "Abertura de parede com vidro",
  "Entrada de uma casa",
  "Objeto que abre portas",
  "Fonte de iluminação",
  "Pessoa que gosta de companhia",
  "Animal de estimação",
  "Oposto de água ou gelo",
];

const dicasMedias = [
  "Fruta amarela com casca",
  "Lugar com plantas e flores",
  "Companheiros de brincadeira",
  "Lugar onde se aprende",
  "Utensílio para escrever",
  "Veículo que voa",
  "Veículo que navega",
  "Fruta vermelha ou rosa",
  "Animal de corrida e carga",
  "Animais que nadam",
  "Usado para falar à distância",
  "Assento com encosto",
  "Peça de roupa para tronco",
  "Objeto macio para dormir",
  "Chapéu de cabeça",
  "Elevação grande de terra",
  "Lugar com areia e mar",
  "Área cheia de árvores",
  "Peça de roupa",
  "Aparelho que movimenta o ar",
];

const dicasDificeis = [
  "Máquina para trabalhar e estudar",
  "Veículo de duas rodas",
  "Meio para guardar dinheiro",
  "Estado de alegria intensa",
  "Sensações de sabor",
  "Objeto que marca horas",
  "Fruta tropical com espinhos",
  "Doce feito de cacau",
  "Aparelho que refresca o ar",
  "Aparelho para conservar comida fria",
  "Aparelho de cozinha que aquece rápido",
  "Pessoa que ensina",
  "Aparelho que mostra imagens",
  "Computador portátil",
  "Lugar para comer fora de casa",
  "Veículo motorizado",
  "Lugar que vende lanches rápidos",
  "Registro de momentos com fotos",
  "Objeto para escrever e estudar",
  "Ligação feita por telefone",
];

let indice = 0;

const palavraFacil = ref("");

const dicaFacil = ref("");
const palavraMedia = ref("");
const dicaMedia = ref("");
const palavraDificil = ref("");
const dicaDificil = ref("");
const reiniciarTeclado = ref(false);
const reiniciarPalavra = ref(false);

//estados

function Random() {
  let random = Math.floor(Math.random() * (19 - 0 + 1) + 0);

  indice = random;

  palavraFacil.value = palavrasFaceis[indice];
  palavraMedia.value = palavrasMedias[indice];
  palavraDificil.value = palavrasDificeis[indice];

  dicaDificil.value = dicasDificeis[indice];
  dicaFacil.value = dicasFaceis[indice];
  dicaMedia.value = dicasMedias[indice];
  return;
}

function reiniciar() {
  reiniciarTeclado.value = true;
  reiniciarPalavra.value = true;

  Random();

  setTimeout(() => {
    reiniciarTeclado.value = false;
    reiniciarPalavra.value = false;
  }, 1000);
}
//referência de estado

onMounted(() => {
  Random();
});
</script>

<template>
  <div class="geral">
    <div class="dicas">
      {{ dicaFacil }}
    </div>
    <JogoDaForca
      :palavra="palavraFacil"
      :reiniciarTeclado="reiniciarTeclado"
      :reiniciarPalavra="reiniciarPalavra"
      @onReiniciar="reiniciar"
    />
  </div>
  
</template>

<style scoped>
.geral {
  display: flex;
  flex-direction: column;
  text-align: center;
  justify-content: center;
  align-items: center;
}

.dicas {
  margin: 20px;
}


</style>
