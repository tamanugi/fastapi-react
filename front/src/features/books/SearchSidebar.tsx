import { Button, Input } from "antd";
import React, { useEffect, useState } from "react";

import { useSearchParams } from "react-router-dom";
import { useBookSearchParams } from "./hooks";
import { BookSearchQuery } from "./types";

type SearchConditionBoxProps = {
  title: string;
  name: string;
};

const SearchConditionBox = ({ title, name }: SearchConditionBoxProps) => (
  <div className="mt- grid cursor-pointer grid-cols-2 border-b-2  py-3 hover:opacity-70">
    <span className="font-bold">{title}</span>
    <span>未設定</span>
    <input type="hidden" name={name} />
  </div>
);

export const SearchSidebar = () => {
  const [bookSearchParams, setBookSearchParams] = useBookSearchParams();
  const [state, setState] = useState<BookSearchQuery>({});

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setBookSearchParams(state);
  };

  const handleInputChange = (
    event: React.ChangeEvent<HTMLInputElement>,
    name: keyof BookSearchQuery
  ) => {
    setState({ [name]: event.target.value });
  };

  useEffect(() => {
    setState(bookSearchParams);
  }, []);

  return (
    <form className="h-full" onSubmit={handleSubmit}>
      <div className="flex h-full w-60 flex-col gap-8 border-r-2 bg-white p-8">
        <div>
          <Input
            placeholder="検索キーワード"
            name="keyword"
            value={state.keyword}
            onChange={(event) => {
              handleInputChange(event, "keyword");
            }}
          ></Input>
        </div>

        <Button type="primary" htmlType="submit">
          検索する
        </Button>

        <SearchConditionBox title="著者" name="author"></SearchConditionBox>
        <SearchConditionBox
          title="出版社"
          name="publisher"
        ></SearchConditionBox>
      </div>
    </form>
  );
};
