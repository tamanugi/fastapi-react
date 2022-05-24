import { BasicLayout } from "@/components/layouts/BasicLayout";
import { SearchResult } from "./SearchResult";
import { SearchSidebar } from "./SearchSidebar";

export const Home = () => (
  <BasicLayout>
    <div className="flex h-full">
      <div className="fixed h-full">
        <SearchSidebar></SearchSidebar>
      </div>

      <div className="ml-[300px] w-full px-12 py-6">
        <SearchResult></SearchResult>
      </div>
    </div>
  </BasicLayout>
);
