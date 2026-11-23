# 🟣 2DO BGU — PARCIAL 2 / SEMANA 6 (7 – 11 dic)
**Tema:** Proyecto Codeblocks: Engranaje o Mecanismo Paramétrico  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Práctica Autónoma Evaluada (45 min)  
**Entregable:** Captura en Classroom del engranaje/mecanismo + variables visibles.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Crear** un engranaje en Codeblocks que cambie su número de dientes modificando una sola variable.
* **¿Para qué me sirve en la vida?** Así se diseñan piezas mecánicas profesionales (engranajes, poleas, hélices) que luego se imprimen en 3D o cortan en láser.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy vamos a usar lo aprendido con bucles y variables para hacer una pieza mecánica real: un engranaje (o hélice) que si cambias una variable pase de 8 a 16 dientes automáticamente."*
* **Propósito en pantalla:** *"Crear un engranaje en Codeblocks que cambie su número de dientes modificando una sola variable."*

### 2. Encuadre Técnico (05 – 12 min)
* Mostrar la lógica matemática simple:
  * Variable `dientes = 12`.
  * Ángulo de giro por vuelta = `360 / dientes`.
  * Bucle `Repetir dientes veces`: colocar diente en el borde y rotar `360 / dientes` grados alrededor de `[0,0,0]`, luego unir con cilindro central y perforar eje hueco.

### 3. Trabajo Autónomo con Intervención del Mediador (12 – 40 min)
* **Instrucción:** Cada estudiante programa su engranaje (o hélice/rueda dentada) parametrizado con `dientes`, agrega el hueco central del eje y prueba cambiar el número de `dientes` para verificar que funciona.
* **Tu rol:** Ayudas a quienes olvidan dividir `360 / dientes` o dejan el centro del diente desfasado.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué fórmula matemática usamos para saber cuántos grados rotar cada diente?"*
  2. *"¿Por qué decimos que este diseño es 'paramétrico'?"*
* **Cierre:** Subir captura con bloques y engranaje 3D a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Práctica Evaluada Codeblocks: Engranaje / Hélice Paramétrica

PROPÓSITO: Crear un engranaje en Codeblocks que cambie su número de dientes modificando una sola variable.

INSTRUCCIONES:
1. En Tinkercad Codeblocks, crea una variable llamada "dientes" (ej. 12 o 16).
2. Usa un bucle "Repetir (dientes) veces" rotando cada diente (360 / dientes) grados alrededor del origen.
3. Agrega el disco base, un hueco central para el eje y agrupa todo (Crear grupo).
4. Sube 1 captura donde se vean tus bloques y el engranaje terminado.

Calificación: 10 puntos (Práctica de clase).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 2do BGU (16-17 años) del Volumen 2: "Diseño Paramétrico por Bloques", como un capítulo autoconclusivo independiente ("Engranaje Paramétrico con Variables") basado en el CAPÍTULO #4 de FUENTE_2DO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Destructor (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Conflicto, Práctica y Cierre): usa viñetas dinámicas de cómic con diálogos necesitando fabricar engranajes de distintos tamaños al instante cambiando un solo parámetro.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo ingeniería ("Diseño fijo vs. Diseño Paramétrico con Variables: ángulo = 360 / num_dientes"), presentadas por Donatello sin globos que tapen las fórmulas.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho de ingeniería.
2. Propósito LEV y explicación cercana a su edad (16-17 años) de para qué sirve parametrizar piezas mecánicas con variables en manufactura digital.
3. Lámina explicativa profunda de variables paramétricas y cálculo automático de ángulo (360 / número de dientes).
4. Guía de proyecto en Codeblocks dentro de la historia y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
