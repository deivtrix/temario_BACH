# 📘 8VO EGB — PARCIAL 3 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología  
**Unidad:** Ley de Ohm y Circuitos Serie/Paralelo

---

# 1. Átomos, Cargas y Electrostática (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Comprender** cómo se cargan los objetos por fricción (electrostática) y cómo se comportan las cargas positivas y negativas.
* **¿Para qué me sirve en la vida?** Para entender por qué nos da un pequeño chispazo al tocar una puerta metálica o por qué se eriza el cabello con un suéter o globo.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **Estructura del átomo:** Toda materia está hecha de átomos con **protones** (`+`, carga positiva en el núcleo), **neutrones** (`0`, sin carga) y **electrones** (`-`, carga negativa girando alrededor y capaces de saltar de un material a otro).
* **¿Cómo se produce la carga electrostática?** Cuando frotamos dos materiales distintos (como un globo contra lana o cabello), los electrones se transfieren de un material al otro:
  * El que **gana electrones** queda con **carga negativa (`-`)**.
  * El que **pierde electrones** queda con **carga positiva (`+`)**.
* **Ley de las cargas:** Cargas **iguales se repelen** (`+` con `+`, `-` con `-`) y cargas **opuestas se atraen** (`+` con `-`).
* **Ejemplos de la vida real:** El chispazo al tocar la manija metálica del carro después de caminar en alfombra, el cabello levantado al quitarse un saco de lana o el polvo pegado a la pantalla del televisor.
* **Práctica guiada en PhET:** Usar *Globos y Electricidad Estática* y *John Travoltage* para observar la transferencia de electrones por fricción y la descarga eléctrica al tocar metal.

---

# 2. Taller Físico Electrostático y Toma a Tierra (`👤 ACTIVIDAD INDIVIDUAL 1`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Experimentar** la atracción y repulsión electrostática con materiales cotidianos y entender cómo nos protege la toma a tierra frente a descargas.
* **¿Para qué me sirve en la vida?** Para comprender cómo funcionan los pararrayos y por qué los electrodomésticos grandes tienen una tercera pata de conexión a tierra.

## 🛠️ CONTENIDO, MATERIALES Y PROCEDIMIENTO PASO A PASO
* **Fundamento técnico (Rayos y Toma a Tierra):** En una tormenta, las nubes acumulan enorme carga electrostática por fricción del aire y hielo. El rayo es una descarga gigante buscando equilibrarse. La **toma a tierra** (cable de cobre conectado a una varilla enterrada en el suelo) ofrece un camino seguro para que esa carga excesiva se descargue hacia la Tierra sin dañar personas ni aparatos.
* **Materiales exactos:** 2 globos de látex inflados, 1 pedazo de tela de lana o cabello seco, 1 lata de aluminio vacía y limpia, papel picado en trocitos pequeños y 1 regla plástica.
* **Experimento 1 — Atracción de papel picado:**
  1. Frotar el globo (o regla plástica) vigorosamente contra la tela de lana o cabello seco durante 15 segundos.
  2. Acercar el globo sin tocarlo a los trocitos de papel sobre la mesa y observar cómo saltan y se adhieren (inducción electrostática).
* **Experimento 2 — Carrera de latas sin tocarlas:**
  1. Colocar la lata de aluminio acostada sobre una mesa lisa y seca.
  2. Cargar el globo frotándolo 20 segundos y acercarlo a 2–3 cm del costado de la lata; mover el globo despacio hacia adelante para hacer rodar la lata sin tocarla.
* **Experimento 3 — Repulsión entre dos globos:**
  1. Frotar ambos globos con lana para que queden con la misma carga (`-`).
  2. Acercarlos suavemente y comprobar cómo se separan o se empujan entre sí.
* **Verificación:** Registrar en tabla qué ocurrió en cada experimento, qué carga adquirió el globo y cómo actúa el cable a tierra en casa (tercer pin del enchufe) o el pararrayos de un edificio.

---

# 3. Ley de Ohm (`V = I × R`), Símbolos y Tinkercad Circuits (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Calcular** la resistencia adecuada usando la Ley de Ohm (`V = I × R`) y leer símbolos eléctricos estándar en Tinkercad Circuits para proteger un LED sin quemarlo.
* **¿Para qué me sirve en la vida?** Para saber qué resistencia necesita cualquier componente electrónico antes de conectarlo a una pila y entender planos eléctricos reales.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **Las 3 magnitudes de la Ley de Ohm:**
  * **Voltaje (`V`, en Voltios):** La "fuerza" o presión que empuja a los electrones (ej. pila de 9V o USB de 5V).
  * **Corriente (`I`, en Amperios o miliamperios `mA`):** La cantidad de electrones que pasan por el cable cada segundo.
  * **Resistencia (`R`, en Ohmios `Ω`):** La oposición al paso de la corriente para frenar electrones y proteger componentes delicados como un LED.
* **Fórmula práctica:** `V = I × R` -> para hallar la resistencia protectora de un LED: `R = (V_fuente - V_LED) / I_LED`.
  * **Ejemplo real:** Con pila de `9V` y un LED rojo (`2V` y `0.02A` / `20 mA`): `R = (9 - 2) / 0.02 = 350 Ω` (en la práctica usamos el valor comercial cercano **330 Ω** o **470 Ω**). *(En 8vo trabajamos con el valor numérico directo en Tinkercad).*
* **Símbolos eléctricos estándar (Vista Esquemática):** En Tinkercad Circuits podemos alternar a la **Vista Esquemática** para leer los símbolos internacionales de batería/fuente, resistencia (zigzag o rectángulo), LED (diodo con flechas), interruptor y multímetro.
* **Práctica guiada en Tinkercad:** Conectar una pila 9V + resistencia de 330 Ω + LED en protoboard virtual, medir con el multímetro y revisar la Vista Esquemática.

---

# 4. Circuito en Serie en Tinkercad Circuits (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** y medir un circuito en Serie en Tinkercad (vista física y esquemática) para comprobar cómo se reparte el voltaje y qué pasa si falla un componente.
* **¿Para qué me sirve en la vida?** Para entender por qué las antiguas luces navideñas se apagaban enteras cuando se dañaba un solo foquito y cómo funcionan los interruptores en serie.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **¿Qué es un Circuito en Serie?** Es una conexión donde los componentes van conectados **uno detrás del otro** formando **un único camino** cerrado para la corriente eléctrica.
* **Comportamiento eléctrico en Serie:**
  * **Misma corriente (`I`):** Toda la corriente pasa por cada bombilla/LED en fila.
  * **Voltaje repartido (`V`):** El voltaje de la pila se divide entre los componentes (por eso, al agregar más bombillas en serie, cada una **brilla menos**).
  * **Dependencia total:** Si se abre o se quema **un solo** componente, se corta el único camino y **se apagan todos**.
* **Ejemplos de la vida real:** El interruptor de la luz de un cuarto (va en serie con el foco para poder cortarlo), el fusible/breaker de protección y las guirnaldas de luces antiguas en serie.
* **Práctica guiada + Diagnóstico rápido:** En Tinkercad, armar 1 batería 9V + 1 interruptor + 2 bombillas en Serie, observar su Vista Esquemática, medir voltaje en cada bombilla y diagnosticar qué falla ocurre cuando se desconecta una de ellas o se coloca un LED al revés.

---

# 5. Circuito en Paralelo y Comparativa Serie vs. Paralelo (`👤 ACTIVIDAD INDIVIDUAL 2`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un circuito en Paralelo en Tinkercad y compararlo frente a uno en Serie (brillo, voltaje, esquema y continuidad) para elegir la conexión adecuada.
* **¿Para qué me sirve en la vida?** Para entender por qué todos los focos y tomacorrientes de una casa o colegio se conectan en paralelo.

## 📚 CONTENIDO Y ACTIVIDAD
* **¿Qué es un Circuito en Paralelo?** Es una conexión donde cada componente tiene **su propia rama o camino independiente** conectado directamente a la fuente.
* **Comportamiento eléctrico en Paralelo:**
  * **Mismo voltaje (`V`):** Cada bombilla recibe el voltaje completo de la fuente, por eso todas **brillan con intensidad completa**.
  * **Corriente dividida (`I`):** La corriente total se reparte entre las ramas.
  * **Independencia:** Si una bombilla se quema o se desconecta, **las demás siguen funcionando** normalmente.
* **`👤 ACTIVIDAD INDIVIDUAL 2` (Tinkercad Circuits):** Armar en Tinkercad un circuito en **Paralelo** (con fuente, interruptor y 2 cargas protegidas), activar la **Vista Esquemática** para observar sus símbolos, medir el voltaje en cada rama con el multímetro y completar la tabla comparativa **Serie vs. Paralelo** (brillo, voltaje por carga y qué ocurre al desconectar 1 carga).

---

# 6. Taller Físico: Masa Conductora — Serie y Paralelo (`👥 ACTIVIDAD GRUPAL`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** en equipos circuitos físicos en Serie y en Paralelo usando masa conductora casera y LEDs para comprobar en la práctica la conducción y la polaridad.
* **¿Para qué me sirve en la vida?** Para demostrar que materiales cotidianos con agua y sal conducen electricidad y para diferenciar físicamente una conexión en serie de una en paralelo.

## 🛠️ CONTENIDO, MATERIALES Y PROCEDIMIENTO PASO A PASO
* **Fundamento técnico:** La harina y el agua con **sal** forman una masa conductora gracias a los iones de sal disueltos; en cambio, la masa hecha con **azúcar** (o aceite sin sal) actúa como aislante. Si dos bloques de masa conductora se tocan directo sin dejar espacio, hacen **cortocircuito** y el LED no enciende.
* **Materiales exactos (por equipo):** 1 taza de harina de trigo, 1/4 de taza de sal, 1/2 taza de agua tibia, 1 cucharada de aceite vegetal, colorante alimenticio (opcional), 1 recipiente para mezclar, 1 pila de 9V (o portapilas de 4.5V–6V) con broche/cables, 2 a 3 LEDs y 1 trozo de cartón o plástico aislante como base. *(Si se usa pila de 9V, limitar o no dejar los LEDs conectados mucho tiempo en corto o usar resistencia de 330 Ω en serie con la batería).*
* **Paso 1 — Preparación de la masa conductora (10 min):**
  1. Mezclar en el recipiente la harina y la sal en seco.
  2. Agregar poco a poco el agua tibia y el aceite mientras se amasa durante 3–4 minutos hasta lograr una plastilina suave que no se pegue a las manos (si queda muy aguada, añadir un poco más de harina).
* **Paso 2 — Circuito en Serie con masa (10 min):**
  1. Formar **3 bolitas o tiras separadas** de masa sobre la base de cartón/plástico (sin que se toquen entre sí).
  2. Clavar las patas de los LEDs haciendo puente de una masa a la siguiente respetando siempre la polaridad (pata larga `+` hacia el lado del `+` de la pila; pata corta `-` hacia el lado del `-`).
  3. Conectar los cables de la batería a la primera y última masa para encenderlos en fila y observar el brillo.
* **Paso 3 — Circuito en Paralelo con masa (10 min):**
  1. Formar **2 tiras largas paralelas** de masa separadas por 2 cm de aire (riel `+` y riel `-`, nunca deben tocarse).
  2. Conectar cada LED haciendo puente entre la tira `+` y la tira `-` (todas las patas largas al riel `+`, todas las patas cortas al riel `-`).
  3. Conectar la batería a ambos rieles y comprobar que los LEDs brillan fuerte y si retiras uno, los demás siguen encendidos.
* **Verificación de calidad:** Comprobar que no haya contacto directo entre masas de polos opuestos (cortocircuito) y que al retirar un LED en paralelo los demás continúen encendidos.

---

# 7. Refuerzo, Repaso y Autoevaluación del Parcial 3 (`🛠️ REFUERZO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Consolidar** electrostática, Ley de Ohm, lectura esquemática y circuitos Serie/Paralelo mediante reto práctico y autoevaluación antes de cerrar el parcial.
* **¿Para qué me sirve en la vida?** Para resolver fallas simples en circuitos reales y saber calcular protecciones básicas para LEDs.

## 📚 CONTENIDO, RETO Y AUTOEVALUACIÓN LIKERT (1 AL 5)
* **Repaso rápido integrador (sin respuestas visibles):**
  * ¿Por qué un globo frotado con lana atrae papelitos o mueve una lata?
  * ¿Cómo proteges un LED de 2V si solo tienes una pila de 9V (Ley de Ohm)?
  * En la Vista Esquemática, ¿en qué se diferencia un circuito en Serie de uno en Paralelo al desconectar una carga?
* **Reto integrador en Tinkercad (`🛠️ REFUERZO`):** Armar un circuito mixto simple o Paralelo con 2 LEDs protegidos por resistencia de 330 Ω, verificar su **Vista Esquemática** y nivelar cualquier actividad pendiente del parcial.
* **Autoevaluación Escala de Likert (1 = Todavía me cuesta | 3 = Lo entiendo con ayuda | 5 = Lo domino y lo puedo explicar):**
  1. Explicar cómo se producen las cargas electrostáticas y para qué sirve la toma a tierra.
  2. Aplicar la Ley de Ohm (`V = I × R`) para calcular una resistencia protectora de LED.
  3. Leer símbolos eléctricos básicos en Vista Esquemática y distinguir un circuito en Serie de uno en Paralelo.
  4. Construir físicamente conexiones en Serie y Paralelo respetando polaridad y evitando cortocircuitos.
