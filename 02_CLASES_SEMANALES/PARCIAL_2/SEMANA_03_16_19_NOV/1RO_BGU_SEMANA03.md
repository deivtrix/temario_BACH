# 🔴 1RO BGU — PARCIAL 2 / SEMANA 3 (16 – 19 nov)
**Tema:** Informe de Potenciómetro con 4 LEDs (`analogRead`, `>`, `<`) + Cuestionario *(Individual 1)*  
**Mediador:** David Castro  
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

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Lectura Analógica: Potenciómetro con 4 LEDs", etiqueta 👤 ACTIVIDAD INDIVIDUAL 1) basado en el CAPÍTULO #1 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Krang (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Conflicto, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos midiendo niveles de energía con un indicador analógico.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo pizarra/cuadrícula comparativa ("Pin digital 0/1 vs. Pin analógico A0 con analogRead 0-1023" y "Rangos por umbrales > y < para 4 LEDs"), con diagramas claros presentados por Donatello sin globos que tapen la escala.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho de conflicto con etiqueta 👤 ACTIVIDAD INDIVIDUAL.
2. Propósito LEV y explicación cercana a chicos de 15-16 años de para qué les sirve leer señales continuas en medidores de volumen, batería o sensores industriales.
3. Lámina explicativa profunda de analogRead (0–1023) y división en 4 rangos.
4. Enunciado claro de la actividad individual + 1 consejo (PROHIBIDO resolverles el cuestionario o el informe).
5. Verificación y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
