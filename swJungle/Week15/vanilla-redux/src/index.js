import { createStore } from "redux";

const add = document.getElementById("add");
const minus = document.getElementById("minus");
const number = document.querySelector("span");
number.innerText = 0;

const countModifier = (count = 0, action) =>{
  // console.log(count , action);
  if(action.type === "ADD"){
   return count + 1; 
  }else if (action.type === "MINUS"){
    return count - 1;
  }else{
    return count;
  }
  //  console.log(action);
};

const countStore = createStore(countModifier);

const onChage = () => {
  // console.log(countStore.getState())
  number.innerText = countStore.getState();
}

countStore.subscribe(onChage);

add.addEventListener("click", ()=>countStore.dispatch({type : "ADD"}));
minus.addEventListener("click", ()=>countStore.dispatch({type : "MINUS"}));

