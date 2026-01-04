import { getProfile } from '../api/auth';

useEffect(() => {
  getProfile(localStorage.getItem("token"))
    .then(res => setProfile(res.data));
}, []);
