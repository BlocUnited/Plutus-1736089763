import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import InputField from '../components/InputField';
import Button from '../components/Button';
import { postData } from '../utils/api';
import { API_ENDPOINTS } from '../utils/constants';
import './LoginPage.css';

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const history = useHistory();

    const handleLogin = async (e) => {
        e.preventDefault();
        setError('');
        try {
            const response = await postData(API_ENDPOINTS.LOGIN, { email, password });
            // Handle successful login (e.g., store token, redirect)
            console.log(response);
            history.push('/dashboard');
        } catch (err) {
            setError('Login failed. Please check your credentials.');
        }
    };

    return (
        <div className="login-page">
            <h1>Login</h1>
            {error && <p className="error-message">{error}</p>}
            <form onSubmit={handleLogin}>
                <InputField type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <InputField type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <Button label="Login" type="primary" onClick={handleLogin} />
            </form>
        </div>
    );
};

export default LoginPage;
