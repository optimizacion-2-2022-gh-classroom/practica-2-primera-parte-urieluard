<p align = "center">
    <img src="images/logo_itam.png" width="300" height="110" />

---

## Tabla de contenido:
    
1. [Integrantes y roles asignados](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#integrantes-y-roles-asignados)
    
2. [Acerca de este proyecto](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#acerca-de-este-proyecto)
    
3. [Estructura básica del repositorio](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#estructura-b%C3%A1sica-del-repositorio)
    
4. [¿Qué lenguajes y paqueterías utlizamos?](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#qu%C3%A9-lenguajes-y-paqueter%C3%ADas-utlizamos)

5. [Ambientes en Contenedor](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#ambientes-en-contenedor)

6. [Instancia de AWS](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#instancia-de-aws)

7. [Resultados obtenidos](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#resultados-obtenidos)
    
8. [Referencias](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#referencias)
    
---

## Integrantes y roles asignados

|     ***Integrante***      |             ***Usuario de GitHub***             |  ***Rol asignado***        |                       
|:-------------------------:|:-----------------------------------------------:|:--------------------------:|
|  Ita                      |    [sancas96](https://github.com/sancas96)      | Equipo de Programación     | 
|  Luz                      |    [LuzVerde23](https://github.com/LuzVerde23)  | Equipo de Programación     | 
|  Edgar                    |    [EddOselotl](https://github.com/EddOselotl)  | Equipo de Programación     | 
|  Uriel                    |    [urieluard](https://github.com/urieluard)    | Administrador del proyecto | 

---    

## Acerca de este proyecto
    
Esta práctica se enfoca en el uso de Minikube, Kubeflow y Kale para construcción y lanzamiento de pipelines de procesamiento y experimentación del paquete construído en la parte II de la práctica 1 [(consultar aquí)](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23) para resolver el problema de flujo máximo con el algoritmo de Ford-Fulkerson.

El objetivo es realizar experimentos con las herramientas de Minikube, kubeflow y Kale para reportar el funcionamiento del programa implementado en la parte II de la práctica 1. Para elllo se se hacen pruebas con diferentes redes: con tamaños y conectividad diferentes (redes de pequeña y mediana escala), algunas de representaciones documentadas y otras de redes generadas de forma aleatoria.
 
## Estructura básica del repositorio

```
practica-2-primera-parte-urieluard:
 |
 ├── README.md                                   <- Contiene información relevante del proyecto.
 │
 ├── reporte_equipo_2_parte_1_practica_2.ipynb   <- Note Book con el reporte donde se muestran los resultados de las pruebas realizadas al algoritmo.
 |
 ├── BD                                          <- Bases de datos utilizadas para comprobar el método
 │
 ├── dockerfiles                                 <- Carpeta con archivo de Docker que crea la imágen del entorno para la ejecución del método
 │
 ├── notebooks_apoyo                             <- Notebooks de apoyo al proyecto
 │
 └── images                                      <- Contiene las imágenes utilizadas en el repositorio.
``` 

## ¿Qué lenguajes y paqueterías utlizamos?

<img src="images/minikube.jpeg" width="270" height="100" />

[Minikube](https://minikube.sigs.k8s.io/docs/start/)


<img src="images/kubeflow.png" width="270" height="100" />

[kubeflow](https://www.kubeflow.org/)


<img src="images/kale_logo.png" width="270" height="100" />

[kubeflow-kale](https://github.com/kubeflow-kale/kale)

---

## Ambientes en Contenedor

### Binder

En el siguiente botón se realiza el lanzamiento de un ambiente ejeutable donde se podrá interactuar con el paquete realizado (**MaxFlowAeiu**) y se ejecuta el notebook del reporte.
    
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard/main?labpath=reporte_equipo_2_parte_1_practica_2.ipynb)

### Docker

De igual forma, en este repositorio se cuenta con un archivo de Docker (Docker File) para crear una imagen del contenedor con las librerías y el paquete MaxFlowAeiu para que pueda ser utilizado desde [Docker](https://www.docker.com/).

<p align = "center">
    <img src="images/Docker-Logo.png" width="300" height="110" />

Las imágenes de Docker que se utilizaron de referencia para esta práctica se tomaron de [-1-](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#referencias)

---

## Instancia de AWS

Se creó una instancia de AWS con la configuración mostrada en [-2-](https://github.com/optimizacion-2-2022-gh-classroom/practica-2-primera-parte-urieluard#referencias) para correr el pipeline de nuestro programa y validar que las pruebas realizadas fueron ejecutadas correctamente.

<p align = "center">
    <img src="images/aws.png" width="300" height="110" />

---

## Resultados obtenidos

El Pipeline final, después de las pruebas realizadas conforme se reporta en el archivo: _reporte_equipo_2_parte_1_practica_2.ipynb_, se muestra a continuación:

<p align = "center">
    <img src="images/ejemplo4.png" width="900" height="530" />

La tabla de resultados siguiente reporta el comportamiento del algoritmo implementado en las pruebas realizadas:



---

## Referencias

[1] Dockerfiles, Erick Palacios Moreno -ITAM [(liga al repositorio)](https://github.com/palmoreck/dockerfiles/tree/master/jupyterlab/kale/general/certs/0.6.1)
    
[2] Wiki del repositorio de la materia de Análisis Numérico y Computo Científico, Erick Palacios Moreno -ITAM [(liga al repositorio)](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/6.Minikube-y-AWS)
