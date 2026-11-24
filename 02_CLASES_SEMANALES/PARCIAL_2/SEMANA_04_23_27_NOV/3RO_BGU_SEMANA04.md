# 🟠 3RO BGU — PARCIAL 2 / SEMANA 4 (23 – 27 nov)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Semáforo Inteligente con ESP32 en Wokwi  
**Subtemas puntuales (2 nuevos):**
1. Pines digitales del ESP32 (3.3V) y resistencia protectora por LED / Secuencia temporizada de 3 estados (Verde $\rightarrow$ Amarillo $\rightarrow$ Rojo).
2. Monitoreo de estado en tiempo real con `Serial.println()` / Simulación y prueba de circuito en Wokwi.
**Mediador:** David Castro    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Tema Nuevo / Ambientación (45 min)  
**Entregable:** Práctica en vivo en Wokwi sin entrega obligatoria *(Ind. 1 y 2 ya completas en Classroom)*.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un semáforo de 3 luces en el ESP32 usando Wokwi para controlar varios pines a tiempo.
* **¿Cómo sé que lo logré?** Tu semáforo ESP32 en Wokwi respeta la secuencia Verde -> Amarillo -> Rojo usando GPIO válidos.
* **¿Para qué me sirve en la vida?** Para controlar secuencias temporizadas en tráfico, procesos industriales y cualquier sistema con múltiples indicadores.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"La semana pasada hicimos la nivelación y la sirena de 2 LEDs. Hoy nos ambientamos con el clásico semáforo de 3 luces, pero ya en arquitectura ESP32."*
* **Propósito en pantalla:** *"Construir un semáforo de 3 luces en el ESP32 usando Wokwi para controlar varios pines a tiempo."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Predicción PRIMM (30 seg antes de simular):** Preguntar qué hará el ejemplo o qué cambia si modifican un parámetro antes de correrlo.
* **Pines seguros en ESP32 (Wokwi):** Usar por ejemplo `GPIO 12` (Rojo), `GPIO 14` (Amarillo), `GPIO 27` (Verde), cada uno con su resistencia de $220\,\Omega$ a `GND`.
* **Buenas prácticas:** Declarar variables `const int` al inicio y usar `Serial.begin(115200);` para imprimir en consola qué luz está activa (`"VERDE - AVANCE"`).

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **15 – 25 min (Guiada):** Montan en `wokwi.com/projects/new/esp32` los 3 LEDs y prueban el ciclo básico Verde $\rightarrow$ Amarillo $\rightarrow$ Rojo.
* **25 – 40 min (Reto Solos):** *"Haz que la luz Verde parpadee 3 veces antes de pasar a Amarillo (aviso peatonal) e imprime el estado actual en el Monitor Serial a 115200 baudios."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Por qué declaramos los pines como `const int` en lugar de escribir el número directo en cada `digitalWrite`?"*
  2. *"¿Qué velocidad de baudios usamos en `Serial.begin()` con el ESP32?"*
* **Cierre:** Subir captura de Wokwi (LED encendido + código con `// Nombre` + Monitor Serial) a Classroom.
---

## ❓ PREGUNTAS DE CIERRE (CON RESPUESTA ESPERADA)
1. **¿Qué ventaja tiene simular el ESP32 en Wokwi antes de armar en físico?**
   * *Respuesta esperada:* Permite probar el código, las conexiones y el Monitor Serial sin riesgo de quemar pines ni depender de cables físicos.
2. **¿Por qué cada LED en el semáforo necesita su propia resistencia en serie?**
   * *Respuesta esperada:* Para limitar la corriente que entrega el pin del ESP32 (3.3V) y evitar que el LED o el pin se dañen.
3. **¿Cómo podemos verificar en tiempo real en qué estado está el semáforo sin mirar solo los LEDs?**
   * *Respuesta esperada:* Imprimiendo mensajes de estado en el Monitor Serial con `Serial.println()`.
