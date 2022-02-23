const socket = new WebSocket(`ws://${window.location.host}`);

socket.addEventListener("open",()=>{
    console.log("connect!");
});

socket.addEventListener("message",(message)=>{
    console.log("server sent this", message.data);
});

socket.addEventListener("close",()=>{
    console.log("disconnect");
})    



   