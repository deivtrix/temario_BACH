# 📘 1RO BGU — PLAN DE CLASE PRÁCTICO (SEMANA 4)
## 🚦 RETO CONDICIONAL IF - ELSE: PROMEDIO DE 3 NOTAS Y SEMÁFORO DE APROBACIÓN (ACTIVIDAD GRUPAL)

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** colaborativamente la toma de decisiones con la sentencia `if - else` y tipos de variables `float` según el Módulo Arduino 2 (`CA.2.RB.5.PR.26-27`), **diseñar** en equipo un circuito indicador dual con dos focos (Verde/Azul para Aprobado y Rojo para Reprobado), y **programar** el cálculo del promedio de 3 calificaciones escolares que active el foco correspondiente en tiempo real.

* **Curso:** 1ro BGU  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 👥 **ACTIVIDAD GRUPAL (Equipos en Laboratorio / PC en Tinkercad Circuits o Mesa Física)**.  
* **Docente:** Ing. David Castro T.  
* **Diapositivas Oficiales Base:** `CA.2.RB.5.PR.26-27 (Ard mod2)` — Toma de Decisiones y Salidas Digitales.  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Solo se entrega **1 sola fotografía / captura de pantalla** por grupo. Todos los integrantes suben la **misma captura** a Classroom, la cual debe tener obligatoriamente los nombres de los integrantes anotados como comentario en las primeras líneas del código C++.

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (TRABAJO COLABORATIVO)

#### 1. 🎯 Planteamiento del Reto en la Pizarra (00 - 08 min)
* *"Chicos, hoy trabajamos en equipo resolviendo un problema real: automatizar la secretaría del colegio. Tienen 2 focos y 3 notas. Si el promedio de las 3 notas da 7 o más ($\ge 7.0$), se prende el foco de PASAR. Si da menos de 7, se apaga el de pasar y se prende el foco de NO PASAR."*
* **Fórmula matemática en C++:**
  $$\text{promedio} = \frac{\text{nota}_1 + \text{nota}_2 + \text{nota}_3}{3.0}$$

---

#### 2. 🛠️ Armado del Circuito en Equipo (08 - 20 min)
* **Componentes por Grupo:** Placa Arduino UNO, protoboard, 2 Focos LED (uno Verde/Azul y uno Rojo), 2 resistencias de $220\ \Omega$ o $330\ \Omega$, cables jumper.
* **Cableado Grupal:**
  1. Pin **GND** de Arduino al bus negativo ($-$) de la protoboard.
  2. **Foco PASA (Verde o Azul):** Ánodo al **Pin 8**, Cátodo a través de resistencia a GND.
  3. **Foco NO PASA (Rojo):** Ánodo al **Pin 9**, Cátodo a través de resistencia a GND.

---

#### 3. 💻 Programación Grupal y Candado de Nombres en el Código (20 - 38 min)
Los integrantes abren el editor de código C++ y **lo primero que hacen es escribir sus nombres completos en el encabezado como comentario**:

```cpp
// =======================================================
// RETO ARDUINO: PROMEDIO DE 3 NOTAS CON CONDICIONAL IF-ELSE
// INTEGRANTES DEL GRUPO:
// 1. ____________________________________________________
// 2. ____________________________________________________
// 3. ____________________________________________________
// CURSO Y PARALELO: 1ro BGU "____"
// =======================================================

const int ledPasa = 8;     // Foco de Aprobado (Verde o Azul)
const int ledNoPasa = 9;   // Foco de Reprobado (Rojo)

// Prueben juntos diferentes valores de notas:
float nota1 = 8.5;
float nota2 = 6.0;
float nota3 = 9.0;

void setup() {
  pinMode(ledPasa, OUTPUT);
  pinMode(ledNoPasa, OUTPUT);
  Serial.begin(9600); // Para verificar el valor por monitor serie
}

void loop() {
  // 1. Cálculo del promedio con decimales
  float promedio = (nota1 + nota2 + nota3) / 3.0;
  
  Serial.print("Promedio calculado por el grupo: ");
  Serial.println(promedio);

  // 2. Lógica condicional
  if (promedio >= 7.0) {
    digitalWrite(ledPasa, HIGH);    // Enciende foco de Aprobado
    digitalWrite(ledNoPasa, LOW);   // Apaga foco de Reprobado
  } else {
    digitalWrite(ledPasa, LOW);    // Apaga foco de Aprobado
    digitalWrite(ledNoPasa, HIGH);  // Enciende foco de Reprobado
  }

  delay(1000);
}
```

* **Doble Comprobación Grupal Obligatoria:**
  1. *Ensayo 1 (Aprobados):* Probar con notas altas (ej. $8.5, 7.0, 9.0$) y ver que se encienda el foco Verde/Azul.
  2. *Ensayo 2 (Reprobados):* Cambiar las variables a notas menores (ej. $4.0, 5.0, 6.0$), dar Play y verificar que se encienda inmediatamente el foco Rojo.

---

#### 4. 📸 Captura Compartida y Cierre (38 - 45 min)
1. El equipo toma **una sola captura de pantalla o fotografía** donde se aprecie claramente:
   * El circuito simulando con el foco correcto encendido.
   * La ventana de código abierta donde se lean con total claridad los nombres de todos los integrantes en las primeras líneas de comentarios (`// INTEGRANTES: ...`).
2. **Cada estudiante del grupo sube esa misma fotografía a su propia tarea de Classroom.**
3. Cero tareas para la casa y cero informes escritos.

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM (ENTREGA GRUPAL EXPRÉS)

```text
TÍTULO: Reto Práctico Grupal Arduino: Promedio de 3 Notas con Condicional IF - ELSE

INSTRUCCIONES:
Estimados estudiantes, en esta clase trabajamos en equipo programando la toma de decisiones con Arduino C++:

📌 INSTRUCCIONES DE ENTREGA GRUPAL (Sin informe escrito):
1. En el editor de código C++, añadan como comentario en las primeras líneas los nombres y apellidos de todos los integrantes del grupo (ej: // Integrantes: Juan Pérez, María López).
2. Tomen UNA SOLA captura de pantalla o fotografía clara donde se observe:
   - Los 2 focos conectados (Pin 8 y Pin 9) con el foco correspondiente encendido.
   - El código C++ abierto mostrando claramente el comentario con los nombres del grupo y la lógica if - else.
3. TODOS los integrantes del equipo suben la MISMA captura de pantalla a su respectiva cuenta de Google Classroom.

* Calificación: 10 Puntos grupales por funcionamiento correcto demostrado en el laboratorio.
```
