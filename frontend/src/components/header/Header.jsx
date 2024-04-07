import "./header.css";

const Header = () => {
    return (
        <div style={{ fontWeight: 'bold', fontFamily: 'Helvetica, sans-serif', padding: '20px', textAlign: 'center', backgroundColor: '#646464', color: 'white', fontSize: '24px'}}>
            <img src="/src/assets/sfmta-logo-400x400_1.svg" alt="SFMTA Logo" style={{ marginRight: '20px', height: '1.3em' }} />
            SFMTA GARAGES
        </div>
    )
}
export default Header