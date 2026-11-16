# UNIDAD EDUCATIVA / ÁREA DE ROBÓTICA Y TECNOLOGÍA
## INFORME DE PRÁCTICA: CONDICIONALES IF - ELSE Y PROMEDIO DE NOTAS (SEMANA 3)

---

### 📋 DATOS DEL ESTUDIANTE
* **Estudiante:** ___________________________________________________________
* **Curso y Paralelo:** 1ro BGU "____"
* **Fecha:** ____ / ____ / 2026
* **Docente:** Ing. David Castro T.
* **Tema:** Toma de Decisiones en Arduino C++ con `if - else` (Mayor de 2 valores y Promedio de 3 Notas)

---

## 1. OBJETIVO
Aprender a usar la estructura condicional `if - else` en Arduino para tomar decisiones lógicas en dos etapas: primero comparando dos valores numéricos para prender o apagar un foco, y luego calculando el promedio de 3 notas para encender un **foco Azul** (si aprueba con 7 o más) o un **foco Rojo** (si reprueba).

---

## 2. COMPONENTES VIRTUALES UTILIZADOS EN TINKERCAD
* Placa Arduino UNO R3 y Protoboard.
* 1 Foco LED Azul (Pin 8).
* 1 Foco LED Rojo (Pin 9).
* 2 Resistencias de $220\ \Omega$ o $330\ \Omega$.

---

## 3. CAPTURA DE PANTALLA EN TINKERCAD CIRCUITS

> 🔒 **CANDADO DE AUTORÍA (NOTA VIRTUAL):**  
> Coloca una **Nota Virtual** sobre el protoboard que diga:  
> *"Práctica de: [Tu Nombre y Apellido] - 1ro BGU"*.  
> *(Pega la captura completa con la simulación activa mostrando qué foco se encendió según las notas que probaste y la ventana de código C++ abierta).*

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│       [ PEGA AQUÍ LA CAPTURA DE PANTALLA DE TU CIRCUITO SIMULANDO ]    │
│            (Con tu Nota Virtual y la ventana de código C++)            │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```
<br>

---

## 4. CÓDIGO C++ DEL RETO: PROMEDIO DE 3 NOTAS
*(Copia y pega aquí tu código con las 3 notas y la condición `if - else` funcionando)*

```cpp
const int ledAzul = 8;
const int ledRojo = 9;

// Escribe aquí las 3 notas que probaste en tu pantalla:
float nota1 = ____;
float nota2 = ____;
float nota3 = ____;

void setup() {
  pinMode(ledAzul, OUTPUT);
  pinMode(ledRojo, OUTPUT);
}

void loop() {
  // Cálculo del promedio de las 3 notas
  float promedio = (nota1 + nota2 + nota3) / 3.0;

  // Si el promedio es mayor o igual a 7.0, prende Azul. Sino, prende Rojo.
  if (promedio >= 7.0) {
    digitalWrite(ledAzul, HIGH);
    digitalWrite(ledRojo, LOW);
  } else {
    digitalWrite(ledAzul, LOW);
    digitalWrite(ledRojo, HIGH);
  }
}
```

---

## 5. PREGUNTAS CORTAS DE LA PRÁCTICA (RESPONDE EN 1 O 2 LÍNEAS)
*(Prohibido usar ChatGPT. Responde con tus propias palabras según lo que probaste en tu pantalla).*

**📌 Pregunta 1 (Primer ejercicio con 2 valores):**  
En el primer ejercicio donde comparamos dos números (`valorA > valorB`), ¿qué le pasó al foco cuando el primer valor era mayor y qué le pasó cuando cambiaste los números para que fuera menor?  
* **Respuesta:**  
___________________________________________________________________________________________________  
___________________________________________________________________________________________________  

**📌 Pregunta 2 (Reto del promedio de 3 notas):**  
En tu programa de las 3 notas, ¿qué notas le pusiste en tu prueba final y cuál de los dos focos (**Azul** o **Rojo**) se encendió en tu pantalla?  
* **Respuesta:**  
  * Mis notas fueron: _________________________________________________________  
  * El promedio calculado fue: ________ y se encendió el foco: _________________  

---

## 6. CONCLUSIÓN CORTA
¿Por qué la sentencia `if - else` es tan importante para que una máquina o robot pueda tomar decisiones por sí solo?  
___________________________________________________________________________________________________  
___________________________________________________________________________________________________  

---

## 7. RÚBRICA DE CALIFICACIÓN (TOTAL: 10 PUNTOS)

| Criterio | Detalle | Puntaje |
| :--- | :--- | :---: |
| **1. Captura con Nota Virtual** | Circuito simulando con Nota Virtual y foco correcto encendido. | 4.0 pts |
| **2. Código C++ Completo** | Cálculo correcto de promedio de 3 notas y estructura `if - else`. | 3.0 pts |
| **3. Preguntas Cortas y Conclusión**| Respuestas claras sobre la comparación de valores y el foco encendido. | 3.0 pts |
