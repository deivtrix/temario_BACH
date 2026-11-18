# 📘 10MO EGB — PARCIAL 2 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología
**Unidad:** Conexiones Seguras y Primer Código
**Ya ejecutado al inicio del Parcial 2:** S1: ¿Qué es Arduino? (concepto). S2: Práctica de Empalmes (Taller Calificado Grupal).


---

# CAPÍTULO #1
**Tema:** Conectores y Aislantes Eléctricos *(Individual 1 — Infografía / Consulta)*  
**Modo de Clase:** Modo A/B — Mini-teoría (10 min) + Consulta e Infografía Autónoma (30 min) + Cierre (5 min)  
**Entregable:** Infografía en Canva / Documento de consulta en Classroom.

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Clasificar** qué conectores y aislantes usar para unir cables sin que se suelten ni hagan corto.
* **¿Para qué me sirve en la vida?** Para conectar cables en Arduino o en casa de forma limpia, segura y sin cinta suelta.

---

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)

### 1. Inicio, Motivación y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada hicimos empalmes torciendo cables y poniendo cinta. Pero cuando un robot vibra o quieres desconectar rápido un Arduino, ¿cómo lo hacen los ingenieros sin usar cinta?"*
* **Presentar el Propósito (Página 2):** *"Clasificar qué conectores y aislantes usar para unir cables sin que se suelten ni hagan corto."**clasificar** conectores y aislantes modernos para realizar uniones seguras y ordenadas en electrónica y robótica."*

### 2. Teoría Relámpago (05 – 15 min | máx. 10 min)
* **Proyectar Página 3 (Conectores):** Explicar **Jumper/Dupont** (para Arduino/protoboard), **Borneras/Clemas** (tornillo seguro) y **Capuchones/Caimanes** (pruebas).
* **Proyectar Página 4 (Aislantes):** Explicar **Cinta PVC**, **Tubo Termocontraíble** (se encoge con calor) y **Silicona/Cerámica** (alta temperatura).

### 3. Trabajo Individual en Canva (15 – 40 min)
* **Instrucción (Página 5 y 6):** *"Abran Canva en formato de 1 página. Armen una infografía con 4 conectores (incluyendo Dupont y Bornera) y 4 aislantes (incluyendo PVC y Termocontraíble), con imagen y 1 línea explicando para qué sirve cada uno."*
* **Tu rol:** Revisas que no copien párrafos largos de internet, sino 1 línea clara con sus palabras.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Preguntas orales antes de salir:**
  1. *"¿Qué conector usarías en un protoboard con Arduino y cuál en una lámpara de 110V?"*
  2. *"¿Qué ventaja tiene el tubo termocontraíble frente a la cinta aislante común?"*
* **Entrega:** Subir la infografía en PDF/PNG a Google Classroom.

---

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Individual 1: Infografía de Conectores y Aislantes

PROPÓSITO: Clasificar qué conectores y aislantes usar para unir cables sin que se suelten ni hagan corto.

INSTRUCCIONES:
1. En Canva (1 sola página), diseña una infografía clara con:
   - 4 tipos de Conectores Eléctricos/Electrónicos (debe incluir Jumper Dupont y Regleta/Bornera).
   - 4 tipos de Aislantes Eléctricos (debe incluir Cinta PVC y Tubo Termocontraíble).
2. Cada ítem debe tener: Nombre, imagen y 1 línea explicando para qué sirve.
3. Incluye tu nombre y curso en el pie de la infografía y súbela en PDF o PNG.

Calificación: 10 puntos (Trabajo individual de clase).
```


---

# CAPÍTULO #2
**Tema:** Primer Programa en Arduino (*Blink*) en Tinkercad *(Individual 2)*  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura exprés en Classroom del circuito Blink funcionando con código propio.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un LED que parpadea solo con código Arduino (`Blink`) para dar vida a un circuito.
* **¿Para qué me sirve en la vida?** Es el primer paso para automatizar cualquier cosa: desde luces intermitentes de bicicleta hasta semáforos y alarmas.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hasta el parcial pasado, un foco solo prendía si tú aplastabas el interruptor con el dedo. Hoy jubilamos al dedo: vamos a darle cerebro con código C++ para que prenda y apague solo."*
* **Propósito en pantalla:** *"Simular un LED que parpadea solo con código Arduino (`Blink`) para dar vida a un circuito."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **2 bloques obligatorios de Arduino:**
  * `void setup()` -> Corre **una sola vez** al prender (`pinMode(13, OUTPUT);`).
  * `void loop()` -> Se **repite por siempre** (`digitalWrite(13, HIGH);`, `delay(1000);`, `LOW`).
* **Modelación en Tinkercad:** Arrastrar Arduino UNO + LED + Resistencia 220 Ω en Pin 13 y GND, cambiar código a **Texto**, simular y ver parpadear.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Todos arman el circuito del LED en Pin 13 y prueban el código *Blink* básico contigo.
* **25 – 40 min (Reto Solos):** *"Agrega un segundo LED en el Pin 12 (con su resistencia) y haz que parpadeen alternados: cuando uno prende, el otro se apaga cada 500 ms. Pon tu nombre en un comentario `// Nombre`."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué diferencia hay entre `void setup()` y `void loop()`?"*
  2. *"Si pongo `delay(500);`, ¿cuántos segundos espera el Arduino?"*
* **Cierre:** Subir captura en Tinkercad con el LED encendido y el código visible a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Individual 2: Mi Primer Programa en Arduino (Blink Alternado)

PROPÓSITO: Simular un LED que parpadea solo con código Arduino (`Blink`) para dar vida a un circuito.

CÓDIGO BASE DE REFERENCIA:
void setup() {
  pinMode(13, OUTPUT);
}
void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}

RETO INDIVIDUAL:
1. Agrega un segundo LED en el Pin 12 (con resistencia de 220 ohmios a GND).
2. Haz que ambos LEDs parpadeen alternados cada 500 ms.
3. Escribe // Tu Nombre Apellido en la línea 1 del código y sube 1 captura de la simulación corriendo.

Calificación: 10 puntos (Actividad Individual 2).
```


---

# CAPÍTULO #3
**Tema:** Múltiples Salidas Digitales: Semáforo en Tinkercad  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura exprés en Classroom del semáforo funcionando con variables `int`.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.
* **¿Para qué me sirve en la vida?** Para organizar cualquier programa grande usando nombres claros (`ledRojo`, `ledVerde`) en lugar de memorizar números de pines.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada controlamos 1 o 2 LEDs usando `13` y `12`. Pero si tuviéramos 20 luces, ¿se acordarían qué hace cada número? Hoy vamos a ponerles nombre con variables."*
* **Propósito en pantalla:** *"Simular un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Variables `int`:** `int rojo = 13;`, `int amarillo = 12;`, `int verde = 11;`. Si mañana cambias un cable de pin, solo cambias el número arriba una vez.
* **Modelación en Tinkercad:** Conectar 3 LEDs (Rojo, Amarillo, Verde) con resistencias de 220 Ω a GND y cargar el ciclo básico.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Todos arman el semáforo de 3 LEDs en protoboard dentro de Tinkercad y prueban el encendido secuencial.
* **25 – 40 min (Reto Solos):** *"Haz que la luz **Verde** parpadee 3 veces antes de pasar a Amarillo (como semáforo real de ciudad), y coloca tiempos reales: Verde 3s, Amarillo 1s, Rojo 3s."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Para qué sirve declarar `int rojo = 13;` al inicio del código?"*
  2. *"¿Qué pasa si olvidas apagar el LED anterior con `LOW` antes de encender el siguiente?"*
* **Cierre:** Subir captura de Tinkercad con el código y el semáforo encendido a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Práctica Arduino: Semáforo Inteligente en Tinkercad

PROPÓSITO: Simular un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.

INSTRUCCIONES:
1. Conecta 3 LEDs (Rojo en Pin 13, Amarillo en Pin 12, Verde en Pin 11) con sus resistencias de 220 ohmios a GND.
2. Declara variables int para cada color al inicio del código.
3. Programa el ciclo completo haciendo que el Verde parpadee 3 veces antes de cambiar a Amarillo.
4. Escribe // Tu Nombre Apellido en la línea 1 y sube 1 captura de la simulación corriendo.

Calificación: 10 puntos (Práctica de clase).
```


---

# CAPÍTULO #4
**Tema:** Semáforo Físico en Protoboard con Arduino UNO *(Grupal Físico)*  
**Modo de Clase:** Modo B — Trabajo Grupal Físico (45 min)  
**Entregable:** Visto bueno en vivo + foto grupal del semáforo físico encendido en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** nuestro semáforo en protoboard real con Arduino UNO para verlo funcionar fuera de la pantalla.
* **¿Para qué me sirve en la vida?** Para aprender a cablear componentes reales sin quemar LEDs y cargar programas desde la computadora a una placa física.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada su semáforo funcionó en la pantalla de Tinkercad. Hoy lo traemos al mundo real: van a armarlo en protoboard física y cargarle el código al Arduino UNO."*
* **Propósito en pantalla:** *"Construir nuestro semáforo en protoboard real con Arduino UNO para verlo funcionar fuera de la pantalla."*

### 2. Encuadre de Seguridad y Pines (05 – 10 min)
* **Reglas físicas:** 1) Nunca conectar LEDs sin resistencia de 220 Ω, 2) Verificar pata larga (+ al pin) y pata corta (- a GND), 3) Seleccionar `Arduino UNO` y puerto `COM` correcto en el IDE.

### 3. Trabajo Grupal Físico con Intervención del Mediador (10 – 40 min)
* **Instrucción:** En parejas/grupos arman el circuito (Pines 13, 12, 11 + bus común GND), copian su código de Tinkercad al Arduino IDE, lo suben por USB y prueban el parpadeo real.
* **Tu rol:** Ayudas a destrabar errores de puerto COM o LEDs puestos al revés en la protoboard.

### 4. Cierre, Preguntas y Entrega (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Cómo identificas físicamente cuál es el ánodo (+) y el cátodo (-) de un LED real?"*
  2. *"¿Qué pasó al subir el código si el cable USB o el puerto COM no estaban seleccionados?"*
* **Cierre:** Visto bueno en mesa + subir foto con papelito de nombres en Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Grupal Física: Semáforo Real con Arduino UNO

PROPÓSITO: Construir nuestro semáforo en protoboard real con Arduino UNO para verlo funcionar fuera de la pantalla.

INSTRUCCIONES (En grupos):
1. Armen en protoboard física los 3 LEDs (Rojo, Amarillo, Verde) con resistencias de 220 ohmios hacia GND y conectados a los pines 13, 12 y 11.
2. Carguen su código al Arduino UNO desde el IDE.
3. Coloquen un papelito con los nombres del grupo al lado del circuito encendido, tomen 1 foto y súbanla aquí.

Calificación: 10 puntos (Actividad Grupal Física).
```


---

# CAPÍTULO #5
**Tema:** Reto de Secuencias e Intro a Bucles `for` *(Refuerzo)*  
**Modo de Clase:** Modo A — Tema Nuevo / Refuerzo (45 min)  
**Entregable:** Captura en Tinkercad del barrido de LEDs usando `for` en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Optimizar** el encendido de 6 LEDs en fila usando un bucle `for` en lugar de repetir tantas líneas.
* **¿Para qué me sirve en la vida?** En programación real nadie escribe 100 veces la misma línea: los bucles `for` automatizan tareas repetitivas en segundos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Si les pido encender 6 LEDs en fila uno por uno, tendrían que escribir 24 líneas de `digitalWrite`. Hoy les enseño el truco para hacerlo en solo 4 líneas."*
* **Propósito en pantalla:** *"Optimizar el encendido de 6 LEDs en fila usando un bucle `for` en lugar de repetir tantas líneas."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Estructura del `for`:**
  ```cpp
  for (int pin = 2; pin <= 7; pin++) {
    digitalWrite(pin, HIGH);
    delay(150);
    digitalWrite(pin, LOW);
  }
  ```
* Explicar las 3 partes: inicio (`pin = 2`), límite (`pin <= 7`) y paso (`pin++`).

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Conectan 4–6 LEDs en pines consecutivos (`2` al `7`) en Tinkercad y prueban el bucle `for` de ida.
* **25 – 40 min (Reto Solos):** *"Agrega un segundo bucle `for` debajo que regrese la luz de derecha a izquierda (`for (int pin = 7; pin >= 2; pin--)`)."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué significa `pin++` y qué significa `pin--`?"*
  2. *"¿Qué pasa si conectas los LEDs en pines saltados (ej. 2, 5, 9) cuando usas un `for` consecutivo?"*
* **Cierre:** Subir captura de Tinkercad corriendo a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Refuerzo Arduino: Secuencia de Luces con Bucle for

PROPÓSITO: Optimizar el encendido de 6 LEDs en fila usando un bucle `for` en lugar de repetir tantas líneas.

INSTRUCCIONES:
1. En Tinkercad, conecta 6 LEDs desde el Pin 2 hasta el Pin 7 (con resistencias de 220 ohmios a GND).
2. Usa un bucle for para encenderlos en orden de ida (2 -> 7) y otro bucle for para regresarlos (7 -> 2).
3. Pon // Tu Nombre en la línea 1 y sube 1 captura de la simulación corriendo.

Calificación: Refuerzo formativo (10 puntos).
```


---

# CAPÍTULO #6
**Tema:** Repaso de Sintaxis C++ y Cierre del Parcial 2 *(Colchón)*  
**Modo de Clase:** Modo B — Repaso y Nivelación (45 min)  
**Entregable:** Revisión en vivo y nivelación previa a evaluación quimestral.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Corregir** errores clásicos de código Arduino (`;`, llaves y pines) antes de la evaluación.
* **¿Para qué me sirve en la vida?** Para dominar las reglas básicas del código C++ (llaves `{}`, punto y coma `;`) antes de programar robots que tomen decisiones.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"¡Bienvenidos! La próxima semana cerramos Áreas Especiales. Hoy hacemos un reto rápido de 'encuentra el error en el código' y ponemos al día cualquier pendiente."*
* **Propósito en pantalla:** *"Corregir errores clásicos de código Arduino (`;`, llaves y pines) antes de la evaluación."*

### 2. Reto "Encuentra el Error" (05 – 20 min)
* Proyectas 3 errores clásicos en Tinkercad: 1) falta `;`, 2) falta `pinMode`, 3) LED sin resistencia o al revés. Los alumnos lo corrigen en vivo.

### 3. Nivelación Final (20 – 40 min)
* Revisión de notas y entrega de prácticas pendientes (*Blink*, Semáforo o `for`).

### 4. Cierre y Autoevaluación Likert (1 al 5) (40 – 45 min)
* Indicaciones para la evaluación del 11 de enero + autoevaluación del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino*):
  1. Diferenciar conectores (Dupont, borneras) y aislantes (PVC, termocontraíble).
  2. Escribir la estructura base de Arduino (`setup()`, `loop()`, `pinMode()`, `digitalWrite()`).
  3. Usar variables `int` para programar un semáforo en Tinkercad y protoboard real.
  4. Simplificar secuencias de varios LEDs usando bucles `for`.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Cierre del Parcial 2: Depuración de Código Arduino y Repaso

PROPÓSITO: Corregir errores clásicos de código Arduino (`;`, llaves y pines) antes de la evaluación.

ACTIVIDAD:
- Práctica de depuración en Tinkercad (encontrar errores de llaves, punto y coma y pines).
- Cierre y nivelación de entregas previas a Evaluaciones de Áreas Especiales (11 de enero).
```
