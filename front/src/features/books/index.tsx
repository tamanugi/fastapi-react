import { BasicLayout } from "@/components/layouts/BasicLayout";
import { useSearchParams } from "react-router-dom";
import { SearchResult } from "./SearchResult";
import { SearchSidebar } from "./SearchSidebar";
import useAspidaSWR from "@aspida/swr";
import { client } from "@/lib/ApiClient";

export const BookHome = () => {
  const [searchParams] = useSearchParams();

  const { data } = useAspidaSWR(client.api.books.search, {
    query: { keyword: searchParams.get("keyword") as string },
  });

  return (
    <BasicLayout>
      <div className="flex h-full">
        <div className="fixed h-full">
          <SearchSidebar></SearchSidebar>
        </div>

        <div className="ml-[300px] w-full px-12 py-6">
          {data && <SearchResult datas={data?.books}></SearchResult>}
        </div>
      </div>
    </BasicLayout>
  );
};
