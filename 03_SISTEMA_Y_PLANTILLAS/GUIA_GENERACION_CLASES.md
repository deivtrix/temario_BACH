# 📘 GUÍA MAESTRA DE GENERACIÓN DE CLASES (45 MINUTOS)

**Propósito de este archivo:** Cuando el mediador pida *"genera las clases de la semana X"* o *"genera todas las semanas del parcial"*, se debe seguir **estrictamente** este formato y leer primero `01_TEMARIOS_POR_CURSO/` y `03_SISTEMA_Y_PLANTILLAS/REGLAS_Y_MEMORIA_DOCENTE.md`.

---

## 1. REGLA DEL PROPÓSITO DE CLASE (ULTRA CORTO Y EN LENGUAJE DE ADOLESCENTES)
* **Fórmula:** `[Verbo sencillo en infinitivo de Taxonomía LEV]` + `[qué haremos hoy, máximo 12–15 palabras]` + `[ejemplo cotidiano]`.
* **Regla de oro:** Cero palabras rebuscadas (*experimentalmente, tolerancias, rectilíneo, modular, fundamentos*). Si un chico de 13 años no lo entiende en 3 segundos al leerlo en voz alta, está mal.
  * ❌ *Mal:* *"Comprobar experimentalmente el comportamiento de materiales aislantes y conductores para prevenir riesgos eléctricos."*
  * ✅ *Bien:* *"Probar qué materiales dejan pasar la corriente y cuáles nos protegen de un choque eléctrico."*

---

## 2. ESTRUCTURA EXACTA DE CADA ARCHIVO DE CLASE
*(NO mezclar diapositivas ni prompts de Canva aquí; las diapositivas se generan aparte con `PLANTILLA_SLIDES_Y_PROMPT.md`).*

Cada archivo (`<CURSO>_SEMANA<NN>.md`) dentro de `02_CLASES_SEMANALES/PARCIAL_<N>/SEMANA_<NN>_<FECHAS>/` debe tener exactamente estas 4 secciones:

```markdown
# <EMOJI> <CURSO> — PARCIAL <N> / SEMANA <NN> (<FECHAS>)
**Tema:** <Nombre exacto del tema en 01_TEMARIOS_POR_CURSO>
**Mediador:** David Castro
**Modo de Clase:** <Modo A: Tema Nuevo (45 min) | Modo B: Actividad Autónoma (45 min)>
**Entregable:** <Captura exprés en Classroom | Visto bueno en vivo | Informe corto anti-IA>

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** <1 sola frase corta con verbo LEV en infinitivo + tema + para qué sirve>
* **¿Para qué me sirve en la vida?** <1 frase directa y cotidiana>

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** "<Frase natural de entrada + pregunta cotidiana>"
* **Propósito en pantalla:** "<Propósito corto>"

### 2. Teoría Corta / Encuadre (05 – 15 min | máx. 10 min)
*(Si es Modo A: esquema visual + demostración guiada; si es Modo B: 5 min de reglas/rúbrica y arrancan).*

### 3. Práctica / Trabajo en Clase (15 – 40 min)
*(Modo A: 10 min guiados contigo + 15 min reto solos | Modo B: 35 min trabajo autónomo individual/grupal con tu ayuda en puestos).*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas para comprobar qué aprendieron:**
  1. <Pregunta corta 1>
  2. <Pregunta corta 2>
* **Cierre:** <Indicación de entrega>

## 📢 TEXTO PARA GOOGLE CLASSROOM
(Bloque listo para copiar y pegar con título, propósito, pasos claros y puntaje).
```

---

## 3. REGLAS INNEGOCIABLES AL GENERAR
1. **Mediador:** Siempre y exclusivamente **Mediador: David Castro** (nunca `Ing.`, `Docente` ni `Profesor`).
2. **Herramientas reales por curso:**
   * **8vo:** PhET, Canva, Tinkercad Circuits, prácticas físicas, LEGO WeDo 2.0.
   * **9no:** Tinkercad 3D, Inkscape `.SVG`, mBot/mBlock, Tinkercad Circuits (Protoboard).
   * **10mo:** Protoboard, Tinkercad Circuits / Arduino UNO, Canva, LEGO WeDo 2.0.
   * **1ro BGU:** Tinkercad Circuits + Kit físico Arduino con sensores.
   * **2do BGU:** Tinkercad Sim Lab / Codeblocks, Arduino (`millis()`, Puente H, LCD 16x2).
   * **3ro BGU:** **100% Wokwi gratuito** (`wokwi.com`, sin ESP32 físico) + APIs WiFi / *Google Teachable Machine* (según `01_TEMARIOS_POR_CURSO/3RO_BGU.md`).
3. **Respetar los candados anti-IA** solo cuando el entregable sea **Informe Corto** (no en capturas exprés).
