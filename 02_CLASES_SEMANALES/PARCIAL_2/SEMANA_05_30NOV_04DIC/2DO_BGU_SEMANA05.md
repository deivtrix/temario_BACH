# 🟣 2DO BGU — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)
**Tema:** Bucles y Rotación en Tinkercad Codeblocks (Escalera / Torre Paramétrica)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura exprés en Classroom de la estructura generada con bucles `repetir`.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** una escalera en espiral en Codeblocks usando bucles `repetir` para no dibujar pieza por pieza.
* **¿Para qué me sirve en la vida?** Para automatizar patrones repetitivos (dientes de un engranaje, gradas, edificios o piezas mecánicas) con pocas líneas de código.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Si les pido hacer una escalera de caracol de 20 escalones a mano, se demoran toda la hora. Con un bucle `repetir` y una variable de ángulo, sale en 8 bloques."*
* **Propósito en pantalla:** *"Construir una escalera en espiral en Codeblocks usando bucles `repetir` para no dibujar pieza por pieza."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **2 bloques nuevos:**
  * `Crear variable` (ej. `altura = 0` o `angulo = 0`).
  * `Repetir N veces` + `Cambiar variable por X` dentro del bucle.
* **Modelación:** Crear 1 escalón desplazado del centro, meterlo en `Repetir 15 veces`, subir en `Z` y rotar `24°` en cada vuelta alrededor de `[0,0,0]`.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Todos programan la escalera en espiral básica de 12–15 escalones contigo.
* **25 – 40 min (Reto Solos):** *"Agrega una columna central o barandal, o modifica el código para crear una **torre retorcida / adorno paramétrico** cambiando los colores o la escala en cada vuelta."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué hace el bloque `Cambiar variable por...` dentro del bucle `Repetir`?"*
  2. *"¿Qué pasa si rotas la pieza alrededor de su propio centro vs. alrededor del origen `[0,0,0]`?"*
* **Cierre:** Subir captura con los bloques y la figura 3D terminada a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Práctica Codeblocks: Escalera en Espiral / Torre con Bucles

PROPÓSITO: Construir una escalera en espiral en Codeblocks usando bucles `repetir` para no dibujar pieza por pieza.

INSTRUCCIONES:
1. En Tinkercad Codeblocks, programa una escalera en espiral o torre paramétrica usando al menos 1 bucle "Repetir" y 1 variable que cambie altura o ángulo en cada vuelta.
2. Agrega una base o columna central para completar la estructura.
3. Toma 1 captura donde se vean los bloques y la figura final, y súbela aquí.

Calificación: 10 puntos (Práctica de clase).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 2do BGU (16-17 años) del Volumen 2: "Diseño Paramétrico por Bloques", como un capítulo autoconclusivo independiente ("Bucles y Rotación Espacial en 3D") basado en el CAPÍTULO #3 de FUENTE_2DO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael y Miguel Ángel (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Desafío arquitectónico, Práctica y Cierre): usa viñetas dinámicas de cómic con diálogos construyendo una torre en espiral con pocas líneas de código.
- En los bloques de TEORÍA: usa láminas explicativas profundas ("Bucle Repetir N veces + Desplazamiento incremental en Z + Rotación alrededor del eje Z usando pivote 0,0,0"), presentadas por Donatello sin globos que tapen la geometría.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial.
2. Propósito LEV y explicación cercana a su edad (16-17 años) de para qué sirven los bucles en diseño generativo, arquitectura e ingeniería CAD.
3. Láminas explicativas profundas sobre bucles `repeat`, rotación en eje Z y pivote.
4. Práctica guiada paso a paso (escalera en espiral / torre) dentro de la historia.
5. Preguntas de verificación y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
