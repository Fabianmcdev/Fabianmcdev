import React from 'react';
//expression function o arrow functions
const Footer = ({fecha}) => (
    
    //ACA PUEDE IR CODIGO JAVASCRIPT PARA VALIDACIONES ANTES, COMO UN CARRITO DE COMPRAS
    //return(ventajas de usar SFC)
     
    <footer>
        <p>
            Todos los derechos reservados &copy; {fecha}
        </p>
    </footer> );
export default Footer; 