import axios from 'axios';

export const axiosInstance = ({ url, method, ...options }: { url: string, method: string, [key: string]: any }) => {
  return axios({
    ...options,
    url: `http://localhost:8000${url}`,
    method,
  });
};
