<script setup>
import { watch } from "vue";
import suporte from "./Desenhos/suporte.png";
import cabeca from "./Desenhos/cabeca.png";
import torso from "./Desenhos/torso.png";
import bracoD from "./Desenhos/bracoD.png";
import bracoE from "./Desenhos/bracoE.png";
import pernaD from "./Desenhos/pernaD.png";
import pernaE from "./Desenhos/pernaE.png";

const props = defineProps({ erros: Number });
</script>

<template>
  <div class="desenho">
    <div class="suporte">
      <img :src="suporte" class="suporte" />
    </div>
    <div class="conteiner">
      <img v-if="props.erros >= 1" :src="cabeca" class="topo" />
      <img v-if="props.erros >= 2" :src="torso" class="centro" />
      <img v-if="props.erros >= 3" :src="bracoD" class="direitaS" />
      <img v-if="props.erros >= 4" :src="bracoE" class="esquerdaS" />
      <img v-if="props.erros >= 5" :src="pernaD" class="direitaI" />
      <img v-if="props.erros === 6" :src="pernaE" class="esquerdaI" />
    </div>
  </div>
</template>

<style scoped>
.desenho {
  display: inline-block;
  position: absolute;
  top: 70px;
  right: 70px;
  height: 100px;
}

.conteiner {
  transform: scale(0.1);
  transform-origin: top center;
  position: relative;
  width: 1080px;
  height: 300px;
  margin: 0;
  display: flex;
  justify-content: center;
  font-size: 16px;
}

.suporte {
  display: flex;
  transform: scale(0.4);
  transform-origin: top center;
  position: absolute;
  left: 550px;
  top: -27px;
}

.topo {
  position: absolute;
  width: 17em;
  left: 234em;
  height: auto;
}

.centro {
  display: flex;
  position: absolute;
  top: 14.8em;
  height: 38em;
  margin-left: 417em;
}

.direitaS {
  display: flex;
  margin-left: 130px;
  position: absolute;
  height: 300px;
  top: 22em;
  left: 233.5em;
}

.esquerdaS {
  position: absolute;
  height: 300px;
  top: 22em;
  left: 234em;
}

.esquerdaI {
  display: flex;
  position: absolute;
  height: 470px;
  width: 150px;
  top: 800px;
  left: 3760px;
}

.direitaI {
  position: absolute;
  height: 30em;
  width: 150px;
  top: 50em;
  left: 3839px;
}
</style>