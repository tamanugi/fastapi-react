import { useSearchParams } from "react-router-dom";
import type { BookSearchQuery } from "./types";

type BookSearchParamsCustomHook = [
  BookSearchQuery,
  (params: BookSearchQuery) => void
];

export const useBookSearchParams = (): BookSearchParamsCustomHook => {
  const [searchParams, setSearchParams] = useSearchParams();

  const updateSearchParams = (params: BookSearchQuery): void => {
    const p: [string, string][] = Object.entries(params).map(([k, v]) => [
      k,
      String(v),
    ]);

    setSearchParams(p);
  };

  // SearchParamsはアクセスしないと値を取得できないので、
  // entries()で各要素にアクセスしてObjectに詰め直している
  const query = Object.fromEntries([
    ...searchParams.entries(),
  ]) as BookSearchQuery;

  return [query, updateSearchParams];
};
