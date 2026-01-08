const palavra = 'ÁÍÁÍÁÍÂÁÂ'
const acentoA = ['Á', 'Â', 'Ã'];

function acentuacao(letra) {

  //verifica se existe uma letra - recebida como parâmetro quando esta for uma vogal - com acento dentro da palavra.


  function filtrar(lista) {

    let filtro = palavra.split("").filter(
      letraPalavra => {
        return acentoA.find(
          letraListaAcentos => {

            if (letraListaAcentos === letraPalavra) {
              return letraPalavra

            }
          })
      })

      return filtro;

  }

  if (letra === 'A') {
    return filtrar(acentoA);
    
  }

  

}

console.log(acentuacao('A'))