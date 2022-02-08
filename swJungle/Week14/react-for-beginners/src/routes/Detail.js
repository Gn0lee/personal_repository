import { useEffect, useState } from "react";
import { useParams } from "react-router";


function Detail() {
    const {id} = useParams();
    const [detail, setDetail] = useState([]);
    const [loading, setLoading] = useState(true);
    const getMovies = async ()=>{
        const json = await( 
            await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
            ).json();
        setDetail(json.data.movie);
        setLoading(false);
    }

    useEffect(()=>{
        getMovies();
        
    },[]);

    return (
    <div>
        <h1>Detail</h1>
        {loading ? <strong>loading...</strong> : 
        <div>
        
        <img src={detail.large_cover_image} alt={detail.title}/>
        <h2>{detail.title_long}</h2>
        <p>{detail.description_intro.length > 700 ? `${detail.description_intro.substr(0,700)}...` : detail.description_intro}</p>
        
        </div>
        }


    </div>
    );
}

export default Detail;