import { lazyImport } from "@/utils/lazyload";

const { BookHome } = lazyImport(
  () => import("@/features/books/index"),
  "BookHome"
);

export const protectedRoutes = [{ path: "/", element: <BookHome /> }];
