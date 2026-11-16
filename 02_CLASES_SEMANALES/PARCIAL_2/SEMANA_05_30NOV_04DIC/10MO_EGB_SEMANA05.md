# 📘 10MO EGB — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)
**Tema:** Múltiples Salidas Digitales: Semáforo en Tinkercad  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura exprés en Classroom del semáforo funcionando con variables `int`.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.
* **¿Para qué me sirve en la vida?** Para organizar cualquier programa grande usando nombres claros (`ledRojo`, `ledVerde`) en lugar de memorizar números de pines.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada controlamos 1 o 2 LEDs usando `13` y `12`. Pero si tuviéramos 20 luces, ¿se acordarían qué hace cada número? Hoy vamos a ponerles nombre con variables."*
* **Propósito en pantalla:** *"Simular un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Variables `int`:** `int rojo = 13;`, `int amarillo = 12;`, `int verde = 11;`. Si mañana cambias un cable de pin, solo cambias el número arriba una vez.
* **Modelación en Tinkercad:** Conectar 3 LEDs (Rojo, Amarillo, Verde) con resistencias de $220\,\Omega$ a GND y cargar el ciclo básico.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Todos arman el semáforo de 3 LEDs en protoboard dentro de Tinkercad y prueban el encendido secuencial.
* **25 – 40 min (Reto Solos):** *"Haz que la luz **Verde** parpadee 3 veces antes de pasar a Amarillo (como semáforo real de ciudad), y coloca tiempos reales: Verde 3s, Amarillo 1s, Rojo 3s."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Para qué sirve declarar `int rojo = 13;` al inicio del código?"*
  2. *"¿Qué pasa si olvidas apagar el LED anterior con `LOW` antes de encender el siguiente?"*
* **Cierre:** Subir captura de Tinkercad con el código y el semáforo encendido a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Práctica Arduino: Semáforo Inteligente en Tinkercad

PROPÓSITO: Simular un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.

INSTRUCCIONES:
1. Conecta 3 LEDs (Rojo en Pin 13, Amarillo en Pin 12, Verde en Pin 11) con sus resistencias de 220 ohmios a GND.
2. Declara variables int para cada color al inicio del código.
3. Programa el ciclo completo haciendo que el Verde parpadee 3 veces antes de cambiar a Amarillo.
4. Escribe // Tu Nombre Apellido en la línea 1 y sube 1 captura de la simulación corriendo.

Calificación: 10 puntos (Práctica de clase).
```
