# 🎨 PLANTILLA MAESTRA DE CLASE, PROMPT Y DIAPOSITIVAS (CANVA / GEMINI / NOTEBOOKLM)

Usa esta plantilla cada vez que vayas a generar las diapositivas de una clase desde `TEMARIOS_POR_CURSO/`.

---

## 1. ESTRUCTURA FIJA DE DIAPOSITIVAS (7 PÁGINAS PARA 45 MIN)

* **Página 1 — Portada:**
  * Título llamativo del tema + Curso (ej. `1ro BGU`) + Materia: Robótica y Tecnología *(sin nombre del mediador)*.
* **Página 2 — Propósito y "¿Para qué me sirve en la vida?":**
  * **Propósito LEV:** `[Verbo infinitivo LEV]` + `[Tema corto y preciso]` + `[Contexto real]`.
  * **Motivación:** 1 pregunta activadora sobre un problema cotidiano.
  * **¿Para qué sirve?** 1 frase directa conectada con la vida real / industria.
* **Página 3 — Teoría Relámpago (Concepto Clave):**
  * Máximo 3 puntos cortos (sin párrafos largos) + espacio para esquema/diagrama.
* **Página 4 — Diagrama / Código o Esquema Técnico (Enunciación):**
  * Pines, conexiones, bloques o fórmula visual (listo para proyectar mientras explicas).
* **Página 5 — Práctica Guiada (Paso a Paso en Conjunto — 10 min):**
  * Pasos numerados (1, 2, 3) de lo que todos arman o programan contigo.
* **Página 6 — Reto Autónomo (Individual o Grupal — 15 a 35 min):**
  * Qué deben lograr solos + variación/desafío.
* **Página 7 — Cierre, Preguntas y Entregable (5 min):**
  * **2–3 preguntas rápidas de verificación** (¿Qué aprendimos hoy?).
  * **Entregable Classroom:** Captura exprés / Visto bueno en vivo / Informe corto anti-IA.

---

## 2. PROMPT LISTO PARA COPIAR Y PEGAR (AQUÍ, GEMINI O NOTEBOOKLM)

```text
Actúa como asistente pedagógico del David Castro (Unidad Educativa Lev Vygotsky).
Genera el guion de clase de 45 minutos y el contenido exacto página por página (Página 1 a Página 7) listo para pasar a Canva, usando estos datos:

- Curso: [EJ. 1RO BGU]
- Tema de TEMARIOS_POR_CURSO: [PEGAR LÍNEA DEL TEMARIO]
- Modo de clase: [Modo A: Tema Nuevo | Modo B: Actividad Autónoma Individual/Grupal]
- Entregable: [Captura exprés en Classroom | Visto bueno en vivo | Informe corto anti-IA]
- Herramienta: [Tinkercad Circuits / Tinkercad 3D / Wokwi ESP32 / PhET / Físico]

Reglas obligatorias:
1. Redacta el Propósito usando un verbo en infinitivo de la Taxonomía LEV + qué haremos hoy (máx. 12–15 palabras, lenguaje natural para adolescentes).
2. Incluye siempre una frase clara de "¿Para qué sirve esto en la vida real?".
3. Diseño visual limpio (CERO muros de texto ni globos largos): prioriza diagramas gráficos, esquemas con flechas, tablas visuales e íconos grandes. Usa definiciones cortas de 1–2 líneas solo cuando sean necesarias.
4. INCLUYE SIEMPRE la etiqueta grande del tipo de clase (`👤 ACTIVIDAD INDIVIDUAL` / `👥 ACTIVIDAD GRUPAL` / `🛠️ REFUERZO` o `📘 TEMA NUEVO`):
   - Si es **TEMA NUEVO**: incluye mapa conceptual, diagrama/diseño de referencia, CÓDIGO REFERENCIAL completo (si aplica) y paso a paso numerado.
   - Si es **👤 ACTIVIDAD INDIVIDUAL o 👥 ACTIVIDAD GRUPAL**: incluye SOLO el enunciado claro + imagen/diseño de referencia + **medidas o materiales necesarios** (si aplica) + máximo 1 tip corto (**CERO código y CERO paso a paso**, porque ya se explicó previamente).
   - Si es **🛠️ REFUERZO**: incluir la actividad completa que harán en clase (casos, preguntas o reto a armar desde cero) + materiales/referencia, sin regalar las respuestas.
5. Cierra con 2 o 3 preguntas cortas de verificación oral/escrita y el texto listo para pegar en Google Classroom.
6. Al final de cada parcial, incluye SIEMPRE una diapositiva exclusiva de **Autoevaluación con Escala de Likert (1 al 5)** evaluando 4 aspectos concretos aprendidos en el parcial.
```

---

## 3. CÓMO PASARLO A CANVA RÁPIDO
1. Copia el resultado de **Página 1 a Página 7**.
2. En Canva, abre un **Canva Doc** $\rightarrow$ pega el texto $\rightarrow$ clic en **Convertir a presentación** *(o pégalo directo en tu plantilla base de 7 diapositivas)*.
3. Ajusta solo imágenes/iconos y listo.
