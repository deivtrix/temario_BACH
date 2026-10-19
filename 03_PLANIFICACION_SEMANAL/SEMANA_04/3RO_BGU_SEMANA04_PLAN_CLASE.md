# 📘 3RO BGU — PLAN DE CLASE PRÁCTICO (SEMANA 4)
## ⚡ ETAPA DE POTENCIA: ACCIONAMIENTO DE MOTOR DC CON TRANSISTOR NPN Y DIODO FLYBACK (FÍSICO O SIMULADOR)

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** mediante la experimentación de circuitos de potencia la necesidad de desacoplar el control lógico de cargas inductivas de alta corriente (motores DC), **conectar** un transistor bipolar NPN (2N2222 o TIP120) como interruptor de potencia con un diodo volante (*Flyback* 1N4007) de protección, y **comprobar** el giro del motor y la absorción de picos inductivos.

* **Curso:** 3ro BGU  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 🛠️ **100% PRÁCTICA ACTIVA (Montaje Físico en Protoboard o Tinkercad Circuits en PC)**.  
* **Docente:** Ing. David Castro T.  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** La semana anterior ya se entregó el informe teórico de TBJ; hoy la calificación es 100% formativa en mesa/pantalla viendo girar el motor con su protección.

---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 3 ➔ SEMANA 4)
* **Semana 3 (TBJ con LED):** Se completó y entregó el informe técnico del transistor NPN como interruptor de un foco LED.
* **Semana 4 (Hoy):** *"Ya terminamos el informe de TBJ la semana pasada; hoy nos metemos de lleno a la **robótica de potencia**. Conectaremos un **Motor DC real**: una carga que consume mucha corriente y que exige sí o sí una etapa de potencia y un diodo de protección para no quemar el circuito."*

---

### 🛠️ DOS OPCIONES DE EJECUCIÓN PRÁCTICA

#### 🟢 OPCIÓN A: MONTAJE FÍSICO EN MESA DE TALLER
* **Componentes por puesto:** 1 Transistor NPN (2N2222, TIP120 o equivalente), 1 Motor DC de $5\text{V}$ a $9\text{V}$, 1 Diodo rectificador 1N4007, 1 Pulsador, 1 Resistencia de $1\ \text{k}\Omega$, Batería de $9\text{V}$ o fuente de taller, protoboard y cables.
* **Pasos de Conexión en Protoboard:**
  1. Alimentar rieles de la protoboard ($+9\text{V}$ y GND).
  2. Terminal positivo del motor al riel $+9\text{V}$.
  3. Terminal negativo del motor al pin **Colector (C)** del transistor.
  4. Pin **Emisor (E)** del transistor directo al riel negativo (GND).
  5. **Diodo Flyback 1N4007 en antiparalelo con el motor:** Cátodo (franja plateada) hacia $+9\text{V}$, Ánodo hacia el Colector.
  6. **Disparo en Base:** Desde $+9\text{V} \rightarrow$ Pulsador $\rightarrow$ Resistencia de $1\ \text{k}\Omega \rightarrow$ Pin **Base (B)** del transistor.

#### 💻 OPCIÓN B: SIMULACIÓN EN TINKERCAD CIRCUITS
* Armar exactamente el mismo circuito en pantalla con el motor de aficionado de Tinkercad. Al darle simular y oprimir el pulsador, el tacómetro virtual muestra las RPM en giro instantáneo.

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (100% DE ACCIÓN)

1. **🎯 Demostración de Arranque en Pizarra (00 - 10 min):**
   * ¿Por qué no conectar el motor directo a un botón o chip pequeño? Porque el motor jala hasta $500\text{ mA}$ (el músculo) y el chip solo da $20\text{ mA}$ (el cerebro).
   * ¿Para qué sirve el diodo 1N4007 al revés? Para absorber la patada inductiva de alto voltaje cuando el motor se apaga de golpe.
2. **🛠️ Armado Práctico en Parejas (10 - 32 min):**
   * Los alumnos realizan las conexiones físicas en protoboard o virtuales en Tinkercad.
   * Verificación obligatoria de las 3 patitas del transistor (Base, Colector, Emisor) y la orientación de la franja del diodo 1N4007.
3. **🚀 Prueba de Potencia y Marcha (32 - 40 min):**
   * Presionar el botón: el motor arranca con fuerza a altas RPM.
   * Soltar el botón: el motor frena con suavidad sin generar chispas ni recalentamiento en el transistor gracias al diodo.
4. **✅ Calificación Formativa en Vivo (40 - 45 min):**
   * El docente pasa por los puestos y verifica el funcionamiento del motor accionado por el transistor (10/10 en planilla).

---

### 📢 TEXTO RÁPIDO PARA GOOGLE CLASSROOM (REGISTRO FORMATIVO)

```text
TÍTULO: Práctica N° 4: Etapa de Potencia con Transistor NPN y Protección Flyback para Motor DC

INSTRUCCIONES:
Estimados estudiantes, en esta sesión comprobamos en la práctica el control de cargas de alta corriente:

📌 EVIDENCIA DE CLASE (Sin informe escrito):
- Práctica en mesa física: Verificación y calificación formativa directa en tu mesa de trabajo con el profesor.
- Práctica en Tinkercad Circuits: Sube 1 captura de pantalla del circuito con el botón presionado y el motor girando a RPM activas.

* Calificación: 10 Puntos registrados en el laboratorio de robótica.
```
