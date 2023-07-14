# Resultados de optimisacion de rendimiento
A traves de procesos de ensayo y error hemos determinado los diferentes errores en el codigo.
Consideramos que el programa main2 descrito en esta carpeta esta siendo afectada por los procesos propios del CPU basado en los siguientes datos:
1. utilizando la herramienta Htop del sistema operativo Linux podemos determinar que el porcentaje de uso del CPU sin ejecutar el programa. el mismo es del 6.6%
Al correr el programa main2 la herramiento Htop muestra que el porcentaje de uso del CPU pasa del 
6.6% al 29.7% marcando un incremento significativo el el uso del CPU de casi 350% del que usa normalmente
2. el la terminal de linux se ejecuta la herramienta psstat y su funcion iostat que muestra el rendimiento del sistema al ejecutarse las operaciones de entrada y salida E/S. 
Al ejecutarse la herramienta se muestran diferentes datos pero los que nos interesan son:
- con el programa sin correr: 
Transacciones por segundo (tps): 7.54
Tasa de transferencia de lectura (kB_read/s): 64.98
Tasa de transferencia de escritura (kB_wrtn/s): 193.74

- corriendo el programa en la terminal
Transacciones por segundo (tps): 7.54
Tasa de transferencia de lectura (kB_read/s): 64.87
Tasa de transferencia de escritura (kB_wrtn/s): 194.02

## Conclusiones basada en datos
No se muestra una diferencia significativa en el movimiento de datos de E/S de acuerdo a la herramienta iostat, por lo tanto buscaremos concurrencias que puedan mejorar la funcion del CPU.
- La primera herramienta de concurrencia que usamos fue Threadts. a pesar de que bajo el tiempo de ejecucion del programa de 24s a 14s consideramos que aun podemos mejorar este tiempo
- La segunda herramienta de concurrencia que utilizamos fue multiprocessing. Esta ultima bajo el tiempo de ejecucion del programa de 24s a 4.7s siendo una herramienta util al momento de optimizar el rendimiento de nuestro programa.