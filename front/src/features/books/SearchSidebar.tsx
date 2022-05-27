import { Button, Input, Modal } from "antd";
import React, { useEffect, useState } from "react";

import { useBookSearchParams } from "./hooks";
import { PublisherCandidates } from "./PublisherCandidates";
import { BookSearchQuery } from "./types";

export const SearchSidebar = () => {
  const [bookSearchParams, setBookSearchParams] = useBookSearchParams();
  const [state, setState] = useState<BookSearchQuery>({});
  const [modalVisible, setModalVisble] = useState(false);

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

        <span className="border-t-2" />

        <div
          className="mt- grid cursor-pointer grid-cols-2 border-b-2  py-3 hover:opacity-70"
          onClick={() => setModalVisble(true)}
        >
          <span className="font-bold">出版社</span>
          <span>{state.publisher || "未設定"}</span>
          <input type="hidden" name="publisher" />
        </div>
      </div>

      <Modal
        className="max-h-[50vh]"
        visible={modalVisible}
        onCancel={() => {
          setModalVisble(false);
        }}
        footer={null /* hide button */}
        width={1200}
      >
        <PublisherCandidates
          setPublisher={(publisher) => {
            setState({ publisher });
            setModalVisble(false);
          }}
        />
      </Modal>
    </form>
  );
};
