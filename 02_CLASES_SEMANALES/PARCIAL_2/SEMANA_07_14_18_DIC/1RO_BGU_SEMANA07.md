# 🔴 1RO BGU — PARCIAL 2 / SEMANA 7 (14 – 18 dic)

> [!IMPORTANT]
> # 👥 ACTIVIDAD GRUPAL EVALUADA
**Tema:** Theremin Musical Controlado por Luz (LDR + Buzzer `tone()`) *(Grupal Físico — Kits Arduino)*  
**Cargo:** Mediador    
**📊 Slides:** Sección 2 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo B — Montaje Grupal Físico en Kit Arduino (45 min) *(usando código validado en S6)*  
**Entregable:** Visto bueno en vivo del kit físico sonando + Informe corto grupal anti-IA en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Verificar** los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores.
* **¿Cómo sé que lo logré?** Tu Theremin físico en kit Arduino suena limpio al mover la mano sobre la LDR y calibras su rango.
* **¿Para qué me sirve en la vida?** Todo sensor físico cambia según el lugar (más o menos luz); saber leer el Monitor Serial permite ajustar cualquier proyecto en segundos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **Pregunta relámpago (60 seg):** Conectar oralmente con el concepto clave de la clase anterior.
* **¿Qué decirles?** *"Muchos copiaron un número como `400` para su LDR sin mirar qué número marcaba su propio sensor en esta aula. Hoy aprendemos a diagnosticar y calibrar como ingenieros."*
* **Propósito en pantalla:** *"Verificar los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores."*

### 2. Demostración Rápida de Diagnóstico (05 – 12 min)
* Proyectar cómo imprimir `Serial.print("Valor: "); Serial.println(analogRead(A0));` y calcular el **punto medio** `(min + max) / 2` como umbral perfecto.

### 3. Nivelación y Reto de Calibración (12 – 40 min)
* **Protocolo de Autodepuración (3 pasos antes de llamar al mediador):** 1. Energía/GND -> 2. Pines/Polaridad -> 3. Monitor Serial/Multímetro.
* **Roles rotativos (3 por equipo):** 1. Armado/Diseño -> 2. Código/Parámetros -> 3. Verificador/Evidencia.
* Quienes deban alguna práctica del Parcial 2 (Potenciómetro, Atenuador PWM, LDR o Theremin) la completan hoy.
* Quienes estén al día calibran un circuito en Tinkercad/kit usando la fórmula de punto medio e imprimen en Serial `"DIA"` o `"NOCHE"`.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **Dinámica de cierre (30 seg):** Respuesta simultánea (dedos/pulgar) o *Cold Call* al azar (evitar que respondan solo los mismos 2).
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
