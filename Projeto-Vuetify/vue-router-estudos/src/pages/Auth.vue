<template>
  <v-container>
    <div>
      <v-row class="d-flex justify-center align-center mt-16 flex-column">
        <p class="text-h3">Cadastre-se</p>
        <v-col style="width: 400px">
          <v-form class="d-flex flex-column" style="width: 366px">
            <v-text-field
              prepend-icon="mdi-account"
              clearable
              label="nome"
              v-model="nome"
            ></v-text-field>
            <v-text-field
              prepend-icon="mdi-email"
              clearable
              :rules="rulesEmail"
              label="email"
              type="email"
              v-model="email"
            ></v-text-field>
            <v-text-field
              type="password"
              prepend-icon="mdi-lock"
              clearable
              :rules="rules"
              label="senha"
              v-model="senha"
            ></v-text-field>
            <v-btn @click="registrarUsuario" :loading="loading"
              >REGISTRAR</v-btn
            >
          </v-form>

          <p>{{ text }}</p>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script setup>
import { ref } from "vue";

import { authService } from "../services/authService";

const nome = ref("");
const email = ref("");
const senha = ref("");
const text = ref("");
const loading = ref(false);
const formPreenchido = ref(false);

async function registrarUsuario() {
  text.value = "";
  try {
    const payload = {
      user: nome.value,
      email: email.value,
      password: senha.value,
    };

    loading.value = true;
    const response = await authService.registrar(payload);
    loading.value = false;
    console.log(response);
  } catch (error) {
    text.value = "ERRO";
    loading.value = false;
    text.value = "";
  }
}

const rules = [(v) => !!v || "Campo Obrigatório"];

const rulesEmail = [
  (v) => !!v || "Campo Obrigatório",
  (v) => {
    const padraoEmail = /.+@.+\..+/;
    return padraoEmail.test(v) || "Formato de e-mail inválido";
  },
];
</script>
