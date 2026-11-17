# 📗 9NO EGB — PARCIAL 3 / CLASE 6
**Tema:** Sensor Ultrasonido: Robot Esquiva-Obstáculos (`👥 ACTIVIDAD GRUPAL`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo + Práctica Grupal (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Programar** el sensor ultrasonido del mBot para que detecte obstáculos y gire automáticamente sin chocar.
* **¿Para qué me sirve en la vida?** Es la tecnología que usan las aspiradoras robot y los sistemas anticolisión de vehículos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy su mBot deja de ser ciego: le activamos los 'ojos' de ultrasonido para que esquive cajas y paredes solo."*
* **Propósito en pantalla:** *"Programar el sensor ultrasonido del mBot para que detecte obstáculos y gire automáticamente sin chocar."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* Condicional `si [distancia del sensor ultrasonido < 20 cm] entonces`: retroceder 0.5s y girar a la derecha; `si no`: avanzar recto.

### 3. Práctica Grupal en Pista/Laberinto (15 – 40 min)
* En equipos cargan el algoritmo de evasión y prueban el mBot navegando entre cajas/obstáculos sin chocar.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿A qué distancia en cm configuraron el freno de su robot?"*
2. *"¿Por qué todo el `si / si no` debe ir dentro de un bucle `por siempre`?"*
