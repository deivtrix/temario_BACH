# 🟠 3RO BGU — PARCIAL 2 / SEMANA 4 (23 – 27 nov)
**Tema:** Semáforo Inteligente con ESP32 en Wokwi *(Individual 1)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo / Ambientación (45 min)  
**Entregable:** Captura o enlace de Wokwi con el semáforo funcionando en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un semáforo de 3 luces en el ESP32 usando Wokwi para controlar varios pines a tiempo.
* **¿Para qué me sirve en la vida?** Para controlar secuencias temporizadas en tráfico, procesos industriales y cualquier sistema con múltiples indicadores.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada hicimos la nivelación y la sirena de 2 LEDs. Hoy nos ambientamos con el clásico semáforo de 3 luces, pero ya en arquitectura ESP32."*
* **Propósito en pantalla:** *"Construir un semáforo de 3 luces en el ESP32 usando Wokwi para controlar varios pines a tiempo."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Pines seguros en ESP32 (Wokwi):** Usar por ejemplo `GPIO 12` (Rojo), `GPIO 14` (Amarillo), `GPIO 27` (Verde), cada uno con su resistencia de $220\,\Omega$ a `GND`.
* **Buenas prácticas:** Declarar variables `const int` al inicio y usar `Serial.begin(115200);` para imprimir en consola qué luz está activa (`"VERDE - AVANCE"`).

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Montan en `wokwi.com/projects/new/esp32` los 3 LEDs y prueban el ciclo básico Verde $\rightarrow$ Amarillo $\rightarrow$ Rojo.
* **25 – 40 min (Reto Solos):** *"Haz que la luz Verde parpadee 3 veces antes de pasar a Amarillo (aviso peatonal) e imprime el estado actual en el Monitor Serial a 115200 baudios."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Por qué declaramos los pines como `const int` en lugar de escribir el número directo en cada `digitalWrite`?"*
  2. *"¿Qué velocidad de baudios usamos en `Serial.begin()` con el ESP32?"*
* **Cierre:** Subir captura de Wokwi (LED encendido + código con `// Nombre` + Monitor Serial) a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Individual 1: Semáforo en ESP32 (Wokwi)

PROPÓSITO: Construir un semáforo de 3 luces en el ESP32 usando Wokwi para controlar varios pines a tiempo.

INSTRUCCIONES:
1. En wokwi.com (ESP32), conecta 3 LEDs (Rojo, Amarillo, Verde) con resistencias de 220 ohmios a GND.
2. Programa el ciclo del semáforo e incluye un parpadeo de 3 veces en el Verde antes de cambiar a Amarillo.
3. Imprime el estado ("VERDE", "AMARILLO", "ROJO") en el Monitor Serial a 115200 baudios.
4. Pon // Tu Nombre Apellido en la línea 1 del código y sube 1 captura de la simulación funcionando.

Calificación: 10 puntos (Actividad Individual 1).
```
