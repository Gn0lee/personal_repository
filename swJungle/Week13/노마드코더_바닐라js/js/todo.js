const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");
const toDoInput = document.querySelector("#todo-form input");

let toDos = [];

const TODOS_KEY = "todos"



function deleteTodo(event){
    const li = event.target.parentElement;
    toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));
    li.remove();

}

function saveTodos(){
    localStorage.setItem(TODOS_KEY,JSON.stringify(toDos));
}


function paintToDo(newTodo){
    const li = document.createElement("li");
    li.id = newTodo.id;
    const span = document.createElement("span");
    const button = document.createElement("button");

    button.innerText = "❌";
    button.addEventListener("click",deleteTodo);
    span.innerText = newTodo.text;


    li.appendChild(span);
    li.appendChild(button);

    toDoList.appendChild(li);
}

function handleToDoSubmit(event){
    event.preventDefault();
    const newTodo = toDoInput.value;
    toDoInput.value = "";
    
    const newTodoObj = {
        text : newTodo,
        id:Date.now(),
    };

    toDos.push(newTodoObj);
    paintToDo(newTodoObj);
    saveTodos();
}

toDoForm.addEventListener("submit",handleToDoSubmit);

const savedTodos = localStorage.getItem(TODOS_KEY);

if(savedTodos !== null){
    const parsedTodos = JSON.parse(savedTodos);
    toDos = parsedTodos;
    parsedTodos.forEach(paintToDo);

}