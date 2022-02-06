const loginInput = document.querySelector("#login-form input");
const loginForm = document.querySelector("#login-form");
const link = document.querySelector("a");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";

function onLoginSubmit(event){
    event.preventDefault();
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY,username);

    loginForm.classList.add(HIDDEN_CLASSNAME);
    // greeting.innerText = "hello " + username;
    paintGreeting(username);
}

function handleClick(event){
    event.preventDefault();
}

function paintGreeting(username){
    greeting.innerText = `hello ${username}`;
    greeting.classList.remove(HIDDEN_CLASSNAME);
}

link.addEventListener("click",handleClick);

const savedUsername = localStorage.getItem(USERNAME_KEY);

if (savedUsername === null){
    loginForm.classList.remove(HIDDEN_CLASSNAME);
    loginForm.addEventListener("submit",onLoginSubmit);
}else{
    paintGreeting(savedUsername);
}