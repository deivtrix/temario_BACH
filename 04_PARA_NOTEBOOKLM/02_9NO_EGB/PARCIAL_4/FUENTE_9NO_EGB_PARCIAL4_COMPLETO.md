# 📗 9NO EGB — PARCIAL 4 (FUENTE ÚNICA PARA NOTEBOOKLM: CAPÍTULOS 1 A 8)
**Materia:** Robótica y Tecnología
**Unidad:** Electrónica Básica y Protoboard en Tinkercad Circuits


---

# 📗 9NO EGB — PARCIAL 4 / CLASE 1
**Tema:** Herramientas, Electricidad y Magnitudes ($V, I, R$) (`👤 ACTIVIDAD INDIVIDUAL 1`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Diferenciar** voltaje, corriente y resistencia eléctrica para entender qué mide cada magnitud antes de armar circuitos en protoboard.
* **¿Para qué me sirve en la vida?** Para leer etiquetas de cargadores, pilas y aparatos sin dañar componentes electrónicos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Antes de armar circuitos en protoboard (que será su base para Arduino en 10mo), hoy aclaramos qué son Voltios, Amperios y Ohmios."*
* **Propósito en pantalla:** *"Diferenciar voltaje, corriente y resistencia eléctrica para entender qué mide cada magnitud antes de armar circuitos en protoboard."*

### 2. Teoría Corta (05 – 15 min)
* **Voltaje ($V$ - Voltios):** Fuerza que empuja los electrones.
* **Corriente ($I$ - Amperios):** Cantidad de electrones que pasan por segundo.
* **Resistencia ($R$ - Ohmios $\Omega$):** Oposición que frena el paso de corriente.

### 3. Actividad Individual (15 – 40 min)
* Elaboran una ficha visual comparando $V, I, R$ (unidad, símbolo y analogía) y leyendo 3 cargadores/pilas reales o proyectados.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿En qué unidad se mide la resistencia eléctrica?"*
2. *"¿Qué magnitud eléctrica es la 'fuerza' que empuja a los electrones?"*


---

# 📗 9NO EGB — PARCIAL 4 / CLASE 2
**Tema:** Ley de Ohm y Componentes Básicos (LED, Resistencia y Pulsador) (`📘 TEMA NUEVO`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Identificar** la polaridad del diodo LED, el código de colores de resistencias y la función de un pulsador para conectarlos sin quemarlos.
* **¿Para qué me sirve en la vida?** Para saber conectar cualquier foco LED o botón en electrónica sin equivocarse de pata.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"¿Por qué un LED tiene una pata más larga que la otra? Si lo conectas al revés no enciende, y si no le pones resistencia se quema."*
* **Propósito en pantalla:** *"Identificar la polaridad del diodo LED, el código de colores de resistencias y la función de un pulsador para conectarlos sin quemarlos."*

### 2. Teoría Corta (05 – 15 min)
* **Diodo LED:** Pata larga = Ánodo ($+$); pata corta / lado plano = Cátodo ($-$).
* **Resistencia ($220\,\Omega$ = Rojo-Rojo-Marrón):** Protege el LED limitando la corriente.
* **Pulsador (4 patas):** Deja pasar corriente solo mientras lo mantienes presionado.

### 3. Práctica en Tinkercad Circuits (15 – 40 min)
* Prueban identificar en Tinkercad los valores de resistencias ($220\,\Omega$, $1\text{k}\Omega$, $10\text{k}\Omega$) viendo cómo cambian sus bandas de color, y prueban encender 1 LED con pulsador y pila 9V.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Cuál es la pata positiva (Ánodo) de un LED?"*
2. *"¿Para qué sirve la resistencia de $220\,\Omega$ junto al LED?"*


---

# 📗 9NO EGB — PARCIAL 4 / CLASE 3
**Tema:** Uso del Protoboard en Tinkercad Circuits (`👤 ACTIVIDAD INDIVIDUAL 1`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo + Individual (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** nuestro primer circuito LED en protoboard virtual de Tinkercad entendiendo sus filas y columnas internas.
* **¿Para qué me sirve en la vida?** El protoboard es la placa universal para probar circuitos sin soldar; dominarlo ahora te deja listo para Arduino en 10mo.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy conocemos la placa de pruebas o protoboard. Por debajo tiene láminas metálicas escondidas que conectan los agujeros."*
* **Propósito en pantalla:** *"Construir nuestro primer circuito LED en protoboard virtual de Tinkercad entendiendo sus filas y columnas internas."*

### 2. Modelación en Tinkercad Circuits (05 – 15 min)
* **Buses horizontales ($+$ rojo / $-$ azul):** Conectan toda la fila a lo largo para alimentar energía.
* **Columnas centrales (`a–e` y `f–j`):** Conectan de 5 en 5 en vertical, **divididas por el canal central** (donde nunca se debe puentear en corto un componente).

### 3. Actividad Individual (15 – 40 min)
* Cada estudiante arma en protoboard virtual de Tinkercad: pila 9V energizando los buses $+$ y $-$ $\rightarrow$ pulsador cruzando el canal central $\rightarrow$ resistencia $330\,\Omega$ $\rightarrow$ LED funcionando al presionar.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿En qué dirección están conectados los agujeros del bus rojo (+) vs. los agujeros del centro?"*
2. *"¿Por qué el protoboard tiene una zanja o división en la mitad?"*


---

# 📗 9NO EGB — PARCIAL 4 / CLASE 4
**Tema:** Circuitos Serie y Paralelo en Protoboard (Tinkercad) (`👤 ACTIVIDAD INDIVIDUAL 2`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo + Individual (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** circuitos en serie y en paralelo dentro de un protoboard en Tinkercad para comparar su brillo y conexiones.
* **¿Para qué me sirve en la vida?** Para saber cablear varios LEDs o sensores ordenadamente en una sola placa sin enredar cables.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Ya saben prender 1 LED en protoboard. Hoy conectamos 3 LEDs en Serie y 3 LEDs en Paralelo dentro del mismo protoboard."*
* **Propósito en pantalla:** *"Simular circuitos en serie y en paralelo dentro de un protoboard en Tinkercad para comparar su brillo y conexiones."*

### 2. Modelación (05 – 15 min)
* Mostrar cómo en **Serie** la salida de un LED va a la columna de entrada del siguiente; en **Paralelo**, todos los cátodos van al bus $-$ y todos los ánodos (con su resistencia) al bus $+$.

### 3. Actividad Individual (15 – 40 min)
* Arman en un mismo protoboard de Tinkercad un bloque de **3 LEDs en Serie** y un bloque de **3 LEDs en Paralelo**, cada uno con su interruptor/pulsador.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Qué pasa en el protoboard si pones las dos patas de un LED en la misma columna de 5 agujeros?"*
2. *"¿En qué conexión brillaron más los 3 LEDs?"*


---

# 📗 9NO EGB — PARCIAL 4 / CLASE 5
**Tema:** Taller Físico en Protoboard — Parte 1 (`👥 ACTIVIDAD GRUPAL`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Armado Grupal Físico (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** en equipo un circuito real en protoboard física con LEDs, resistencias y pila para comprobar lo simulado.
* **¿Para qué me sirve en la vida?** Para desarrollar destreza real al insertar componentes y cables jumper sin doblar pines ni hacer cortos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Dejamos el simulador y pasamos a protoboard física real. En grupos arman su circuito en paralelo con LEDs reales y pila."*
* **Propósito en pantalla:** *"Construir en equipo un circuito real en protoboard física con LEDs, resistencias y pila para comprobar lo simulado."*

### 2. Trabajo Grupal Físico (05 – 40 min)
* **Materiales:** Protoboard real, pila 9V con broche, 3 LEDs, resistencias $330\,\Omega$, pulsador, cables jumper.
* Arman el circuito paralelo en protoboard física y verifican que encienda al presionar el pulsador.

### 3. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Qué fue lo más difícil de pasar de Tinkercad a la protoboard física?"*
2. *"¿Cómo comprobaron que la pata del LED y la resistencia estaban en la misma columna?"*


---

# 📗 9NO EGB — PARCIAL 4 / CLASE 6
**Tema:** Taller Físico en Protoboard — Parte 2 (`👥 ACTIVIDAD GRUPAL`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Pruebas, Serie/Paralelo y Entrega Grupal (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Comprobar** y **corregir** conexiones físicas en protoboard comparando circuitos en serie y paralelo reales en equipo.
* **¿Para qué me sirve en la vida?** Para diagnosticar por qué un circuito real no enciende (LED invertido, cable suelto o fila equivocada).

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Propósito en pantalla:** *"Comprobar y corregir conexiones físicas en protoboard comparando circuitos en serie y paralelo reales en equipo."*

### 2. Trabajo Grupal y Pruebas (05 – 40 min)
* Completan el armado comparativo (serie + paralelo) en protoboard física, miden/observan el brillo real y presentan el funcionamiento al mediador.

### 3. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Qué revisan primero si un LED real no prende en el protoboard?"*
2. *"¿Por qué nunca debemos conectar el cable rojo y negro directo al mismo bus?"*


---

# 📗 9NO EGB — PARCIAL 4 / CLASE 7
**Tema:** Challenge Tinkercad Circuits: Errores en Protoboard (`🛠️ REFUERZO`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Refuerzo Práctico (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Corregir** errores clásicos de conexión en protoboard dentro de Tinkercad Circuits para afianzar todo antes de 10mo EGB.
* **¿Para qué me sirve en la vida?** Para detectar fallas de protoboard en segundos cuando empecemos a conectar Arduino el próximo año.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Propósito en pantalla:** *"Corregir errores clásicos de conexión en protoboard dentro de Tinkercad Circuits para afianzar todo antes de 10mo EGB."*

### 2. Refuerzo en Tinkercad (05 – 40 min)
* Abren el enlace del circuito compartido en Tinkercad con errores típicos (LED invertido, resistencia faltante, componente mal ubicado en la columna) y lo reparan hasta que funcione.

### 3. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Cuál fue el error más escondido que encontraron en el protoboard?"*
2. *"¿Qué pasa si un LED queda conectado sin resistencia a 9V?"*


---

# 📗 9NO EGB — PARCIAL 4 / CLASE 8
**Tema:** Cierre del Año Lectivo, Repaso Protoboard y Autoevaluación (`🛠️ REFUERZO`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Cierre y Autoevaluación (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Evaluar** lo aprendido sobre electrónica básica y protoboard para cerrar el año listos para programar Arduino en 10mo EGB.
* **¿Para qué me sirve en la vida?** Para llevar una base sólida de electrónica y diseño 3D hacia el siguiente nivel.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Propósito en pantalla:** *"Evaluar lo aprendido sobre electrónica básica y protoboard para cerrar el año listos para programar Arduino en 10mo EGB."*

### 2. Repaso General (`🛠️ REFUERZO`, 05 – 35 min)
* Cuestionario/trivia de repaso sobre $V, I, R$, polaridad del LED, código de colores y conexiones del protoboard + nivelación final.

### 3. Autoevaluación Final del Parcial 4 (Escala de Likert 1 al 5) (35 – 45 min)
Cada estudiante valora del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino y lo puedo explicar*):
1. Diferenciar Voltaje ($V$), Corriente ($I$) y Resistencia ($R$).
2. Identificar el Ánodo ($+$) y Cátodo ($-$) de un LED y su resistencia de protección.
3. Conectar circuitos ordenados usando las filas y columnas del protoboard.
4. Armar y probar circuitos en Serie y Paralelo en Tinkercad y en protoboard física.
