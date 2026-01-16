import api from './api';

export const authService = {

    teste(dado) {
        return api.post('/teste', dado);
    }

}
