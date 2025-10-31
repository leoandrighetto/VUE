<script setup>

//const Borracha = "Borracha";
//const preco = 2.50;

//  codigo js 
import comDados from './components/reativosenaoreativos/com-dados.vue';
import comDadosReativosPrimitivos from './components/reativosenaoreativos/com-dados-reativos-primitivos.vue';
import comDadosReativosNAOprimitivos from './components/reativosenaoreativos/com-dados-reativos-NAOprimitivos.vue';
import dataBiding from './components/reativosenaoreativos/dataBiding.vue';
import ComponenteComProps from './components/props/ComponenteComProps.vue';
import EscutaEvento from './components/eventos/EscutaEvento.vue';
import PropriedadesComputadas from './components/props/PropriedadesComputadas.vue';
import PropriedadesAssistidas from './components/props/PropriedadesAssistidas.vue';
import PropriedadesAssistidasWatchEffect from './components/props/PropriedadesAssistidasWatchEffect.vue';
import RenderizacaoCondicional from './components/renderizacao/RenderizacaoCondicional.vue';
import RenderizacaoDeListas from './components/renderizacao/RenderizacaoDeListas.vue';
import Slots from './components/slots/Slots.vue';
import SlotsComNomes from './components/slots/SlotsComNomes.vue';

const cachorrosLeo = [{ nome: 'Bob', idade: 13 }, { nome: 'Mel', idade: 5 }];
</script>


<template>
  <!-- codigo html agrupado-->
  <div>
    <header>Prazer, Vue!</header>
    <comDados />
    <comDadosReativosPrimitivos />
    <comDadosReativosNAOprimitivos />
    <dataBiding />
    <ComponenteComProps item="Borracha" :preco="10.00" />
    <ComponenteComProps item="Apontador" :preco="5.00" />
    <ComponenteComProps item="Caderno" :preco="30.00" />
    <EscutaEvento />
    <PropriedadesComputadas />
    <PropriedadesAssistidas />
    <PropriedadesAssistidasWatchEffect />
    <RenderizacaoCondicional nome="Leonardo" :qntcachorros="0" />
    <RenderizacaoDeListas nome="Leonardo" :cachorros="cachorrosLeo" />

    <SlotsComNomes>

      <template v-slot:icone>

        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
          stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
          class="icon icon-tabler icons-tabler-outline icon-tabler-users-group">
          <path stroke="none" d="M0 0h24v24H0z" fill="none" />
          <path d="M10 13a2 2 0 1 0 4 0a2 2 0 0 0 -4 0" />
          <path d="M8 21v-1a2 2 0 0 1 2 -2h4a2 2 0 0 1 2 2v1" />
          <path d="M15 5a2 2 0 1 0 4 0a2 2 0 0 0 -4 0" />
          <path d="M17 10h2a2 2 0 0 1 2 2v1" />
          <path d="M5 5a2 2 0 1 0 4 0a2 2 0 0 0 -4 0" />
          <path d="M3 13v-1a2 2 0 0 1 2 -2h2" />
        </svg>
      </template>

      <template v-slot:texto>
        HOME
      </template>

  </SlotsComNomes>

    <!-- https://tabler.io/icons -->
    <Slots>
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
        class="icon icon-tabler icons-tabler-filled icon-tabler-message">
        <path stroke="none" d="M0 0h24v24H0z" fill="none" />
        <path
          d="M18 3a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-4.724l-4.762 2.857a1 1 0 0 1 -1.508 -.743l-.006 -.114v-2h-1a4 4 0 0 1 -3.995 -3.8l-.005 -.2v-8a4 4 0 0 1 4 -4zm-4 9h-6a1 1 0 0 0 0 2h6a1 1 0 0 0 0 -2m2 -4h-8a1 1 0 1 0 0 2h8a1 1 0 0 0 0 -2" />
    </svg>
      HOME
    </Slots>

  </div>
</template>



<style scoped>
div {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 500px;
}
</style>