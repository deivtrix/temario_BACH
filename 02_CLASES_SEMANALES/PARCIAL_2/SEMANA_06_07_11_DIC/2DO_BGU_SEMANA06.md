# 🟣 2DO BGU — PARCIAL 2 / SEMANA 6 (7 – 11 dic)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Proyecto Codeblocks: Engranaje o Mecanismo Paramétrico  
**Cargo:** Mediador    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo B — Práctica Autónoma Evaluada (45 min)  
**Entregable:** Captura en Classroom del engranaje/mecanismo + variables visibles.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Crear** un engranaje en Codeblocks que cambie su número de dientes modificando una sola variable.
* **¿Cómo sé que lo logré?** Al cambiar una sola variable (ej. número de dientes), tu engranaje en Codeblocks se recalcula automáticamente.
* **¿Para qué me sirve en la vida?** Así se diseñan piezas mecánicas profesionales (engranajes, poleas, hélices) que luego se imprimen en 3D o cortan en láser.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"Hoy vamos a usar lo aprendido con bucles y variables para hacer una pieza mecánica real: un engranaje (o hélice) que si cambias una variable pase de 8 a 16 dientes automáticamente."*
* **Propósito en pantalla:** *"Crear un engranaje en Codeblocks que cambie su número de dientes modificando una sola variable."*

### 2. Encuadre Técnico (05 – 12 min)
* Mostrar la lógica matemática simple:
  * Variable `dientes = 12`.
  * Ángulo de giro por vuelta = `360 / dientes`.
  * Bucle `Repetir dientes veces`: colocar diente en el borde y rotar `360 / dientes` grados alrededor de `[0,0,0]`, luego unir con cilindro central y perforar eje hueco.

### 3. Trabajo Autónomo con Intervención del Mediador (12 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **Instrucción:** Cada estudiante programa su engranaje (o hélice/rueda dentada) parametrizado con `dientes`, agrega el hueco central del eje y prueba cambiar el número de `dientes` para verificar que funciona.
* **Tu rol:** Ayudas a quienes olvidan dividir `360 / dientes` o dejan el centro del diente desfasado.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Qué fórmula matemática usamos para saber cuántos grados rotar cada diente?"*
  2. *"¿Por qué decimos que este diseño es 'paramétrico'?"*
* **Cierre:** Subir captura con bloques y engranaje 3D a Classroom.
