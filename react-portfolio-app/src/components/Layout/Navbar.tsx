import { useNavigate } from 'react-router-dom';

const Navbar = () => {
  const navigate = useNavigate();

  return (
    <nav style={{
      height: '60px',
      backgroundColor: '#ffffff',
      boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '0 20px',
      position: 'sticky',
      top: 0,
      zIndex: 1000
    }}>
      <div 
        style={{ cursor: 'pointer', fontWeight: 'bold', fontSize: '1.2rem' }}
        onClick={() => navigate('/')}
      >
        Prithwish
      </div>
      
      <div style={{
        display: 'flex',
        gap: '20px'
      }}>
        <button
          onClick={() => navigate('/')}
          style={{
            border: 'none',
            background: 'none',
            cursor: 'pointer',
            padding: '8px',
            color: '#333'
          }}
        >
          Home
        </button>
        {/* <button
          onClick={() => navigate('/form')}
          style={{
            border: 'none',
            background: 'none',
            cursor: 'pointer',
            padding: '8px',
            color: '#333'
          }}
        >
          Add Item
        </button> */}
      </div>
    </nav>
  );
};

export default Navbar;
