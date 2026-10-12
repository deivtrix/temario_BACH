# 📘 1RO BGU — PLANIFICACIÓN DE CLASE (SEMANA 3)
## 🚦 TOMA DE DECISIONES CON IF - ELSE: DEL MAYOR AL PROMEDIO DE 3 NOTAS

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** la sintaxis y lógica de la sentencia `if - else` en C++, **experimentar** una primera condición comparando dos valores numéricos para encender o apagar un foco, y **resolver** el reto de cálculo del promedio de 3 notas con encendido condicional de foco Azul (Aprobado $\ge 7.0$) o foco Rojo (Reprobado) en Tinkercad Circuits.

* **Curso:** 1ro BGU  
* **Duración:** 45 Minutos  
* **Modalidad:** 💻 100% Virtual en Computadoras.  
* **Docente:** Ing. David Castro T.  
* **Plataforma:** [Autodesk Tinkercad Circuits](https://www.tinkercad.com/).  
* **Circuito:** Placa Arduino UNO, protoboard, 1 Foco LED Azul (Pin 8), 1 Foco LED Rojo (Pin 9), 2 resistencias de $220\ \Omega$ a GND.  
* **Entregable:** Informe individual de práctica en Google Classroom.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Explicación de la Sentencia IF - ELSE (00 - 10 min)
* El docente explica la estructura en la pizarra con analogías de la vida real:
  * *"Un programa normal ejecuta líneas en orden. Con un condicional, el Arduino toma un camino o el otro según si la condición es Verdadera o Falsa."*
* **Sintaxis Básica:**
  ```cpp
  if (condicion) {
    // Lo que hace si es VERDADERO
  } else {
    // Lo que hace si es FALSO (sino)
  }
  ```

---

#### 2. 💡 Ejercicio 1 Guiado: Comprobar el Mayor entre Dos Valores (10 - 20 min)
* **Objetivo rápido:** Comparar dos números. Si el primero es mayor, el foco se prende; si no, se queda apagado.
* **Código de prueba en la pizarra:**
  ```cpp
  const int foco = 8;
  int valorA = 10;
  int valorB = 4;

  void setup() {
    pinMode(foco, OUTPUT);
  }

  void loop() {
    // Si valorA es mayor que valorB, prende el foco
    if (valorA > valorB) {
      digitalWrite(foco, HIGH);
    } else {
      digitalWrite(foco, LOW); // Sino, se queda apagado
    }
  }
  ```
* **Dinámica en vivo:** Los estudiantes cambian `valorA = 2;` y comprueban que el foco inmediatamente se queda apagado al no cumplirse la condición.

---

#### 3. 🚀 Reto Principal: Promedio de 3 Notas (Foco Azul vs Foco Rojo) (20 - 35 min)
* **Misión de los estudiantes:**
  1. Conectar dos focos en Tinkercad: **Foco Azul** en Pin 8 y **Foco Rojo** en Pin 9.
  2. Declarar 3 notas con decimales (`float`).
  3. Calcular el promedio sumando las 3 notas y dividiendo para 3.
  4. Aplicar la regla:
     * Si el promedio es mayor o igual a 7.0 ($\ge 7.0$): **se prende el foco Azul** (Aprobado) y el Rojo queda apagado.
     * Si no (`else`): **se prende el foco Rojo** (Reprobado) y el Azul queda apagado.

* **Código Maestro de la Solución:**
  ```cpp
  const int ledAzul = 8;
  const int ledRojo = 9;

  float nota1 = 8.0;
  float nota2 = 7.5;
  float nota3 = 9.0;

  void setup() {
    pinMode(ledAzul, OUTPUT);
    pinMode(ledRojo, OUTPUT);
  }

  void loop() {
    float promedio = (nota1 + nota2 + nota3) / 3.0;

    if (promedio >= 7.0) {
      digitalWrite(ledAzul, HIGH); // Prende foco Azul
      digitalWrite(ledRojo, LOW);  // Apaga foco Rojo
    } else {
      digitalWrite(ledAzul, LOW);  // Apaga foco Azul
      digitalWrite(ledRojo, HIGH); // Prende foco Rojo
    }
  }
  ```
* **Prueba obligatoria:** Probar primero con notas aprobadas (se enciende el Azul) y luego cambiar las notas a valores menores (ej. 4.0, 5.0, 6.0) para ver cómo el foco Rojo se enciende automáticamente.

---

#### 4. 📝 Llenado del Informe y Cierre (35 - 45 min)
* Colocar la Nota Virtual con su nombre en Tinkercad.
* Capturar pantalla de su circuito simulando con el código C++ visible.
* Llenar la plantilla [1RO_BGU_SEMANA03_INFORME.md](file:///c:/Users/Master_Lab2_DavidC/Documents/LEV/temario_BACH/03_PLANIFICACION_SEMANAL/SEMANA_03/1RO_BGU_SEMANA03_INFORME.md) y subir a Google Classroom.

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM

```text
TÍTULO: Práctica Arduino: Toma de Decisiones con IF - ELSE (Promedio de 3 Notas)

INSTRUCCIONES:
Estimados estudiantes, en esta clase aprendimos a usar la sentencia condicional IF - ELSE en Arduino:

1. Explicamos cómo funciona la estructura if - else comparando dos números para prender o apagar un foco.
2. Desarrollamos el programa para calcular el promedio de 3 notas:
   - Si el promedio es mayor o igual a 7.0: se prende el foco AZUL (Aprobado).
   - Sino (else): se prende el foco ROJO (Reprobado).
3. Entrega tu informe con la captura de pantalla de tu circuito simulando, tu código C++ y las 2 preguntas cortas.

RÚBRICA DE CALIFICACIÓN (Total: 10 Puntos):
- Captura de pantalla en Tinkercad con Nota Virtual y foco correcto encendido: 4.0 pts
- Código C++ con cálculo de promedio y condición if-else funcionando: 3.0 pts
- Preguntas cortas de la práctica contestadas con tus propias palabras: 3.0 pts
```
