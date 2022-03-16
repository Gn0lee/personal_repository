import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import styled from "styled-components";

function Movie({id , coverImg, title, summary, genres}){

    let video = <Video/>
    console.log(video);
    document.getElementById('div111').appendChild(video);
    // console.log(div);
    // div.appendChild(video);

    return (
    <div id="div111">
        <img src={coverImg} alt={title}/>
        <h2><Link to={`/movie/${id}`} >{title}</Link></h2>
        <p>{summary.length > 235 ? `${summary.slice(0,235)}...` : summary }</p>
        <ul>
            {genres.map((g)=><li key={g}>{g}</li>)}
        </ul>
    </div>
    );
}

Movie.propTypes = {
    id : PropTypes.number.isRequired,
    coverImg: PropTypes.string.isRequired,
    title : PropTypes.string.isRequired,
    summary : PropTypes.string.isRequired,
    genres : PropTypes.array.isRequired
}

export default Movie;


const  Video = styled.video`

`