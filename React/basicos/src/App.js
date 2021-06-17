import React, {Fragment, useState} from 'react'; //Para no Crear Divs demás, se usa fragments
import Header from './components/Header';
import Footer from './components/Footer';
import Producto from './components/Producto';
import Carrito from './components/Carrito';


function App() 
  //Crear listado de productos
{
  const [ productos, setProductos] = useState([
    {id:1, nombre:'Camisa', precio: 25000},
    {id:2, nombre:'Pantalon', precio: 35000},
    {id:3, nombre:'Polera', precio: 10000},
    {id:4, nombre:'Zapatos', precio: 45000},
  ]);
  //State para un carrito de compras
  const[carrito, agregarProducto]= useState([

  ]);

  //Obtener fecha
  const fecha = new Date().getFullYear();
  return (
    <Fragment>

      <Header 
        titulo='Tienda Virtual'
      />

      <h1>Lista de Productos</h1>
      {productos.map(producto => (
        <Producto 
        key= {producto.id}
        producto={producto}
        productos={productos}
        carrito={carrito}
        agregarProducto={agregarProducto}/>  
      ))}
      <Carrito/>

      
      <Footer fecha={fecha} />

    </Fragment>
  );
}
export default App;
