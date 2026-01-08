<script setup>
import JogoDaForca from "./components/JogoDaForca.vue";

import { ref, onMounted } from "vue";
//constantes e variáveis

const palavrasFaceis = [
  "CAFÉ",
  "GATO",
  "PÉ",
  "PATO",
  "MÃE",
  "FLOR",
  "BAÚ",
  "BOLO",
  "ÍMÃ",
  "COPO",
  "BALÃO",
  "LIVRO",
  "VÔO",
  "JANELA",
  "MAÇÃ",
  "CHAVE",
  "BÊBÊ",
  "AMIGO",
  "CIPÓ",
  "FOGO",
];

const palavrasMedias = [
  "BANANA",
  "AVIÃO",
  "AMIGOS",
  "PANTUFA",
  "CANETA",
  "SABÃO",
  "NAVIO",
  "RÉGUA",
  "CAVALO",
  "ÓCULOS",
  "TELEFONE",
  "SÓTÃO",
  "CAMISA",
  "MÁGICO",
  "ROUPA",
  "CARTÃO",
  "PRAIA",
  "TÊNIS",
  "JARDIM",
  "CÉREBRO",
];

const palavrasDificeis = [
  "COMPUTADOR",
  "AUTOMÓVEL",
  "DINHEIRO",
  "ESTÁSTICA",
  "SABORES",
  "RELÓGIO",
  "ABACAXI",
  "LÂMPADA",
  "VENTILADOR",
  "PÁGINA",
  "MICROONDAS",
  "ÂNGULO",
  "TELEVISÃO",
  "MÚSICA",
  "RESTAURANTE",
  "ASTRONAUTA",
  "LANCHONETE",
  "EXÉRCITO",
  "CADERNO",
  "EXPERIÊNCIA",
];

const dicasFaceis = [
  "Bebida quente de grãos",
  "Animal que mia",
  "Parte do corpo que calça o sapato",
  "Ave que grasna",
  "Mulher que deu à luz",
  "Planta colorida",
  "Objeto antigo para guardar tesouros",
  "Doce assado",
  "Objeto que atrai metal",
  "Recipiente para líquidos",
  "Objeto que voa cheio de gás",
  "Objeto para ler",
  "Ato de voar das aves",
  "Abertura de parede com vidro",
  "Fruta vermelha da macieira",
  "Objeto que abre portas",
  "Criança recém-nascida",
  "Pessoa que gosta de companhia",
  "Planta que escala árvores",
  "Oposto de água ou gelo",
];

const dicasMedias = [
  "Fruta amarela com casca",
  "Veículo que voa",
  "Companheiros de brincadeira",
  "Calçado para usar em casa",
  "Utensílio para escrever",
  "Produto usado para lavar",
  "Veículo que navega",
  "Objeto para medir linhas",
  "Animal de corrida e carga",
  "Usado para enxergar melhor",
  "Usado para falar à distância",
  "Parte mais alta de uma casa",
  "Peça de roupa para tronco",
  "Aquele que faz truques",
  "Peça de vestuário",
  "Objeto retangular de banco ou felicitação",
  "Lugar com areia e mar",
  "Calçado esportivo",
  "Lugar com plantas e flores",
  "Órgão do pensamento",
];

const dicasDificeis = [
  "Máquina para trabalhar e estudar",
  "Veículo motorizado",
  "Meio para comprar coisas",
  "Ciência que analisa dados",
  "Sensações de sabor",
  "Objeto que marca as horas",
  "Fruta tropical com espinhos",
  "Objeto que produz luz elétrica",
  "Aparelho que movimenta o ar",
  "Uma das folhas de um livro",
  "Aparelho de cozinha que aquece rápido",
  "Figura geométrica de dois segmentos",
  "Aparelho que mostra imagens",
  "Arte dos sons e ritmos",
  "Lugar para comer fora de casa",
  "Viajante do espaço",
  "Lugar que vende lanches rápidos",
  "Conjunto de soldados de um país",
  "Objeto para escrever e estudar",
  "Conhecimento adquirido com o tempo",
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
