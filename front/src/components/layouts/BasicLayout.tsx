import { Layout } from "antd";

const { Header, Content } = Layout;

type BasicLayoutProps = {
  children: React.ReactNode;
};

export const BasicLayout = ({ children }: BasicLayoutProps) => (
  <Layout className="h-screen">
    <Layout className="bg-white pt-16">
      <Content className="">{children}</Content>
    </Layout>
    <Header className="fixed top-0 w-full bg-blue-400">
      <div className=" flex">
        <div>BOOKS</div>
      </div>
    </Header>
  </Layout>
);
