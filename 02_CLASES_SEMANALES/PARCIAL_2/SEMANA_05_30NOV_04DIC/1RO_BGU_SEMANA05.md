# 🔴 1RO BGU — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Poste de Alumbrado Público Automático (Sensor LDR)  
**Subtemas puntuales (2 nuevos):**
1. Cómo funciona una fotorresistencia (LDR): cambia su resistencia según la luz / Armado del divisor de voltaje (LDR + resistencia fija) en pin analógico `A0`.
2. Lectura de valores de luz con `analogRead(A0)` y umbral `>` / `<` / Encendido automático de LED al oscurecer (Poste de Alumbrado en Tinkercad).
**Mediador:** David Castro    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura en Tinkercad / visto bueno en kit físico + lectura serial en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un circuito con sensor de luz (LDR) que prenda un LED solo cuando oscurece, como un poste de calle.
* **¿Cómo sé que lo logré?** Al tapar la LDR (bajar la luz) en Tinkercad, el LED del poste se enciende automáticamente.
* **¿Para qué me sirve en la vida?** Para automatizar luces de jardines, pasillos, faros de vehículos y pantallas que ajustan su brillo según la luz del ambiente.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"¿Quién apaga y prende los postes de luz de la calle cada noche? No hay una persona con un interruptor: usan un sensor que 've' la oscuridad. Hoy lo armamos."*
* **Propósito en pantalla:** *"Construir un circuito con sensor de luz (LDR) que prenda un LED solo cuando oscurece, como un poste de calle."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Predicción PRIMM (30 seg antes de simular):** Preguntar qué hará el ejemplo o qué cambia si modifican un parámetro antes de correrlo.
* **¿Qué es una LDR?** Una resistencia que cambia su valor según la luz que recibe.
* **Conexión (Divisor de Voltaje):** 1 pata de la LDR a `5V`, la otra pata al pin **`A0`**, y desde ese mismo punto **`A0`** una resistencia de **$10\text{k}\Omega$ a `GND`**.
* **Modelación:** Leer `analogRead(A0)` en Monitor Serial, tapar la LDR con el dedo para ver cómo cambia el número y poner el `if (luz < umbral)`.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **15 – 25 min (Guiada):** Conectan la LDR + resistencia $10\text{k}\Omega$ + 1 LED en Pin 9 y ven los valores de luz vs. oscuridad en el Monitor Serial.
* **25 – 40 min (Reto Solos):** *"Ajusta tu umbral para que el LED prenda cuando tapas la LDR, y agrega un **segundo LED** o haz que el brillo suba gradualmente con `map()` mientras más oscuro esté."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Por qué la LDR necesita una resistencia de $10\text{k}\Omega$ hacia `GND` para poder leerse en `A0`?"*
  2. *"¿Qué número marcó tu Monitor Serial con luz vs. tapado con el dedo?"*
* **Cierre:** Visto bueno en kit / subida de captura con valores reales en Classroom.
---

## ❓ PREGUNTAS DE CIERRE (CON RESPUESTA ESPERADA)
1. **¿Qué ocurre con el valor de `analogRead()` cuando tapamos la LDR con la mano?**
   * *Respuesta esperada:* El valor cambia (sube o baja según cómo esté armado el divisor de voltaje) indicando menos luz.
2. **¿Por qué la LDR necesita una resistencia fija acompañándola en el circuito?**
   * *Respuesta esperada:* Para formar un divisor de voltaje que permita al Arduino leer variaciones de tensión en `A0`.
3. **¿Qué estructura de control usamos para decidir si el poste se enciende o se apaga?**
   * *Respuesta esperada:* Una condición `if / else` comparando la lectura contra un umbral.
