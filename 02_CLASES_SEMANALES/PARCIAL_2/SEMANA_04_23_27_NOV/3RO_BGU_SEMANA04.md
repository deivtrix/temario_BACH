# 🟠 3RO BGU — PARCIAL 2 / SEMANA 4 (23 – 27 nov)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Semáforo Inteligente con ESP32 en Wokwi  
**Subtemas puntuales (4):**
1. Pines digitales del ESP32 (3.3V) y resistencia protectora por LED.
2. Secuencia temporizada de 3 estados (Verde $\rightarrow$ Amarillo $\rightarrow$ Rojo).
3. Monitoreo de estado en tiempo real con `Serial.println()`.
4. Simulación y prueba de circuito en Wokwi.
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo / Ambientación (45 min)  
**Entregable:** Práctica en vivo en Wokwi sin entrega obligatoria *(Ind. 1 y 2 ya completas en Classroom)*.

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
---

## ❓ PREGUNTAS DE CIERRE (CON RESPUESTA ESPERADA)
1. **¿Qué ventaja tiene simular el ESP32 en Wokwi antes de armar en físico?**
   * *Respuesta esperada:* Permite probar el código, las conexiones y el Monitor Serial sin riesgo de quemar pines ni depender de cables físicos.
2. **¿Por qué cada LED en el semáforo necesita su propia resistencia en serie?**
   * *Respuesta esperada:* Para limitar la corriente que entrega el pin del ESP32 (3.3V) y evitar que el LED o el pin se dañen.
3. **¿Cómo podemos verificar en tiempo real en qué estado está el semáforo sin mirar solo los LEDs?**
   * *Respuesta esperada:* Imprimiendo mensajes de estado en el Monitor Serial con `Serial.println()`.

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 3ro BGU (17-18 años) del Volumen 2: "Microcontroladores y Periféricos Digitales", como un capítulo autoconclusivo independiente ("Semáforo ESP32 en Wokwi", etiqueta 👤 ACTIVIDAD INDIVIDUAL 1) basado en el CAPÍTULO #2 de FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Destructor (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Conflicto, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos controlando intersecciones urbanas en simulador Wokwi.
- En los bloques de TEORÍA: usa láminas explicativas profundas ("Flujo de trabajo en Wokwi: pines seguros GPIO 12/14/27, resistencias y temporización"), presentadas por Donatello sin globos que tapen el esquema.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 👤 ACTIVIDAD INDIVIDUAL.
2. Propósito LEV y explicación cercana a su edad (17-18 años) de para qué sirve validar circuitos digitales en simuladores profesionales antes de armar hardware.
3. Lámina explicativa profunda de pines seguros en ESP32 y lógica de tiempos del semáforo.
4. Enunciado claro de la actividad individual en Wokwi + 1 consejo (PROHIBIDO dar el código terminado del reto).
5. Verificación y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
