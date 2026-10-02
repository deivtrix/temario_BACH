# 📘 3RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 3: EL TRANSISTOR BJT COMO INTERRUPTOR)

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** el principio de conmutación electrónica en semiconductores mediante el diseño y simulación en Tinkercad Circuits de un circuito con **Transistor NPN**, pulsador y diodo LED, **identificando** los estados de corte y saturación, y **sintetizar** los fundamentos en un informe técnico en Google Docs con rúbrica estándar.

* **Duración:** 45 Minutos  
* **Modalidad:** 💻 100% Virtual en Computadoras.  
* **Software:** [Autodesk Tinkercad Circuits](https://www.tinkercad.com/).  
* **Componentes Virtuales:** 1 Transistor NPN (BJT 2N2222), 1 Pulsador (Pushbutton), 1 Resistencia de Base ($1\ \text{k}\Omega$), 1 Resistencia de Colector ($330\ \Omega$), 1 Diodo LED, Fuente de alimentación de $5\text{V}$ (o placa Arduino para tomar $5\text{V}$ y $\text{GND}$) y Protoboard virtual.  
* **Entregable:** Informe en Google Docs (Captura del circuito en simulación activa + Diagrama/Componentes + 2 Preguntas reflexivas) subido a Google Classroom.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

1. **🎯 Motivación y Enfoque Industrial (00 - 05 min):**  
   * *"Chicos, la semana pasada analizamos los transistores como el componente más importante del siglo XX. Hoy resolveremos el circuito práctico pendiente: utilizaremos un transistor NPN como una 'llave de paso' o interruptor electrónico controlado por una mínima señal de corriente."*

2. **💡 Principio de Conmutación: Corte y Saturación (05 - 15 min):**  
   * El docente proyecta los 3 terminales del transistor BJT:
     * **B (Base):** El gatillo de control. Si no entra corriente por aquí, no pasa nada.
     * **C (Colector):** Por donde entra la corriente principal hacia el circuito de carga (LED).
     * **E (Emisor):** Por donde sale la corriente hacia la tierra ($\text{GND}$).
   * **Los dos estados de trabajo:**
     * **1. Estado de CORTE ($I_B = 0$):** Interruptor abierto. Resistencia infinita. El LED está 100% apagado.
     * **2. Estado de SATURACIÓN ($I_B > 0$):** Interruptor cerrado. El transistor conduce al máximo entre Colector y Emisor. El LED se enciende intensamente.

3. **💻 Armado Virtual en Tinkercad Circuits (15 - 35 min):**  
   * **Paso 1 (Circuito de Potencia / Colector):**
     * Conectar $+5\text{V}$ al ánodo del LED a través de la resistencia de $330\ \Omega$.
     * Conectar el cátodo del LED al pin **Colector** del transistor NPN.
     * Conectar el pin **Emisor** directo a $\text{GND}$ (Tierra).
   * **Paso 2 (Circuito de Control / Base):**
     * Conectar un terminal del pulsador a $+5\text{V}$.
     * Conectar el otro terminal del pulsador a la resistencia de $1\ \text{k}\Omega$, y de ahí directo a la **Base** del transistor.
   * **Paso 3 (Simulación y Verificación):**
     * Clic en *Iniciar Simulación*. El LED debe permanecer apagado.
     * Al hacer clic sostenido sobre el pulsador virtual, el LED se enciende de inmediato. Al soltarlo, se apaga.
     * Tomar captura de pantalla de la simulación activa.

4. **📝 Redacción del Informe y Entrega en Classroom (35 - 45 min):**  
   * Los estudiantes abren la [Plantilla de Informe Anti-IA](file:///C:/Users/Master_Lab2_DavidC/Documents/LEV/temario_BACH/03_PLANIFICACION_SEMANAL/SEMANA_03/3RO_BGU_PLANTILLA_INFORME_TRANSISTOR_SWITCH.md), pegan su captura con la Nota Virtual, registran sus componentes y responden las 2 preguntas vivenciales.

---

### 📌 2 PREGUNTAS REFLEXIVAS VIVENCIALES (ANTI-IA)

1. **Pregunta 1 (Prueba de desconexión en vivo):** Con la simulación iniciada, mantén presionado el botón (LED encendido) y borra el cable que conecta la resistencia con la Base del transistor. ¿Qué le ocurre al LED inmediatamente en tu pantalla y qué estado del transistor se activó al perder la corriente de base?
2. **Pregunta 2 (Prueba de sobrecorriente y daño en Tinkercad):** Haz esta prueba destructiva en Tinkercad: Quita la resistencia de la Base y conecta un cable directo desde el pulsador (5V) a la Base del transistor. Al presionar el botón, ¿qué símbolo de explosión o advertencia saca Tinkercad sobre el transistor y por qué la base se destruye sin resistencia?

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM

```text
TÍTULO: Informe Técnico: El Transistor BJT como Interruptor Electrónico (Tinkercad)

INSTRUCCIONES:
Estimados estudiantes, en esta sesión validamos el funcionamiento del transistor NPN como interruptor de estado sólido en Tinkercad Circuits. Cada estudiante debe presentar su informe individual en Google Docs utilizando la plantilla oficial del curso.

🔒 REGLA ANTI-IA: Prohibido usar definiciones de enciclopedia sacadas de ChatGPT. Las preguntas evalúan las pruebas de conmutación y sobrecarga en tu circuito virtual.

Tu informe debe contener obligatoriamente:
1. Captura de pantalla completa y nítida de tu circuito en Tinkercad Circuits simulando con la NOTA VIRTUAL de tu nombre sobre el protoboard.
2. Parámetros reales de tus componentes (colores y valores en Ohmios).
3. Respuestas en máximo 3 líneas a las dos preguntas reflexivas sobre desconexión de Base y prueba destructiva.

RÚBRICA DE CALIFICACIÓN (Total: 10 Puntos):
- Captura con circuito simulando y Nota Virtual personalizada: 2.5 pts
- Parámetros reales registrados desde su simulador: 2.5 pts
- Pregunta 1 respondida comprobando la desconexión de Base: 2.5 pts
- Pregunta 2 respondida ejecutando la prueba de sobrecorriente: 2.5 pts
```
