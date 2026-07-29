const menu = document.getElementById("theme-menu");

const btn = document.getElementById("theme-btn");

btn.addEventListener("click",()=>{

    menu.classList.toggle("show");

});

document.addEventListener("click",(e)=>{

    if(!e.target.closest(".theme-dropdown")){

        menu.classList.remove("show");

    }

});

function applyTheme(theme){

    if(theme==="system"){

        const dark=window.matchMedia("(prefers-color-scheme: dark)").matches;

        document.documentElement.setAttribute(
            "data-theme",
            dark?"dark":"light"
        );

    }

    else{

        document.documentElement.setAttribute(
            "data-theme",
            theme
        );

    }

    localStorage.setItem("theme",theme);

}

const saved=localStorage.getItem("theme")||"system";

applyTheme(saved);

document.querySelectorAll("#theme-menu button").forEach(button=>{

    button.onclick=()=>{

        applyTheme(button.dataset.theme);

        menu.classList.remove("show");

    }

});