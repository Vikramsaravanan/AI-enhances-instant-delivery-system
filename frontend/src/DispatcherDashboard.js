import React, { useState, useEffect } from 'react';
import axios from 'axios';

function DispatcherDashboard() {
  const [orders, setOrders] = useState([]);
  
  useEffect(() => {
    axios.get('http://localhost:5000/orders').then(res => setOrders(res.data));
  }, []);

  return (
    <div>
      <h1>Live Orders</h1>
      {orders.map(order => (
        <div key={order.id}>
          <p>{order.address} - ETA: {order.eta}</p>
        </div>
      ))}
    </div>
  );
}

export default DispatcherDashboard;