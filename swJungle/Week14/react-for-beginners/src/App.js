import { useState ,useEffect} from "react";

function App() {
  const [toDo,setTodo] = useState("");
  const [toDos,setToDos] = useState([]);
  const [counter, setValue] = useState(0);
  const onChange = (event) => setTodo(event.target.value);
  const onClick = () => setValue((prev) => prev + 1);
  const onSubmit = (event) =>{
    event.preventDefault();
    if(toDo ===""){
      return;
    }
    setTodo("");
    setToDos((current) => [toDo, ...current]);
  };
  console.log(toDos);
  return (
    <div>
      <h1>My To Dos ({counter})</h1>
      <form onSubmit={onSubmit}>
        <input onChange={onChange} value={toDo} type="text" placeholder="write todo"></input>
        <button onClick={onClick}>Add Todo</button>
      </form>
      <hr></hr>
      <ul>
        {toDos.map((item, index) => <li key={index}>{item}</li>)}
      </ul>
    </div>
  );
}

export default App;
