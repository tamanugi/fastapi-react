import { BasicLayout } from "@/components/layouts/BasicLayout";
import { SearchResult } from "./SearchResult";
import { SearchSidebar } from "./SearchSidebar";
import useAspidaSWR from "@aspida/swr";
import { client } from "@/lib/ApiClient";
import { useBookSearchParams } from "./hooks";

export const BookHome = () => {
  const [bookSearchParams] = useBookSearchParams();

  const { data } = useAspidaSWR(client.api.books.search, {
    query: bookSearchParams,
  });

  console.log(data);

  return (
    <BasicLayout>
      <div className="flex h-full">
        <div className="fixed h-full">
          <SearchSidebar />
        </div>

        <div className="ml-[300px] w-full px-12 py-6">
          <span>検索結果: {data?.count}件</span>
          {data && <SearchResult datas={data?.books}></SearchResult>}
        </div>
      </div>
    </BasicLayout>
  );
};
