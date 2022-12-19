let page = document.querySelector('.page');
let themeButton = document.querySelector('.theme-button');

let i = 0

themeButton.onclick = function() {
    comments.insertAdjacentHTML('beforeend', '<p>' + i + ' Пока</p>');
    i++;
};