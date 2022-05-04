import SEO from "../components/SEO";
import { useEffect, useState } from "react";

const API_KEY = "9294115f977f365ac41138e43e60c7a8";

export default function Home() {
  const [movies, setMovies] = useState<any>();
  useEffect(() => {
    (async () => {
      const { results } = await (
        await fetch(
          `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
        )
      ).json();
      setMovies(results);
    })();
  }, []);
  return (
    <div className="container">
      <SEO title="Home" />
      {!movies && <h4>Loading..</h4>}
      {movies?.map((movie: any) => (
        <h4>{movie.original_title}</h4>
      ))}
      <style jsx>{`
        .container {
          display: grid;
          grid-template-columns: 1fr 1fr;
          padding: 20px;
          gap: 20px;
        }
        .movie img {
          max-width: 100%;
          border-radius: 12px;
          transition: transform 0.2s ease-in-out;
          box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
        }
        .movie:hover img {
          transform: scale(1.05) translateY(-10px);
        }
        .movie h4 {
          font-size: 18px;
          text-align: center;
        }
      `}</style>
    </div>
  );
}
