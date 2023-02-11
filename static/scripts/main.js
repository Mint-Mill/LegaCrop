// Grabbing Elements
const hamBtn = document.querySelector("#ham-btn");
const menu = document.querySelector("#menu");
const closeBtn = document.querySelector("#close-btn");

// Adding Event Listener
hamBtn.addEventListener("click", openMenu)
closeBtn.addEventListener("click", closeMenu)

// Functions
function openMenu() {
    if (menu.classList.contains("hide")) {
        menu.classList.toggle("hide");
    }
    // console.log(menu.classList)
    menu.classList.toggle("show");
}

function closeMenu() {
    if (menu.classList.contains("show")) {
        menu.classList.toggle("show");
    }
    // console.log(menu.classList)
    menu.classList.toggle("hide");
}