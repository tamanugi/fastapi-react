import Maybe from "@/components/ui/Maybe";
import { client } from "@/lib/ApiClient";
import useAspidaSWR from "@aspida/swr";
import { Button, Input, List, Modal } from "antd";
import React, { useEffect, useState } from "react";

import { useBookSearchParams } from "./hooks";
import { PublisherCandidates } from "./PublisherCandidates";
import { BookSearchQuery } from "./types";

import type { SearchConditionRead } from "@/api/@types";

type SearchSidebarProps = {
  search_conditions: SearchConditionRead[];
};

export const SearchSidebar: React.FC<SearchSidebarProps> = ({
  search_conditions,
}: SearchSidebarProps) => {
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
    <form
      className="h-full w-60 border-r-2 bg-white p-8"
      onSubmit={handleSubmit}
    >
      <div className="flex flex-col gap-8 bg-white">
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

      <div className="mt-16">
        <h3 className="font-semibold">保存した検索条件</h3>

        <List
          className="max-h-60 overflow-auto"
          size="small"
          bordered
          dataSource={search_conditions}
          renderItem={(item) => (
            <List.Item className="flex flex-col items-start justify-start">
              <Maybe test={!!item.condition.keyword}>
                <div>キーワード: {item.condition.keyword}</div>
              </Maybe>
              <Maybe test={!!item.condition.publisher}>
                <div>出版社: {item.condition.publisher}</div>
              </Maybe>
            </List.Item>
          )}
        />
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
