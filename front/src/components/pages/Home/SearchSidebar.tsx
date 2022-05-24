import { Button, Input, Radio } from "antd";

const SearchConditionBox = ({ title }: { title: string }) => (
  <div className="mt- grid cursor-pointer grid-cols-2 border-b-2  py-3 hover:opacity-70">
    <span className="font-bold">{title}</span>
    <span>未設定</span>
  </div>
);

export const SearchSidebar = () => (
  <div className="flex h-full w-60 flex-col gap-8 border-r-2 bg-white p-8">
    <div>
      <Input placeholder="検索キーワード"></Input>
    </div>

    <Button type="primary">検索する</Button>

    <SearchConditionBox title="ジャンル"></SearchConditionBox>
    <SearchConditionBox title="発売日"></SearchConditionBox>
    <SearchConditionBox title="出版社"></SearchConditionBox>
  </div>
);
