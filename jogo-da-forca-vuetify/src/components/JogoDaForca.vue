<script setup>

import { ref, watch, } from 'vue';
import Forca from './Forca.vue';

//props
const props = defineProps({ palavra: String });

//emits
const emits = defineEmits(['onReiniciar']);

//const e variaveis
const palavra = props.palavra.split("");

//refs
const snackbar = ref(false);
const text = ref("");
const snackbarColor = ref("")
const tentativas = ref(6);
const acertos = ref(0);
const erros = ref(0);
const botaoSnackbar = ref(false);

const reiniciarTeclado = ref(false);
const reiniciarPalavra = ref(false);

const dialogoDerrota = ref(false);


//functions
function tentarLetra(params) {
    if (typeof params === 'number') {

        acertos.value += params;

        if (acertos.value === palavra.length) {
            snackbar.value = true;
            botaoSnackbar.value = true;
            snackbarColor.value = "green-darken-1"
            text.value = "VOCÊ GANHOU! \n Gostaria de tentar outra palavra?"
        }


    } else {

        erros.value += 1;
        tentativas.value -= 1;

        if (erros.value === 6) {
            dialogoDerrota.value = true;

        } else {

            botaoSnackbar.value = false;
            snackbar.value = true;
            snackbarColor.value = "deep-orange-darken-4"
            text.value = "ERROU! Restam " + tentativas.value + " tentativas"
        }

    }
}

function reiniciar() {

    emits("onReiniciar")
    snackbar.value = false;
    text.value = "";
    snackbarColor.value = "";
    tentativas.value = 6
    acertos.value = 0;
    erros.value = 0;
    botaoSnackbar.value = false;
    dialogoDerrota.value = false;
    reiniciarPalavra.value = true
    reiniciarTeclado.value = true

}


// color="deep-orange-darken-4" PARA ERROS
</script>
<template>
    <v-snackbar v-model="snackbar" position="absolute" :color='snackbarColor' location="center">
        {{ text }}

        {{ '\n' }}
        <v-btn v-if="botaoSnackbar" class="botaoSnackbar" dark flat width: 20px height:20px @click="reiniciar"> Sim!
        </v-btn>

    </v-snackbar>

    <v-dialog v-model="dialogoDerrota" persistent>
        <v-card title="Você perdeu ☹︎" width="400px" location="center" color="#546E7A
">
            <div style="margin: 20px">
                <div style="margin-bottom: 30px; font-family: system-ui; font-size: 15pt;">
                    Que pena! Acabaram as tentativas! <br>
                    Você gostaria de tentar resolver outra palavra?
                </div>
                <div>
                    <VCardActions>
                        <v-btn elevation="17" location="top" @click="reiniciar">
                            SIM
                        </v-btn>
                    </VCardActions>
                </div>
            </div>
        </v-card>
    </v-dialog>

    <Forca :palavra="props.palavra" @onTentarLetra="tentarLetra" :reiniciarPalavra="reiniciarPalavra"
        :reiniciarTeclado="reiniciarTeclado" />

</template>

<style scoped>
.botaoSnackbar {
    font-size: 10px;
    height: 30px;

}
</style>