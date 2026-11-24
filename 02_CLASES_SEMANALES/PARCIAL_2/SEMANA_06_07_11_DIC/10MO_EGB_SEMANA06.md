# 📘 10MO EGB — PARCIAL 2 / SEMANA 6 (7 – 11 dic)

> [!IMPORTANT]
> # 👥 ACTIVIDAD GRUPAL EVALUADA
**Tema:** Semáforo Físico en Protoboard con Arduino UNO *(Grupal Físico)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Trabajo Grupal Físico (45 min)  
**Entregable:** Visto bueno en vivo + foto grupal del semáforo físico encendido en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** nuestro semáforo en protoboard real con Arduino UNO para verlo funcionar fuera de la pantalla.
* **¿Para qué me sirve en la vida?** Para aprender a cablear componentes reales sin quemar LEDs y cargar programas desde la computadora a una placa física.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada su semáforo funcionó en la pantalla de Tinkercad. Hoy lo traemos al mundo real: van a armarlo en protoboard física y cargarle el código al Arduino UNO."*
* **Propósito en pantalla:** *"Construir nuestro semáforo en protoboard real con Arduino UNO para verlo funcionar fuera de la pantalla."*

### 2. Encuadre de Seguridad y Pines (05 – 10 min)
* **Reglas físicas:** 1) Nunca conectar LEDs sin resistencia de $220\,\Omega$, 2) Verificar pata larga ($+$ al pin) y pata corta ($-$ a GND), 3) Seleccionar `Arduino UNO` y puerto `COM` correcto en el IDE.

### 3. Trabajo Grupal Físico con Intervención del Mediador (10 – 40 min)
* **Instrucción:** En parejas/grupos arman el circuito (Pines 13, 12, 11 + bus común GND), copian su código de Tinkercad al Arduino IDE, lo suben por USB y prueban el parpadeo real.
* **Tu rol:** Ayudas a destrabar errores de puerto COM o LEDs puestos al revés en la protoboard.

### 4. Cierre, Preguntas y Entrega (40 – 45 min)
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

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 10mo EGB (14-15 años) del Volumen 2: "Conexiones Seguras y Primer Código", como un capítulo autoconclusivo independiente ("Semáforo Físico con Arduino UNO") basado en el CAPÍTULO #4 de FUENTE_10MO_EGB_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y el Maestro Splinter (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Transición al taller físico y Cierre): usa viñetas dinámicas de cómic con diálogos armando su primer circuito programable real en mesa.
- En los bloques de TEORÍA Y SEGURIDAD: usa láminas explicativas profundas estilo manual visual ("3 Reglas de Oro antes de conectar el USB: Resistencias 220 Ω, Polaridad del LED y GND común en protoboard"), presentadas por Donatello sin globos que tapen el diagrama físico.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial.
2. Propósito LEV y explicación cercana a su edad (14-15 años) de para qué les sirve pasar del simulador al montaje físico cuidando pines y polaridad.
3. Lámina explicativa profunda de reglas de seguridad física y mapa de conexiones a protoboard + Arduino UNO.
4. Procedimiento paso a paso de montaje y carga de código desde la PC.
5. Pruebas de verificación y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
