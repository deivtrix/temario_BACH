# 📘 3RO BGU — PLAN DE CLASE PRÁCTICO (SEMANA 5)
## 🌐 INTRODUCCIÓN AL ESP32 Y ROBÓTICA IOT: DEL ARDUINO UNO AL MICROCONTROLADOR DE 32 BITS

**Propósito de la Clase (Taxonomía Lev / Robótica Avanzada):**  
> **Comprender** la evolución tecnológica de los microcontroladores comparando la arquitectura clásica de 8 bits (Arduino UNO) frente a la placa de 32 bits de doble núcleo **ESP32** (con WiFi y Bluetooth integrados), **identificar** la distribución de pines de propósito general (**GPIO**) y el nivel de voltaje lógico de $3.3\text{V}$, y **programar** el primer sistema "Hola Mundo IoT" con control de salidas y telemetría por Monitor Serial a $115200\text{ baudios}$ en el simulador online [Wokwi](https://wokwi.com/).

* **Curso:** 3ro BGU  
* **Duración:** 45 Minutos  
* **Modalidad de Trabajo:** 💻 **100% PRÁCTICA EN COMPUTADORA (Simulador Wokwi ESP32 / Arduino IDE)**.  
* **Docente:** Ing. David Castro T.  
* **Software / Plataforma:** [Wokwi ESP32 Simulator](https://wokwi.com/projects/new/esp32) (Simulador Web interactivo de ESP32 sin instalación).  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Solo se entrega **1 sola captura de pantalla** de la simulación activa en Wokwi mostrando el parpadeo del LED y los mensajes en el monitor serial a 115200 baudios.

---

### 🔗 CONEXIÓN PEDAGÓGICA (SEMANA 4 ➔ SEMANA 5)
* **Semana 4:** Concluimos la etapa de potencia con transistores TBJ y motores DC.
* **Semana 5 (Hoy):** *"Dejamos atrás la electrónica básica tradicional. Hoy entramos a la **robótica moderna y el Internet de las Cosas (IoT)**. Conoceremos la placa reina de la industria actual: el **ESP32**, una bestia tecnológica que cuesta casi lo mismo que un Arduino pero tiene procesador de celular, antena WiFi y Bluetooth."*

---

### ⚡ ARDUINO UNO VS ESP32: EL SALTO TECNOLÓGICO

| Característica Técnica | Placa Arduino UNO | Placa ESP32 DevKit | ¿Por qué es mejor el ESP32? |
| :--- | :--- | :--- | :--- |
| **Procesador / Núcleos** | ATmega328P (1 núcleo de 8 bits) | Xtensa LX6 (2 núcleos de 32 bits) | Trabaja 15 veces más rápido ($240\text{ MHz}$ vs $16\text{ MHz}$) |
| **Memoria RAM (SRAM)** | $2\text{ KB}$ | $520\text{ KB}$ | Puede almacenar páginas web y datos de sensores |
| **Conectividad Inalámbrica** | Ninguna (Requiere módulos caros) | **WiFi ($2.4\text{ GHz}$) + Bluetooth 4.2 BLE** | Conecta robots a internet y a celulares |
| **Voltaje Lógico de Trabajo** | **$5\text{V}$** | **$3.3\text{V}$** | ⚠️ *¡Regla de Oro!* Los pines del ESP32 son de $3.3\text{V}$ |
| **Pines Especiales** | Analógicos convencionales | Pines táctiles capacitivos (Touch Pins) | Detecta si tocas un cable con el dedo |

---

### 🛠️ MONTAJE VIRTUAL EN WOKWI SIMULATOR

1. Entrar directamente al navegador en: 🔗 [https://wokwi.com/projects/new/esp32](https://wokwi.com/projects/new/esp32)
2. El simulador muestra la placa **ESP32 DevKit V1** en el centro.
3. Hacer clic en el botón de añadir componente (`+` azul) y agregar:
   * 1 **LED** (color azul o verde).
   * 1 **Resistencia** de $220\ \Omega$ (o $330\ \Omega$).
4. **Conexiones:**
   * Ánodo del LED al pin **GPIO 2** (o GPIO 4) del ESP32.
   * Cátodo del LED conectado a través de la resistencia al pin **GND** del ESP32.

---

### 💻 CÓDIGO C++ EN ESP32 (HOLA MUNDO IOT)

```cpp
// =======================================================
// RETO ESP32: HOLA MUNDO IOT Y SALIDAS GPIO
// Estudiante: [Nombre y Apellido] - 3ro BGU "____"
// Plataforma: Wokwi ESP32 Simulator
// =======================================================

const int pinLed = 2; // Pin GPIO 2 del ESP32 (LED integrado / externo)

void setup() {
  // En ESP32 la velocidad estándar del Serial es 115200 baudios
  Serial.begin(115200);
  
  // Configurar el pin GPIO como salida
  pinMode(pinLed, OUTPUT);
  
  // Mensaje de bienvenida en la consola serial
  Serial.println("=========================================");
  Serial.println("🚀 ¡BIENVENIDO AL ESP32 Y ROBOTICA IOT! 🚀");
  Serial.println("Procesador: Dual Core 240 MHz | WiFi Activo");
  Serial.println("=========================================");
}

void loop() {
  // Encender LED y enviar estado a la terminal
  digitalWrite(pinLed, HIGH);
  Serial.println("LED ESP32: [ENCENDIDO] -> Estado 1 (3.3V)");
  delay(1000);

  // Apagar LED y enviar estado a la terminal
  digitalWrite(pinLed, LOW);
  Serial.println("LED ESP32: [APAGADO]   -> Estado 0 (0V)");
  delay(1000);
}
```

---

### ⏱️ DESGLOSE DE LOS 45 MINUTOS (100% DINÁMICO)

1. **🎯 Demostración de Impacto — ¿Por qué ESP32? (00 - 12 min):**
   * Mostrar una placa ESP32 física o en video: la antena dorada de WiFi impresa en la tarjeta.
   * Explicar el cambio de velocidad en la terminal: en Arduino usábamos $9600\text{ baudios}$, en ESP32 usamos **$115200\text{ baudios}$**.
   * Advertencia crítica de hardware: el ESP32 opera a **$3.3\text{V}$**, no a $5\text{V}$.
2. **🛠️ Acceso y Armado en Wokwi (12 - 25 min):**
   * Todos abren [wokwi.com/projects/new/esp32](https://wokwi.com/projects/new/esp32).
   * Conectan el LED en GPIO 2 y GND con su resistencia.
3. **🚀 Programación y Monitor Serial a 115200 (25 - 38 min):**
   * Copian y ejecutan el código de prueba.
   * Dar clic en el botón verde de "Play" en Wokwi.
   * Observar en la parte inferior la terminal serial corriendo a alta velocidad con los mensajes personalizados del alumno.
   * *Reto rápido:* Cambiar el tiempo a `delay(200);` y verificar el destello ultrarrápido.
4. **📸 Calificación en Vivo y Cierre (38 - 45 min):**
   * El docente pasa por las pantallas registrando el 10/10.
   * Cada alumno toma **1 captura de pantalla** mostrando el LED encendido en Wokwi y la consola serial con sus mensajes.

---

### 📢 TEXTO LISTO PARA PEGAR EN GOOGLE CLASSROOM (ENTREGA EXPRÉS)

```text
TÍTULO: Práctica N° 5: Introducción al ESP32 y Robótica IoT (Wokwi Simulator)

INSTRUCCIONES:
Estimados estudiantes, en esta clase damos el gran salto hacia la robótica moderna y el Internet de las Cosas utilizando el microcontrolador ESP32 de 32 bits:

📌 EVIDENCIA DE CLASE (Sin informe escrito):
1. Ingresa al simulador web: https://wokwi.com/projects/new/esp32
2. Conecta un foco LED al pin GPIO 2 y GND con su resistencia.
3. Programa el código "Hola Mundo IoT" configurando la velocidad Serial a 115200 baudios.
4. Toma UNA captura de pantalla donde se observe:
   - La placa ESP32 con el LED parpadeando en la simulación.
   - La consola serial inferior corriendo a 115200 baudios con tus mensajes de bienvenida.
5. Sube la imagen y marca como entregada.

* Calificación: 10 Puntos evaluados en vivo en el laboratorio de robótica.
```
