# 📘 1RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 2)

**Propósito de la Clase:**  
> **Analizar** la optimización de memoria y conmutación de salidas digitales mediante la declaración de tipos de datos (`int`, `unsigned int`, `bool`) y valores lógicos (`true`/`false`) en la simulación de una sirena de policía con LEDs en Tinkercad.

---

### ⏱️ DESGLOSE DE CLASE (45 MINUTOS)

1. **🎯 Motivación y Presentación de Diapositivas (00 - 10 min):**
   * Diapositivas 1 a 5 de `PRESENTACION_1RO_BGU_ARDUINO_MOD2.pdf`.
   * Introducción a tipos de variables (`int`, `unsigned int`, `bool`) y equivalencias de memoria (Diapositivas 4 y 5: `HIGH = 1 = true`, `LOW = 0 = false`).

2. **💻 Paso 1: El Código Simple (Todas prenden juntas):**
   * El docente muestra el código directo donde todo parpadea al mismo tiempo:
   ```cpp
   void setup() {
     pinMode(6, OUTPUT);
     pinMode(7, OUTPUT);
     pinMode(12, OUTPUT);
     pinMode(13, OUTPUT);
   }

   void loop() {
     digitalWrite(6, HIGH);
     digitalWrite(7, HIGH);
     digitalWrite(12, HIGH);
     digitalWrite(13, HIGH);
     delay(500);

     digitalWrite(6, LOW);
     digitalWrite(7, LOW);
     digitalWrite(12, LOW);
     digitalWrite(13, LOW);
     delay(500);
   }
   ```

3. **🧠 Paso 2: Tu Explicación (Usar `true` y `false` con nombres):**
   * El docente muestra cómo reemplazar `HIGH/LOW` por variables sencillas:
   ```cpp
   int rojo = 6;
   int azul = 12;
   bool si = true;
   bool no = false;

   void setup() {
     pinMode(rojo, OUTPUT);
     pinMode(azul, OUTPUT);
   }
   ```

4. **🚀 Paso 3: Código Final del Reto (Focos LEDs de Sirena de Policía):**
   * Explicación a los alumnos: *"Simularemos la sirena de un patrullero de policía: los 2 focos LEDs rojos (pines 6 y 7) se encienden juntos mientras los 2 focos LEDs azules (pines 12 y 13) se apagan; luego se invierten."*
   ```cpp
   void loop() {
     // Focos LEDs Rojos prendidos (true), Focos LEDs Azules apagados (false)
     digitalWrite(6, true);
     digitalWrite(7, true);
     digitalWrite(12, false);
     digitalWrite(13, false);
     delay(500);

     // Focos LEDs Rojos apagados (false), Focos LEDs Azules prendidos (true)
     digitalWrite(6, false);
     digitalWrite(7, false);
     digitalWrite(12, true);
     digitalWrite(13, true);
     delay(500);
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

