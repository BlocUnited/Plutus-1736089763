import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './styles/style.css';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import App from './App';

const Main = () => {
    return (
        <Router>
            <Switch>
                <Route path="/login" component={LoginPage} />
                <Route path="/dashboard" component={Dashboard} />
                <Route path="/" component={App} />
            </Switch>
        </Router>
    );
};

ReactDOM.render(<Main />, document.getElementById('root'));
