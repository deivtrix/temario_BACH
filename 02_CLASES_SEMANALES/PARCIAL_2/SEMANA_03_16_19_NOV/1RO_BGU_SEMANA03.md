# 🔴 1RO BGU — PARCIAL 2 / SEMANA 3 (16 – 19 nov)

> [!TIP]
> # 👤 ACTIVIDAD INDIVIDUAL EVALUADA
**Tema:** Informe de Potenciómetro con 4 LEDs (`analogRead`, `>`, `<`) + Cuestionario *(Individual 1)*  
**Mediador:** David Castro    
**📊 Slides:** Sección 1 (ver PROMPTS_BLOQUES.md)
**Modo de Clase:** Modo B — Actividad Autónoma Evaluada (45 min)  
**Entregable:** Informe corto anti-IA (con código, parámetros y 3 preguntas vivenciales) + Cuestionario en Classroom.

---

## 🎯 PROPÓSITO LEV Y SENTIDO PRÁCTICO
* **Propósito:** **Explicar** cómo la perilla del potenciómetro enciende 4 LEDs por turnos, igual que un medidor de batería.
* **¿Para qué me sirve en la vida?** Es la misma idea que usan los indicadores de batería, gasolina o volumen por luces.

---

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)

### 1. Inicio, Motivación y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Chicos, ya lograron que 4 LEDs se enciendan por rangos con el potenciómetro. Hoy vamos a documentar técnicamente su circuito y comprobar que entienden qué pasa por dentro."*
* **Presentar el Propósito (Página 2):** *"Explicar cómo la perilla del potenciómetro enciende 4 LEDs por turnos, igual que un medidor de batería."**documentar y verificar** el funcionamiento del potenciómetro con condicionales (`>` / `<`) para entender cómo los sensores controlan indicadores por rangos en la vida real."*

### 2. Encuadre de los 3 Candados Anti-IA (05 – 10 min)
* **Proyectar Página 5:** *"Ojo: no quiero definiciones de ChatGPT. Su informe debe tener: 1) Captura con su Nota de Nombre y LEDs prendidos, 2) Sus 4 números exactos de umbral `>`, y 3) Respuestas de máximo 3 líneas sobre lo que vieron en pantalla."*

### 3. Trabajo Autónomo: Informe Corto (10 – 35 min)
* **Instrucción:** Abren su Tinkercad de la semana pasada, verifican sus valores `>` / `<`, toman la captura, pegan su código en Google Docs y responden las 3 preguntas vivenciales.
* **Tu rol:** Ayudas a quienes tenían el error de que los LEDs no se apagaban al bajar el potenciómetro (faltaba el `else { digitalWrite(..., LOW); }`).

### 4. Cuestionario y Cierre (35 – 45 min)
* **35 – 42 min:** Responden el cuestionario corto de 4 preguntas en Classroom.
* **42 – 45 min (Preguntas orales de cierre):**
  1. *"¿Cuál es el valor mínimo y máximo de `analogRead()` en Arduino UNO?"*
  2. *"¿Por qué usamos `>` o `<` en lugar de `==` con un potenciómetro?"*

---

## 📢 TEXTO PARA GOOGLE CLASSROOM (INFORME + CUESTIONARIO)
```text
TÍTULO: Actividad Individual 1: Informe Potenciómetro 4 LEDs + Cuestionario

PROPÓSITO: Explicar cómo la perilla del potenciómetro enciende 4 LEDs por turnos, igual que un medidor de batería.

PARTE 1 — INFORME CORTO (En Google Docs):
1. Captura de pantalla de tu circuito en Tinkercad (o foto en físico) con una Nota Virtual / papel con tu NOMBRE y al menos 2 LEDs encendidos.
2. Pega tu código C++ completo e indica los 4 umbrales exactos que usaste (ej. >200, >450...).
3. Responde en máximo 3 líneas cada pregunta (cero definiciones de internet):
   a) ¿Qué pasaba cuando dejabas los 4 LEDs con ">" sin poner el "else { digitalWrite(..., LOW); }" al regresar la perilla?
   b) ¿En qué posición aproximada del potenciómetro se encendía tu tercer LED?
   c) ¿Qué ocurrió si probaste cambiar uno de los valores de comparación a "<"?

PARTE 2 — CUESTIONARIO (4 preguntas):
1. ¿Qué rango numérico entrega analogRead() en Arduino UNO?
2. ¿Qué pines se conectan en los extremos del potenciómetro y cuál en el centro?
3. ¿Por qué usamos ">" o "<" en lugar de "==" con un potenciómetro?
4. Menciona 1 aparato real que funcione por rangos analógicos como esta práctica.

Calificación: 10 puntos (Informe 6 pts + Cuestionario 4 pts).
```
