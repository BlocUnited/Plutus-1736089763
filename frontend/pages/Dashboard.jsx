import React, { useEffect, useState } from 'react';
import { fetchData } from '../utils/api';
import { API_ENDPOINTS } from '../utils/constants';
import Card from '../components/Card';
import Button from '../components/Button';
import './Dashboard.css';

const Dashboard = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchDashboardData = async () => {
            try {
                const result = await fetchData(API_ENDPOINTS.GET_DASHBOARD + 'user_id'); // Replace 'user_id' with actual user ID
                setData(result);
            } catch (err) {
                setError('Failed to load dashboard data.');
            } finally {
                setLoading(false);
            }
        };
        fetchDashboardData();
    }, []);

    if (loading) return <p>Loading...</p>;
    if (error) return <p className="error-message">{error}</p>;

    return (
        <div className="dashboard">
            <h1>Dashboard</h1>
            {data && data.map(item => (
                <Card key={item.id} title={item.title} content={item.content} footer={<Button label="View" type="primary" onClick={() => {}} />} />
            ))}
        </div>
    );
};

export default Dashboard;
