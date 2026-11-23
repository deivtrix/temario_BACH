#!/usr/bin/env python3
"""Servidor local cero-tokens para el Diario de Clases y Semáforo de 21 Paralelos."""

from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import threading
import webbrowser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "03_SISTEMA_Y_PLANTILLAS", "diario_data.json")
MD_PATH = os.path.join(BASE_DIR, "DIARIO_CLASES.md")
PORT = 8765

DIAS_NOMBRE = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
ESTADOS_ICON = {
    "dada": "✅ Dada",
    "perdida": "❌ Perdida",
    "alcance": "⚡ Alcance dado",
    "pendiente": "⬜ Pendiente",
}


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    export_markdown(data)


def compute_pendientes(data):
    """Calcula desfases acumulados por paralelo."""
    semanas_ord = sorted(data["semanas"].keys(), key=lambda x: int(x))
    pendientes = {}
    for p in data["horario"]:
        pid = p["id"]
        perdidas = []
        alcances = 0
        for sem in semanas_ord:
            reg = data["semanas"][sem]["registros"].get(pid, {})
            est = reg.get("estado", "pendiente")
            if est == "perdida":
                perdidas.append({"semana": sem, "motivo": reg.get("motivo", ""), "nota": reg.get("nota", "")})
            elif est == "alcance":
                alcances += 1
        neto = max(0, len(perdidas) - alcances)
        pendientes[pid] = {"neto": neto, "perdidas": perdidas}
    return pendientes


def export_markdown(data):
    """Regenera DIARIO_CLASES.md automáticamente para mantener Obsidian sincronizado."""
    pendientes = compute_pendientes(data)
    sem_actual = str(data.get("semana_actual", "4"))
    sem_obj = data["semanas"].get(sem_actual, {})
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M")

    lines = [
        "# 📔 DIARIO DE CLASES Y TOMA DE DECISIONES (PARCIAL 2)",
        "",
        f"**Mediador:** David Castro | **Actualizado automáticamente:** {ahora} *(0 tokens — App Local)*",
        "",
        "---",
        "",
        "## 🚨 1. TABLERO DE DECISIONES ACTIVAS",
        "",
        "| Nivel / Paralelo | Desfase | Situación | Decisión / Acción Recomendada | Estado |",
        "| :--- | :---: | :--- | :--- | :---: |",
    ]

    hay_alertas = False
    for p in data["horario"]:
        info = pendientes[p["id"]]
        if info["neto"] > 0:
            hay_alertas = True
            sems = ", ".join(f"S{x['semana']} ({x['motivo'] or 'Sin motivo'})" for x in info["perdidas"])
            if p["progresivo"]:
                accion = "Avance progresivo: continuar secuencia normal o enviar formulario a casa."
                badge = "🔵 Progresivo"
            else:
                accion = "Plan de Alcance: enviar tarea/cuestionario en Classroom y fusionar en próxima clase."
                badge = f"🟡 -{info['neto']} clase" if info["neto"] == 1 else f"🔴 -{info['neto']} clases"
            lines.append(f"| **{p['nivel']} — {p['paralelo']}** | -{info['neto']} | {sems} | {accion} | {badge} |")

    if not hay_alertas:
        lines.append("| **Todos los paralelos (21)** | 0 | Sin clases perdidas pendientes | Continuar planificación normal | 🟢 Al día |")

    lines.extend([
        "",
        "---",
        "",
        f"## 📅 2. REGISTRO — {sem_obj.get('nombre', f'Semana {sem_actual}').upper()}",
        "",
    ])

    for dia_idx, dia_nom in enumerate(DIAS_NOMBRE):
        lines.append(f"### {dia_nom}")
        for p in [x for x in data["horario"] if x["dia"] == dia_idx]:
            reg = sem_obj.get("registros", {}).get(p["id"], {})
            est = reg.get("estado", "pendiente")
            icon = ESTADOS_ICON.get(est, "⬜ Pendiente")
            tema = sem_obj.get("temas", {}).get(p["nivel"], "")
            extra = ""
            if reg.get("motivo"):
                extra += f" — *Motivo: {reg['motivo']}*"
            if reg.get("nota"):
                extra += f" ({reg['nota']})"
            lines.append(f"* `{p['hora']}` | **{p['nivel']} — {p['paralelo']}:** {icon} | {tema}{extra}")
        lines.append("")

    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


HTML_PAGE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Diario de Clases — 21 Paralelos</title>
<style>
  :root {
    --bg: #0f172a; --card: #1e293b; --border: #334155; --text: #f8fafc;
    --muted: #94a3b8; --green: #16a34a; --red: #dc2626; --amber: #d97706; --blue: #2563eb;
  }
  * { box-sizing: border-box; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }
  body { margin: 0; background: var(--bg); color: var(--text); padding: 20px; max-width: 1100px; margin-inline: auto; }
  header { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 18px; }
  h1 { margin: 0; font-size: 1.4rem; }
  .controls { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
  select, button, input { background: var(--card); color: var(--text); border: 1px solid var(--border); border-radius: 8px; padding: 8px 12px; font-size: 0.9rem; }
  button { cursor: pointer; font-weight: 600; transition: 0.15s; }
  button:hover { filter: brightness(1.15); }
  .btn-primary { background: var(--blue); border-color: var(--blue); }
  .btn-green { background: var(--green); border-color: var(--green); }
  .panel { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 16px; margin-bottom: 18px; }
  .panel h2 { margin: 0 0 12px 0; font-size: 1.05rem; display: flex; justify-content: space-between; align-items: center; }
  .alerts-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 10px; }
  .alert-card { background: #0f172a; border-left: 4px solid var(--amber); border-radius: 8px; padding: 10px 12px; font-size: 0.88rem; }
  .alert-card.prog { border-left-color: var(--blue); }
  .alert-card.red { border-left-color: var(--red); }
  .tabs { display: flex; gap: 6px; margin-bottom: 14px; flex-wrap: wrap; }
  .tab { padding: 8px 16px; border-radius: 8px; background: var(--card); border: 1px solid var(--border); cursor: pointer; font-weight: 600; }
  .tab.active { background: var(--blue); border-color: var(--blue); }
  .class-list { display: flex; flex-direction: column; gap: 10px; }
  .class-card { background: #0f172a; border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 10px; }
  .class-info { flex: 1; min-width: 240px; }
  .class-title { font-weight: 700; font-size: 1rem; }
  .class-meta { color: var(--muted); font-size: 0.85rem; margin-top: 3px; }
  .class-actions { display: flex; gap: 6px; align-items: center; flex-wrap: wrap; }
  .st-btn { padding: 6px 11px; font-size: 0.85rem; opacity: 0.55; }
  .st-btn.selected { opacity: 1; box-shadow: 0 0 0 2px #fff4; }
  .st-dada.selected { background: var(--green); border-color: var(--green); }
  .st-perdida.selected { background: var(--red); border-color: var(--red); }
  .st-alcance.selected { background: var(--amber); border-color: var(--amber); }
  .toast { position: fixed; bottom: 16px; right: 16px; background: var(--green); color: #fff; padding: 10px 16px; border-radius: 8px; font-weight: 600; display: none; }
</style>
</head>
<body>
<header>
  <div>
    <h1>📔 Diario de Clases &mdash; Robótica (21 Paralelos)</h1>
    <div style="color:var(--muted);font-size:0.85rem;">0 tokens &bull; Sincroniza automático con Obsidian (DIARIO_CLASES.md)</div>
  </div>
  <div class="controls">
    <select id="weekSelect"></select>
    <button onclick="addNewWeek()">+ Nueva Semana</button>
  </div>
</header>

<div class="panel">
  <h2><span>🚨 Tablero de Decisiones (Qué hacer con atrasos)</span><span id="summaryBadge" style="font-size:0.85rem;color:var(--muted);"></span></h2>
  <div id="alertsGrid" class="alerts-grid"></div>
</div>

<div class="panel">
  <h2>
    <span>📅 Registro del Día</span>
    <button class="btn-green" onclick="markAllDay()">✅ Marcar todo el día como Dado</button>
  </h2>
  <div class="tabs" id="dayTabs"></div>
  <div class="class-list" id="classList"></div>
</div>

<div id="toast" class="toast">Guardado y sincronizado con Obsidian ✓</div>

<script>
const DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"];
let DATA = null;
let PENDIENTES = {};
let selectedWeek = "4";
let selectedDay = Math.min(4, Math.max(0, new Date().getDay() - 1));
if (new Date().getDay() === 0 || new Date().getDay() === 6) selectedDay = 0;

async function loadAll() {
  const res = await fetch("/api/data");
  const json = await res.json();
  DATA = json.data;
  PENDIENTES = json.pendientes;
  if (!DATA.semanas[selectedWeek]) selectedWeek = String(DATA.semana_actual || Object.keys(DATA.semanas)[0]);
  renderWeeks();
  renderAlerts();
  renderTabs();
  renderClasses();
}

function renderWeeks() {
  const sel = document.getElementById("weekSelect");
  sel.innerHTML = "";
  Object.keys(DATA.semanas).sort((a,b)=>Number(a)-Number(b)).forEach(k => {
    const opt = document.createElement("option");
    opt.value = k;
    opt.textContent = DATA.semanas[k].nombre || ("Semana " + k);
    if (k === selectedWeek) opt.selected = true;
    sel.appendChild(opt);
  });
  sel.onchange = () => { selectedWeek = sel.value; renderClasses(); };
}

function renderAlerts() {
  const grid = document.getElementById("alertsGrid");
  grid.innerHTML = "";
  let atrasos = 0;
  DATA.horario.forEach(p => {
    const info = PENDIENTES[p.id];
    if (info && info.neto > 0) {
      atrasos++;
      const div = document.createElement("div");
      div.className = "alert-card " + (p.progresivo ? "prog" : (info.neto > 1 ? "red" : ""));
      const sems = info.perdidas.map(x => `S${x.semana} (${x.motivo || "Sin motivo"})`).join(", ");
      const decision = p.progresivo
        ? "🔵 Avance progresivo: seguir secuencia normal o enviar formulario a casa."
        : "⚡ Plan de Alcance: enviar tarea/cuestionario en Classroom y fusionar en próxima clase.";
      div.innerHTML = `<strong>${p.nivel} — ${p.paralelo}</strong> (${DIAS[p.dia]}) &bull; <b>-${info.neto} clase</b><br>
        <span style="color:var(--muted)">Perdida: ${sems}</span><br>
        <div style="margin-top:4px">${decision}</div>`;
      grid.appendChild(div);
    }
  });
  if (atrasos === 0) {
    grid.innerHTML = `<div style="color:#4ade80;font-weight:600;">🟢 ¡Todos los 21 paralelos están al día!</div>`;
  }
  document.getElementById("summaryBadge").textContent = `${21 - atrasos}/21 al día`;
}

function renderTabs() {
  const tabs = document.getElementById("dayTabs");
  tabs.innerHTML = "";
  DIAS.forEach((d, idx) => {
    const btn = document.createElement("div");
    btn.className = "tab" + (idx === selectedDay ? " active" : "");
    btn.textContent = d;
    btn.onclick = () => { selectedDay = idx; renderTabs(); renderClasses(); };
    tabs.appendChild(btn);
  });
}

function renderClasses() {
  const list = document.getElementById("classList");
  list.innerHTML = "";
  const sem = DATA.semanas[selectedWeek];
  const clases = DATA.horario.filter(p => p.dia === selectedDay);
  clases.forEach(p => {
    const reg = (sem.registros && sem.registros[p.id]) || {estado: "pendiente", motivo: "", nota: ""};
    const tema = (sem.temas && sem.temas[p.nivel]) || "";
    const card = document.createElement("div");
    card.className = "class-card";
    card.innerHTML = `
      <div class="class-info">
        <div class="class-title">${p.hora} &bull; ${p.nivel} — ${p.paralelo}</div>
        <div class="class-meta">${tema}</div>
      </div>
      <div class="class-actions">
        <button class="st-btn st-dada ${reg.estado==='dada'?'selected':''}" onclick="setEstado('${p.id}','dada')">✅ Dada</button>
        <button class="st-btn st-perdida ${reg.estado==='perdida'?'selected':''}" onclick="setEstado('${p.id}','perdida')">❌ Perdida</button>
        <button class="st-btn st-alcance ${reg.estado==='alcance'?'selected':''}" onclick="setEstado('${p.id}','alcance')">⚡ Alcance</button>
        <select onchange="setMotivo('${p.id}', this.value)" title="Motivo si se perdió">
          <option value="">Motivo...</option>
          ${["Feriado","Acto cívico","Falla técnica","Falta tiempo","Otro"].map(m => `<option ${reg.motivo===m?'selected':''}>${m}</option>`).join("")}
        </select>
        <input type="text" placeholder="Nota rápida..." value="${reg.nota||''}" onchange="setNota('${p.id}', this.value)" style="width:140px;">
      </div>
    `;
    list.appendChild(card);
  });
}

async function updateRegistro(pid, patch) {
  const res = await fetch("/api/update", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({semana: selectedWeek, paralelo_id: pid, patch})
  });
  const json = await res.json();
  DATA = json.data;
  PENDIENTES = json.pendientes;
  renderAlerts();
  renderClasses();
  showToast();
}

function setEstado(pid, estado) { updateRegistro(pid, {estado}); }
function setMotivo(pid, motivo) { updateRegistro(pid, {motivo}); }
function setNota(pid, nota) { updateRegistro(pid, {nota}); }

async function markAllDay() {
  const res = await fetch("/api/mark_day", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({semana: selectedWeek, dia: selectedDay})
  });
  const json = await res.json();
  DATA = json.data;
  PENDIENTES = json.pendientes;
  renderAlerts();
  renderClasses();
  showToast();
}

async function addNewWeek() {
  const nextNum = String(Math.max(...Object.keys(DATA.semanas).map(Number)) + 1);
  const nombre = prompt("Nombre de la nueva semana:", `Semana ${nextNum}`);
  if (!nombre) return;
  const res = await fetch("/api/new_week", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({semana: nextNum, nombre})
  });
  const json = await res.json();
  DATA = json.data;
  PENDIENTES = json.pendientes;
  selectedWeek = nextNum;
  renderWeeks();
  renderClasses();
  showToast();
}

function showToast() {
  const t = document.getElementById("toast");
  t.style.display = "block";
  setTimeout(() => t.style.display = "none", 1800);
}

loadAll();
</script>
</body>
</html>
"""


class DiarioHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def _send_json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/data":
            data = load_data()
            self._send_json({"data": data, "pendientes": compute_pendientes(data)})
        else:
            body = HTML_PAGE.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        payload = json.loads(self.rfile.read(length).decode("utf-8"))
        data = load_data()

        if self.path == "/api/update":
            sem = str(payload["semana"])
            pid = payload["paralelo_id"]
            regs = data["semanas"][sem].setdefault("registros", {})
            cur = regs.get(pid, {"estado": "pendiente", "motivo": "", "nota": ""})
            cur.update(payload["patch"])
            regs[pid] = cur
            save_data(data)

        elif self.path == "/api/mark_day":
            sem = str(payload["semana"])
            dia = int(payload["dia"])
            regs = data["semanas"][sem].setdefault("registros", {})
            for p in data["horario"]:
                if p["dia"] == dia:
                    cur = regs.get(p["id"], {"estado": "pendiente", "motivo": "", "nota": ""})
                    if cur.get("estado") in ("pendiente", ""):
                        cur["estado"] = "dada"
                    elif cur.get("estado") != "perdida":
                        cur["estado"] = "dada"
                    regs[p["id"]] = cur
            save_data(data)

        elif self.path == "/api/new_week":
            sem = str(payload["semana"])
            data["semanas"][sem] = {
                "nombre": payload["nombre"],
                "temas": {},
                "registros": {},
            }
            data["semana_actual"] = int(sem)
            save_data(data)

        self._send_json({"data": data, "pendientes": compute_pendientes(data)})


def main():
    data = load_data()
    export_markdown(data)
    server = HTTPServer(("127.0.0.1", PORT), DiarioHandler)
    url = f"http://127.0.0.1:{PORT}"
    print(f"Diario de Clases activo en {url} (Ctrl+C para cerrar)")
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


if __name__ == "__main__":
    main()
