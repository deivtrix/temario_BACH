# 📗 9NO EGB — PARCIAL 3 (FUENTE ÚNICA PARA NOTEBOOKLM: CAPÍTULOS 1 A 8)
**Materia:** Robótica y Tecnología
**Unidad:** Robótica Móvil con mBot y mBlock 5


---

# 📗 9NO EGB — PARCIAL 3 / CLASE 1
**Tema:** Kit mBot y Placa mCore (`👤 ACTIVIDAD INDIVIDUAL 1`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Identificar** las partes del robot mBot y los puertos de la placa mCore para conectarlo sin dañar sensores ni motores.
* **¿Para qué me sirve en la vida?** Para reconocer cómo se conectan el "cerebro", los sensores y los motores en cualquier robot móvil real.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Dejamos el diseño 3D en pantalla y pasamos a robots reales que se mueven. Hoy conocemos al mBot y su placa mCore."*
* **Propósito en pantalla:** *"Identificar las partes del robot mBot y los puertos de la placa mCore para conectarlo sin dañar sensores ni motores."*

### 2. Teoría Corta (05 – 15 min)
* **Placa mCore (cerebro):** Puertos `RJ25` numerados `1, 2, 3, 4` (colores indican qué sensor va ahí), 2 LEDs RGB integrados, Buzzer, botón integrado, salidas `M1` y `M2` para motores.

### 3. Actividad Individual (15 – 40 min)
* Cada estudiante completa el mapa/ficha de identificación de partes del kit mBot y puertos de la placa mCore (qué conecta en `M1/M2` y qué en los puertos `1–4`).

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Para qué sirven los puertos `M1` y `M2` de la placa mCore?"*
2. *"¿Qué componentes ya vienen soldados dentro de la placa sin necesidad de cables?"*


---

# 📗 9NO EGB — PARCIAL 3 / CLASE 2
**Tema:** Montaje Básico del mBot y Entorno mBlock 5 (`👥 ACTIVIDAD GRUPAL`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A/B — Mini-teoría (10 min) + Armado Grupal (30 min) + Cierre (5 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** el chasis básico del mBot y conectarlo a mBlock 5 para probar la comunicación entre la computadora y el robot.
* **¿Para qué me sirve en la vida?** Para aprender cómo se arma un chasis mecánico y se carga un programa desde la PC hacia un robot físico.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy armamos el mBot en equipos y lo conectamos a mBlock 5 por USB/Bluetooth para dejarlo listo para programar."*
* **Propósito en pantalla:** *"Construir el chasis básico del mBot y conectarlo a mBlock 5 para probar la comunicación entre la computadora y el robot."*

### 2. Teoría Corta (05 – 15 min)
* **Modo En Vivo (*Live*):** El robot responde conectado a la PC.
* **Modo Cargar (*Upload*):** El código queda guardado dentro del mBot para que funcione desconectado.

### 3. Armado y Conexión Grupal (15 – 40 min)
* En equipos ensamblan motores, llantas, rueda loca, placa mCore y batería, y verifican conexión con mBlock 5.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Qué diferencia hay entre Modo En Vivo y Modo Cargar en mBlock?"*
2. *"¿Por qué debemos revisar que los cables de motores queden bien puestos en M1 y M2?"*


---

# 📗 9NO EGB — PARCIAL 3 / CLASE 3
**Tema:** Programación Básica: Luces RGB y Sonidos en mBlock 5 (`👤 ACTIVIDAD INDIVIDUAL 1`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo + Individual (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Programar** los LEDs RGB y el buzzer del mBot en mBlock 5 para crear señales luminosas y sonoras.
* **¿Para qué me sirve en la vida?** Así funcionan las alertas visuales y sonoras de robots repartidores, alarmas y juguetes inteligentes.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Antes de hacer correr al mBot por el piso, hoy le damos señales de luz y sonido como un robot real."*
* **Propósito en pantalla:** *"Programar los LEDs RGB y el buzzer del mBot en mBlock 5 para crear señales luminosas y sonoras."*

### 2. Modelación en mBlock 5 (05 – 15 min)
* Bloques de **Iluminación** (`encender LED todos/izquierdo/derecho` con colores RGB) y **Sonido** (`reproducir nota` + `esperar`).

### 3. Práctica Individual (15 – 40 min)
* Cada estudiante programa una secuencia en mBlock 5 combinando **3 colores distintos** en los LEDs del mBot y una **mini melodía de 4 notas** sincronizada.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Qué significan las siglas RGB en los LEDs del mBot?"*
2. *"¿Por qué ponemos un bloque `esperar` entre un color y otro?"*


---

# 📗 9NO EGB — PARCIAL 3 / CLASE 4
**Tema:** Control de Motores DC y Velocidad ($0\text{–}255$) (`👤 ACTIVIDAD INDIVIDUAL 2`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo + Individual (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Controlar** la dirección y velocidad de los motores del mBot en mBlock 5 para que avance, retroceda y gire con precisión.
* **¿Para qué me sirve en la vida?** Es la base de la robótica móvil: controlar tracción diferencial (dos ruedas independientes) como en aspiradoras robot o rovers.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy hacemos que el mBot ruede. Para girar, una rueda avanza y la otra frena o retrocede."*
* **Propósito en pantalla:** *"Controlar la dirección y velocidad de los motores del mBot en mBlock 5 para que avance, retroceda y gire con precisión."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* Bloques de **Acción:** `avanzar a potencia X% durante Y seg`, `girar izquierda/derecha`, `detener movimiento`.
* Explicar rango de potencia/velocidad y cómo el **tiempo** define la distancia recorrida.

### 3. Práctica Individual (15 – 40 min)
* Programan en mBlock 5 una maniobra de **avanzar 2s $\rightarrow$ girar 90° $\rightarrow$ retroceder 1s $\rightarrow$ detenerse** y la prueban en el mBot.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Cómo logra girar un robot de 2 ruedas si no tiene volante como un carro?"*
2. *"¿Qué bloque es obligatorio al final para que el mBot no siga rodando infinito?"*


---

# 📗 9NO EGB — PARCIAL 3 / CLASE 5
**Tema:** Reto de Trayectoria Cuadrada ($50 \times 50\text{ cm}$) (`👥 ACTIVIDAD GRUPAL`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Reto Grupal en Pista (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Calibrar** tiempos de avance y giros de $90^\circ$ en el mBot para recorrer un cuadrado exacto en pista.
* **¿Para qué me sirve en la vida?** Para entender cómo la fricción del piso y la batería afectan a un robot y cómo se calibran trayectorias autónomas.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"El reto de hoy es en pista: su mBot debe dibujar un cuadrado de 50×50 cm usando un bucle `repetir 4 veces` y volver al punto de inicio."*
* **Propósito en pantalla:** *"Calibrar tiempos de avance y giros de $90^\circ$ en el mBot para recorrer un cuadrado exacto en pista."*

### 2. Trabajo Grupal en Pista (05 – 40 min)
* En equipos cargan su programa con bucle `repetir 4`, prueban en el piso del laboratorio y ajustan milisegundos de giro hasta lograr los 4 ángulos rectos.

### 3. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Por qué usamos un bucle `repetir 4` en vez de copiar 4 veces los mismos bloques?"*
2. *"¿Qué ajustaron cuando el robot giraba más o menos de 90°?"*


---

# 📗 9NO EGB — PARCIAL 3 / CLASE 6
**Tema:** Sensor Ultrasonido: Robot Esquiva-Obstáculos (`👥 ACTIVIDAD GRUPAL`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo + Práctica Grupal (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Programar** el sensor ultrasonido del mBot para que detecte obstáculos y gire automáticamente sin chocar.
* **¿Para qué me sirve en la vida?** Es la tecnología que usan las aspiradoras robot y los sistemas anticolisión de vehículos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy su mBot deja de ser ciego: le activamos los 'ojos' de ultrasonido para que esquive cajas y paredes solo."*
* **Propósito en pantalla:** *"Programar el sensor ultrasonido del mBot para que detecte obstáculos y gire automáticamente sin chocar."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* Condicional `si [distancia del sensor ultrasonido < 20 cm] entonces`: retroceder 0.5s y girar a la derecha; `si no`: avanzar recto.

### 3. Práctica Grupal en Pista/Laberinto (15 – 40 min)
* En equipos cargan el algoritmo de evasión y prueban el mBot navegando entre cajas/obstáculos sin chocar.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿A qué distancia en cm configuraron el freno de su robot?"*
2. *"¿Por qué todo el `si / si no` debe ir dentro de un bucle `por siempre`?"*


---

# 📗 9NO EGB — PARCIAL 3 / CLASE 7
**Tema:** Sensor Sigue-Líneas (IR) en Pista Negra (`🛠️ REFUERZO`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A/B — Mini-teoría (10 min) + Práctica en Pista (30 min) + Cierre (5 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Aplicar** el sensor infrarrojo (IR) del mBot para que siga una línea negra sobre fondo blanco automáticamente.
* **¿Para qué me sirve en la vida?** Así se guían los robots transportadores en bodegas y fábricas siguiendo líneas en el suelo.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"En las fábricas, los robots siguen caminos pintados en el piso. Hoy probamos el sensor sigue-líneas de nuestro mBot."*
* **Propósito en pantalla:** *"Aplicar el sensor infrarrojo (IR) del mBot para que siga una línea negra sobre fondo blanco automáticamente."*

### 2. Teoría Corta (05 – 15 min)
* Los 2 ojos infrarrojos detectan blanco (refleja luz = `1`) vs. negro (absorbe luz = `0`).
* Lógica simple: ambos en negro $\rightarrow$ avanzar; se sale a la izquierda $\rightarrow$ corregir a la derecha; se sale a la derecha $\rightarrow$ corregir a la izquierda.

### 3. Práctica en Pista (`🛠️ REFUERZO`, 15 – 40 min)
* Prueban el algoritmo sigue-líneas sobre la pista de cinta negra y ajustan velocidad baja para no salirse en curvas.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Por qué el sensor IR distingue entre blanco y negro?"*
2. *"¿Qué pasa si ponemos la velocidad al 100% en una curva cerrada?"*


---

# 📗 9NO EGB — PARCIAL 3 / CLASE 8
**Tema:** Cierre de Parcial 3, Repaso mBot y Autoevaluación (`🛠️ REFUERZO`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Cierre y Autoevaluación (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Comprobar** el dominio de programación y sensores del mBot antes de pasar a electrónica en protoboard.
* **¿Para qué me sirve en la vida?** Para consolidar nuestra lógica de programación antes de armar circuitos electrónicos en el Parcial 4.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Propósito en pantalla:** *"Comprobar el dominio de programación y sensores del mBot antes de pasar a electrónica en protoboard."*

### 2. Repaso y Demostración Final (`🛠️ REFUERZO`, 05 – 35 min)
* Cuestionario/trivia de repaso sobre placa mCore, motores, ultrasonido e infrarrojo + nivelación de prácticas en pista.

### 3. Autoevaluación Final del Parcial 3 (Escala de Likert 1 al 5) (35 – 45 min)
Cada estudiante valora del **1 al 5** (*1 = Todavía me cuesta | 5 = Lo domino y lo puedo explicar*):
1. Identificar los puertos RJ25, LEDs RGB, buzzer y motores en la placa mCore.
2. Programar luces, sonidos y desplazamientos calibrados (cuadrado) en mBlock 5.
3. Usar el sensor ultrasonido para que el mBot esquive obstáculos solo.
4. Comprender cómo el sensor infrarrojo (IR) sigue una línea negra.
