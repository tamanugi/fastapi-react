import { client } from "@/lib/ApiClient";
import useAspidaSWR from "@aspida/swr";

type Props = {
  setPublisher: (v: string) => void;
};

export const PublisherCandidates = ({ setPublisher }: Props) => {
  const { data } = useAspidaSWR(client.api.books.search.conditions.publisher);
  console.log("hoge", data);

  return (
    <div
      className="grid gap-3 max-h-[60vh] overflow-auto mt-10"
      style={styles["grid-wrapper"]}
    >
      {data?.candidates.map((item, i) => (
        <div key={i}>
          <span
            className="cursor-pointer hover:font-bold"
            onClick={() => {
              setPublisher(item.key);
            }}
          >
            {item.key}
          </span>
        </div>
      ))}
    </div>
  );
};

const styles = {
  "grid-wrapper": {
    gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
  },
};
