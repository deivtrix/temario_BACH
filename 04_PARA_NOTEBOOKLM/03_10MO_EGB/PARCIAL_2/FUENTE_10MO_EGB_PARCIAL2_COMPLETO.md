# 📘 10MO EGB — PARCIAL 2 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología
**Unidad:** Conexiones Seguras y Primer Código
**Ya ejecutado al inicio del Parcial 2:** S1: ¿Qué es Arduino? (concepto). S2: Práctica de Empalmes (Taller Calificado Grupal).

---

# CAPÍTULO #1
**Tema:** Conectores y Aislantes Eléctricos *(Individual 1 — Infografía / Consulta)*  

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Clasificar** qué conectores y aislantes usar para unir cables sin que se suelten ni hagan corto.
* **¿Para qué me sirve en la vida?** Para conectar cables en Arduino o en casa de forma limpia, segura y sin cinta suelta.

---

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Conectores:** Explicar **Jumper/Dupont** (para Arduino/protoboard), **Borneras/Clemas** (tornillo seguro) y **Capuchones/Caimanes** (pruebas).
* **Aislantes:** Explicar **Cinta PVC**, **Tubo Termocontraíble** (se encoge con calor) y **Silicona/Cerámica** (alta temperatura).

### Práctica / Reto
* **Instrucción :** *"Abran Canva en formato de 1 página. Armen una infografía con 4 conectores (incluyendo Dupont y Bornera) y 4 aislantes (incluyendo PVC y Termocontraíble), con imagen y 1 línea explicando para qué sirve cada uno."*

---

---

# CAPÍTULO #2
**Tema:** Primer Programa en Arduino (*Blink*) en Tinkercad *(Individual 2)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un LED que parpadea solo con código Arduino (`Blink`) para dar vida a un circuito.
* **¿Para qué me sirve en la vida?** Es el primer paso para automatizar cualquier cosa: desde luces intermitentes de bicicleta hasta semáforos y alarmas.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **2 bloques obligatorios de Arduino:**
  * `void setup()` -> Corre **una sola vez** al prender (`pinMode(13, OUTPUT);`).
  * `void loop()` -> Se **repite por siempre** (`digitalWrite(13, HIGH);`, `delay(1000);`, `LOW`).
* **Modelación en Tinkercad:** Arrastrar Arduino UNO + LED + Resistencia 220 Ω en Pin 13 y GND, cambiar código a **Texto**, simular y ver parpadear.

### Práctica / Reto
* **15 – 25 min (Guiada):** Todos arman el circuito del LED en Pin 13 y prueban el código *Blink* básico.
* **25 – 40 min (Reto Solos):** *"Agrega un segundo LED en el Pin 12 (con su resistencia) y haz que parpadeen alternados: cuando uno prende, el otro se apaga cada 500 ms. Pon tu nombre en un comentario `// Nombre`."*

---

# CAPÍTULO #3
**Tema:** Múltiples Salidas Digitales: Semáforo en Tinkercad  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.
* **¿Para qué me sirve en la vida?** Para organizar cualquier programa grande usando nombres claros (`ledRojo`, `ledVerde`) en lugar de memorizar números de pines.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Variables `int`:** `int rojo = 13;`, `int amarillo = 12;`, `int verde = 11;`. Si mañana cambias un cable de pin, solo cambias el número arriba una vez.
* **Modelación en Tinkercad:** Conectar 3 LEDs (Rojo, Amarillo, Verde) con resistencias de 220 Ω a GND y cargar el ciclo básico.

### Práctica / Reto
* **15 – 25 min (Guiada):** Todos arman el semáforo de 3 LEDs en protoboard dentro de Tinkercad y prueban el encendido secuencial.
* **25 – 40 min (Reto Solos):** *"Haz que la luz **Verde** parpadee 3 veces antes de pasar a Amarillo (como semáforo real de ciudad), y coloca tiempos reales: Verde 3s, Amarillo 1s, Rojo 3s."*

---

# CAPÍTULO #4
**Tema:** Semáforo Físico en Protoboard con Arduino UNO *(Grupal Físico)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** nuestro semáforo en protoboard real con Arduino UNO para verlo funcionar fuera de la pantalla.
* **¿Para qué me sirve en la vida?** Para aprender a cablear componentes reales sin quemar LEDs y cargar programas desde la computadora a una placa física.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Reglas físicas:** 1) Nunca conectar LEDs sin resistencia de 220 Ω, 2) Verificar pata larga (+ al pin) y pata corta (- a GND), 3) Seleccionar `Arduino UNO` y puerto `COM` correcto en el IDE.

### Práctica / Reto
* **Instrucción:** En parejas/grupos arman el circuito (Pines 13, 12, 11 + bus común GND), copian su código de Tinkercad al Arduino IDE, lo suben por USB y prueban el parpadeo real.

---

# CAPÍTULO #5
**Tema:** Reto de Secuencias e Intro a Bucles `for` *(Refuerzo)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Optimizar** el encendido de 6 LEDs en fila usando un bucle `for` en lugar de repetir tantas líneas.
* **¿Para qué me sirve en la vida?** En programación real nadie escribe 100 veces la misma línea: los bucles `for` automatizan tareas repetitivas en segundos.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* **Estructura del `for`:**
  ```cpp
  for (int pin = 2; pin <= 7; pin++) {
    digitalWrite(pin, HIGH);
    delay(150);
    digitalWrite(pin, LOW);
  }
  ```
* Explicar las 3 partes: inicio (`pin = 2`), límite (`pin <= 7`) y paso (`pin++`).

### Práctica / Reto
* **15 – 25 min (Guiada):** Conectan 4–6 LEDs en pines consecutivos (`2` al `7`) en Tinkercad y prueban el bucle `for` de ida.
* **25 – 40 min (Reto Solos):** *"Agrega un segundo bucle `for` debajo que regrese la luz de derecha a izquierda (`for (int pin = 7; pin >= 2; pin--)`)."*

---

# CAPÍTULO #6
**Tema:** Repaso de Sintaxis C++ y Cierre del Parcial 2 *(Colchón)*  

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Corregir** errores clásicos de código Arduino (`;`, llaves y pines) antes de la evaluación.
* **¿Para qué me sirve en la vida?** Para dominar las reglas básicas del código C++ (llaves `{}`, punto y coma `;`) antes de programar robots que tomen decisiones.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA

### Teoría Puntual
* Proyectas 3 errores clásicos en Tinkercad: 1) falta `;`, 2) falta `pinMode`, 3) LED sin resistencia o al revés. Los alumnos lo corrigen en vivo.

### Práctica / Reto
* Revisión de notas y entrega de prácticas pendientes (*Blink*, Semáforo o `for`).
