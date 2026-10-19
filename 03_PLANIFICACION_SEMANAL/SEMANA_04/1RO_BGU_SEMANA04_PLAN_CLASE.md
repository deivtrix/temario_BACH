# 📘 1RO BGU — PLAN DE CLASE PRÁCTICO (SEMANA 4)
## 🚦 RETO CONDICIONAL IF - ELSE IF: SEMÁFORO DE RENDIMIENTO CON 4 NOTAS Y 3 FOCOS (ACTIVIDAD GRUPAL)

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** la lógica condicional anidada (`if - else if - else`) en Arduino C++ según el Módulo Arduino 2 (`CA.2.RB.5.PR.26-27`), **construir** en equipo un semáforo de 3 focos (Rojo, Amarillo y Verde), y **programar** el cálculo automático del promedio de 4 calificaciones escolares activando el foco indicador según la escala institucional de rendimiento.

* **Curso:** 1ro BGU  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 👥 **ACTIVIDAD GRUPAL (Equipos en Laboratorio / PC en Tinkercad Circuits o Mesa Física)**.  
* **Docente:** Ing. David Castro T.  
* **Diapositivas Oficiales Base:** `CA.2.RB.5.PR.26-27 (Ard mod2)` — Toma de Decisiones y Salidas Digitales.  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Solo se entrega **1 sola fotografía / captura de pantalla** por grupo. Todos los integrantes suben la **misma captura** a Classroom, la cual debe tener obligatoriamente los nombres de los integrantes anotados como comentario en las primeras líneas del código C++.

---

### 🚦 LA REGLA INSTITUCIONAL DEL SEMÁFORO DE NOTAS

$$\text{Promedio Final} = \frac{\text{Nota}_1 + \text{Nota}_2 + \text{Nota}_3 + \text{Nota}_4}{4.0}$$

Según el puntaje obtenido, el circuito activa de forma exclusiva un solo foco:

| Color del Foco | Pin Arduino | Rango de Promedio | Significado Pedagógico |
| :--- | :---: | :--- | :--- |
| 🔴 **Rojo** | **Pin 8** | **De 0 a menos de 5** ($< 5.0$) | **Zona de riesgo / No aprobado:** Necesita reforzamiento urgente. |
| 🟡 **Amarillo** | **Pin 9** | **De 5 a 7** ($5.0 \le \text{Promedio} \le 7.0$) | **Nivel aceptable / En mejora:** Cumple lo básico, hay espacio para crecer. |
| 🟢 **Verde** | **Pin 10** | **Más de 7** ($> 7.0$) | **¡Zona de Excelencia!** Logro destacado y dominio sobresaliente. |

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (TRABAJO COLABORATIVO)

#### 1. 🎯 Planteamiento del Reto en la Pizarra (00 - 08 min)
* *"Chicos, hoy construimos el semáforo inteligente de calificaciones del colegio. Recibimos 4 notas, calculamos la media dividiendo para 4.0 y el sistema encenderá el foco correspondiente a su nivel académico: Rojo (Riesgo), Amarillo (En mejora) o Verde (Excelencia)."*
* Explicación de la estructura condicional de 3 vías: `if` $\rightarrow$ `else if` $\rightarrow$ `else`.

---

#### 2. 🛠️ Armado del Circuito Semáforo en Equipo (08 - 20 min)
* **Componentes por Grupo:** Placa Arduino UNO, protoboard, 3 Focos LED (1 Rojo, 1 Amarillo, 1 Verde), 3 resistencias de $220\ \Omega$ o $330\ \Omega$, cables jumper.
* **Cableado Grupal:**
  1. Pin **GND** de Arduino conectado al bus azul/negro ($-$) de la protoboard.
  2. 🔴 **Foco Rojo (Riesgo):** Ánodo al **Pin 8**, Cátodo con resistencia a GND.
  3. 🟡 **Foco Amarillo (Mejora):** Ánodo al **Pin 9**, Cátodo con resistencia a GND.
  4. 🟢 **Foco Verde (Excelencia):** Ánodo al **Pin 10**, Cátodo con resistencia a GND.

---

#### 3. 💻 Programación Grupal con Candado de Nombres (20 - 38 min)
Los integrantes abren el editor de código C++ y **lo primero que hacen es escribir sus nombres completos en el encabezado como comentario**:

```cpp
// =======================================================
// RETO ARDUINO: SEMÁFORO DE 4 NOTAS (IF - ELSE IF - ELSE)
// INTEGRANTES DEL GRUPO:
// 1. ____________________________________________________
// 2. ____________________________________________________
// 3. ____________________________________________________
// CURSO Y PARALELO: 1ro BGU "____"
// =======================================================

const int ledRojo = 8;      // De 0 a menos de 5 (Riesgo)
const int ledAmarillo = 9;  // De 5 a 7 (Aceptable / En mejora)
const int ledVerde = 10;    // Más de 7 (Zona de Excelencia)

// Modifiquen en grupo las 4 notas para probar los 3 casos:
float nota1 = 8.0;
float nota2 = 7.5;
float nota3 = 9.0;
float nota4 = 8.5;

void setup() {
  pinMode(ledRojo, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  Serial.begin(9600); // Para monitorear el promedio en la computadora
}

void loop() {
  // 1. Cálculo del promedio de las 4 notas
  float promedio = (nota1 + nota2 + nota3 + nota4) / 4.0;
  
  Serial.print("Promedio del estudiante: ");
  Serial.println(promedio);

  // 2. Toma de decisiones condicional (Semáforo de 3 zonas)
  if (promedio > 7.0) {
    // 🟢 Zona de Excelencia (Más de 7)
    digitalWrite(ledVerde, HIGH);
    digitalWrite(ledAmarillo, LOW);
    digitalWrite(ledRojo, LOW);
  } 
  else if (promedio >= 5.0) {
    // 🟡 Nivel Aceptable / En mejora (De 5 a 7)
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledAmarillo, HIGH);
    digitalWrite(ledRojo, LOW);
  } 
  else {
    // 🔴 Zona de Riesgo (De 0 a menos de 5)
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledAmarillo, LOW);
    digitalWrite(ledRojo, HIGH);
  }

  delay(1000); // Pausa de 1 segundo
}
```

* **Triple Comprobación Grupal Obligatoria:**
  1. *Caso Verde (Excelencia):* Ingresar notas altas (ej: $8.0, 7.5, 9.0, 8.5 \rightarrow \text{Promedio } 8.25$). Verificar que solo se prenda el **foco Verde**.
  2. *Caso Amarillo (Aceptable):* Modificar las notas a rango medio (ej: $6.0, 5.5, 7.0, 6.0 \rightarrow \text{Promedio } 6.12$). Comprobar que se apague el verde y se prenda el **foco Amarillo**.
  3. *Caso Rojo (Riesgo):* Modificar notas a valores bajos (ej: $4.0, 3.5, 5.0, 4.0 \rightarrow \text{Promedio } 4.12$). Comprobar que se prenda el **foco Rojo**.

---

#### 4. 📸 Captura Compartida y Cierre (38 - 45 min)
1. El equipo toma **una sola captura de pantalla o fotografía** donde se aprecie claramente:
   * El circuito simulando con el foco correcto encendido.
   * La ventana de código abierta mostrando en las primeras líneas de comentarios los nombres de todos los integrantes del grupo (`// INTEGRANTES: ...`).
2. **Cada estudiante del grupo sube esa misma fotografía a su propia tarea de Classroom.**
3. Cero tareas para la casa y cero informes escritos.

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM (ENTREGA GRUPAL EXPRÉS)

```text
TÍTULO: Reto Práctico Grupal Arduino: Semáforo de Calificaciones (4 Notas y 3 Focos)

INSTRUCCIONES:
Estimados estudiantes, en esta clase trabajamos en equipo programando el semáforo condicional de rendimiento escolar con Arduino C++:

📌 REGLA DEL SEMÁFORO (Promedio de 4 Notas):
🔴 Rojo (De 0 a menos de 5): Zona de riesgo o no aprobado (Reforzamiento urgente).
🟡 Amarillo (De 5 a 7): Nivel aceptable o en proceso de mejora.
🟢 Verde (Más de 7): ¡Zona de excelencia! Logro destacado.

📌 INSTRUCCIONES DE ENTREGA GRUPAL (Sin informe escrito):
1. En el editor de código C++, añadan como comentario en las primeras líneas los nombres y apellidos de todos los integrantes del grupo.
2. Tomen UNA SOLA captura de pantalla o fotografía clara donde se observe:
   - El circuito con los 3 focos (Pines 8, 9 y 10) y el foco correspondiente encendido.
   - El código C++ abierto mostrando claramente el comentario con los nombres del grupo y la lógica if - else if - else.
3. TODOS los integrantes del equipo suben la MISMA captura de pantalla a su respectiva cuenta de Google Classroom.

* Calificación: 10 Puntos grupales por funcionamiento correcto demostrado en el laboratorio.
```
