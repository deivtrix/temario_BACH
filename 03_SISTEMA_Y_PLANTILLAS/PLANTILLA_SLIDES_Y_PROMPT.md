# 🎨 PLANTILLA MAESTRA DE DIAPOSITIVAS Y PROMPT (NOTEBOOKLM / CANVA / GEMINI)

Usa esta plantilla alineada con [REGLAS_Y_MEMORIA_DOCENTE.md](REGLAS_Y_MEMORIA_DOCENTE.md) para generar presentaciones en formato híbrido (*Cómic de Historia/Versus + Láminas Explicativas Profundas*).

---

## 1. ESTRUCTURA SEGÚN EL MODO DE CLASE (SIN NÚMERO FIJO DE SLIDES)

* **Modo A — Tema Nuevo (sin etiqueta):**
  * Portada (título + curso, sin nombre del mediador ni fechas) $\rightarrow$ Propósito LEV + *¿Para qué sirve en la vida real?* $\rightarrow$ Láminas explicativas con diagramas/esquemas claros $\rightarrow$ Preguntas de verificación y cierre.
* **Modo B — Actividad Evaluada (`👤 ACTIVIDAD INDIVIDUAL` o `👥 ACTIVIDAD GRUPAL`):**
  * Portada con etiqueta grande $\rightarrow$ Propósito LEV $\rightarrow$ Recordatorio técnico visual breve *(sin regalar código ni solución)* $\rightarrow$ Enunciado claro del reto + requisitos + 1 consejo $\rightarrow$ Verificación y cierre *(máx. 4–5 slides)*.
* **Refuerzo / Cierre (`🛠️ REFUERZO`):**
  * Portada con etiqueta $\rightarrow$ Propósito LEV $\rightarrow$ Mapa visual resumen / errores comunes $\rightarrow$ Trivia o casos de diagnóstico *(sin respuestas visibles)* $\rightarrow$ Autoevaluación Likert (1–5) en cierres de parcial.

---

## 2. PROMPT BASE PARA NOTEBOOKLM

```text
Crea una presentación estilo cómic educativo en español para estudiantes de [CURSO] ([EDAD] años) del Volumen [X]: "[NOMBRE_OFICIAL_PARCIAL]", como un capítulo autoconclusivo independiente ("[TÍTULO_CAPÍTULO]", [ETIQUETA_SI_APLICA: 👤 ACTIVIDAD INDIVIDUAL | 👥 ACTIVIDAD GRUPAL | 🛠️ REFUERZO | o ninguna]) basado en el CAPÍTULO #[N] de FUENTE_[CURSO]_PARCIAL[X]_COMPLETO.md.

Reglas obligatorias:
1. Redacta el Propósito usando un verbo en infinitivo de la Taxonomía LEV + qué haremos hoy + "¿Para qué me sirve en la vida real?".
2. Formato híbrido: combina narrativa visual (cómic/versus) con láminas explicativas limpias (diagramas, flechas, tablas visuales, cero muros de texto).
3. Candado de alcance: usa ÚNICAMENTE los bloques, instrucciones y componentes de este capítulo; PROHIBIDO introducir temas avanzados no vistos aún o inventar código.
4. Si es actividad evaluativa (👤 Individual / 👥 Grupal): ve directo al reto con un recordatorio técnico breve y PROHIBIDO regalar el código completo o la solución resuelta.
5. PROHIBIDO poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados ("sube a Classroom"), "Continuará..." o adelantos del próximo capítulo.
```
