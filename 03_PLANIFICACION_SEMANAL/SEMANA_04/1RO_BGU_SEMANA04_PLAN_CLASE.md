# 📘 1RO BGU — PLAN DE CLASE PRÁCTICO (SEMANA 4)
## 🚦 RETO CONDICIONAL IF - ELSE: PROMEDIO DE 3 NOTAS Y SEMÁFORO DE APROBACIÓN (FÍSICO O SIMULADOR)

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** la estructura lógica de decisión `if - else` en C++, **construir** un circuito dual con dos focos indicadores (Verde/Azul para Aprobado y Rojo para Reprobado), y **programar** el cálculo automático del promedio de 3 calificaciones escolares activando el foco correcto en tiempo real.

* **Curso:** 1ro BGU  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 💻 **100% PRÁCTICA ACTIVA (Tinkercad Circuits en PC o Arduino UNO Físico en Mesa)**.  
* **Docente:** Ing. David Castro T.  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO LARGO.** Verificación directa en pantalla o entrega exprés de **1 sola captura** del circuito simulando con el código C++ en Classroom.

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (100% INTERACTIVO)

#### 1. 🎯 Planteamiento del Reto en Pizarra (00 - 08 min)
* *"Chicos, hoy automatizamos la secretaría del colegio: tenemos 2 focos y 3 notas. Si el promedio de las 3 notas da 7 o más ($\ge 7.0$), se enciende el foco de PASAR. Si da menos de 7, se apaga el de pasar y se enciende el foco de NO PASAR."*
* **Fórmula en C++:**
  ```cpp
  float promedio = (nota1 + nota2 + nota3) / 3.0;
  ```

---

#### 2. 🛠️ Conexión del Circuito Dual (08 - 20 min)
* **Componentes:** Placa Arduino UNO, protoboard, 2 Focos LED (uno Verde/Azul y uno Rojo), 2 resistencias de $220\ \Omega$ o $330\ \Omega$, cables.
* **Cableado:**
  1. Pin **GND** de Arduino al bus negativo ($-$) de la protoboard.
  2. **Foco PASA (Verde/Azul):** Ánodo al **Pin 8**, Cátodo con resistencia a GND.
  3. **Foco NO PASA (Rojo):** Ánodo al **Pin 9**, Cátodo con resistencia a GND.

---

#### 3. 💻 El Código C++ y el Reto en Pantalla (20 - 38 min)
* Los estudiantes programan en el editor:
  ```cpp
  // Práctica: Promedio con IF - ELSE
  const int ledPasa = 8;     // Foco de Aprobado (Verde o Azul)
  const int ledNoPasa = 9;   // Foco de Reprobado (Rojo)

  // Modifica aquí las 3 notas para poner a prueba tu código:
  float nota1 = 8.0;
  float nota2 = 6.5;
  float nota3 = 9.0;

  void setup() {
    pinMode(ledPasa, OUTPUT);
    pinMode(ledNoPasa, OUTPUT);
    Serial.begin(9600); // Para ver el promedio en la terminal
  }

  void loop() {
    float promedio = (nota1 + nota2 + nota3) / 3.0;
    
    Serial.print("Promedio calculado: ");
    Serial.println(promedio);

    // Toma de decisión lógica
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

* **La Prueba de Fuego Interactiva (Obligatoria):**
  1. Probar con notas altas (ej: $9.0, 8.0, 7.5$): Verificar que se prenda **únicamente** el foco Verde/Azul.
  2. Modificar las variables a notas bajas (ej: $4.0, 5.0, 6.0$): Darle Play y ver cómo inmediatamente el foco Verde se apaga y se enciende el foco Rojo.

---

#### 4. ✅ Calificación Formativa en Vivo (38 - 45 min)
* El docente pasa por las computadoras / mesas. El estudiante cambia las notas frente al profesor para demostrar que el circuito conmuta de foco en vivo.
* Registro del 10/10 en el aula, o subida de 1 captura a Classroom.

---

### 📢 TEXTO RÁPIDO PARA GOOGLE CLASSROOM (ENTREGA EXPRÉS)

```text
TÍTULO: Reto Práctico Arduino: Promedio de 3 Notas con Condicional IF - ELSE

INSTRUCCIONES:
Estimados estudiantes, en esta sesión comprobamos la toma de decisiones con Arduino C++:

📌 EVIDENCIA DE CLASE (Sin informe escrito):
1. Captura de pantalla de tu circuito en Tinkercad Circuits mostrando:
   - Los 2 focos conectados (Pin 8 y Pin 9).
   - El foco correcto encendido según las 3 notas que pusiste.
   - La ventana de código C++ con la fórmula y la sentencia if - else.
2. Sube la imagen y marca como entregada.

* Calificación: 10 Puntos registrados en laboratorio durante la prueba interactiva.
```
