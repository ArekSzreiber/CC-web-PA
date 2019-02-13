function hideModal(){
    this.style.display = 'none';
}
let modalBody = document.getElementById('episodesModalWrapper');
modalBody.addEventListener('click', hideModal);

function showModal(){
    document.getElementById('episodesModalWrapper').style.display = 'block';
}


let modalButton = document.getElementById('episodesButton');
modalButton.addEventListener('click', showModal);
