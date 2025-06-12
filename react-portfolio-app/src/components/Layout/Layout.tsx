import React from 'react';
import { Outlet } from 'react-router-dom';
import Navbar from './Navbar';
import Footer from './Footer';

const Layout: React.FC = () => {
  return (
    <div className="layout" style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <Navbar />
      <main
        style={{
          flexGrow: 1,
          minHeight: 'calc(100vh - 120px)', // assuming 60px header + 60px footer
          padding: '20px',
          backgroundColor: '#f5f5f5',
        }}
      >
        <Outlet />
      </main>
      <Footer />
    </div>
  );
};

export default Layout;
