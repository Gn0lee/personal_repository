import express from "express";
import http from "http";
import WebSocket from "ws";
const app = express();

app.set("view engine", "pug");
app.set("views", __dirname + "/views");
app.use("/public", express.static(__dirname + "/public"));
app.get("/", (_,res) => res.render("home"));
app.get("/*" , (_,res)=>res.redirect("/"));

const handleListen = () => console.log("Listening on http://localhost:3000")

const server = http.createServer(app);

const wss = new WebSocket.Server({server});

const sockets = [];

wss.on("connection",(socket)=>{
    sockets.push(socket);
    socket["nickname"] = "Anon";
    socket.on("close",()=>{
        console.log("client close connect");
    });
    socket.on("message",(message)=>{
        // console.log(message);
        const parsed = JSON.parse(message.toString());

        switch(parsed.type){
            case "new_message":
                sockets.forEach(aSocket => aSocket.send(`${socket.nickname}:${parsed.payload}`));
            case "nickname":
                console.log(parsed.payload);
                socket["nickname"] = parsed.payload;
        }       
    });
});

server.listen(3000,handleListen);