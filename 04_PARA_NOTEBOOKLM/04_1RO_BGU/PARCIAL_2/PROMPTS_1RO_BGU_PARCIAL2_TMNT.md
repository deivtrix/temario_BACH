# 🐢 PROMPTS PARA NOTEBOOKLM — 1RO BGU PARCIAL 2 (TORTUGAS NINJA)

## 📌 CÓMO USARLO
1. En **NotebookLM**, crea **1 cuaderno nuevo** para este parcial y sube **1 solo archivo**: `FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md`.
2. *(Opcional)* En **Descubrir fuentes**, pega estas búsquedas cortas en español:
   * `Arduino analogRead potenciómetro rango 0 a 1023`
   * `Arduino PWM analogWrite y función map`
   * `Circuito divisor de voltaje con fotorresistencia LDR Arduino`
   * `Arduino función tone buzzer pasivo frecuencias`
3. Copia y pega **1 prompt por tema** en el orden que necesites. Todos comparten el universo de **Tortugas Ninja**, alternando **viñetas de acción/conflicto** con **láminas explicativas profundas** para estudiar en Classroom.

---

## 🎬 VIDEO DE REPASO DEL PARCIAL (Para Studio -> Video)
```text
Crea un video explicativo de repaso en español para estudiantes de 1ro BGU (15-16 años) sobre todo el Volumen 2: "Señales Analógicas y Regulación PWM" usando el archivo FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

Cubre de forma ordenada y solo teórica todos los temas y subtemas del parcial (lectura analógica analogRead de 0 a 1023, función map() para reescalar rangos, modulación PWM con analogWrite de 0 a 255, divisor de voltaje con fotorresistencia LDR y resistencia de 10 kΩ, generación de frecuencias con tone() y calibración de umbrales con punto medio en Monitor Serial). Usa gráficos claros, esquemas de señal y ejemplos cercanos a su edad (sin personajes de cómics).

Prohibido mencionar nombres de profesor/mediador, fechas, "Semana X" o entregables.
```

---

## 🟢 CAPÍTULO #1: Informe de Potenciómetro con 4 LEDs + Cuestionario
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Lectura Analógica: Potenciómetro con 4 LEDs", etiqueta 👤 ACTIVIDAD INDIVIDUAL 1) basado en el CAPÍTULO #1 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Krang (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Conflicto, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos midiendo niveles de energía con un indicador analógico.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo pizarra/cuadrícula comparativa ("Pin digital 0/1 vs. Pin analógico A0 con analogRead 0-1023" y "Rangos por umbrales > y < para 4 LEDs"), con diagramas claros presentados por Donatello sin globos que tapen la escala.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho de conflicto con etiqueta 👤 ACTIVIDAD INDIVIDUAL.
2. Propósito LEV y explicación cercana a chicos de 15-16 años de para qué les sirve leer señales continuas en medidores de volumen, batería o sensores industriales.
3. Lámina explicativa profunda de analogRead (0–1023) y división en 4 rangos.
4. Enunciado claro de la actividad individual + 1 consejo (PROHIBIDO resolverles el cuestionario o el informe).
5. Verificación y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```

---

## 🟢 CAPÍTULO #2: Atenuador de Brillo LED (`map()` + PWM `analogWrite`)
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Atenuador de Brillo PWM con map()", etiqueta 👤 ACTIVIDAD INDIVIDUAL 2) basado en el CAPÍTULO #2 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Destructor (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Conflicto, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos regulando sigilosamente la intensidad de las luces en una infiltración nocturna.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo cuadrícula comparativa ("Qué es PWM: pulsos rápidos ON/OFF con analogWrite 0-255" y "Por qué necesitamos map(valor, 0, 1023, 0, 255)"), con ondas cuadradas y diagramas claros presentados por Donatello sin globos que tapen las fórmulas.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 👤 ACTIVIDAD INDIVIDUAL.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué sirve PWM en reguladores de brillo de pantallas, motores y luces inteligentes.
3. Láminas explicativas profundas de PWM (pines ~) y la función map().
4. Enunciado claro de la actividad individual en Tinkercad y kit físico + 1 consejo (PROHIBIDO regalar el código final del reto).
5. Verificación y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```

---

## 🟡 CAPÍTULO #3: Poste de Alumbrado Automático con LDR
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Poste de Alumbrado Automático (LDR)") basado en el CAPÍTULO #3 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael y Miguel Ángel (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Problema al anochecer, Práctica y Cierre): usa viñetas dinámicas de cómic con diálogos automatizando las luminarias de la ciudad al caer la noche.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo cuadrícula comparativa ("Por qué la LDR necesita resistencia de 10 kΩ en divisor de voltaje" y "De día vs. De noche: cambio de lectura en A0 y decisión if/else"), presentadas por Donatello sin globos que tapen el circuito.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué les sirve usar divisores de voltaje con sensores resistivos en alumbrado público o celulares.
3. Láminas explicativas profundas de la LDR, divisor de voltaje con 10 kΩ y lectura en A0.
4. Práctica guiada paso a paso en Tinkercad y kit físico dentro de la historia.
5. Preguntas de verificación (con pista breve de comprobación) y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```

---

## 🟡 CAPÍTULO #4: Theremin Musical con Luz (LDR + Buzzer `tone()`)
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Theremin Musical con Luz", etiqueta 👥 ACTIVIDAD GRUPAL) basado en el CAPÍTULO #4 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Krang (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Desafío sonoro, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos creando un instrumento musical sin contacto controlado por sombra y luz.
- En los bloques de TEORÍA: usa láminas explicativas profundas ("Función tone(pin, frecuencia) y mapeo de luz 0-1023 a rango audible en Hz"), con diagramas claros presentados por Donatello sin globos que tapen la sintaxis.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 👥 ACTIVIDAD GRUPAL.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué sirve convertir la lectura de un sensor en frecuencias sonoras o alarmas variables.
3. Lámina explicativa profunda de tone() y mapeo de frecuencias.
4. Enunciado claro de la actividad grupal física + 1 consejo de montaje (PROHIBIDO dar el código resuelto del reto).
5. Verificación y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```

---

## 🟠 CAPÍTULO #5: Refuerzo — Calibración con Monitor Serial
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Calibración con Monitor Serial", etiqueta 🛠️ REFUERZO) basado en el CAPÍTULO #5 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Destructor (prohibido dibujar niños genéricos, profesores o personajes externos).
- En Portada, Problema de luz real y Cierre: viñetas dinámicas de cómic con diálogos resolviendo por qué un código falla cuando cambia la luz del aula.
- En Teoría: lámina explicativa profunda paso a paso ("Medir Mínimo (oscuro) + Medir Máximo (luz) -> Calcular Punto Medio (min + max) / 2"), presentada por Donatello sin globos que tapen la fórmula.

Usa las diapositivas que necesites, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 🛠️ REFUERZO.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué sirve calibrar umbrales reales en vez de copiar números fijos de internet.
3. Lámina explicativa profunda del método de calibración con Monitor Serial.
4. Reto práctico de calibración en clase (SIN regalar los valores medidos) y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```

---

## 🔵 CAPÍTULO #6: Cierre del Parcial 2 — Repaso y Autoevaluación
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Repaso Integrador y Autoevaluación", etiqueta 🛠️ REFUERZO) basado en el CAPÍTULO #6 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y el Maestro Splinter (prohibido dibujar niños genéricos, profesores o personajes externos).
- En Portada, Reto y Cierre: viñetas dinámicas de cómic con diálogos en la evaluación de dominio del dojo.
- En el Resumen: lámina visual limpia integrando analogRead, map(), PWM, LDR y calibración Serial sin globos largos que tapen los esquemas.

Usa las diapositivas que necesites, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 🛠️ REFUERZO.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué les sirve dominar entradas analógicas y salidas PWM.
3. Lámina visual resumen del Parcial 2.
4. Preguntas de repaso (SIN respuestas visibles) y tabla de Autoevaluación Escala de Likert (1 al 5) con los 4 aspectos clave del parcial.
5. Cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
