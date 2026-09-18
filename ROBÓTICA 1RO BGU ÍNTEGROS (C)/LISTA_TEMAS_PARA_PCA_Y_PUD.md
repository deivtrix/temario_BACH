# 📋 LISTA OFICIAL DE TEMAS PARA PCA Y PUD
**Curso:** 1ro BGU — Telemetría Serial UART, Displays y Entradas Analógicas ADC

> 💡 **INSTRUCCIÓN:** Utiliza esta lista para copiar y pegar directamente los temas en los formatos oficiales de la institución (Plan Curricular Anual - PCA y Plan de Unidad Didáctica - PUD).

---

### 📌 Unidad 1: Comunicación Serial UART (Arduino <-> Computadora)
* Tema 1.1: Protocolo asíncrono Serial UART (Pines TX/RX, baudios 9600 bps y Serial.begin).
* Tema 1.2: Envío de telemetría a la PC (Diferencias entre Serial.print y Serial.println).
* Tema 1.3: Práctica física de transmisión serial desde el Arduino UNO hacia la laptop.
* Tema 1.4: Recepción de comandos desde la PC (Buffer serial, Serial.available y Serial.read).
* Tema 1.5: Control teleoperado de velocidad de motores desde la consola serial.
* Tema 1.6: Sistema de seguridad por contraseña en la consola serial (String matching).

### 📌 Unidad 2: Displays Digitales (7 Segmentos y LCD 16x2)
* Tema 2.1: Display de 7 segmentos (Configuración Ánodo Común y Cátodo Común).
* Tema 2.2: Montaje físico y programación de contador automático de 0 a 9 en 7 segmentos.
* Tema 2.3: Pantalla de Cristal Líquido LCD 16x2 en modo 4-bits (Librería LiquidCrystal.h).
* Tema 2.4: Montaje físico de pantalla LCD 16x2 con potenciómetro de ajuste de contraste.
* Tema 2.5: Funciones avanzadas de LCD (setCursor, scrollDisplay, marquesinas dinámicas).
* Tema 2.6: Proyecto integrador: Pantalla LCD + Entrada de mensajes desde el teclado serial.

### 📌 Unidad 3: Entradas Analógicas y Conversor ADC de 10 Bits
* Tema 3.1: Convertidor Analógico-Digital ADC (Pines A0-A5, escala 0-5V a 0-1023 niveles).
* Tema 3.2: Montaje físico de divisor de voltaje con potenciómetro de 10k ohm y medición VDC.
* Tema 3.3: Re-escalado de valores analógicos con la función map() (Mapeo ADC a PWM).
* Tema 3.4: Sensor de luz LDR (Fotoresistencia) y comportamiento resistivo ante la luz.
* Tema 3.5: Lámpara crepuscular automática (Umbral de disparo por software para alumbrado).
* Tema 3.6: Montaje físico de sistema de iluminación crepuscular con ajuste por potenciómetro.

### 📌 Unidad 4: Sensores Analógicos de Temperatura y Climatización
* Tema 4.1: Sensor de temperatura analógico TMP36/LM35 (Escala 10mV/°C y fórmula de grados C).
* Tema 4.2: Montaje físico de termómetro digital desplegado en Pantalla LCD 16x2.
* Tema 4.3: Climatizador automático domótico (Control de encendido de ventilador/calefactor).
* Tema 4.4: Sistema de alerta por sobretemperatura con alarmas sonoras en Buzzer piezoeléctrico.
* Tema 4.5: Integración final de instrumentación (Sensores LDR + Temperatura + LCD + UART).
* Tema 4.6: Evaluación práctica final y defensa individual del sistema de medición.

