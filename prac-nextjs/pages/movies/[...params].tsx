import { useRouter } from "next/router";

export default function Detail({ params }: any) {
  const router = useRouter();
  const [title, id]: any = params || [];
  return (
    <div>
      <h4>{title}</h4>
    </div>
  );
}

export function getServerSideProps({ params: { params } }: any) {
  return {
    props: {
      params,
    },
  };
}
