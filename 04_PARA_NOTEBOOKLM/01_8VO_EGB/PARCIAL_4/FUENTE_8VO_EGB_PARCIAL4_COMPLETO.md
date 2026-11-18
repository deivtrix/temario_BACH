# 🤖 8VO EGB — PARCIAL 4 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología  
**Unidad:** Mecanismos y Control Inicial

---

# 1. Introducción a LEGO WeDo 2.0: Milo, el Róver Científico (Parte A) (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Identificar** los componentes electrónicos y mecánicos básicos de LEGO WeDo 2.0 (Smart Hub, motor y piezas estructurales) construyendo y programando el modelo oficial Milo (Parte A).
* **¿Para qué me sirve en la vida?** Para entender cómo se conectan las piezas mecánicas con un controlador programable que da vida a robots reales, como los róvers de exploración espacial.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **¿Qué es un robot educativo WeDo 2.0?** Es un sistema que combina **estructura mecánica** (vigas, ejes, ruedas y conectores LEGO) con **electrónica programable** controlada por software mediante Bluetooth.
* **Componentes principales del Kit 45300:**
  * **Smart Hub (Concentrador Inteligente):** El "cerebro" que recibe el programa desde la computadora o tablet y reparte energía/señales a sus 2 puertos.
  * **Motor Mediano:** Actuador rotatorio que convierte energía eléctrica en movimiento mecánico (puede girar en sentido horario o antihorario y variar potencia de 1 a 10).
  * **Bloques de programación básicos:** Bloque de *Inicio (Play)*, *Potencia del motor*, *Dirección de giro*, *Tiempo de encendido* y *Parar motor*.
* **Ejemplos de la vida real:** Los róvers marcianos de la NASA (como Perseverance), brazos robóticos de fábricas y carros automatizados.
* **Práctica guiada oficial (Milo — Parte A):** Abrir en la app WeDo 2.0 el proyecto *Primeros pasos: Milo, el róver científico (Parte A)*, construir el chasis paso a paso siguiendo el manual oficial, conectar el Smart Hub por Bluetooth y programar un desplazamiento de 2 segundos adelante y detención segura.

---

# 2. Poleas, Correas y Velocidad: Auto de Carreras (`👤 ACTIVIDAD INDIVIDUAL 1`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un mecanismo de transmisión por poleas y correas usando el proyecto oficial *Velocidad (Auto de Carreras)* para analizar cómo cambia la rapidez según el tamaño de poleas y ruedas.
* **¿Para qué me sirve en la vida?** Para comprender cómo funcionan las bandas de transmisión en bicicletas, impresoras, lavadoras y motores de autos.

## 🛠️ CONTENIDO, MATERIALES Y ACTIVIDAD
* **Fundamento técnico (Transmisión por Poleas y Correas):** Una **polea** es una rueda acanalada conectada a otra mediante una **correa** elástica.
  * **Polea motriz (pequeña) -> Polea conducida (grande):** Reduce velocidad y aumenta fuerza.
  * **Polea motriz (grande) -> Polea conducida (pequeña):** **Multiplica la velocidad** (el vehículo avanza más rápido, como en el auto de carreras).
  * **Efecto del tamaño de rueda:** Ruedas de mayor diámetro recorren más distancia por cada giro completo.
* **Materiales:** Kit oficial LEGO WeDo 2.0 (45300) con Smart Hub, motor, poleas, correas elásticas, ruedas pequeñas/grandes y guía oficial en la app (*Velocidad / Speed*).
* **`👤 ACTIVIDAD INDIVIDUAL 1` (Parejas / Individual — Taller Práctico):** Construir el modelo oficial *Velocidad (Auto de Carreras)* siguiendo el manual de la app WeDo 2.0, probar el tiempo que tarda en recorrer una distancia fija con ruedas pequeñas vs. ruedas grandes (o cambiando la relación de poleas) y registrar qué configuración logra mayor velocidad.

---

# 3. Fuerza, Fricción y Engranajes: Robot de Arrastre (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Experimentar** la relación entre fuerza, fricción y trenes de engranajes usando el proyecto oficial *Tirando (Robot de Arrastre)* para mover cargas pesadas sin que el motor se detenga.
* **¿Para qué me sirve en la vida?** Para entender por qué un camión o bicicleta usa marchas bajas (mucha fuerza, poca velocidad) al subir una cuesta empinada.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **Fuerza y Fricción:** Para mover un objeto pesado se necesita superar la **fricción** (rozamiento entre las superficies). Las llantas de goma aumentan la tracción/agarre al suelo; las piezas lisas reducen fricción al deslizar.
* **Tren de Engranajes (Velocidad vs. Torque/Fuerza):**
  * Los **engranajes** son ruedas dentadas que engranan entre sí sin resbalar. Cada par invertirá el sentido de giro.
  * **Engranaje pequeño (conductor) -> Engranaje grande (conducido):** Reduce la velocidad, pero **multiplica el torque (fuerza)** para arrastrar carga pesada.
  * **Tornillo sin fin:** Bloquea el retroceso y entrega altísima fuerza en poco espacio.
* **Ejemplos de la vida real:** Caja de cambios de un vehículo, grúas de construcción, portones eléctricos y taladros.
* **Práctica guiada oficial (*Tirando / Pulling*):** Armar el robot oficial de arrastre siguiendo el manual de la app WeDo 2.0 y probar cuánta carga logra arrastrar con tracción directa vs. reducción por engranajes.

---

# 4. Sensores de Movimiento e Inclinación: Milo Partes B y C (`👤 ACTIVIDAD INDIVIDUAL 2`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Programar** un sistema robótico bajo el modelo **Entrada -> Proceso -> Salida (IPO)** integrando el Sensor de Movimiento y el Sensor de Inclinación en las Partes B y C de Milo.
* **¿Para qué me sirve en la vida?** Para comprender cómo los carros modernos frenan solos ante un obstáculo o cómo un celular gira la pantalla automáticamente al inclinarlo.

## 📚 CONTENIDO Y ACTIVIDAD
* **Modelo de Sistemas IPO (Entrada -> Proceso -> Salida):** Todo sistema robótico funciona en tres etapas:
  * **Entrada (Input / Sensores):** Captan datos del entorno. En WeDo 2.0: **Sensor de Movimiento** (detecta distancia/objetos enfrente) y **Sensor de Inclinación** (detecta arriba, abajo, izquierda, derecha o sacudida).
  * **Proceso (Process / Programa):** El bloque condicional (*Esperar hasta que...* / bucle) toma una decisión según la lectura del sensor.
  * **Salida (Output / Actuadores):** La acción física que ejecuta el robot (detener el motor, cambiar dirección, encender luz del Hub o emitir sonido).
* **`👤 ACTIVIDAD INDIVIDUAL 2` (Parejas / Individual — Taller Práctico):** Armar y programar los módulos oficiales **Milo Parte B (Sensor de Movimiento)** y **Milo Parte C (Sensor de Inclinación)** en la app WeDo 2.0, logrando que el róver se detenga frente a un objeto y reaccione con movimiento o señal al inclinarse, identificando claramente cuál es la **Entrada**, el **Proceso** y la **Salida**.

---

# 5. Proyecto Integrador WeDo — Parte 1: Construcción (`📘 PRÁCTICA EN EQUIPOS`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** en equipos la estructura mecánica y los acoplamientos electrónicos de un prototipo oficial WeDo 2.0 (*Rescate / Helicóptero* o *Prevención de Inundaciones / Compuerta*) para resolver un problema real.
* **¿Para qué me sirve en la vida?** Para trabajar en equipo planificando el ensamblaje mecánico firme antes de pasar a la etapa de programación.

## 🛠️ CONTENIDO Y AVANCE EN EQUIPOS
* **Modelos oficiales a elegir (app LEGO WeDo 2.0):**
  * **Opción A — Soltar y Rescatar (*Helicóptero de Rescate*):** Mecanismo con poleas y cuerda para bajar y subir carga o rescatar elementos tras un desastre.
  * **Opción B — Prevención de Inundaciones (*Compuerta Automática*):** Mecanismo con engranajes que abre y cierra una compuerta según el nivel de riesgo.
* **Criterios de construcción firme (Parte 1):**
  1. Revisar que vigas y conectores queden bien ajustados para que no vibren ni se suelten al activar el motor.
  2. Dejar accesible el botón de encendido del Smart Hub y el espacio libre para conectar el motor y el sensor elegido.
  3. Verificar manualmente que poleas o engranajes giren suaves sin atascarse antes de encender el motor.

---

# 6. Proyecto Integrador WeDo — Parte 2: Programación y Demo (`👥 ACTIVIDAD GRUPAL`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Programar**, calibrar y demostrar en vivo el prototipo oficial WeDo 2.0 funcionando con lógica **Entrada -> Proceso -> Salida** para validar si resuelve el problema planteado.
* **¿Para qué me sirve en la vida?** Para comprobar que en ingeniería un proyecto no termina al armarlo: hay que probarlo, calibrar tiempos/potencias y evaluar su desempeño real.

## 📚 CONTENIDO Y ACTIVIDAD GRUPAL
* **Calibración y Pruebas (*Troubleshooting*):** Ajustar potencia (no siempre 10 es mejor; para precisión conviene potencia media 4–6), verificar tiempos exactos de giro y comprobar que el sensor dispare la acción correcta sin falsas lecturas.
* **Evaluación del prototipo:** Todo equipo debe responder dos criterios clave tras su prueba: ¿Cumple la función para la que fue diseñado? ¿Qué mejora mecánica o de programación le harían?
* **`👥 ACTIVIDAD GRUPAL` (Demostración en Vivo):** En equipos, completar la programación IPO del prototipo elegido (*Helicóptero de Rescate* o *Compuerta de Inundaciones*), calibrar su funcionamiento y realizar la **demostración en vivo** explicando su mecánica, sensores y una mejora detectada durante las pruebas.

---

# 7. Refuerzo, Inventario y Autoevaluación del Parcial 4 (`🛠️ REFUERZO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Consolidar** los conceptos mecánicos, de sensores y de programación IPO mediante repaso final, inventario ordenado del kit WeDo 2.0 y autoevaluación de cierre de año.
* **¿Para qué me sirve en la vida?** Para cuidar el equipo tecnológico compartido y reflexionar con honestidad sobre los logros y áreas por mejorar en robótica.

## 📚 CONTENIDO, INVENTARIO Y AUTOEVALUACIÓN LIKERT (1 AL 5)
* **Repaso integrador en vivo (sin respuestas visibles):**
  * ¿Qué diferencia mecánica hay entre usar poleas para velocidad (*Auto*) y engranajes para fuerza (*Robot de Arrastre*)?
  * En tu prototipo WeDo, ¿cuál es la **Entrada**, el **Proceso** y la **Salida**?
  * ¿Qué parte fue clave calibrar para que el motor y los sensores no fallaran?
* **Protocolo obligatorio de Inventario y Desmontaje (Kit 45300):**
  1. Apagar el Smart Hub y desconectar cables suavemente sin halar del cable.
  2. Desarmar los modelos por completo sin forzar ejes ni doblar conectores.
  3. Clasificar y guardar cada pieza en su compartimento de la bandeja según la plantilla de inventario del kit.
* **Autoevaluación Escala de Likert (1 = Todavía me cuesta | 3 = Lo entiendo con ayuda | 5 = Lo domino y lo puedo explicar):**
  1. Identificar las funciones del Smart Hub, motor, poleas y engranajes en LEGO WeDo 2.0.
  2. Aplicar el modelo Entrada -> Proceso -> Salida (IPO) programando sensores de movimiento e inclinación.
  3. Construir, calibrar y mejorar un prototipo robótico trabajando de forma colaborativa en equipo.
  4. Cuidar, desmontar e inventariar con orden y responsabilidad los kits de robótica.
