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

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de Super Mario en español para estudiantes de 9no EGB (13-14 años) del Volumen 3: "Navegación y Robótica Móvil", como un capítulo autoconclusivo independiente ("Sensor Sigue-Líneas IR") basado en el punto 6 de FUENTE_9NO_EGB_PARCIAL3_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de Super Mario en TODAS las diapositivas: Mario, Luigi y Toad en una pista oscura estrecha (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Conflicto, Práctica y Cierre): usa viñetas dinámicas de cómic con diálogos cruzando un puente estrecho guiado por cinta negra.
- En los bloques de TEORÍA (Conceptos 1 y 2): usa láminas explicativas profundas estilo cuadrícula comparativa ("Superficie blanca refleja = 1 vs. Cinta negra absorbe = 0" y "Tabla de los 4 estados de corrección en curvas"), con diagramas claros presentados por Toad sin globos que tapen la tabla.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho de pista.
2. Propósito LEV y explicación cercana a su edad (13-14 años) de para qué les sirve la lógica binaria de sensores infrarrojos en robots de bodegas industriales o líneas guiadas.
3. Concepto 1 (reflexión de luz infrarroja: blanco = 1 vs. negro = 0) en lámina explicativa profunda.
4. Concepto 2 (los 4 estados posibles de lectura y corrección en curvas) en lámina comparativa clara + ejemplo en el universo Mario.
5. Práctica guiada paso a paso sobre pista de cinta negra a velocidad moderada dentro de la historia.
6. Preguntas de verificación (con pista breve de comprobación) y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
