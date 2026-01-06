<script setup>
import JogoDaForca from './components/JogoDaForca.vue'

//constantes e variáveis
const palavrasFaceis = [
  "casa", "gato", "bola", "pato", "mesa",
  "flor", "uva", "bolo", "faca", "copo",
  "sapato", "livro", "carro", "janela", "porta",
  "chave", "luz", "amigo", "cachorro", "fogo"
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
  "Oposto de água ou gelo"
];

const palavrasMedias = [
  "banana", "jardim", "amigos", "escola", "caneta",
  "aviao", "navio", "morango", "cavalo", "peixes",
  "telefone", "cadeira", "camisa", "travesse", "chapéu",
  "montanha", "praia", "floresta", "roupa", "ventilar"
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
  "Aparelho que movimenta o ar"
];

const palavrasDificeis = [
  "computador", "bicicleta", "dinheiro", "felicidade", "sabores",
  "relógio", "abacaxi", "chocolate", "ventilador", "refrigerar",
  "microondas", "professor", "televisão", "notebook", "restaurante",
  "automóvel", "lanchonete", "fotografia", "caderno", "telefonema"
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
  "Ligação feita por telefone"
];

let indice = 0

function Random() {

  let random = Math.floor(Math.random() * (20 - 0 + 1) + 0);
  indice = random;
  console.log(indice)
  return indice;

}

function reiniciar() {

  Random();
  
}

Random()

const palavraFacil = palavrasFaceis[indice].toUpperCase();

const dicaFacil = dicasFaceis[indice];

const palavraMedia = palavrasMedias[indice].toUpperCase();
const dicaMedia = dicasMedias[indice];

const palavraDificil = palavrasDificeis[indice].toUpperCase();
const dicaDificil = dicasDificeis[indice];


console.log(indice)
//referência de estado

</script>

<template>
  {{ dicaFacil }}
  <JogoDaForca :palavra="palavraFacil" @onReiniciar="reiniciar" />
</template>

<style scoped></style>
