// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DispatcherDashboard from './DispatcherDashboard';
import MapView from './MapView';
import './styles.css';

function App() {
  const [orders, setOrders] = useState([]);
  const [agents, setAgents] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch live data from backend
  const fetchData = async () => {
    try {
      const [ordersRes, agentsRes] = await Promise.all([
        axios.get('http://localhost:5000/orders'),
        axios.get('http://localhost:5000/agents')
      ]);
      
      setOrders(ordersRes.data);
      setAgents(agentsRes.data);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Real-time updates every 10 seconds
  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 10000);
    return () => clearInterval(interval);
  }, []);

  // Handle new order submission
  const handleNewOrder = async (orderData) => {
    try {
      await axios.post('http://localhost:5000/new_order', orderData);
      fetchData(); // Refresh data
    } catch (err) {
      setError('Failed to create order');
    }
  };

  if (isLoading) return <div className="loading">Loading live data...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="app">
      <header>
        <h1>?? Instant Delivery Dispatch</h1>
        <p>Real-time AI-powered delivery management</p>
      </header>

      <div className="main-container">
        <div className="map-container">
          <MapView agents={agents} orders={orders} />
        </div>
        
        <div className="dashboard-container">
          <DispatcherDashboard 
            orders={orders} 
            agents={agents} 
            onNewOrder={handleNewOrder} 
          />
        </div>
      </div>

      <footer>
        <p>AI Routing System | {new Date().toLocaleTimeString()}</p>
      </footer>
    </div>
  );
}

export default App;