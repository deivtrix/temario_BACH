# 📘 10MO EGB — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Múltiples Salidas Digitales: Semáforo en Tinkercad  
**Subtemas puntuales (2 nuevos):**
1. Control de 3 pines digitales independientes (Rojo, Amarillo, Verde) / Secuencia lógica de un semáforo real con `digitalWrite()` y `delay()`.
2. Conexión ordenada de 3 LEDs + 3 resistencias en protoboard virtual / Validación del código en Tinkercad (base para el Grupal Físico de Semana 6).
**Mediador:** David Castro    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura exprés en Classroom del semáforo funcionando con variables `int`.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.
* **¿Cómo sé que lo logré?** Tu semáforo en Tinkercad usa variables int y ejecuta la secuencia completa de los 3 LEDs en orden.
* **¿Para qué me sirve en la vida?** Para organizar cualquier programa grande usando nombres claros (`ledRojo`, `ledVerde`) en lugar de memorizar números de pines.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"La semana pasada controlamos 1 o 2 LEDs usando `13` y `12`. Pero si tuviéramos 20 luces, ¿se acordarían qué hace cada número? Hoy vamos a ponerles nombre con variables."*
* **Propósito en pantalla:** *"Simular un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Predicción PRIMM (30 seg antes de simular):** Preguntar qué hará el ejemplo o qué cambia si modifican un parámetro antes de correrlo.
* **Variables `int`:** `int rojo = 13;`, `int amarillo = 12;`, `int verde = 11;`. Si mañana cambias un cable de pin, solo cambias el número arriba una vez.
* **Modelación en Tinkercad:** Conectar 3 LEDs (Rojo, Amarillo, Verde) con resistencias de $220\,\Omega$ a GND y cargar el ciclo básico.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **15 – 25 min (Guiada):** Todos arman el semáforo de 3 LEDs en protoboard dentro de Tinkercad y prueban el encendido secuencial.
* **25 – 40 min (Reto Solos):** *"Haz que la luz **Verde** parpadee 3 veces antes de pasar a Amarillo (como semáforo real de ciudad), y coloca tiempos reales: Verde 3s, Amarillo 1s, Rojo 3s."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
* **2 preguntas rápidas:**
  1. *"¿Para qué sirve declarar `int rojo = 13;` al inicio del código?"*
  2. *"¿Qué pasa si olvidas apagar el LED anterior con `LOW` antes de encender el siguiente?"*
* **Cierre:** Subir captura de Tinkercad con el código y el semáforo encendido a Classroom.
---

## ❓ PREGUNTAS DE CIERRE (CON RESPUESTA ESPERADA)
1. **¿Cuántas resistencias necesita un semáforo de 3 LEDs y por qué?**
   * *Respuesta esperada:* 3 resistencias (una por cada LED) para proteger cada pin y evitar que se quemen.
2. **¿Qué pasa si olvidamos apagar el LED verde (`LOW`) cuando encendemos el amarillo (`HIGH`)?**
   * *Respuesta esperada:* Quedan encendidos dos colores al mismo tiempo, rompiendo la lógica del semáforo.
3. **¿Por qué probamos primero el semáforo en Tinkercad antes de armarlo en físico?**
   * *Respuesta esperada:* Para verificar que el código y las conexiones funcionan sin riesgo de dañar componentes reales.
