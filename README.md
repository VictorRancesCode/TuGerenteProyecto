# Tu Gerente / Bookings API

![TuGerenteHotel](https://github.com/VictorRancesCode/TuGerenteProyecto/raw/master/documents/hoteltugerente.png) 

## Demo
[Demo](https://tu-gerente-booking.herokuapp.com/api/)

## Requisitos
Para el desarrollo de este proyecto se utilizo Python 3.9.1, los demas requerimientos se encuentran en el archivo requirements.txt

## Instalación
* Clonar Repositorio
```
git clone git@github.com:VictorRancesCode/TuGerenteProyecto.git
```
* Ingresamos a la carpeta
```
cd TuGerenteProyecto
```
* Instalar los requerimientos
```
pip install -r requirements.txt
//Dev
pip install -r requirements.dev.txt
```
* Ejecutar Migraciones
```
    python manage.py migrate
    // o también puedes utilizar
    make migrate
```
* Levantar Proyecto
```
    python manage.py runserver 0.0.0.0:8000
    // o también puedes utilizar
    make runserver
```
## Problema
Se necesita implementar un sistema de reservas para un Hotel con los siguientes requerimientos:
*  Las reservas pueden tener 3 estados: Pendiente, Pagado y Eliminado
* Los datos a almacenar para la reserva son: los detalles del cuarto reservado, los días de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago.

## Solución
* Para la solución se creo las siguientes tablas (Modelos)
- Customer:  Guardamos los datos del cliente que quiere realizar las reservas
- Room: Guardamos los datos de los cuartos(habitaciones)
- Booking: Guardamos los datos de la reserva como la fecha de ingreso y fecha de salida, también los datos del pago (Se podria realizar en otra tabla, pero por el tiempo se decisidio agregarlo a la tabla booking)

## Urls
- [Api](https://tu-gerente-booking.herokuapp.com/api/) : muesta la lista de endpoints habilitados y poder realizar pruebas para eso se utilizo 
- [Admin](https://tu-gerente-booking.herokuapp.com/admin/) 
```
// Credenciales 
username: admin
password: admin
```

## Tests

## Mejoras
* Terminar de agregar Django Money
* Implementar control de permisos
* Algoritmos para control de habitaciones al momento de reserva
* Crear una tabla propia para Pagos(Payment)
* Implentación de tests

## Observaciones
* Uno de los factores importantes al analizar el problema, es poder entender la forma de operación y manejo de reservas de un Hotel [Libro](https://www.pearson.com/store/p/check-in-check-out-pearson-new-international-edition-managing-hotel-operations/P100000056832/9781292034355)