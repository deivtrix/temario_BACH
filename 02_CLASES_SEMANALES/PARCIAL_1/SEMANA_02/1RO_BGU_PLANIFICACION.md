# 📘 1RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 2)

**Propósito de la Clase:**  
> **Analizar** la optimización de memoria y conmutación de salidas digitales mediante la declaración de tipos de datos (`int`, `unsigned int`, `bool`) y valores lógicos (`true`/`false`) en la simulación de una sirena de policía con LEDs en Tinkercad.

---

### ⏱️ DESGLOSE DE CLASE (45 MINUTOS)

1. **🎯 Motivación y Presentación de Diapositivas (00 - 10 min):**
   * Diapositivas 1 a 5 de `PRESENTACION_1RO_BGU_ARDUINO_MOD2.pdf`.
   * Introducción a tipos de variables (`int`, `unsigned int`, `bool`) y equivalencias de memoria (Diapositivas 4 y 5: `HIGH = 1 = true`, `LOW = 0 = false`).

2. **💻 Paso 1: El Código Base / Novato (Todas prenden juntas, sin variables):**
   * El docente muestra el código rústico directo donde todo parpadea al mismo tiempo con números fijos:
   ```cpp
   // ==========================================
   // PASO 1: CÓDIGO BASE (NOVATO)
   // Todo parpadea al mismo tiempo, sin variables
   // ==========================================

   void setup() {
     pinMode(6, OUTPUT);
     pinMode(7, OUTPUT);
     pinMode(12, OUTPUT);
     pinMode(13, OUTPUT);
   }

   void loop() {
     // Todos los LEDs se encienden
     digitalWrite(6, HIGH);
     digitalWrite(7, HIGH);
     digitalWrite(12, HIGH);
     digitalWrite(13, HIGH);
     delay(500);

     // Todos los LEDs se apagan
     digitalWrite(6, LOW);
     digitalWrite(7, LOW);
     digitalWrite(12, LOW);
     digitalWrite(13, LOW);
     delay(500);
   }
   ```

3. **🧠 Paso 2: Explicación del Docente (Variables de pines y booleanos `true`/`false`):**
   * El docente explica cómo optimizar la memoria y la legibilidad: se definen nombres para los pines con `int` y estados lógicos con `bool`:
   ```cpp
   // ==========================================
   // PASO 2: EXPLICACIÓN Y REFACTORIZACIÓN
   // Código completo usando variables legibles y booleanos
   // ==========================================

   // Definición de pines para los 4 LEDs
   int rojo1 = 6;
   int rojo2 = 7;
   int azul1 = 12;
   int azul2 = 13;

   // Variables booleanas para estados lógicos (1 bit)
   bool encendido = true;  // true equivale a HIGH o 1
   bool apagado = false;   // false equivale a LOW o 0

   void setup() {
     pinMode(rojo1, OUTPUT);
     pinMode(rojo2, OUTPUT);
     pinMode(azul1, OUTPUT);
     pinMode(azul2, OUTPUT);
   }

   void loop() {
     // Demostración: encendemos todos usando las variables
     digitalWrite(rojo1, encendido);
     digitalWrite(rojo2, encendido);
     digitalWrite(azul1, encendido);
     digitalWrite(azul2, encendido);
     delay(500);

     // Apagamos todos usando las variables
     digitalWrite(rojo1, apagado);
     digitalWrite(rojo2, apagado);
     digitalWrite(azul1, apagado);
     digitalWrite(azul2, apagado);
     delay(500);
   }
   ```

4. **🚀 Paso 3: Reto Autónomo de Estudiantes (Focos LEDs de Sirena de Policía):**
   * Explicación a los alumnos: *"Simularemos la sirena de un patrullero de policía: los 2 focos LEDs rojos (pines 6 y 7) se encienden juntos mientras los 2 focos LEDs azules (pines 12 y 13) se apagan; luego se invierten a ritmo rápido de sirena."*
   ```cpp
   // ==========================================
   // PASO 3: RETO FINAL COMPLETO (SIRENA DE POLICÍA)
   // Código 100% funcional y listo para Tinkercad Circuits
   // ==========================================

   // Pines de los LEDs Rojos
   int rojo1 = 6;
   int rojo2 = 7;

   // Pines de los LEDs Azules
   int azul1 = 12;
   int azul2 = 13;

   // Variables lógicas de control booleano
   bool encendido = true;  // Luz activa
   bool apagado = false;   // Luz inactiva

   void setup() {
     // Configuración de los 4 pines como salidas digitales
     pinMode(rojo1, OUTPUT);
     pinMode(rojo2, OUTPUT);
     pinMode(azul1, OUTPUT);
     pinMode(azul2, OUTPUT);
   }

   void loop() {
     // FASE 1: Destello Rojo (Rojos prendidos, Azules apagados)
     digitalWrite(rojo1, encendido);
     digitalWrite(rojo2, encendido);
     digitalWrite(azul1, apagado);
     digitalWrite(azul2, apagado);
     delay(300); // Ritmo de sirena policial

     // FASE 2: Destello Azul (Rojos apagados, Azules prendidos)
     digitalWrite(rojo1, apagado);
     digitalWrite(rojo2, apagado);
     digitalWrite(azul1, encendido);
     digitalWrite(azul2, encendido);
     delay(300); // Ritmo de sirena policial
   }
   ```




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

