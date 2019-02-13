function hideModal(){
    this.style.display = 'none';
}
let modalBody = document.getElementById('episodesModalWrapper');
modalBody.addEventListener('click', hideModal);
