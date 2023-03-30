document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('.temples-toggle').addEventListener('click', function(){
        document.querySelector('.temples-nav').classList.toggle('clicked');
    })
})