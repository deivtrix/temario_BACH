# 📘 10MO EGB — PARCIAL 2 / SEMANA 6 (7 – 11 dic)

> [!IMPORTANT]
> # 👥 ACTIVIDAD GRUPAL EVALUADA (GRUPAL 1)
**Tema:** Semáforo Físico en Protoboard con Arduino UNO y Variables `int` *(Grupal 1 — Práctica en vivo)*  
**Subtemas puntuales (2 nuevos):**
1. Uso de variables `int` para nombrar pines (`int rojo = 13;`, `int amarillo = 12;`, `int verde = 11;`).
2. Cableado ordenado de 3 LEDs + 3 resistencias de $220\,\Omega$ compartiendo bus común `GND` en protoboard física.
**Cargo:** Mediador    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo B — Trabajo Grupal Físico en Vivo (45 min)  
**Entregable:** Visto bueno en vivo + foto grupal del semáforo físico encendido en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** nuestro semáforo en protoboard real con Arduino UNO para verlo funcionar fuera de la pantalla.
* **¿Cómo sé que lo logré?** Tu semáforo físico en protoboard enciende los 3 LEDs con resistencia protectora y código cargado por USB.
* **¿Para qué me sirve en la vida?** Para aprender a cablear componentes reales sin quemar LEDs y cargar programas desde la computadora a una placa física.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"La semana pasada instalamos Arduino IDE e hicimos parpadear 1 LED físico. Hoy subimos de nivel: vamos a controlar 3 LEDs como un semáforo real usando variables `int` para no confundir los pines."*
* **Propósito en pantalla:** *"Construir nuestro semáforo en protoboard real con Arduino UNO para verlo funcionar fuera de la pantalla."*

### 2. Encuadre de Variables `int`, Seguridad y Pines (05 – 12 min)
* **Variables `int`:** `int rojo = 13;`, `int amarillo = 12;`, `int verde = 11;`. Ordena el código y evita memorizar números.
* **Reglas físicas:** 1) Nunca conectar LEDs sin resistencia de $220\,\Omega$, 2) Verificar pata larga ($+$ al pin) y pata corta ($-$ al bus común `GND`), 3) Seleccionar `Arduino UNO` y puerto `COM` correcto en el IDE.

### 3. Trabajo Grupal Físico con Intervención del Mediador (12 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Puerto `COM`/Sintaxis.
* **Roles rotativos (3 por equipo):** 1. Armado/Diseño -> 2. Código/Parámetros -> 3. Verificador/Evidencia.
* **Instrucción:** En grupos arman el circuito (Pines 13, 12, 11 + bus común GND), programan la secuencia Verde $\rightarrow$ Amarillo $\rightarrow$ Rojo en Arduino IDE, la suben por USB y prueban el semáforo real.
* **Tu rol:** Ayudas a destrabar errores de puerto COM o LEDs puestos al revés en la protoboard.

### 4. Cierre, Preguntas y Entrega (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Cómo identificas físicamente cuál es el ánodo ($+$) y el cátodo ($-$) de un LED real?"*
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
