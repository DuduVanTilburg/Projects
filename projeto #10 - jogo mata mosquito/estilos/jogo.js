var altura = 0
var largura = 0
var vidas = 1
var tempo = 15
var criaMosquitoTempo=1500
// o comando search é pra nos retornar toda a string que está depois da "?" na url
var nivel = window.location.search
nivel = nivel.replace('?','')
if(nivel ==='facil'){
	//1500 ms
	criaMosquitoTempo=1500
}else if (nivel==='normal'){
	//1000 ms
	criaMosquitoTempo=1000
}else if (nivel ==='dificil'){
	//750 ms
	criaMosquitoTempo=750
}
function ajustaTamanhoDaTela(){
	altura = window.innerHeight
	largura = window.innerWidth
}

ajustaTamanhoDaTela()

var cronometro = setInterval(function(){
	tempo-=1
	if (tempo<0){
		clearInterval(cronometro)
		clearInterval(criaMosquito)
		window.location.href = "vitoria.html"

	}else{
		// innerHTML é o valor contido entre as tags
		document.getElementById('cronometro').innerHTML = tempo
	}
	
},1000)
function randomPositionForMosquito(){
	// remover o mosquito anterios (caso exista)
	if (document.getElementById('mosquito')){
		
		document.getElementById('mosquito').remove()
		if (vidas>3){
			window.location.href = "fim_de_jogo.html"
		}else{

			document.getElementById('coracao'+vidas).src = "estilos/imagens/coracao_vazio.png"
			vidas+=1
		}
	}
	



	// o math.floor arredonda o numero pra inteiro pra baixo
	var posicaoMosquitoX = Math.floor(Math.random()* largura)-110
	var posicaoMosquitoY = Math.floor(Math.random()* altura)-110
	if ((largura-posicaoMosquitoX)>=largura){
		posicaoMosquitoX+=110

	}
	if((altura-posicaoMosquitoY)>=altura){
		posicaoMosquitoY+=110
	}
	console.log(posicaoMosquitoY,posicaoMosquitoX)

	// aqui vamos criar o elemento html
	var mosquito = document.createElement('img')
	mosquito.src = 'estilos/imagens/mosca.png'
	mosquito.className = tamanhoAleatorio() + ' ' + ladoAleatorio()
	mosquito.style.left= posicaoMosquitoX+'px'
	mosquito.style.top= posicaoMosquitoY+'px'
	mosquito.style.position= 'absolute'
	mosquito.id='mosquito'
	mosquito.onclick=function(){
		this.remove()
	}

	document.body.appendChild(mosquito)

}

function tamanhoAleatorio(){
	var tamanho = Math.round(Math.random()*3)
	switch(tamanho){
		case 0:
			return 'mosquito1'
		case 1:
			return 'mosquito2'
		case 2:
			return 'mosquito3'
		case 3:
			return 'mosquito4'
	}
}

function ladoAleatorio(){
	var lado = Math.floor(Math.random()*2)
	switch(lado){
		case 0:
			return 'esquerdo'
		case 1:
			return 'direito'

	}
}