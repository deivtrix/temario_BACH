# 🟠 3RO BGU — PARCIAL 2 / SEMANA 3 (16 – 19 nov)
**Tema:** Formulario de Mejora de Calificaciones + Repaso Base ESP32 en Wokwi  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Recuperación y Nivelación Autónoma (45 min)  
**Entregable:** Formulario de recuperación enviado + verificación en Wokwi (para quienes debían práctica).

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Revisar** cómo funciona el ESP32 y recuperar notas con el formulario antes de pasar a sensores.
* **¿Para qué me sirve en la vida?** Para no quemar placas de $3.3\text{V}$ y tener claras las bases antes de programar proyectos IoT.

---

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)

### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Chicos, hoy tenemos una oportunidad puntual para nivelar y mejorar calificaciones antes de avanzar a sensores en el ESP32. Primero hacemos el formulario individual y luego nivelamos en Wokwi."*
* **Presentar el Propósito (Página 2):** *"Revisar cómo funciona el ESP32 y recuperar notas con el formulario antes de pasar a sensores."**verificar y corregir** los fundamentos del ESP32 (pines GPIO y $3.3\text{V}$) para consolidar la base técnica sin dañar hardware."*

### 2. Repaso Express + Formulario Individual (05 – 25 min)
* **05 – 08 min (Repaso rápido con Página 3):** Recordar: ESP32 trabaja a **$3.3\text{V}$** (no $5\text{V}$), tiene WiFi/Bluetooth integrado y usa `115200` baudios.
* **08 – 25 min (Formulario):** Trabajo estrictamente individual en el formulario de Classroom.

### 3. Nivelación Práctica en Wokwi (25 – 40 min)
* **Instrucción:**
  * *"Quienes debían la Sirena de Policía en Wokwi, termínenla ahora con su nombre en la línea 1 (`// Nombre`) y súbanla."*
  * *"Quienes ya la entregaron, agreguen un tercer LED o un patrón de ráfaga doble para practicar."*
* **Tu rol:** Revisas los enlaces/capturas de quienes están recuperando y corriges errores de pines GPIO o resistencias en Wokwi.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Retroalimentación rápida del formulario:**
  1. *"¿Por qué un sensor o alimentación de $5\text{V}$ directo al pin GPIO puede dañar el ESP32?"*
  2. *"¿A cuántos baudios configuramos el Monitor Serial del ESP32?"*

---

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Nivelación y Mejora de Calificaciones — Fundamentos ESP32 (Wokwi)

PROPÓSITO: Revisar cómo funciona el ESP32 y recuperar notas con el formulario antes de pasar a sensores.

INSTRUCCIONES:
1. Completa el Formulario de Nivelación adjunto (20 minutos, individual).
2. Si tenías pendiente la práctica de Sirena de Policía en Wokwi, corrígela/termínala y adjunta tu captura con tu nombre en la línea 1 del código (// Nombre Apellido).

Calificación: Nota de recuperación / mejora registrada en el parcial.
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 3ro BGU (17-18 años) del Volumen 2: "Microcontroladores y Periféricos Digitales", como un capítulo autoconclusivo independiente ("Arquitectura ESP32 y Lógica 3.3V", etiqueta 🛠️ REFUERZO) basado en el CAPÍTULO #1 de FUENTE_3RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Krang (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Conflicto, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos migrando los sistemas de control a un microcontrolador moderno de 3.3V.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo hoja de datos técnica ("Arduino 5V vs. ESP32 3.3V: qué pines son seguros y cuáles son solo entrada"), con pinout claro presentado por Donatello sin globos que tapen los pines.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho técnico con etiqueta 🛠️ REFUERZO.
2. Propósito LEV y explicación cercana a jóvenes de 17-18 años de para qué sirve respetar niveles lógicos de 3.3V y conocer el pinout del ESP32 en hardware IoT real.
3. Lámina explicativa profunda de pines GPIO del ESP32 y precauciones de 3.3V.
4. Preguntas de verificación y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
