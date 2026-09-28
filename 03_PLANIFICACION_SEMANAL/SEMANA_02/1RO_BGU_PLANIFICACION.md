# 📘 1RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 2)

**Propósito de la Clase:**  
> **Analizar** la optimización de memoria y conmutación de salidas digitales mediante la declaración de tipos de datos (`int`, `unsigned int`, `bool`) y valores lógicos (`true`/`false`) en la simulación de una sirena de policía con LEDs en Tinkercad.

---

### ⏱️ DESGLOSE DE CLASE (45 MINUTOS)

1. **🎯 Motivación y Presentación de Diapositivas (00 - 10 min):**
   * Diapositivas 1 a 5 de `PRESENTACION_1RO_BGU_ARDUINO_MOD2.pdf`.
   * Introducción a tipos de variables (`int`, `unsigned int`, `bool`) y equivalencias de memoria (Diapositivas 4 y 5: `HIGH = 1 = true`, `LOW = 0 = false`).

2. **💻 Paso 1: Demostración con Código Base Novato (10 - 18 min):**
   * El docente proyecta un código "simple" donde todas las luces parpadean juntas sin variables (Pines 6, 7, 12, 13 como la diapositiva):
   ```cpp
   void setup() {
     pinMode(6, OUTPUT);  // Rojo 1
     pinMode(7, OUTPUT);  // Rojo 2
     pinMode(12, OUTPUT); // Azul 1
     pinMode(13, OUTPUT); // Azul 2
   }
   void loop() {
     digitalWrite(6, HIGH); digitalWrite(7, HIGH); digitalWrite(12, HIGH); digitalWrite(13, HIGH);
     delay(500);
     digitalWrite(6, LOW); digitalWrite(7, LOW); digitalWrite(12, LOW); digitalWrite(13, LOW);
     delay(500);
   }
   ```

3. **🧠 Paso 2: Explicación y Refactorización del Docente (18 - 25 min):**
   * El docente transforma el código aplicando variables `bool` e `int` profesionales:
   ```cpp
   int rojo1 = 6, rojo2 = 7;
   int azul1 = 12, azul2 = 13;
   bool prendido = true;
   bool apagado = false;

   void setup() {
     pinMode(rojo1, OUTPUT); pinMode(rojo2, OUTPUT);
     pinMode(azul1, OUTPUT); pinMode(azul2, OUTPUT);
   }
   ```

4. **🚀 Paso 3: Reto Autónomo de Estudiantes (25 - 40 min):**
   * **Actividad N°3 (Diapositivas 6 y 7):** Modificar el `void loop()` por sí mismos usando las variables `prendido` y `apagado` para alternar la **Sirena de Policía**:
     * *Fase 1:* 2 Rojos en `prendido` (Pines 6 y 7) y 2 Azules en `apagado` (Pines 12 y 13).
     * *Fase 2:* 2 Rojos en `apagado` y 2 Azules en `prendido`.


5. **📝 Evaluación Directa (40 - 45 min):** Captura del circuito y código en Google Classroom / revisión en pantalla.

---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 1 $\rightarrow$ SEMANA 2)
* **Semana 1:** Manejo básico de circuito digital y parpadeo simple (`digitalWrite`, `delay`).
* **Semana 2:** *"Hoy pasamos a la programación estructurada usando variables booleanas y nombres de pines para simular sistemas reales."*

---

### 🔮 ¿QUÉ VEREMOS LA PRÓXIMA CLASE? (SEMANA 3)
* **Tema a Futuro:** Lectura de **Entradas Digitales** con pulsadores en modo `Pull-Up` (`digitalRead`).

---

### 📦 MATERIALES Y PERMISOS PARA LA PRÓXIMA CLASE (SEMANA 3)
> 📢 **AVISO A ESTUDIANTES:**  
> 💻 **Sin material físico extra.** Continuación en Tinkercad Circuits.

