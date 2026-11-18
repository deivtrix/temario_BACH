# 🦾 9NO EGB — PARCIAL 4 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología  
**Unidad:** Electrónica Analógica y Lógica Digital

---

# 1. Código de Colores (4 bandas) y Polaridad del LED (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Interpretar** el código de colores de resistencias de 4 bandas y respetar la polaridad del diodo LED para armar circuitos básicos seguros en simulador.
* **¿Para qué me sirve en la vida?** Para proteger componentes electrónicos evitando que se quemen por exceso de corriente o conexión invertida.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **¿Por qué un LED necesita resistencia?** Un LED común funciona aprox. con `2V` y `20 mA`; si se conecta directo a `9V` sin resistencia limitadora, se quema al instante.
* **Código de colores (4 bandas):**
  * Banda 1: primer dígito. Banda 2: segundo dígito. Banda 3: multiplicador (cantidad de ceros). Banda 4: tolerancia (dorado = `±5%`).
  * **Tabla clave:** Negro `0`, Marrón `1`, Rojo `2`, Naranja `3`, Amarillo `4`, Verde `5`, Azul `6`, Violeta `7`, Gris `8`, Blanco `9`.
  * **Ejemplo práctico:** `Rojo - Rojo - Marrón - Dorado` = `2`, `2`, `x10` = `220 Ω`; `Naranja - Naranja - Marrón` = `330 Ω`; `Marrón - Negro - Naranja` = `10 000 Ω (10 kΩ)`.
* **Polaridad del LED:**
  * **Ánodo (`+`):** pata más larga (o esquina doblada en el símbolo).
  * **Cátodo (`-`):** pata más corta y borde plano en la cápsula.
* **Práctica guiada:** En Tinkercad Circuits (sin protoboard aún, usando conexiones directas), probar pila de `9V` + resistencia de `330 Ω` + LED verificando brillo y qué ocurre si se invierte la polaridad.
* **Preguntas de verificación:** ¿Qué valor tiene una resistencia `Naranja - Naranja - Marrón`? ¿Cómo reconoces físicamente el Ánodo y el Cátodo de un LED?

---

# 2. Lógica Digital (`AND` / `OR`) y Tablas de Verdad (`👤 ACTIVIDAD INDIVIDUAL 1`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modelar** circuitos de seguridad con lógica `AND` (serie) y lógica `OR` (paralelo) completando sus tablas de verdad (`0/1`) en simulador.
* **¿Para qué me sirve en la vida?** Para comprender cómo toman decisiones los sistemas reales de seguridad (por ejemplo, una caja fuerte que exige llave Y clave, o una alarma que suena si se abre puerta O ventana).

## 📚 CONTENIDO Y RETO INDIVIDUAL
* **Fundamento técnico (10 min):**
  * **Lógica `AND` (Y — Interruptores en serie):** la salida solo se activa (`1`) cuando **ambos** interruptores están cerrados (`1` y `1`). Si falta uno, la corriente no pasa (`0`).
  * **Lógica `OR` (O — Interruptores en paralelo):** basta con que **al menos uno** de los interruptores esté cerrado (`1`) para que la salida se active (`1`).
  * **Tabla de verdad:** tabla ordenada con las 4 combinaciones posibles de 2 entradas (`0-0`, `0-1`, `1-0`, `1-1`).
* **Actividad individual (`👤 ACTIVIDAD INDIVIDUAL` — sin tabla resuelta ni circuito armado):**
  * Simular en Tinkercad Circuits un **sistema de alarma/seguridad** con 2 interruptores deslizantes (o pulsadores), resistencia protectora y LED en configuración `AND` y otro en configuración `OR`, completando manualmente las 4 filas de sus tablas de verdad (`0` = apagado, `1` = encendido).
  * **1 Consejo:** Recuerda colocar una resistencia en serie con el LED para que el simulador no muestre advertencia de sobrecarga.
* **Preguntas de verificación:** En una compuerta `AND`, ¿cuántas combinaciones encienden el LED? Da un ejemplo cotidiano donde usarías lógica `OR`.

---

# 3. Sensores Analógicos: Potenciómetro y Fotorresistencia (LDR) (`📘 TEMA NUEVO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Medir** variaciones de resistencia en un potenciómetro y una fotorresistencia (LDR) usando el multímetro virtual para controlar la intensidad de luz o sonido.
* **¿Para qué me sirve en la vida?** Para entender cómo funcionan las perillas de volumen, los reguladores de brillo y los sensores de luz en lámparas automáticas y celulares.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **Digital vs. Analógico:** Un pulsador solo tiene dos estados (`0` o `1`, encendido/apagado). Un **sensor analógico** cambia de forma continua en un rango amplio de valores.
* **Potenciómetro (resistencia variable manual):** tiene 3 pines; al girar la perilla cambia la resistencia entre el pin central (`wiper`) y un extremo, permitiendo regular el brillo de un LED o el volumen de un buzzer.
* **Fotorresistencia o LDR (resistencia dependiente de la luz):** no tiene polaridad; **a mayor luz, menor resistencia** (deja pasar más corriente) y **en oscuridad, resistencia muy alta** (casi bloquea el paso).
* **Práctica guiada:** Conectar el multímetro de Tinkercad en modo Resistencia (`Ω`) para medir un potenciómetro al girarlo y una LDR al mover su deslizador de oscuridad a luz; luego conectar el potenciómetro en serie con un LED + resistencia fija de `220 Ω` para regular su brillo.
* **Preguntas de verificación:** ¿Por qué necesitamos dejar siempre una resistencia fija de `220 Ω` aunque usemos un potenciómetro? ¿Qué ocurre con la resistencia de la LDR cuando anochece?

---

# 4. El Transistor como Interruptor Automático: Luz Nocturna (`👤 ACTIVIDAD INDIVIDUAL 2`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** en simulador una luz nocturna automática utilizando una LDR y un transistor NPN como interruptor electrónico, interpretando su Vista Esquemática.
* **¿Para qué me sirve en la vida?** Para entender la pieza fundamental (el transistor) que permitió crear toda la electrónica moderna y las computadoras.

## 📚 CONTENIDO Y RETO INDIVIDUAL
* **Fundamento técnico (10 min):**
  * **¿Qué es un transistor NPN (ej. 2N2222)?** Funciona como una llave automática controlada por una corriente pequeñísima en su pin central (**Base**). Cuando la Base recibe suficiente voltaje, deja pasar corriente grande entre **Colector** y **Emisor**.
  * **Divisor de voltaje con LDR:** Al combinar la LDR con una resistencia fija hacia la Base del transistor, cuando llega la **oscuridad** sube el voltaje en la Base, el transistor se activa y **enciende el LED automáticamente**.
  * **Vista Esquemática:** Permite leer el circuito mediante símbolos estándar (símbolo del transistor con flecha hacia afuera en el Emisor, símbolo de la LDR con flechas de luz).
* **Actividad individual (`👤 ACTIVIDAD INDIVIDUAL` — sin circuito armado resuelto):**
  * Armar en Tinkercad Circuits el circuito de **Luz Nocturna Automática** (pila `9V`, transistor NPN, LDR, resistencia de divisor, resistencia de LED `330 Ω` y LED), verificar que el LED encienda únicamente al bajar la luz en el deslizador de la LDR y revisar su **Vista Esquemática**.
  * **1 Consejo:** Revisa con cuidado el orden de pines del transistor NPN (`Emisor`, `Base`, `Colector`) pasando el cursor sobre sus patas en Tinkercad antes de cablear.
* **Preguntas de verificación:** ¿Qué función cumple el pin Base del transistor? ¿Por qué el LED permanece apagado cuando hay mucha luz?

---

# 5. Taller Físico sin Protoboard: Circuito Lógico `AND`/`OR` (`📘 PRÁCTICA EN EQUIPOS`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Ensamblar** físicamente un circuito lógico `AND`/`OR` seguro sin soldadura ni protoboard usando cables caimán o borneras, verificando la resistencia por código de colores.
* **¿Para qué me sirve en la vida?** Para trasladar un plano virtual a conexiones físicas reales firmes, limpias y libres de cortocircuitos.

## 📚 CONTENIDO, MATERIALES Y PROCEDIMIENTO SEGURO
* **Reglas de seguridad (5 min):** Cero cautín ni soldadura; trabajar siempre con la pila desconectada hasta revisar toda la ruta; nunca unir directo el polo `+` con el `-` de la pila de `9V`.
* **Materiales exactos (por equipo):** 1 pila `9V` con broche (o portapilas `6V`), 4 a 6 cables caimán (o regleta/bornera), 2 pulsadores, 1 resistencia de `330 Ω` (`Naranja-Naranja-Marrón`) verificada por colores, 1 LED o buzzer protegido y base de cartón aislante.
* **Procedimiento en equipos:**
  1. Verificar con la tabla de colores que la resistencia sea de `330 Ω` (o `220 Ω`) y localizar el Ánodo (`+`) y Cátodo (`-`) del LED.
  2. Armar primero el circuito **lógico `AND`** conectando los 2 pulsadores en fila (serie) junto con la resistencia y el LED.
  3. Probar la batería: comprobar que solo enciende al presionar **ambos** pulsadores a la vez.
  4. Reconfigurar los 2 pulsadores en ramas paralelas para comprobar la **lógica `OR`** (enciende con cualquiera de los dos).
* **Verificación de calidad:** Revisar que no haya pinzas caimán metálicas rozándose entre sí (cortocircuito) y que el LED no se caliente.

---

# 6. Diagnóstico de Fallas (*Troubleshooting*) y Demo Física (`👥 ACTIVIDAD GRUPAL`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Diagnosticar** fallas intencionales en circuitos de Tinkercad y sustentar en equipo el montaje físico explicando el flujo Entrada -> Proceso -> Salida.
* **¿Para qué me sirve en la vida?** Para desarrollar criterio técnico al reparar equipos que no funcionan en lugar de adivinar cambiando piezas al azar.

## 📚 CONTENIDO Y RETO GRUPAL
* **Método de Diagnóstico (*Troubleshooting* — 5 min):**
  1. **Alimentación:** ¿hay voltaje en la fuente y están bien los polos `+` y `-`?
  2. **Continuidad/Camino:** ¿el circuito está realmente cerrado sin cables sueltos?
  3. **Polaridad y Protección:** ¿el LED o transistor está invertido? ¿la resistencia tiene el valor correcto?
* **Actividad grupal (`👥 ACTIVIDAD GRUPAL` — sin respuestas resueltas):**
  * **Parte A (Simulador):** Abrir el circuito compartido con fallas ocultas en Tinkercad, identificar al menos **3 errores** (polaridad, valor de resistencia o conexión abierta) y repararlo hasta que funcione.
  * **Parte B (Demo física):** Presentar en mesa su circuito físico `AND`/`OR` funcionando y explicar qué actúa como **Entrada**, qué realiza el **Proceso** y cuál es la **Salida**.
  * **1 Consejo:** Sigan el camino de la corriente desde el `+` de la batería hasta el `-` paso a paso usando el multímetro virtual.
* **Preguntas de verificación:** ¿Cuál es el primer paso lógico antes de cambiar un componente que no enciende?

---

# 7. Refuerzo Final, Puente a Arduino (10mo) y Autoevaluación (`🛠️ REFUERZO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Comparar** el control analógico con transistor frente a un sistema programable y consolidar los aprendizajes del parcial antes de pasar a 10mo EGB.
* **¿Para qué me sirve en la vida?** Para comprender por qué existen los microcontroladores (como Arduino) y cuándo conviene usar electrónica fija vs. lógica programada.

## 📚 CONTENIDO, COMPARATIVA Y AUTOEVALUACIÓN LIKERT (1 AL 5)
* **Puente directo a 10mo EGB (*Transistor automático vs. Arduino* — 10 min):**
  * Con el **transistor + LDR** (9no), si queremos que la luz parpadee o espere 5 segundos antes de apagarse, tenemos que cambiar piezas físicas y volver a cablear.
  * Con un **microcontrolador programable** (10mo), el cableado se simplifica y el comportamiento se cambia escribiendo líneas de código (`if/else`, tiempos, contadores).
* **Actividad de cierre (`🛠️ REFUERZO`):** Completar la tabla comparativa *"Electrónica fija (Transistor) vs. Electrónica programable (Microcontrolador)"*, ordenar e inventariar los cables caimán/componentes del taller y responder el repaso rápido.
* **Autoevaluación Escala de Likert (1 = Todavía me cuesta | 3 = Lo entiendo con ayuda | 5 = Lo domino y lo puedo explicar):**
  1. Leer el código de colores de una resistencia de 4 bandas y respetar la polaridad del LED.
  2. Construir e interpretar circuitos lógicos `AND` y `OR` con sus tablas de verdad (`0/1`).
  3. Explicar cómo varían el potenciómetro, la LDR y cómo actúa un transistor NPN como interruptor automático.
  4. Diagnosticar fallas comunes en un circuito y explicar el modelo Entrada -> Proceso -> Salida.
