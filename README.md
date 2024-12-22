# Gestor de Ubicaciones y Clima

Este proyecto es un gestor de ubicaciones que permite a los usuarios insertar, buscar y consultar información relacionada con ubicaciones geográficas, con funcionalidades que incluyen la búsqueda por código postal, provincia, latitud y longitud. Además, utiliza diferentes enfoques para gestionar y almacenar las ubicaciones.

## Funcionalidades

El programa cuenta con un menú interactivo que permite realizar las siguientes operaciones:

1. **Insertar una ubicación**: Permite insertar una nueva ubicación con información como latitud, longitud, dirección, ciudad, barrio, provincia, estado, país y código postal.
2. **Buscar una ubicación**: Permite buscar una ubicación por código postal.
3. **Buscar ubicaciones por provincia**: Permite obtener todas las ubicaciones de una provincia específica y su información.
4. **Mostrar provincias y códigos postales almacenados**: Muestra las provincias y códigos postales almacenados.
5. **Buscar una ubicación por latitud y longitud**: Permite buscar una ubicación específica mediante sus coordenadas geográficas.

## Estructura del Proyecto

Este proyecto está organizado en tres enfoques diferentes para el manejo de las ubicaciones:

1. **Sin base de datos**: Las ubicaciones se almacenan directamente en memoria y se eliminan cuando se cierra el programa.
2. **Modelo híbrido**: Las ubicaciones se almacenan en una base de datos MongoDB y, al iniciar el programa, se cargan en una lista en memoria para su manipulación.
3. **Con base de datos**: Toda la información se obtiene directamente desde la base de datos MongoDB, donde se almacenan y consultan las ubicaciones.



