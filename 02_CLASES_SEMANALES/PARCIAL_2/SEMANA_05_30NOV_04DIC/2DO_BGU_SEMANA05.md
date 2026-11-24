# 🟣 2DO BGU — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)

> [!IMPORTANT]
> # 👤 ACTIVIDAD INDIVIDUAL EVALUADA
**Tema:** Bucles y Rotación en Tinkercad Codeblocks (Escalera / Torre Paramétrica) *(Individual 2)*  
**Subtemas puntuales (2 nuevos):**
1. Concepto de bucle `repetir` en Codeblocks para evitar bloques duplicados / Uso de variables o incrementos en `Z` para subir cada escalón.
2. Rotación incremental alrededor del eje `Z` (escalera en espiral / torre) / Aplicación de bucles en estructuras repetitivas (escalera o torre).
**Mediador:** David Castro    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Formulario corto auto-calificable en Classroom (5 preguntas sobre bucles/rotación) o captura exprés.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** una escalera en espiral en Codeblocks usando bucles `repetir` para no dibujar pieza por pieza.
* **¿Cómo sé que lo logré?** Tu escalera o torre en Codeblocks se construye automáticamente usando un bucle repetir y rotación.
* **¿Para qué me sirve en la vida?** Para automatizar patrones repetitivos (dientes de un engranaje, gradas, edificios o piezas mecánicas) con pocas líneas de código.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"Si les pido hacer una escalera de caracol de 20 escalones a mano, se demoran toda la hora. Con un bucle `repetir` y una variable de ángulo, sale en 8 bloques."*
* **Propósito en pantalla:** *"Construir una escalera en espiral en Codeblocks usando bucles `repetir` para no dibujar pieza por pieza."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **2 bloques nuevos:**
  * `Crear variable` (ej. `altura = 0` o `angulo = 0`).
  * `Repetir N veces` + `Cambiar variable por X` dentro del bucle.
* **Modelación:** Crear 1 escalón desplazado del centro, meterlo en `Repetir 15 veces`, subir en `Z` y rotar `24°` en cada vuelta alrededor de `[0,0,0]`.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
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

## ❓ PREGUNTAS DE CIERRE (CON RESPUESTA ESPERADA)
1. **¿Qué ventaja tiene usar un bucle `repetir` frente a copiar y pegar 10 veces los mismos bloques?**
   * *Respuesta esperada:* Reduce el código, evita errores manuales y permite cambiar el número de escalones en un solo lugar.
2. **¿Qué dos transformaciones combinamos dentro del bucle para lograr una escalera en espiral?**
   * *Respuesta esperada:* `Mover` en el eje `Z` (altura) y `Rotar` alrededor del eje `Z`.
3. **¿Dónde se coloca el bloque `Crear grupo` cuando usamos un bucle?**
   * *Respuesta esperada:* Al final, fuera del bucle, para unir todas las piezas generadas en un solo objeto.
