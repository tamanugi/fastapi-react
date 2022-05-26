import axios from "axios";
import axiosClient from "@aspida/axios";
import api from "@/api/$api";

export const client = api(
  // TODO: from config
  axiosClient(axios, { baseURL: "http://localhost:8000" })
);
