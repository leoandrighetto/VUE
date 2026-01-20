<template>
  <v-container>
    <div>
      <v-row class="d-flex align-center flex-column mt-16" width="200">
        <p class="text-h3">Iniciar Sessão</p>
        <v-col style="width: 400px" class="mt-10">
          <v-form style="width: 366px" class="d-flex flex-column">
            <v-text-field type="email" placeholder="Email..." v-model="email">
            </v-text-field>
            <v-text-field
              type="password"
              placeholder="Senha..."
              v-model="senha"
            >
            </v-text-field>
            <v-btn @click="login"> Login </v-btn>
          </v-form>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { authService } from "../services/authService";
import {useRouter} from 'vue-router';

const email = ref("");
const senha = ref("");

const router = useRouter()

async function login() {
  try {

    const response = await authService.iniciarSessao({
      email: email.value,
      password: senha.value,
    });

    localStorage.setItem(response.data.JWT);
    router.push('/UserPage')
    
  } catch (error) {}
}
</script>
