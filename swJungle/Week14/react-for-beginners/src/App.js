import { useState ,useEffect} from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]); 
  const [money, setMoney] = useState(0);
  const onSubmit = (event) => {
    event.preventDefault();
    setMoney(event.target[0].value);
  };

  useEffect(()=>{
    fetch("https://api.coinpaprika.com/v1/tickers")
    .then((response) => response.json())
    .then((json) => {
      setCoins(json);
      setLoading(false);
    });
  },[]);

 
  const filteredCoins = coins.filter((coin) => coin.quotes.USD.price <= money); 

  return (
    <div>
      <h1>The Coins! {loading ? "" : `(${filteredCoins.length})`}</h1>
      <div>
        <form  onSubmit={onSubmit}>
          <input type="float" placeholder="input money you have"/>
        </form>
      </div>
      {loading ? <strong>Loading...</strong> :
      <select>
       {filteredCoins.map((coin)=>
        <option key={coin.id}>
          {money !== 0 ? `${coin.name} (${coin.symbol}) => price : ${coin.quotes.USD.price}$ --- ${Math.floor(money/(coin.quotes.USD.price))} EA` : `${coin.name} (${coin.symbol}) : 0 EA`}
        </option>)}
      </select>
     }
      
    </div>
  );
}

export default App;
