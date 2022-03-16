import Home from "./routes/Home";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Detail from "./routes/Detail";
import styled from "styled-components";
import React, {useRef, useEffect} from "react";
function App() {
  const divRef = useRef()
  useEffect(() => {
    let video = <Video/>;
    const div = document.getElementById("111");
    console.log(div);
    // divRef.current.appendChild(video);
    div.appendChild(video);

  }, [])
  
  return( 
    <div ref={divRef} id="111">gfyfgy</div>
  );
}

const Video = styled.video`
width : 100;
`

export default App;
