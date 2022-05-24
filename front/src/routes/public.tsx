import { lazyImport } from "@/utils/lazyload";

const { Home } = lazyImport(
  () => import("@/components/pages/Home/index"),
  "Home"
);

export const publicRoutes = [{ path: "/", element: <Home /> }];
