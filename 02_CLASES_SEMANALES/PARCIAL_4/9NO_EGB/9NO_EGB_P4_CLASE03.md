# 📗 9NO EGB — PARCIAL 4 / CLASE 3
**Tema:** Uso del Protoboard en Tinkercad Circuits (`👤 ACTIVIDAD INDIVIDUAL 1`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo + Individual (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** nuestro primer circuito LED en protoboard virtual de Tinkercad entendiendo sus filas y columnas internas.
* **¿Para qué me sirve en la vida?** El protoboard es la placa universal para probar circuitos sin soldar; dominarlo ahora te deja listo para Arduino en 10mo.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy conocemos la placa de pruebas o protoboard. Por debajo tiene láminas metálicas escondidas que conectan los agujeros."*
* **Propósito en pantalla:** *"Construir nuestro primer circuito LED en protoboard virtual de Tinkercad entendiendo sus filas y columnas internas."*

### 2. Modelación en Tinkercad Circuits (05 – 15 min)
* **Buses horizontales ($+$ rojo / $-$ azul):** Conectan toda la fila a lo largo para alimentar energía.
* **Columnas centrales (`a–e` y `f–j`):** Conectan de 5 en 5 en vertical, **divididas por el canal central** (donde nunca se debe puentear en corto un componente).

### 3. Actividad Individual (15 – 40 min)
* Cada estudiante arma en protoboard virtual de Tinkercad: pila 9V energizando los buses $+$ y $-$ $\rightarrow$ pulsador cruzando el canal central $\rightarrow$ resistencia $330\,\Omega$ $\rightarrow$ LED funcionando al presionar.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿En qué dirección están conectados los agujeros del bus rojo (+) vs. los agujeros del centro?"*
2. *"¿Por qué el protoboard tiene una zanja o división en la mitad?"*

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de Bob Esponja en español para estudiantes de 9no EGB (13-14 años) del Volumen 4: "Electrónica Analógica y Lógica Digital", como un capítulo autoconclusivo independiente ("Sensores Analógicos: Potenciómetro y LDR") basado en el punto 3 de FUENTE_9NO_EGB_PARCIAL4_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de Bob Esponja en TODAS las diapositivas: Bob Esponja, Patricio, Arenita y Calamardo (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Conflicto, Práctica y Cierre): usa viñetas dinámicas de cómic con diálogos regulando suavemente la luz y el sonido en la cúpula de Arenita.
- En los bloques de TEORÍA (Conceptos 1 y 2): usa láminas explicativas profundas estilo cuadrícula comparativa ("Señal Digital 0/1 vs. Señal Analógica continua" y "Potenciómetro de 3 pines vs. Fotorresistencia LDR"), con diagramas claros presentados por Arenita sin globos que tapen los esquemas.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial.
2. Propósito LEV y explicación cercana a su edad (13-14 años) de para qué les sirven las señales analógicas en perillas de volumen, brillo automático de pantallas o alumbrado público.
3. Concepto 1 (digital vs. analógico y potenciómetro de 3 pines) en lámina explicativa profunda.
4. Concepto 2 (fotorresistencia LDR: mayor luz = menor resistencia) en lámina comparativa + ejemplo en Bob Esponja y cotidiano.
5. Práctica guiada paso a paso con multímetro en Tinkercad Circuits dentro de la historia.
6. Preguntas de verificación (con pista breve de comprobación) y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
