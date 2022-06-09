import { BasicLayout } from "@/components/layouts/BasicLayout";
import { SearchResult } from "./SearchResult";
import { SearchSidebar } from "./SearchSidebar";
import useAspidaSWR from "@aspida/swr";
import { client } from "@/lib/ApiClient";
import { useBookSearchParams } from "./hooks";
import { Button } from "antd";
import { BookSearchQuery } from "./types";

const isEmptySearchParams = (params: BookSearchQuery) =>
  !params.keyword && !params.publisher;

export const BookHome = () => {
  const [bookSearchParams] = useBookSearchParams();

  const { data } = useAspidaSWR(client.api.books.search, {
    query: bookSearchParams,
  });

  const { data: conditionsData, mutate: consitionsMutate } = useAspidaSWR(
    client.api.search_conditions
  );

  const onClickSaveCondition = async () => {
    await client.api.search_conditions.post({
      body: { condition: bookSearchParams },
    });

    consitionsMutate();
  };

  return (
    <BasicLayout>
      <div className="flex h-full">
        <div className="fixed h-full">
          <SearchSidebar search_conditions={conditionsData?.conditions || []} />
        </div>

        <div className="ml-[300px] w-full px-12 py-6">
          <Button
            onClick={onClickSaveCondition}
            disabled={isEmptySearchParams(bookSearchParams)}
          >
            現在の検索条件を保存する
          </Button>

          <div className="mt-8">
            <span>検索結果: {data?.count}件</span>
            {data && <SearchResult datas={data?.books}></SearchResult>}
          </div>
        </div>
      </div>
    </BasicLayout>
  );
};
