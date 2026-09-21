# 📋 PLANIFICACIÓN DE CLASE 1: 3RO BGU — SENSOR DE NIVEL DE AGUA ANALÓGICO, CONDUCTIVIDAD Y MAPEO DE DATOS

* **Curso:** 3ro BGU
* **Tema:** Sensores Resistivos Analógicos, Conductividad de Líquidos, Conversión ADC (0-1023) y Función `map()` en Arduino C++
* **Modalidad:** 💻 100% Práctico en Simulador PC (`tinkercad.com` - Circuits / Potenciómetro como simulador de Sensor de Agua A0)
* **Duración:** 45 Minutos
* **PDF Guía Base:** `CA.2.RB.5.SG.26-27(Ard mod4).pdf` (Diapositivas 1 a 5)

---

## 🧭 SECCIÓN 1: CONEXIÓN PUD Y MATRIZ DE LOGRO

* **Competencia Medida:** `CE.CN.B.5.11` (Integrar sensores analógicos industriales con algoritmos de conversión de datos para proyectos de titulación y automatización).
* **Eje Afectivo (A2 - Compromiso):** Demuestra iniciativa y visión de innovación tecnológica aplicada a la resolución de problemas ambientales e industriales del entorno. *Cualidad LEV: Innovador / Proactivo*.
* **Eje Cognitivo (C3 - Análisis):** Comprende la variación de resistencia eléctrica por conductividad de un líquido, la conversión analógico-digital (ADC de 10 bits de $0$ a $1023$) y la traslación de rangos numéricos mediante la función `map()`.
* **Eje Praxitivo (P3 - Aplicación):** Desarrolla un programa en C++ para Arduino que lea el pin analógico A0, escale los valores de $0-1023$ a porcentaje de $0\%-100\%$ de agua, y presente un indicador gráfico en el Monitor Serial.

---

## 🎯 SECCIÓN 2: CONEXIÓN INICIAL Y PROPÓSITO LEV

### 1. ¿Para qué me servirá aprender esto?
Para crear sistemas inteligentes como tanques de agua automáticos que nunca se derraman, y aprender a leer cualquier sensor para tu proyecto final de grado.

### 2. PROPÓSITO DE LA CLASE:
🚰 **"Programar un sensor de nivel de agua en Arduino para convertir sus lecturas en porcentaje de 0% a 100% y dar una alerta si se llena el tanque."**

### 3. CONEXIÓN REAL E INTERDISCIPLINAR:
* 🔗 **Vida Real:** Es exactamente como sabe una lavadora inteligente en tu casa cuánta agua tiene antes de empezar a lavar.
* 📚 **Interdisciplinar:** Química (Conductividad del agua) + Matemática (Escalamiento con la función `map`).

### 4. PREGUNTAS DE VERIFICACIÓN DEL PROPÓSITO (Espejo Literal):
* *Pregunta 1:* ¿Qué vamos a medir y calcular hoy?  
  *👉 Respuesta esperada:* El nivel de agua de un tanque de 0% a 100%.
* *Pregunta 2:* ¿En qué puerto del Arduino conectamos los sensores analógicos?  
  *👉 Respuesta esperada:* En el puerto A0.
* *Pregunta 3 (De oro):* ¿Qué función mágica en C++ transforma el rango 0-1023 a porcentaje 0-100%?  
  *👉 Respuesta esperada:* La función `map()`.

---

## 📋 SECCIÓN 3: ESTRUCTURA DE LA PLANIFICACIÓN (45 MINUTOS)

> **REGLA LEV:** Máximo 10 Minutos de Teoría / Mínimo 25 Minutos de Práctica Activa.

### 1. Motivación (00-05 min) — El Caso del Tanque Derramado
* Muestra el sensor de nivel de agua del Kit Elegoo (placa roja con trazas metálicas expuestas) y pregunta: *"¿Cómo puede un circuito electrónico medir el agua sin romperse y evitar que el tanque de agua del colegio se derrame al llenarse?"*

### 2. Encuadre (05-07 min) — Protocolo de Sensórica Analógica
* **Norma 1:** Utilizar el divisor de tensión o potenciómetro analógico en el puerto A0 de Tinkercad.
* **Plataforma:** Abrir Tinkercad Circuits con la tarjeta Arduino UNO en modo C++ Texto.

### 3. Enunciación (07-15 min — TEORÍA 8 MINUTOS MAX)
* **Demostración en Pantalla con Diapositivas 1-5 (`CA.2.RB.5.SG.26-27(Ard mod4).pdf`):**
  * **Conductividad del Agua:** El agua con sales minerales actúa como una resistencia variable. A mayor nivel de inmersión, más trazas de cobre conduce $\rightarrow$ Mayor voltaje hacia A0.
  * **Convertidor ADC (Analog-to-Digital Converter):**
    * $0\text{V} \rightarrow 0$ en código.
    * $5\text{V} \rightarrow 1023$ en código.
  * **La Función de Escalamiento Lineal `map()`:**
    ```cpp
    int porcentaje = map(valorAnalogo, 0, 1023, 0, 100);
    ```

### 4. Simulación / Práctica Intensiva (15-40 min — 25 MINUTOS) — RETO MONITOR DE NIVEL DE TANQUE 0-100%

* **PASO 1 (Conexión del Circuito):**
  1. En Tinkercad Circuits, conectar un **Potenciómetro de 10k** (simulador del sensor de nivel) al pin **A0** de la placa Arduino UNO.
  2. Conectar las patillas extremas del potenciómetro a $5\text{V}$ y $\text{GND}$.

* **PASO 2 (Escritura del Código C++ de Monitoreo de Agua):**
  ```cpp
  // PLANIFICACIÓN CLASE 1 - 3RO BGU
  // Sensor de Nivel de Agua y Mapeo ADC (0-100%)
  // Estudiante: [Nombre del Estudiante]

  int pinSensor = A0;
  int lecturaADC = 0;
  int porcentajeAgua = 0;

  void setup() {
    Serial.begin(9600); // Inicia comunicación serie
  }

  void loop() {
    // 1. Lectura del valor analógico crudo (0 - 1023)
    lecturaADC = analogRead(pinSensor);
    
    // 2. Mapeo del valor ADC a Porcentaje (0 - 100%)
    porcentajeAgua = map(lecturaADC, 0, 1023, 0, 100);

    // 3. Telemetría por Monitor Serial
    Serial.print("Lectura Cruda ADC: ");
    Serial.print(lecturaADC);
    Serial.print("  |  Nivel de Tanque: ");
    Serial.print(porcentajeAgua);
    Serial.println("%");

    // Alerta visual de tanque lleno
    if (porcentajeAgua >= 90) {
      Serial.println("  [ALERTA!] -> TANQUE CASI LLENO - APAGANDO BOMBA");
    }

    delay(500); // Muestra lecturas cada 0.5 segundos
  }
  ```

* **PASO 3 (Simulación e Interacción):**
  1. Hacer clic en **Iniciar Simulación**.
  2. Abrir el **Monitor Serie**.
  3. Mover la perilla del potenciómetro con el cursor para simular el llenado del agua y observar la conversión automática de $0\%$ a $100\%$ y la activación de la alerta.

### 5. Cierre y Entregable (40-45 min)
* Verificación en pantalla del correcto escalamiento numérico e impresión limpia en el Monitor Serial.

---

## 🛠️ SECCIÓN 4: RECURSOS Y CHECKLIST DOCENTE

### Recursos Digitales y Físicos:
* Laptops/PCs de laboratorio.
* Tinkercad Circuits / Kit Elegoo UNO R3 (Sensor de Nivel de Agua).
* PDF Guía: `CA.2.RB.5.SG.26-27(Ard mod4).pdf`.

### Checklist de Prueba Docente (Hacer antes de la clase):
* [x] Probar el escalamiento con la función `map()` en Tinkercad asegurando que el rango 0-1023 responda fluidamente.
* [x] Verificar que el Monitor Serial imprima la alerta cuando el porcentaje supere el 90%.
* [x] Tener lista la conexión física del sensor Elegoo para mostrarlo a los estudiantes en vivo.

---

## 📝 SECCIÓN 5: LISTA DE COTEJO DEL ENTREGABLE

| Criterio de Evaluación | Cumple (1.0) | En Proceso (0.5) | No Cumple (0.0) | Observaciones |
| :--- | :---: | :---: | :---: | :--- |
| **1. Lectura ADC:** Uso correcto del comando `analogRead(A0)` almacenando la variable. | | | | |
| **2. Aplicación de `map()`:** Sintaxis y parámetros correctos en `map(lectura, 0, 1023, 0, 100)`. | | | | |
| **3. Lógica de Control:** Condicional `if` funcional que emita la alerta de tanque lleno al $\ge 90\%$. | | | | |
| **4. Presentación de Datos:** Monitor Serial ordenado mostrando valor crudo vs porcentaje. | | | | |

**Producto Final:** Captura de pantalla del Monitor Serial imprimiendo la conversión analógica a porcentaje de agua ($0\%-100\%$) y la alerta de tanque lleno.
