import { BookRead } from "@/api/@types";
import { Table } from "antd";

const columns = [
  {
    title: "ISBN",
    dataIndex: "isbn",
  },
  {
    title: "タイトル",
    dataIndex: "title",
  },
  {
    title: "サブタイトル",
    dataIndex: "sub_title",
  },
  {
    title: "著者",
    dataIndex: "author",
  },
  {
    title: "出版社",
    dataIndex: "publisher",
  },
  {
    title: "シリーズ",
    dataIndex: "series",
  },
  {
    title: "本体価格",
    dataIndex: "price",
  },
];

type Props = {
  datas: BookRead[] | undefined;
};

export const SearchResult: React.FC<Props> = ({ datas }: Props) => (
  <Table
    rowKey={(row) => row.isbn}
    className=""
    dataSource={datas}
    columns={columns}
    pagination={{ position: ["bottomRight"] }}
  />
);
