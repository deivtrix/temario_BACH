# 📋 PLANIFICACIÓN DE CLASE 1: 2DO BGU — PRINCIPIO DEL PUENTE H Y CONTROL BIDIRECCIONAL DE MOTORES DC

* **Curso:** 2do BGU
* **Tema:** Inversión de Polaridad, Circuito en Puente H Discreto (Transistores Q1-Q4) y Drivers de Potencia Móvil
* **Modalidad:** 💻 100% Práctico en Simulador PC (`tinkercad.com` - Circuits)
* **Duración:** 45 Minutos
* **PDF Guía Base:** `CA.1.RB.4.NV.26-27.pdf` / `FABRICACION.gslides.pdf` (Diapositivas 1 a 5)

---

## 🧭 SECCIÓN 1: CONEXIÓN PUD Y MATRIZ DE LOGRO

* **Competencia Medida:** `CE.CN.B.5.10` (Diseñar y evaluar sistemas de control de potencia y conmutación de motores para robótica móvil).
* **Eje Afectivo (A2 - Compromiso):** Demuestra prudencia y responsabilidad en la configuración de circuitos de potencia evitando cortocircuitos por falso enclavamiento. *Cualidad LEV: Cuidadoso / Riguroso*.
* **Eje Cognitivo (C3 - Análisis):** Comprende el principio de la inversión de corriente a través de la topología en Puente H y la lógica de conmutación por transistores en diagonal.
* **Eje Praxitivo (P3 - Aplicación):** Modela un circuito de Puente H en Tinkercad Circuits controlando el sentido de giro horario (CW) y antihorario (CCW) de un motor DC mediante interruptores de control.

---

## 🎯 SECCIÓN 2: CONEXIÓN INICIAL Y PROPÓSITO LEV

### 1. ¿Para qué me servirá aprender esto?
Para descubrir cómo los carros a control remoto y los vehículos reales logran ir hacia adelante y poner marcha atrás sin necesidad de desconectar ni cambiar cables con la mano.

### 2. PROPÓSITO DE LA CLASE:
🏎️ **"Construir un circuito de Puente H en el simulador para hacer que un motor cambie de giro hacia adelante y en reversa."**

### 3. CONEXIÓN REAL E INTERDISCIPLINAR:
* 🔗 **Vida Real:** Al poner la palanca de cambios en "R" (Reversa) en un carro real, un circuito en Puente H invierte la corriente del motor.
* 📚 **Interdisciplinar:** Física (Electromagnetismo) + Robótica Móvil.

### 4. PREGUNTAS DE VERIFICACIÓN DEL PROPÓSITO (Espejo Literal):
* *Pregunta 1:* ¿Qué vamos a lograr hoy con el motor DC?  
  *👉 Respuesta esperada:* Hacerlo girar hacia adelante y en marcha atrás.
* *Pregunta 2:* ¿Cómo se llama el circuito de 4 interruptores que nos permite este cambio?  
  *👉 Respuesta esperada:* El circuito en Puente H.
* *Pregunta 3 (De oro):* ¿Qué pasa si activas los dos interruptores del mismo lado vertical a la vez?  
  *👉 Respuesta esperada:* Ocurre un cortocircuito.

---

## 📋 SECCIÓN 3: ESTRUCTURA DE LA PLANIFICACIÓN (45 MINUTOS)

> **REGLA LEV:** Máximo 10 Minutos de Teoría / Mínimo 25 Minutos de Práctica Activa.

### 1. Motivación (00-05 min) — El Misterio de la Marcha Atrás
* Muestra un carrito de juguete a control remoto y hazlo andar hacia adelante y luego en reversa: *"¿Cómo hace el motor de las ruedas para cambiar de sentido al instante sin que un humano entre a dar la vuelta a la batería?"*

### 2. Encuadre (05-07 min) — Reglas de Seguridad en Electrónica de Potencia
* **Norma 1:** NUNCA activar los dos interruptores del mismo lado vertical a la vez para evitar cortocircuitos directos en la batería.
* **Plataforma:** Abrir Tinkercad Circuits $\rightarrow$ Crear Nuevo Circuito.

### 3. Enunciación (07-15 min — TEORÍA 8 MINUTOS MAX)
* **Demostración en Pantalla con Diapositivas 1-5 (`FABRICACION.gslides.pdf`):**
  * **Motor DC y Polaridad:**
    * VCC (+) a Pin A y GND (-) a Pin B $\rightarrow$ Giro Horario (CW / RPM Positivas).
    * VCC (+) a Pin B y GND (-) a Pin A $\rightarrow$ Giro Antihorario (CCW / RPM Negativas).
  * **Esquema del Puente H:**
    ```
            +VCC (9V)
           /         \
         [Q1]       [Q3]
          |---MOTOR---|
         [Q2]       [Q4]
           \         /
             GND (0V)
    ```
  * **Lógica de Conmutación:**
    * **Avanzar (CW):** Activar Q1 y Q4 (Diagonal 1).
    * **Retroceder (CCW):** Activar Q3 y Q2 (Diagonal 2).
    * **Cortocircuito (Prohibido):** Activar Q1 y Q2 a la vez.

### 4. Simulación / Práctica Intensiva (15-40 min — 25 MINUTOS) — RETO PUENTE H EN TINKERCAD

* **PASO 1 (Montaje de Componentes):**
  1. Arrastra 1 **Motor DC de aficionado**, 1 **Batería de 9V** y 4 **Interruptores SPDT** (o transistores NPN) simulando el esquema de Puente H.
  2. Realiza las conexiones de las diagonales $Q1-Q4$ y $Q3-Q2$.

* **PASO 2 (Simulación de Marcha Adelante - CW):**
  1. Activar la diagonal 1 (Interruptor 1 e Interruptor 4 en ON).
  2. Hacer clic en **Iniciar Simulación**.
  3. Observar la lectura del tacómetro virtual del motor: Deberá marcar aproximadante $+17,500\text{ RPM}$ (Giro Horario).

* **PASO 3 (Simulación de Marcha Atrás - CCW):**
  1. Desactivar la diagonal 1.
  2. Activar la diagonal 2 (Interruptor 3 e Interruptor 2 en ON).
  3. Observar la lectura del tacómetro virtual del motor: Deberá marcar $-17,500\text{ RPM}$ (Giro Antihorario).

### 5. Cierre y Entregable (40-45 min)
* Comprobación en pantalla con el docente del cambio de RPM de valor positivo a negativo.

---

## 🛠️ SECCIÓN 4: RECURSOS Y CHECKLIST DOCENTE

### Recursos Digitales y Físicos:
* Laptops/PCs de laboratorio.
* Tinkercad Circuits.
* PDF Guía: `FABRICACION.gslides.pdf` / `CA.1.RB.4.NV.26-27.pdf`.

### Checklist de Prueba Docente (Hacer antes de la clase):
* [x] Probar en Tinkercad Circuits la simulación del Puente H con el motor DC.
* [x] Comprobar que los estudiantes distingan entre valores de RPM positivos y negativos en la animación.
* [x] Explicar que en la siguiente clase este circuito se reemplazará por el chip integrado L298N / L293D.

---

## 📝 SECCIÓN 5: LISTA DE COTEJO DEL ENTREGABLE

| Criterio de Evaluación | Cumple (1.0) | En Proceso (0.5) | No Cumple (0.0) | Observaciones |
| :--- | :---: | :---: | :---: | :--- |
| **1. Esquema del Puente H:** Cableado correcto de los 4 conmutadores/transistores en forma de H. | | | | |
| **2. Giro Horario (CW):** Obtención de RPM positivas al activar la diagonal $Q1-Q4$. | | | | |
| **3. Giro Antihorario (CCW):** Obtención de RPM negativas al activar la diagonal $Q3-Q2$. | | | | |
| **4. Análisis de Seguridad:** Explicación correcta de por qué no se deben activar conmutadores verticales en paralelo. | | | | |

**Producto Final:** Captura de pantalla o circuito funcional simulado en Tinkercad demostrando el cambio de giro del motor DC en RPMs.
