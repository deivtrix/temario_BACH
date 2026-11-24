# 📘 2DO BGU — PARCIAL 2 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología
**Unidad:** Diseño Paramétrico por Bloques
**Ya ejecutado al inicio del Parcial 2:** S1-S2: Mini Golf con motores en Tinkercad Sim Lab (Individual 1).

---

# CAPÍTULO #1
**Tema:** Mecanismo de Motor Deslizante en Tinkercad Sim Lab *(Grupal)*  

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Crear** un mecanismo que se mueva en línea recta en Sim Lab, como una puerta automática.
* **¿Para qué me sirve en la vida?** Así funcionan las puertas corredizas de centros comerciales, impresoras 3D y elevadores.

---

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Proyectar Página 3 y 4:** Mostrar en Sim Lab en vivo:
  1. Crear una base (**Estática**) y una pieza móvil (**Dinámica**).
  2. Conectarlas con el **Motor Deslizante (*Slider*)** orientando la flecha en el eje correcto.
  3. Ajustar velocidad/límite y presionar *Play* para que vean el desplazamiento lineal.

### Práctica / Reto
* **Instrucción :** *"En equipos, diseñen una Puerta Corrediza, Prensa o Lanzador Lineal usando al menos 1 motor deslizante. Pongan los nombres del grupo en texto 3D sobre la base."*

---

---

# CAPÍTULO #2
**Tema:** Introducción a Tinkercad Codeblocks (Diseño 3D Programado) *(Individual 2)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Crear** figuras 3D en Tinkercad usando bloques de código en lugar de moverlas con el mouse.
* **¿Para qué me sirve en la vida?** Así funciona el diseño paramétrico en ingeniería y arquitectura: cambias un número y toda la pieza se ajusta automáticamente.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **¿Dónde entrar?** En Tinkercad -> **Crear** -> **Bloques de código (Codeblocks)**.
* **3 bloques base:** `Formas` (Cilindro/Cubo), `Modificar` (`Mover X, Y, Z`, `Escalar`, `Rotar`), `Crear grupo`.
* **Modelación:** Programar una **mini mesa o llavero** en 6 bloques y presionar *Play* para ver cómo se construye solo paso a paso.

### Práctica / Reto
* **15 – 25 min (Guiada):** Todos crean la base de una **mesa pequeña o asiento** usando bloques `Cubo`, `Mover` y `Crear grupo`.
* **25 – 40 min (Reto Solos — Actividad 4):** *"Programa una **Silla 3D completa** usando 100% bloques en Codeblocks (4 patas alineadas en `X, Y, Z`, asiento y espaldar firme, todo unido con `Crear grupo`)."*

---

# CAPÍTULO #3
**Tema:** Bucles y Rotación en Tinkercad Codeblocks (Escalera / Torre Paramétrica)  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** una escalera en espiral en Codeblocks usando bucles `repetir` para no dibujar pieza por pieza.
* **¿Para qué me sirve en la vida?** Para automatizar patrones repetitivos (dientes de un engranaje, gradas, edificios o piezas mecánicas) con pocas líneas de código.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **2 bloques nuevos:**
  * `Crear variable` (ej. `altura = 0` o `angulo = 0`).
  * `Repetir N veces` + `Cambiar variable por X` dentro del bucle.
* **Modelación:** Crear 1 escalón desplazado del centro, meterlo en `Repetir 15 veces`, subir en `Z` y rotar `24°` en cada vuelta alrededor de `[0,0,0]`.

### Práctica / Reto
* **15 – 25 min (Guiada):** Todos programan la escalera en espiral básica de 12–15 escalones.
* **25 – 40 min (Reto Solos):** *"Agrega una columna central o barandal, o modifica el código para crear una **torre retorcida / adorno paramétrico** cambiando los colores o la escala en cada vuelta."*

---

# CAPÍTULO #4
**Tema:** Proyecto Codeblocks: Engranaje o Mecanismo Paramétrico  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Crear** un engranaje en Codeblocks que cambie su número de dientes modificando una sola variable.
* **¿Para qué me sirve en la vida?** Así se diseñan piezas mecánicas profesionales (engranajes, poleas, hélices) que luego se imprimen en 3D o cortan en láser.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* Mostrar la lógica matemática simple:
  * Variable `dientes = 12`.
  * Ángulo de giro por vuelta = `360 / dientes`.
  * Bucle `Repetir dientes veces`: colocar diente en el borde y rotar `360 / dientes` grados alrededor de `[0,0,0]`, luego unir con cilindro central y perforar eje hueco.

### Práctica / Reto
* **Instrucción:** Cada estudiante programa su engranaje (o hélice/rueda dentada) parametrizado con `dientes`, agrega el hueco central del eje y prueba cambiar el número de `dientes` para verificar que funciona.

---

# CAPÍTULO #5
**Tema:** Refuerzo: Diseño Libre Programado en Codeblocks *(Refuerzo)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Diseñar** una figura simétrica propia (estrella o adorno) en Codeblocks usando bucles `repetir`.
* **¿Para qué me sirve en la vida?** Para pensar en patrones y simetría computacional antes de pasar a programación C++ en el siguiente quimestre.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* Mostrar cómo combinar un patrón radial (`360 / ramas`) con escala decreciente (`Escalar`) para hacer un pino o estrella en 10 bloques.

### Práctica / Reto
* Quienes deban algo de Codeblocks se nivelan hoy; el resto diseña su modelo simétrico libre con mínimo 1 bucle `Repetir`.

---

# CAPÍTULO #6
**Tema:** Cierre del Bloque 3D / Codeblocks y Puente a Arduino *(Colchón)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Evaluar** nuestros diseños finales de Sim Lab y Codeblocks para cerrar el módulo 3D antes de Arduino.
* **¿Para qué me sirve en la vida?** Para cerrar ordenadamente un proyecto de diseño antes de pasar a la etapa de electrónica y programación en C++.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* Quienes deban entregas de Sim Lab o Codeblocks las completan hoy; el resto mejora su engranaje/diseño y revisa su promedio.

### Práctica / Reto
* Avance rápido de lo que viene en Parcial 3 (`millis()` y Robot con Puente H) + autoevaluación del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino*):
  1. Simular mecanismos lineales con motor deslizante en Tinkercad Sim Lab.
  2. Crear figuras 3D usando coordenadas y bloques de código en Codeblocks.
  3. Usar variables y bucles `Repetir` para diseñar estructuras en espiral o simétricas.
  4. Programar piezas paramétricas (engranajes) cambiando el número de dientes con una variable.
