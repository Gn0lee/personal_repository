import Layout from "../components/Layout";
import "./../styles/globals.css";
export default function App({ Component, pageProps }: any) {
  return (
    <Layout>
      <Component {...pageProps} />
      <style jsx global>{`
        a {
          text-decoration: none;
          color: blue;
        }
      `}</style>
    </Layout>
  );
}
