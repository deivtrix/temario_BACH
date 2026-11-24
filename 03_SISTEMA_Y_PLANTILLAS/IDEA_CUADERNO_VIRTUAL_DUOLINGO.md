# 📱 DISEÑO DEL CUADERNO VIRTUAL INTERACTIVO (ESTILO DUOLINGO + PDFS)

> **Estado:** Propuesta aprobada para piloto (sin servidores ni bases de datos; 100% estático en **GitHub Pages**).

---

## 1. ¿Qué es y cómo lo ve el estudiante?

Una página web ligera (`HTML + CSS + JS` limpio, **sin Three.js ni 3D decorativo pesado**) donde cada curso (`8vo EGB` a `3ro BGU`) tiene sus **Tarjetas por Parcial**:
* `Q1P1` | **`Q1P2`** | `Q2P3` | `Q2P4`

Al hacer clic en una tarjeta (ejemplo: **`Q1P2 — Conductores, Empalmes y Seguridad Eléctrica`**), el estudiante encuentra **3 pestañas en un solo lugar**:

1. **📖 Láminas del Parcial (PDF):**
   * `Sección 1` (`10–12` slides en PDF)
   * `Sección 2` (`10–12` slides en PDF)
   * `Ficha Resumen` (1 página clave del Prompt 3)
2. **⚡ Repaso General tipo Duolingo (Quiz Interactivo):**
   * Las **10 preguntas compilatorias** generadas con el **Prompt 3** en formato interactivo:
     * Barra de progreso (`Pregunta 3 de 10`) y racha de aciertos.
     * Preguntas de diagnóstico / casos reales (*"Si pasa X, ¿por qué falló Y?"*).
     * **Feedback inmediato en 1 segundo:** al elegir una opción, muestra al instante por qué es correcta o cuál fue el error conceptual.
3. **🧩 Ejercicios Propuestos, Simuladores y Video:**
   * 2–3 retos cortos de práctica autónoma.
   * Botones directos al simulador real del parcial (**PhET**, **Tinkercad** o **Wokwi**).
   * Enlace al **Video de Repaso** (Prompt 4).

---

## 2. Reglas de Arquitectura (Mantenimiento Cero)

* **Separar diseño de contenido:** Una sola plantilla `cuaderno.html` que lee un archivo `data_parcial.json` (títulos, rutas de PDFs y array de 10 preguntas con su explicación). Así, al cerrar un nuevo parcial, solo actualizas el JSON y subes los PDFs sin reescribir código web.
* **Simuladores reales, nunca inventados:** Nunca programar simuladores de circuitos/Arduino hechos por IA en la web; enlazar siempre a **PhET**, **Tinkercad Circuits/3D** y **Wokwi** (física y compilación reales).
* **Mobile-first:** Diseñado para cargar rápido en el celular del estudiante y en las computadoras del laboratorio.

---

## 3. Respaldo Pedagógico y Científico

| Autor / Referente | Principio | Aplicación en el Cuaderno Virtual |
| :--- | :--- | :--- |
| **Henry Roediger & Jeffrey Karpicke** | *Retrieval Practice* (Efecto de Prueba) | Responder el quiz interactivo fija mucho más el aprendizaje que releer diapositivas. |
| **John Dunlosky et al.** | Revisión de Técnicas de Estudio | Combina las dos únicas técnicas de **Alta Utilidad**: autoevaluación con preguntas y práctica espaciada. |
| **John Hattie** | *Visible Learning* — Feedback Inmediato | El alumno recibe la explicación conceptual al instante cuando comete un error, no semanas después. |
| **Karl Kapp & Sebastian Deterding** | Gamificación Significativa | Barra de progreso, rachas y tarjetas por parcial para sostener la motivación voluntaria sin perder rigor técnico. |
| **Richard Mayer** | Principio de Coherencia Multimedia | Interfaz limpia sin animaciones 3D ni adornos que generen carga cognitiva extrínseca. |

---

## 4. Próximos Pasos para el Piloto (`8vo EGB — Q1P2`)

1. Generar en NotebookLM los PDFs finales (`Sección 1`, `Sección 2`, `Ficha`) y las 10 preguntas (`Prompt 3`) de `8vo EGB — Parcial 2`.
2. Organizar los PDFs por curso en el repositorio y unirlos si se requiere un PDF maestro del parcial.
3. Construir el piloto estático de **`8vo EGB — Q1P2`** y publicarlo en GitHub Pages para probarlo desde el celular.
