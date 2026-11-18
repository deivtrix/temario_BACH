# ⛏️ 9NO EGB — PARCIAL 3 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología  
**Unidad:** Navegación y Robótica Móvil

---

# 1. Kit mBot, Placa mCore y Entorno mBlock 5 (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Identificar** la arquitectura del robot mBot (pre-armado), los puertos RJ25 de la placa mCore y la diferencia entre ejecutar código en modo En Vivo y Subir código en mBlock 5.
* **¿Para qué me sirve en la vida?** Para comprender cómo un controlador ordena acciones a motores y sensores y cómo elegir el modo correcto al probar un robot autónomo.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **Arquitectura del mBot (ya armado):**
  * **Placa mCore:** cerebro basado en microcontrolador con LEDs RGB integrados, zumbador (buzzer), botón de prueba, transmisor/receptor IR, puertos de motores (`M1` izquierdo, `M2` derecho) y **4 puertos RJ25 numerados del 1 al 4**.
  * **Regla de puertos RJ25:** Los puertos tienen etiquetas de colores para evitar errores; por defecto en el aula conectamos el **Sensor Sigue-Líneas en el Puerto 2** y el **Sensor Ultrasonido en el Puerto 3**.
  * **Modo En Vivo (Live) vs. Modo Subir (Upload):**
    * **En Vivo:** el código corre desde la computadora por cable USB o dongle inalámbrico; sirve para pruebas rápidas, pero si desconectas el robot se detiene.
    * **Subir (Upload):** graba el programa dentro de la memoria de la placa mCore para que el robot funcione 100% autónomo con sus pilas en el suelo.
* **Práctica guiada:** Conectar el mBot en mBlock 5, verificar firmware/conexión, probar el botón integrado y subir un parpadeo simple en modo Upload.
* **Preguntas de verificación:** ¿Qué diferencia práctica existe entre el modo En Vivo y el modo Subir? ¿En qué puertos conectamos el sigue-líneas y el ultrasonido?

---

# 2. Luces RGB y Buzzer — Salidas Integradas (`👤 ACTIVIDAD INDIVIDUAL 1`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Programar** secuencias visuales (LEDs RGB) y alertas sonoras (buzzer) en la placa mCore mediante bloques de mBlock 5.
* **¿Para qué me sirve en la vida?** Para diseñar indicadores de estado y alertas claras en cualquier dispositivo electrónico o robot móvil.

## 📚 CONTENIDO Y RETO INDIVIDUAL
* **Fundamento técnico (10 min):**
  * La placa mCore integra **2 LEDs RGB** (Rojo, Verde, Azul) que combinan intensidades de `0` a `255` para crear cualquier color, y un **buzzer pasivo** que reproduce notas musicales (frecuencias en Hz) durante tiempos en segundos/tiempos (`beats`).
  * **Importancia de las pausas (`esperar`):** sin un bloque de espera entre cambios de color o nota, el procesador ejecuta todo en milisegundos y el ojo humano no percibe la secuencia.
* **Actividad individual (`👤 ACTIVIDAD INDIVIDUAL` — sin código resuelto):**
  * Crear una secuencia de **alerta de emergencia o semáforo** usando los 2 LEDs RGB integrados (mínimo 3 estados distintos) sincronizada con una melodía corta de **4 notas** en el buzzer al presionar el botón de la placa.
  * **1 Consejo:** Usa bloques `esperar` entre cada cambio de color para que la transición sea visible.
* **Preguntas de verificación:** ¿Por qué necesitamos un bloque de espera después de encender un color RGB? ¿Qué valores mínimos y máximos acepta cada canal R, G y B?

---

# 3. Motores DC, Velocidad (0–255) y Giros (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Controlar** la dirección y velocidad de los motores DC del mBot diseñando un diagrama de flujo previo antes de programar giros y desplazamientos.
* **¿Para qué me sirve en la vida?** Para entender cómo funcionan los vehículos de tracción diferencial (como aspiradoras robot o sillas motorizadas) y planificar movimientos con lógica.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **Tracción diferencial (`M1` y `M2`):**
  * **Avanzar:** ambos motores giran hacia adelante a la misma potencia (o velocidad guardada en una **variable `velocidad`**, rango `0` a `255`, equivalente a porcentaje `0%` a `100%` en mBlock).
  * **Retroceder:** ambos motores giran hacia atrás.
  * **Giro sobre su eje (90 grados):** una rueda avanza y la otra retrocede (o se detiene) durante un tiempo calibrado (aprox. `0.4` a `0.6` segundos según la carga de las pilas).
  * **Diagrama de flujo previo:** Antes de arrastrar bloques, dibujamos Inicio -> Acción -> Tiempo -> Giro -> Fin para no adivinar a ciegas.
* **Práctica guiada:** Crear la variable `velocidad`, diseñar el diagrama de flujo de ida y vuelta en línea recta y subirlo al mBot para probarlo en el suelo.
* **Preguntas de verificación:** ¿Qué ocurre si el motor izquierdo gira más rápido que el derecho al intentar avanzar recto? ¿Para qué sirve guardar la velocidad en una variable?

---

# 4. Reto Pista Cuadrada (50 x 50 cm) (`👥 ACTIVIDAD GRUPAL`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Calibrar** en equipos los tiempos de avance y giro de 90 grados del mBot mediante iteración práctica hasta completar una pista cuadrada real de 50 x 50 cm.
* **¿Para qué me sirve en la vida?** Para aprender que en ingeniería física la teoría debe calibrarse frente a variables reales como fricción del piso y desgaste de batería.

## 📚 CONTENIDO Y RETO GRUPAL
* **Fundamento técnico (5 min):**
  * En simulador un giro de 90 grados siempre es exacto; en el mundo real depende de la **fricción del suelo** y del **voltaje de las pilas**. Si la batería baja, el mismo tiempo gira menos ángulo.
  * Uso de bucles (`repetir 4 veces`) para evitar repetir cuatro veces los mismos bloques de lado + giro.
* **Actividad grupal (`👥 ACTIVIDAD GRUPAL` — sin tiempos/códigos resueltos):**
  * En equipos, programar el mBot en modo **Subir (Upload)** para recorrer el perímetro completo de la **pista cuadrada de 50 x 50 cm** sin salirse de las esquinas y regresar al punto de partida usando un bucle de repetición.
  * **1 Consejo:** Calibren primero 1 solo lado + 1 giro de 90 grados; cuando quede exacto, recién enciérrenlo en el bucle de 4 repeticiones.
* **Preguntas de verificación:** ¿Por qué un código calibrado en una mesa lisa puede desviarse en el piso del patio? ¿Qué ventaja da usar el bloque `repetir 4`?

---

# 5. Sensor Ultrasonido — Esquiva-Obstáculos (`👤 ACTIVIDAD INDIVIDUAL 2`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Implementar** una rutina autónoma de evasión de obstáculos leyendo distancias en centímetros con el sensor ultrasonido y un diagrama de flujo condicional.
* **¿Para qué me sirve en la vida?** Para comprender cómo los sensores de parqueo de los autos y los robots de reparto miden distancia sin tocar los objetos.

## 📚 CONTENIDO Y RETO INDIVIDUAL
* **Fundamento técnico (10 min):**
  * El sensor ultrasonido (Puerto 3) tiene dos "ojos": uno emite una onda sonora inaudible y el otro mide el tiempo que tarda en rebotar (`eco`) para calcular la distancia en **centímetros** (rango útil aprox. `3 cm` a `400 cm`).
  * **Lógica condicional continua:** dentro de un bucle `por siempre`, comparamos `distancia < 20 cm`: si se cumple, el robot frena, retrocede un instante y gira; si no, continúa avanzando.
* **Actividad individual (`👤 ACTIVIDAD INDIVIDUAL` — sin código resuelto):**
  * Dibujar primero el diagrama de flujo de decisión y luego programar el mBot para navegar de forma autónoma evitando cajas u obstáculos puestos en su camino (encendiendo LED rojo al detectar obstáculo y verde al avanzar libre).
  * **1 Consejo:** No uses una distancia límite demasiado corta (como 3 cm), porque por inercia el robot chocará antes de alcanzar a frenar.
* **Preguntas de verificación:** ¿Cómo calcula el sensor la distancia sin tocar el objeto? ¿Qué sucede si olvidamos el bucle `por siempre` alrededor de la condición?

---

# 6. Sensor Sigue-Líneas IR (`📘 PRÁCTICA GUIADA`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Interpretar** las lecturas binarias (`0` y `1`) del sensor infrarrojo doble para guiar al mBot sobre una trayectoria de cinta negra.
* **¿Para qué me sirve en la vida?** Para entender cómo los robots industriales de almacenes (AGV) siguen rutas marcadas en el piso de forma automática.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA GUIADA
* **Fundamento técnico (10 min):**
  * El sensor sigue-líneas (Puerto 2) posee **2 sensores infrarrojos** (izquierdo y derecho).
  * **Superficie blanca:** refleja la luz infrarroja (`1`). **Cinta negra:** absorbe la luz (`0`).
  * **4 estados posibles (Tabla de lectura):**
    * Ambos en negro (`0`): avanzar recto.
    * Izquierdo en negro / derecho en blanco (`1`): girar suave a la izquierda para corregir.
    * Derecho en negro / izquierdo en blanco (`2`): girar suave a la derecha para corregir.
    * Ambos en blanco (`3`): retroceder o buscar la línea.
* **Práctica guiada:** Probar la lectura en vivo de los 4 estados sobre cinta negra y cargar el código de seguimiento a velocidad moderada (`100–130`) para evitar que salga en las curvas.
* **Preguntas de verificación:** ¿Por qué el color negro entrega un `0` y el blanco un `1`? ¿Qué pasa en las curvas si ponemos la velocidad al máximo (`255`)?

---

# 7. Refuerzo Integrador en Pista y Autoevaluación (`🛠️ REFUERZO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Integrar** el control de motores, el sensor ultrasonido y el sigue-líneas en un desafío combinado y evaluar el dominio propio antes del cierre de parcial.
* **¿Para qué me sirve en la vida?** Para resolver problemas complejos combinando varias entradas (sensores) y salidas (actuadores) en un mismo sistema autónomo.

## 📚 CONTENIDO, RETO Y AUTOEVALUACIÓN LIKERT (1 AL 5)
* **Repaso rápido integrador (sin respuestas visibles):**
  * ¿Qué puerto RJ25 usa el ultrasonido y cuál usa el sigue-líneas?
  * ¿Por qué un robot móvil necesita calibración física aunque el diagrama de flujo sea perfecto?
  * En lógica sigue-líneas, ¿qué debe hacer el robot si solo el sensor derecho detecta superficie blanca?
* **Reto de refuerzo en pista (`🛠️ REFUERZO`):** Seguir la pista de cinta negra y **detenerse con alerta RGB + buzzer** si aparece un obstáculo a menos de `15 cm`, reanudando la marcha cuando el camino quede libre.
* **Autoevaluación Escala de Likert (1 = Todavía me cuesta | 3 = Lo entiendo con ayuda | 5 = Lo domino y lo puedo explicar):**
  1. Diferenciar el modo En Vivo del modo Subir y conectar los puertos RJ25 de la placa mCore.
  2. Programar luces RGB, buzzer y motores con variables de velocidad y bucles de repetición.
  3. Diseñar diagramas de flujo y calibrar un robot físico en una pista cuadrada real.
  4. Utilizar los sensores ultrasonido (cm) y sigue-líneas (`0/1`) en rutinas autónomas.
