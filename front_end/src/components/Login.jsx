import { login } from '../api/auth';

function Login() {
  const handleLogin = async () => {
    const res = await login({ email, password });
    localStorage.setItem("token", res.data.access);
  };
}
