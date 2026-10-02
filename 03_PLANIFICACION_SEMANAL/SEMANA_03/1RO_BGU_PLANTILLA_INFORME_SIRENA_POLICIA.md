# UNIDAD EDUCATIVA / ÁREA DE ROBÓTICA Y TECNOLOGÍA
## INFORME TÉCNICO: SIRENA DE POLICÍA BICOLOR EN ARDUINO C++ (SEMANA 3)

---

### 📋 DATOS DEL ESTUDIANTE
* **Estudiante:** ___________________________________________________________
* **Curso y Paralelo:** 1ro BGU "____"
* **Fecha:** ____ / ____ / 2026
* **Docente / Mediador:** David Castro T.

---

### 📸 1. CAPTURA DE PANTALLA EN TINKERCAD CIRCUITS

> 🔒 **CANDADO DE SEGURIDAD OBLIGATORIO (ANTI-IA):**  
> Agrega una **Nota Virtual** sobre el protoboard que diga: *"Sirena de: [Tu Nombre y Apellido] - 1ro BGU"*.  
> *(La captura debe mostrar los LEDs alternando en simulación activa, la ventana de código y el cartel con tu nombre).*

```
[ PEGA AQUÍ LA CAPTURA DE PANTALLA COMPLETA CON LA NOTA VIRTUAL Y SIMULACIÓN ACTIVA ]
```
<br><br><br><br>

---

### ⚙️ 2. PARÁMETROS REALES DE TU CIRCUITO

| Elemento | Configuración en tu Circuito |
| :--- | :--- |
| **Pin Digital y Color de LED 1:** | Pin Digital: ______ \| Color: _____________________ |
| **Pin Digital y Color de LED 2:** | Pin Digital: ______ \| Color: _____________________ |
| **Valor de las Resistencias:** | ________ Ohmios ($\Omega$) |
| **Valor de tu variable `tiempo`:** | ________ milisegundos (ms) |

---

### 💻 3. CÓDIGO C++ UTILIZADO EN TU SIMULACIÓN

```cpp
// 1. Declaración de variables globales
const int pinRojo = 2;
const int pinAzul = 3;
const int tiempo = 200; // milisegundos

void setup() {
  pinMode(pinRojo, OUTPUT);
  pinMode(pinAzul, OUTPUT);
}

void loop() {
  digitalWrite(pinRojo, HIGH);
  digitalWrite(pinAzul, LOW);
  delay(tiempo);

  digitalWrite(pinRojo, LOW);
  digitalWrite(pinAzul, HIGH);
  delay(tiempo);
}
```

---

### ✍️ 4. PREGUNTAS REFLEXIVAS VIVENCIALES (MÁXIMO 3 LÍNEAS)
*(Prohibido el uso de ChatGPT. Respuestas de enciclopedia serán anuladas; responde según tus pruebas en pantalla).*

**📌 Pregunta 1 (Prueba de error en vivo en tu simulador):**  
Haz esta prueba en tu código de Tinkercad: En el `setup()`, cambia `pinMode(pinRojo, OUTPUT);` por `pinMode(pinRojo, INPUT);` y dale a *Iniciar Simulación*. ¿Qué le ocurrió visualmente al brillo del LED rojo en tu pantalla y por qué el pin no entregó energía suficiente?  
* **Respuesta:**  
___________________________________________________________________________________________________  
___________________________________________________________________________________________________  

**📌 Pregunta 2 (Modificación extrema de variables):**  
Cambia en tu código el valor de tu variable 'tiempo' a 10 ms (`tiempo = 10;`). Al iniciar la simulación, ¿qué parece que le ocurre a los dos LEDs frente al ojo humano? ¿Por qué es vital usar retardos visibles en sistemas de emergencia?  
* **Respuesta:**  
___________________________________________________________________________________________________  
___________________________________________________________________________________________________  

---

### 📊 RÚBRICA DE EVALUACIÓN (CRITERIOS DE TRABAJO)

| Criterio a Evaluar | Puntaje |
| :--- | :---: |
| **1. Captura con circuito simulando y Nota Virtual con nombre visible** | 2.5 pts |
| **2. Parámetros reales y código C++ compilado en su cuenta** | 2.5 pts |
| **3. Pregunta 1 respondida probando el error en vivo de INPUT/OUTPUT** | 2.5 pts |
| **4. Pregunta 2 explicada desde la observación del retardo en pantalla** | 2.5 pts |
