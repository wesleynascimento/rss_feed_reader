import axios from "axios";

const BASE_URL = "http://localhost:8000/api/";
const ACCESS_TOKEN = "access_token";

export const http = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    "Content-Type": "application/json",
  },
});
