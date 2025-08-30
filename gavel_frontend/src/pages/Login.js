import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import apiClient from '../services/api';
import '../App.css';

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const response = await apiClient.post('/get-token/', formData);
      // Store the token securely
      localStorage.setItem('authToken', response.data.token);
      // Redirect to a dashboard or home page after login
      // For now, let's just log it and show an alert
      alert('Login successful! Token stored.');
      // navigate('/dashboard'); // Example for future navigation
    } catch (err) {
      setError('Invalid username or password. Please try again.');
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-form">
        <h2>Welcome Back!</h2>
        <p>Log in to continue your coding journey.</p>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              name="username"
              id="username"
              value={formData.username}
              onChange={handleChange}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              name="password"
              id="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>
          {error && <p className="error-message">{error}</p>}
          <button type="submit" className="auth-button">Log In</button>
        </form>
        <div className="switch-auth">
          <span>Don't have an account? </span>
          <Link to="/signup">Sign Up</Link>
        </div>
      </div>
    </div>
  );
};

export default Login;