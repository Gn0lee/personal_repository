const API_KEY = "b182a79f43674a9653f59afc923263a3";



function onGeoOk(position){
    console.log(position);
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
    fetch(url)
    .then(response => response.json())
    .then(data => {
        const city = document.querySelector("#weather span:first-child");
        const weather = document.querySelector("#weather span:last-child");
        
        city.innerText = data.name;
        weather.innerText = data.weather[0].main;
    });
}

function onGeoError(){
    alert("fail");
}
navigator.geolocation.getCurrentPosition(onGeoOk,onGeoError);