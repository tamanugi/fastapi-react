import type { Methods } from "@/api/api/books/search";

export type BookSearchQuery = Exclude<Methods["get"]["query"], undefined>;
