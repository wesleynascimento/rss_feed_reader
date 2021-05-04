import axios from 'axios';


const BASE_URL = 'http://localhost:8000';
const ACCESS_TOKEN = 'access_token';
const REFRESH_TOKEN = 'refresh_token';

const tokenRequest = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    accept: 'application/json',
  },
});

const loginUser = (email, password) => {
  const loginBody = { email, password };
  return tokenRequest.post('/api/token', loginBody)
    .then((response) => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
      window.localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
      return Promise.resolve(response.data);
    }).catch((error) => {
      console.log(error);
      return Promise.reject(error);
    });
};

const refreshToken = () => {
  const refreshBody = { refresh: window.localStorage.getItem(REFRESH_TOKEN) };
  return tokenRequest.post('/api/token/refresh', refreshBody)
    .then((response) => {
      window.localStorage.setItem(ACCESS_TOKEN, response.data.access);
      return Promise.resolve(response.data);
    }).catch((error) => Promise.reject(error));
};

const isCorrectRefreshError = (status) => status === 401;

const authRequest = axios.create({
  baseURL: BASE_URL,
  timeout: 5000,
  headers: {
    Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    'Content-Type': 'application/json',
  },
});

const logoutUser = () => {
  window.localStorage.removeItem(ACCESS_TOKEN);
  window.localStorage.removeItem(REFRESH_TOKEN);
  authRequest.defaults.headers.Authorization = '';
};

const errorInterceptor = (error) => {
  const originalRequest = error.config;
  const { status } = error.response;
  if (isCorrectRefreshError(status)) {
    return refreshToken().then(() => {
      const headerAuthorization = `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`;
      authRequest.defaults.headers.Authorization = headerAuthorization;
      originalRequest.headers.Authorization = headerAuthorization;
      return authRequest(originalRequest);
    }).catch((tokenRefreshError) => {
      // if token refresh fails, logout the user to avoid potential security risks.
      logoutUser();
      return Promise.reject(tokenRefreshError);
    });
  }
  return Promise.reject(error);
};

authRequest.interceptors.response.use(
  (response) => response, // this is for all successful requests.
  (error) => errorInterceptor(error), // handle the request
);

export {
  tokenRequest, loginUser, logoutUser, refreshToken, authRequest,
  errorInterceptor, BASE_URL, ACCESS_TOKEN, REFRESH_TOKEN,
};
