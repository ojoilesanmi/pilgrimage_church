let menu = document.querySelector("#menu");
let close = document.querySelector("#close");
let openMenu = document.querySelector(".open-nav");


menu.onclick = function(e) {
    openMenu.classList.remove("nav-out");
    openMenu.classList.add("nav-in");
}
close.onclick = function(e) {
    openMenu.classList.remove("nav-in");
    openMenu.classList.add("nav-out");
}