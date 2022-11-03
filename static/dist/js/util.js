function link(url) {
    window.location.href = url;
}

function verMinilist(id){
    if (document.querySelector('#' + id) != NaN){
        pai = document.querySelector('#' + id);
        menu = pai.children;
        menu[1].style.display = 'block';
        diferenca = -1;
        if(window.screen.width <= 800){
            diferenca *= ((parseInt(window.getComputedStyle(pai, null).width + '') - parseInt(window.getComputedStyle(menu[1], null).width + '')) / 2 )* (-1.5);    
        }
        else {
            diferenca = parseInt(window.getComputedStyle(pai, null).width + '') - parseInt(window.getComputedStyle(menu[1], null).width + '');    
        }
        menu[1].style.transform = 'translateX(' + diferenca + 'px)';
        menu[1].style.opacity = '1';
    }
    
}

function ocultarMinilist(id){
    if (document.querySelector('#' + id) != NaN){
        menu = document.querySelector('#' + id).children[1];
        menu.style.display = 'none';
        menu.style.opacity = '0';
    }
}