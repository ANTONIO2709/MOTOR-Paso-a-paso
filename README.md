# MOTOR-Paso-a-paso
En este proyecto, aprenderemos a conducir el motor paso a paso y entenderemos su principio de funcionamiento.

Motor paso a paso

Hemos aprendido motor de CC y servo antes: el motor de CC puede girar constantemente, pero no podemos hacerlo
rotar a un ángulo específico. Por el contrario, el servo ordinario puede girar a un cierto ángulo, pero no puede girar
Constantemente. En este capítulo, aprenderemos un motor que puede girar no sólo constantemente, sino también a un
ángulo, motor escalonado. El uso del motor paso a paso puede lograr una mayor precisión del movimiento mecánico fácilmente.

Motor paso a paso es un dispositivo de control de bucle abierto que convierte la señal de pulso eléctrico en angular
desplazamiento o desplazamiento lineal. En condiciones de no sobrecarga, la velocidad del motor y la ubicación de
la parada depende solamente de la frecuencia de la señal de pulso y el número de pulso, y no se ve afectada por los cambios de carga.
Un pequeño motor de paso de desaceleración de cuatro fases se muestra de la siguiente manera segun figura 1

El diagrama esquemático del motor paso a paso de cuatro fases se muestra en figura 2

La pieza exterior es el estator y el interior es el rotor del motor. Hay un cierto número de bobinas,
generalmente entero múltiplo de número de fases, en el estator y cuando se enciende, un electroimán será
para atraer una parte convexa (generalmente hierro o imán permanente) del rotor. Por lo tanto, la
motor puede ser accionado por la conducción de las bobinas en el estator ordenadamente.

Un proceso de conducción común es segun figura 3

En el curso anterior, el motor paso a paso gira un cierto ángulo una vez, lo que se denomina paso. Mediante el control
el número de pasos de rotación, puede controlar el ángulo de rotación del motor paso a paso. Controlando el tiempo
entre dos pasos, puede controlar la velocidad de rotación del motor paso a paso. Al girar en el sentido de las agujas del reloj, el orden
de bobina encendida es: A-B-C-D-A-...... . Y el rotor girará de acuerdo con el orden, paso a paso
dimitente, llamado cuatro pasos cuatro palmaditas. Si las bobinas se encienden en el orden inverso, D .C.B.A....
el rotor girará en sentido antihorario.
Motor paso a paso tiene otros métodos de control, tales como conectar una fase, luego conectar la fase A B, el estator
estar situado en el medio de la A B, sólo un medio paso. De esta manera puede mejorar la estabilidad del motor paso a paso,
y reducir el ruido, la secuencia de la bobina encendida es: A -AB - B - BC - C - CD - D - DA - A ...
rotará de acuerdo con la orden, medio paso por medio paso, llamado cuatro paso ocho palmaditas. Igualmente, si la bobina
se enciende en orden inverso, el motor paso a paso girará en rotación inversa.
El estator del motor escalonado que utilizamos tiene 32 polos magnéticos, por lo que un círculo necesita 32 pasos. El eje de salida de
el motor escalonado está conectado con un conjunto de engranajes de reducción, y la relación de reducción es 1/64. Así que la salida final
eje gira un círculo que requiere un paso de 32 * 64 x 2048.

Controlador de motor de paso a paso ULN2003

El controlador de motor paso a paso ULN2003 se utiliza para convertir la señal débil en una potente señal de control para
motor escalonado. La señal de entrada IN1-IN4 corresponde a la señal de salida A-D, y 4 LED está integrado en
la placa para indicar el estado de las señales. La interfaz PWR se puede utilizar como fuente de alimentación para
motor. Por abandono, el PWR y el VCC están conectados por un cortocircuito.

codigo:

Este código utiliza el modo de cuatro pasos y cuatro pat para conducir el motor paso a paso hacia adelante y la dirección inversa.

Después de ejecutar el programa, el motor paso a paso girará 360º en el sentido de las agujas del reloj y luego 360º en el sentido contrario a las agujas del reloj,
Circulamente

En el código, defina cuatro pines del motor paso a paso y el orden de la fuente de alimentación de la bobina del modo de rotación de cuatro pasos.

Subfunción moveSteps (dirección, ms, pasos) se utiliza para el número de ciclo específico del motor paso a paso.

Subfuncion MotorStop () se utiliza para detener el motor paso a paso.

Finalmente, en el ciclo while de la función principal, gire un círculo en el sentido de las agujas del reloj, y luego un círculo en sentido antihorario.
Según el conocimiento previo del motor paso a paso, se puede saber que la rotación del motor paso a paso
para un círculo requiere 2048 pasos, es decir, 2048/4-512 ciclo.

La subfunción moveOnePeriod (dirección, ms) conducirá el motor paso a paso girando cuatro pasos en el sentido de las agujas del reloj o
en sentido antihorario, cuatro pasos como un ciclo. Donde el parámetro "dir" indica la dirección de rotación, si "dir" es 1, el servo
girará hacia adelante, de lo contrario gira para invertir la dirección. El parámetro "ms" indica el tiempo entre cada
dos pasos. El motor de paso a paso de "ms" utilizado en este proyecto es de 3 ms (el tiempo más corto), menos de 3 ms superarán
el límite de velocidad del motor paso a paso que resulta en que el motor no puede girar.
