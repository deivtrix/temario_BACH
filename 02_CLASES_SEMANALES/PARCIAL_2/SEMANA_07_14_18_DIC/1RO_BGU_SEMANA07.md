# 🔴 1RO BGU — PARCIAL 2 / SEMANA 7 (14 – 18 dic)
**Tema:** Refuerzo: Calibración con Monitor Serial y Nivelación *(Refuerzo)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Refuerzo Práctico (45 min)  
**Entregable:** Revisión en vivo / nivelación de prácticas atrasadas del Parcial 2.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Verificar** los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores.
* **¿Para qué me sirve en la vida?** Todo sensor físico cambia según el lugar (más o menos luz); saber leer el Monitor Serial permite ajustar cualquier proyecto en segundos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Muchos copiaron un número como `400` para su LDR sin mirar qué número marcaba su propio sensor en esta aula. Hoy aprendemos a diagnosticar y calibrar como ingenieros."*
* **Propósito en pantalla:** *"Verificar los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores."*

### 2. Demostración Rápida de Diagnóstico (05 – 12 min)
* Proyectar cómo imprimir `Serial.print("Valor: "); Serial.println(analogRead(A0));` y calcular el **punto medio** `(min + max) / 2` como umbral perfecto.

### 3. Nivelación y Reto de Calibración (12 – 40 min)
* Quienes deban alguna práctica del Parcial 2 (Potenciómetro, Atenuador PWM, LDR o Theremin) la completan hoy.
* Quienes estén al día calibran un circuito en Tinkercad/kit usando la fórmula de punto medio e imprimen en Serial `"DIA"` o `"NOCHE"`.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Cómo encuentras el umbral ideal para un sensor LDR en cualquier habitación?"*
  2. *"¿Qué comando inicia la comunicación entre Arduino y la pantalla de la PC?"*

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Refuerzo Práctico: Calibración de Sensores con Monitor Serial

PROPÓSITO: Verificar los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores.

ACTIVIDAD:
- Práctica de diagnóstico en clase calculando el punto medio real de un sensor analógico (LDR / Potenciómetro).
- Nivelación de entregas pendientes antes de vacaciones.
```
