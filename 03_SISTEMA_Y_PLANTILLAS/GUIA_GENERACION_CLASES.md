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

Cada archivo (`<CURSO>_SEMANA<NN>.md`) dentro de `02_CLASES_SEMANALES/PARCIAL_<N>/SEMANA_<NN>_<FECHAS>/` debe tener exactamente estas secciones (sin prompts largos de NotebookLM al pie; los prompts viven en `04_PARA_NOTEBOOKLM/<CURSO>/PARCIAL_<N>/PROMPTS_BLOQUES.md`):

```markdown
# <EMOJI> <CURSO> — PARCIAL <N> / SEMANA <NN> (<FECHAS>)
**Tema:** <Nombre exacto del tema en 01_TEMARIOS_POR_CURSO>
**Cargo:** Mediador
**Modo de Clase:** <Modo A: Tema Nuevo (45 min) | Modo B: Actividad Autónoma (45 min)>
**Entregable:** <Captura exprés en Classroom | Visto bueno en vivo | Informe corto anti-IA>
**📊 Slides:** Bloque <1 o 2> (Láminas <X–Y>)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** <1 sola frase corta con verbo LEV en infinitivo + tema + para qué sirve>
* **¿Cómo sé que lo logré? (Criterio de éxito):** <1 frase observable y medible que el estudiante verifica en su pantalla o mesa>
* **¿Para qué me sirve en la vida?** <1 frase directa y cotidiana>

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Conexión (00 – 05 min)
* **Pregunta relámpago (60 seg):** "<1 pregunta corta conectando con la clase anterior>"
* **¿Qué decirles?** "<Frase natural de entrada + pregunta cotidiana>"
* **Propósito en pantalla:** "<Propósito corto>"

### 2. Teoría Puntual / Encuadre (05 – 15 min | máx. 10 min)
*(Modo A: 1–2 subtemas nuevos sin repetir teoría previa + ejemplo resuelto con **Predicción PRIMM de 30 seg** antes de simular en `10mo–3ro BGU` | Modo B: 5 min de reglas, roles rotativos si es grupal y arrancan).*

### 3. Práctica / Trabajo en Clase (15 – 40 min)
*(Protocolo de Autodepuración en 3 pasos antes de llamar al mediador: 1. Energía/GND, 2. Pines/Polaridad, 3. Monitor Serial/Multímetro).*

### 4. Cierre y Verificación Conceptual (40 – 45 min)
* **2 preguntas rápidas sorpresa (respuesta simultánea dedos/pulgar o Cold Call al azar):**
  1. <Pregunta conceptual corta 1> *(Resp: ...)*
  2. <Pregunta conceptual corta 2> *(Resp: ...)*
* **Cierre:** <Indicación de entrega>

## 📢 TEXTO PARA GOOGLE CLASSROOM
(Solo si es evaluada: bloque listo para copiar y pegar con título, propósito, pasos claros, roles si es grupal y puntaje).
```

---

## 3. REGLAS INNEGOCIABLES AL GENERAR
1. **Mediador:** Usar siempre y exclusivamente **Mediador** (sin nombre propio; nunca `Ing.`, `Docente` ni `Profesor`).
2. **Herramientas reales por curso:**
   * **8vo:** PhET, Canva, Tinkercad Circuits, prácticas físicas, LEGO WeDo 2.0.
   * **9no:** Tinkercad 3D, Inkscape `.SVG`, mBot/mBlock, Tinkercad Circuits (Protoboard).
   * **10mo:** Protoboard, Tinkercad Circuits / Arduino UNO, Canva, LEGO WeDo 2.0.
   * **1ro BGU:** Tinkercad Circuits + Kit físico Arduino con sensores.
   * **2do BGU:** Tinkercad Sim Lab / Codeblocks, Arduino (`millis()`, Puente H, LCD 16x2).
   * **3ro BGU:** **100% Wokwi gratuito** (`wokwi.com`, sin ESP32 físico) + APIs WiFi / *Google Teachable Machine* (según `01_TEMARIOS_POR_CURSO/3RO_BGU.md`).
3. **Respetar los candados anti-IA** solo cuando el entregable sea **Informe Corto** (no en capturas exprés).
