import './assets/main.css'

import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'

const store = createStore({

    state: {
        user: {
            first_name: 'Leonardo',
            last_name: 'Andrighetto Linhares'
        },
        count: 0,
        products: [{
            id: 1,
            name: 'guitar',
            price: 1200
        },
        {
            id: 2,
            name: 'violin',
            price: 1600
        },
        {
            id: 3,
            name: 'banjoo',
            price: 1000
        }],
        carrinho: [],
        total: 0
    },
    mutations: {
        incrementCount(state) {
            state.count++
        },
        decrementCount(state) {
            state.count--
        },
        setUser(state, newUser) {
            state.user = newUser
        },
        setCarrinho(state, produto) {
            state.carrinho.push(produto)
        },
        setMostrarCarrinho(state) {
            return state
        },
        setTotal(state, product) {
            state.total += product
        }
    }
})


const app = createApp(App)
app.use(store)
app.mount('#app')