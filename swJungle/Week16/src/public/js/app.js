const messageList =document.querySelector("ul");
const messageFrom = document.querySelector("#message");
const nicknameFrom = document.querySelector("#nick");

const socket = new WebSocket(`ws://${window.location.host}`);

function makeMessage(type,payload){
    const msg = {type,payload};
    return JSON.stringify(msg);
}


socket.addEventListener("open",()=>{
    console.log("connect!");
});

socket.addEventListener("message",(message)=>{
    const li = document.createElement("li");
    li.innerText = message.data;
    messageList.append(li);
    console.log("server sent this", message.data);
});

socket.addEventListener("close",()=>{
    console.log("disconnect");
})    

function handleSubmit(event){
    event.preventDefault();
    const input = messageFrom.querySelector("input");
    console.log(input.value);
    socket.send(makeMessage("new_message",input.value));
    input.value = "";
}

function handleNickSubmit(event){
    event.preventDefault();
    const input = nicknameFrom.querySelector("input");
    socket.send(makeMessage("nickname",input.value));
    input.value = "";
}

messageFrom.addEventListener("submit",handleSubmit);
nicknameFrom.addEventListener("submit", handleNickSubmit);