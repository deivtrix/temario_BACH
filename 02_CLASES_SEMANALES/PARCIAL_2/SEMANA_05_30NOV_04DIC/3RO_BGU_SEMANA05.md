# 🟠 3RO BGU — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** ESP32 PWM y Buzzer (Zumbador) en Wokwi  
**Subtemas puntuales (2 nuevos):**
1. Generación de tonos en ESP32 con `tone(pin, frecuencia, duracion)` / Control de brillo/intensidad mediante PWM en ESP32.
2. Conexión segura de Buzzer pasivo en Wokwi / Creación de una alerta sonora + visual sincronizada.
**Cargo:** Mediador    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura en Wokwi con brillo PWM + sonido/melodía en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modificar** el brillo de un LED y hacer sonar notas en un buzzer con el ESP32 para crear alertas.
* **¿Cómo sé que lo logré?** El LED regula su brillo por PWM y el buzzer emite tonos distintos según la frecuencia programada.
* **¿Para qué me sirve en la vida?** Así funcionan los reguladores de luces LED, las alarmas de microondas, timbres y alertas auditivas en equipos médicos o industriales.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"En el ESP32 casi todos los pines GPIO sirven para PWM. Hoy vamos a hacer que un LED suba y baje de brillo suavemente y que un buzzer suene con distintas notas."*
* **Propósito en pantalla:** *"Modificar el brillo de un LED y hacer sonar notas en un buzzer con el ESP32 para crear alertas."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Predicción PRIMM (30 seg antes de simular):** Preguntar qué hará el ejemplo o qué cambia si modifican un parámetro antes de correrlo.
* **PWM en ESP32 (Arduino Core 3.x / Wokwi):** Se puede usar `analogWrite(pin, 0–255);` directamente en pines GPIO (ej. `GPIO 13`) con un bucle `for` de `0` a `255`.
* **Buzzer Pasivo:** Conectar un Buzzer en Wokwi (`GPIO 14` y `GND`) y usar `tone(14, frecuencia, duracion);` + `noTone(14);`.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **15 – 25 min (Guiada):** Montan 1 LED en `GPIO 13` + 1 Buzzer en `GPIO 14` en Wokwi y prueban el efecto *Fade* (sube/baja brillo) + un pitido corto.
* **25 – 40 min (Reto Solos):** *"Programa una **alarma de emergencia o mini melodía de 4 notas** donde el LED suba su brillo al ritmo de los tonos del buzzer."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Qué cambia en el buzzer cuando aumentas el número de frecuencia en `tone(pin, freq)`?"*
  2. *"¿Qué rango de valores acepta `analogWrite()` para variar el brillo del LED?"*
* **Cierre:** Subir captura de Wokwi (circuito + código con `// Nombre`) a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Individual 2: ESP32 PWM y Buzzer en Wokwi

PROPÓSITO: Modificar el brillo de un LED y hacer sonar notas en un buzzer con el ESP32 para crear alertas.

INSTRUCCIONES:
1. En wokwi.com (ESP32), conecta 1 LED (con resistencia 220 ohmios) en GPIO 13 y 1 Buzzer en GPIO 14.
2. Usa un bucle for con analogWrite() para hacer efecto Fade en el LED.
3. Usa tone() para reproducir al menos 4 notas o una alarma sincronizada con el LED.
4. Pon // Tu Nombre Apellido en la línea 1 y sube 1 captura de la simulación corriendo.

Calificación: 10 puntos (Actividad Individual 2).
```

---

## ❓ PREGUNTAS DE CIERRE (CON RESPUESTA ESPERADA)
1. **¿Qué parámetro de `tone(pin, frecuencia)` cambia qué tan agudo o grave suena el buzzer?**
   * *Respuesta esperada:* La frecuencia en Hertz (Hz): a mayor frecuencia, sonido más agudo.
2. **¿Qué diferencia práctica hay entre un buzzer activo y un buzzer pasivo?**
   * *Respuesta esperada:* El activo suena con un solo tono al darle corriente; el pasivo permite crear distintas notas musicales con `tone()`.
3. **¿Para qué sirve `noTone(pin)` después de reproducir una nota?**
   * *Respuesta esperada:* Para detener el sonido y generar pausas claras entre notas.
