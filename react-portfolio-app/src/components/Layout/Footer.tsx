const Footer = () => {
  return (
    <footer style={{
      height: '60px',
      backgroundColor: '#ffffff',
      borderTop: '1px solid #eaeaea',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      position: 'fixed',
      bottom: 0,
      width: '100%'
    }}>
      <p style={{ color: '#666', margin: 0 }}>
        © {new Date().getFullYear()} Your Company. All rights reserved.
      </p>
    </footer>
  );
};

export default Footer;
