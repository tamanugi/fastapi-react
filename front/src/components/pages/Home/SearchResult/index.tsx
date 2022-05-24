import { Table } from "antd";
import datas from "./dataset.json";

const columns = [
  {
    title: "ISBN",
    dataIndex: "ISBN",
    key: "isbn",
  },
  {
    title: "タイトル",
    dataIndex: "タイトル",
    key: "title",
  },
  {
    title: "著者",
    dataIndex: "著者1",
    key: "author1",
  },
  {
    title: "出版社",
    dataIndex: "出版社",
    key: "publisher",
  },
  {
    title: "出版年月",
    dataIndex: "出版年月",
    key: "publish_date",
  },
  {
    title: "シリーズ",
    dataIndex: "シリーズ1",
    key: "series1",
  },
  {
    title: "本体価格",
    dataIndex: "本体価格",
    key: "price",
  },
];

export const SearchResult: React.FC = () => (
  <Table
    className=""
    dataSource={datas}
    columns={columns}
    pagination={{ position: ["topRight"] }}
    scroll={{ y: "600px" }}
  />
);
