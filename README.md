**Parte 1 de la práctica II, Optimización 2: uso de *Minikube, Kubeflow* y *Kale* para construcción y lanzamiento de pipelines de procesamiento y experimentación del paquete construído en la práctica 1 para resolver problemas de optimización convexa.**

Antes de iniciar a trabajar: 

* **Sólo una persona de cada equipo debe darle click a la liga** que está indicada en la publicación de canvas. Una vez que le dé click a la liga tal persona **invite** a sus integrantes de su equipo como **Admin**. Para invitar a su integrante ir dentro del repo a Settings -> Manage Access y enviar la invitación ingresando user de github de su integrante.
    

# Instrucciones

Se encuentran en el archivo [instrucciones.ipynb](instrucciones.ipynb).

Usen `git` para llevar la historia de cambios en la realización de sus notebooks o cualquier otro archivo y subirlos a sus repos. No se revisarán aquellos archivos que tengan un commit con todas las respuestas. El trabajo es incremental.

**Deben usar la funcionalidad de github**: *issues*, *milestones*, *projects*, *reviewers*, *asignees* o lo que ustedes consideren de github que les ayudará a comunicarse/organizarse (no tienen que usar todas las funcionalidades anteriores y cada equipo decide qué usar). Ver por [ejemplo video para crear proyectos en github](https://youtu.be/z4Xpif7HI04).


# Dinámica

Dividir a su equipo para realizar cuatro tareas. **Ustedes deciden qué integrante resuelve qué tarea (algunas personas tendrán que hacer más de una tarea)**:

1. 1 persona que defina cuáles son los parámetros que existen en su problema de optimización y en su método numérico. Ya definidos debe utilizarlos para construir y lanzar pipelines con [Kale](https://github.com/kubeflow-kale/kale) y monitorearlos con el dashboard de [Kubeflow](https://github.com/kubeflow/kubeflow). 

2. 1 persona que escriba en una tabla las corridas con los diferentes parámetros utilizados del punto anterior, así como sus resultados y las fechas de lanzamiento. Para esto puede apoyarse del listado que se hace en el dashboard de Kubeflow.

3. 1 persona que escriba un documento de apoyo en el que se incluya la tabla del punto anterior y posibles errores que hayan surgido en las corridas. Con tal documento debe informarle al *project manager* la creación de *issues* que atiendan tales errores y hacer reimplementaciones del paquete desarrollado en su práctica 1 para resolver tales *issues*.

4. 1 persona que sea *project manager* (más detalles de este rol en las notas) y haga una revisión que los *tests* creados en su práctica 1 continúan pasándose exitosamente con las reimplementaciones del punto anterior. Además, debe añadir nuevos *tests* que atiendan las reimplementaciones.

Lo anterior asume que tienen en su cuenta de AWS Academy una instancia con *Kale, Kubeflow* y *minikube* corriendo. Ver [6.Minikube y AWS: AWS Academy](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/6.Minikube-y-AWS) para esto y [video](https://youtu.be/SusT5xQN1ro) de la clase en la que discutimos tales herramientas. Aquí [minikube_kubeflow_kale_examples](https://github.com/palmoreck/minikube_kubeflow_kale_examples) encuentran *notebooks* ejemplos listos para lanzarse con *Kale* y monitorear su ejecución con *Kubeflow*.

Entre todos los y las integrantes tienen que dar *feedback* si es necesario en la resolución de las tareas que haya duda entre ustedes. El *feedback* consiste en resolver/explicar las dudas que existan. **Las personas asignadas a la tarea correspondiente son las que realizan los *commits* una vez resueltas las dudas**.

Los puntos 1, 2, 3 y 4 anteriores los realizan de forma iterativa hasta finalizar las tareas y que estén en acuerdo las y los integrantes de cada equipo con las soluciones.

# Lenguajes de programación

Ustedes eligen el lenguaje de programación a usar. La sugerencia es *Python3*.

# Calificación

La calificación de esta primera parte es la mitad de la práctica 2. Se asgina una calificación individual por tarea asignada y una calificación por equipo. Se calificará de acuerdo a los *commits* realizados y a los avances que realizan en su trabajo incremental. 

# AWS

Agendar reunión con el prof para que muestren el lanzamiento de los pipelines de procesamiento con Kale y monitoreo con Kubeflow. Tal reunión puede ser en cuanto ya tengan un *notebook* con celdas identificadas vía *Kale* y que vayan a utilizar para sus corridas. También puede ser una vez que tengan su reporte o un poquito después de la fecha de entrega de su práctica. En la reunión uds levantan la infraestructura en AWS para usar *Minikube, Kubeflow* y *Kale*.

Adjunten *screenshots* en un directorio de su repo para mostrar su uso de AWS, debe aparecer en el *screenshot* su nombre, clave única u otra forma de identificar su trabajo. En los *screenshots* incluyan la lista de experimentos, algunos de los resultados y el grafo ejecutados en *Kubeflow* así como el *notebook* con celdas identificadas vía *Kale*.

# Notas

* **Para la entrega crear un archivo con nombre:** `reporte_equipo_<aquí colocar_número>_parte_1_practica_2.ipynb` que contiene ejecución del paquete para los ejemplos elegidos y es el que me mostrarán en la reunión. Este *notebook* debe tener la identificación de las celdas con el panel de *Kale*. 

* Es muy importante la **experimentación** para resolver problemas en la ciencia. En esta práctica este es uno de los **objetivos** para robustecer sus implementaciones con ambientes controlados :)

* *Project manager*: es la persona más importante para el éxito del proyecto. Conoce el/los objetivo(s) a resolver, detalla las tareas que realizarán el grupo de programación y el grupo de revisión (creación de *tests* en nuestro caso), organiza y asigna a personas a ambos grupos, crea tarjetas en el [project board de github](https://help.github.com/en/github/managing-your-work-on-github/creating-a-project-board) y [milestones](https://help.github.com/en/github/managing-your-work-on-github/tracking-the-progress-of-your-work-with-milestones) para dar seguimiento a [issues](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue). Mantiene un contacto directo con el prof para dudas que tengan y para avisar en qué fase se encuentran. Les explica a su equipo de trabajo la correcta creación de *issues*, solución de los mismos y el uso de *milestones* y del *project board*.

* La división de las tareas y roles está está inspirada en el *framework* [scrum](https://www.youtube.com/watch?v=b02ZkndLk1Y&feature=emb_logo) en un ambiente laboral real (y en esta práctica estamos super-simplificando tal *framework*).

* Añadan referencias utilizadas para su trabajo en su `README.md`.

* **Los commits deben tener un mensaje explicatorio, no hacer lo siguiente:**

```
git commit -m "create 1" -i archivo1.txt

git commit -m "update 1" -i archivo1.txt #qué es update 1?

git commit -m "update 2" -i archivo1.txt #qué es update 2?

git commit -m "update 3" -i archivo1.txt #qué es update 3?
```

**así también para los *issues*, *projects*, *milestones*...**

* Esta organización es nuestro *playground* utilicen los repos de aquí para practicar :)

* Recuerden:

    * ir guardando su trabajo si usan binder y usar `git` para llevar la historia de sus cambios en sus repos :)
    * poner las referencias que utilizan (aún si le preguntan a una compañera o compañero de la clase coloquen esto en su entrega) pues no está permitido copiar y escribir que lo hicieron sin citar sus fuentes.


* Para dudas creen un *room* de gitter e ínvitenme :) (si ya lo hicieron omitan este enunciado)

* **Su trabajo individual y su tiempo es muy valioso e importante, también el trabajo en equipo. Si alguna persona del equipo no realizó su tarea asignada, esperaría que lo resolvieran entre ustedes, si no lo resuelven avísenme y no realicen su tarea asignada. Si tienen algún problema (familiar, salud,...) infórmenme con tiempo para ver qué podemos hacer :)**


