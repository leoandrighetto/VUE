import api from './api';

export const authService = {

    registrar(dados) {
        return api.post('/auth/registrar', dados);
    }

}
