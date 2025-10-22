const iframe = document.getElementById('grafico-iframe')

const card1 = document.getElementById('card-total')
const labelCard1 = document.getElementById('label-card1')

const card2 = document.getElementById('card-criancas')
const labelCard2 = document.getElementById('label-card2')

const card3 = document.getElementById('card-idosos')
const labelCard3 = document.getElementById('label-card3')

function chamaGraphDensPop(){
    iframe.src = './iframes/grafico_regioes.html'
    labelCard1.textContent = 'População Total';
    labelCard2.textContent = 'Crianças (0-5)';
    labelCard3.textContent = 'Idosos (60+)';
}

function chamaGraphEtariaRegiao(){
    iframe.src = './iframes/grafico_etaria_regiao.html'

    labelCard1.textContent = 'teste1';
    labelCard2.textContent = 'teste';
    labelCard3.textContent = 'teste3)';
}

function chamaGraphDensPo(){
    labelCard1.textContent = 'População Total';
    labelCard2.textContent = 'Crianças (0-5)';
    labelCard3.textContent = 'Idosos (60+)';
}