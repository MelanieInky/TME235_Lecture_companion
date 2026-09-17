```{=html}
<style>
.viz-pi {
  --bg: #ffffff;
    --fg: #1a1a1a;
    --fg-muted: #6b6b6b;
    --panel-bg: #f7f7f8;
    --border: #e2e2e4;
    --vm: #2E86AB;
    --tresca: #C1440E;
    --point: #3E8914;
    --grid: #dcdcde;
    --inside: #3E8914;
    --outside: #C1440E;
}
@media (prefers-color-scheme: dark) {
  .viz-pi {
    --bg: #1c1c1e; --fg: #f0f0f0; --fg-muted: #a0a0a3;
      --panel-bg: #262628; --border: #3a3a3c; --grid: #38383a;
  }
}
.viz-pi *, .viz-pi *::before, .viz-pi *::after {
  box-sizing: border-box;
}
.viz-pi {
  background: var(--bg); color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    margin: 0; padding: 24px 16px 40px;
}
.viz-pi .wrap {
  max-width: 1080px; margin: 0 auto;
}
.viz-pi h1 {
  font-size: 1.3rem; font-weight: 600; text-align: center; margin: 0 0 4px;
}
.viz-pi .subtitle {
  text-align: center; color: var(--fg-muted); font-size: 0.9rem; margin-bottom: 22px;
}
.viz-pi .layout {
  display: grid; grid-template-columns: 300px 1fr; gap: 20px; align-items: start;
}
@media (max-width: 760px) {
  .viz-pi .layout {
    grid-template-columns: 1fr;
  }
}
.viz-pi .controls {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 12px;
    padding: 16px 18px;
}
.viz-pi .controls h3 {
  font-size: 0.85rem; margin: 0 0 10px; color: var(--fg-muted); font-weight: 600;
}
.viz-pi .slider-group {
  margin-bottom: 14px;
}
.viz-pi .slider-group label {
  display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 5px;
}
.viz-pi .slider-group label .val {
  font-variant-numeric: tabular-nums; color: var(--fg-muted);
}
.viz-pi input[type="range"] {
  width: 100%; accent-color: #555;
}
.viz-pi .presets {
  display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px;
}
.viz-pi .presets button {
  font-size: 0.75rem; padding: 5px 10px; border-radius: 999px;
    border: 1px solid var(--border); background: var(--bg); color: var(--fg); cursor: pointer;
}
.viz-pi .presets button:hover {
  border-color: var(--fg-muted);
}
.viz-pi .readouts {
  margin-top: 14px; font-size: 0.8rem; line-height: 1.7;
}
.viz-pi .readouts .row {
  display: flex; justify-content: space-between;
}
.viz-pi .readouts .row span:last-child {
  font-variant-numeric: tabular-nums;
}
.viz-pi .status {
  margin-top: 10px; padding: 8px 10px; border-radius: 8px; font-size: 0.78rem; font-weight: 600; text-align: center;
}
.viz-pi .plot-panel {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 12px;
    padding: 14px; text-align: center;
}
.viz-pi svg {
  display: block; margin: 0 auto; max-width: 100%; height: auto;
}
.viz-pi .legend {
  display: flex; justify-content: center; gap: 18px; margin-top: 10px; font-size: 0.78rem; color: var(--fg-muted);
}
.viz-pi .legend .swatch {
  display: inline-block; width: 14px; height: 3px; margin-right: 5px; vertical-align: middle;
}
.viz-pi .note {
  max-width: 720px; margin: 22px auto 0; font-size: 0.8rem; color: var(--fg-muted);
    line-height: 1.5; text-align: center;
}
.viz-pi svg { width: 100%; height: auto; max-width: 460px; }
.viz-pi .legend span { white-space: nowrap; }
.viz-pi { margin: 0 0 1.5rem; padding: 0; font-family: inherit; }
</style>

<div class="viz-pi">
<div class="subtitle">Deviatoric plane σ₁+σ₂+σ₃ = const, projected orthogonal to the hydrostatic axis (1,1,1)</div>

  <div class="layout">
    <div class="controls">
      <h3>PRINCIPAL STRESSES</h3>
      <div class="slider-group">
        <label>σ₁ <span class="val" id="pi-v1">200</span></label>
        <input type="range" id="pi-s1" min="-300" max="300" step="1" value="200">
      </div>
      <div class="slider-group">
        <label>σ₂ <span class="val" id="pi-v2">0</span></label>
        <input type="range" id="pi-s2" min="-300" max="300" step="1" value="0">
      </div>
      <div class="slider-group">
        <label>σ₃ <span class="val" id="pi-v3">0</span></label>
        <input type="range" id="pi-s3" min="-300" max="300" step="1" value="0">
      </div>
      <h3 style="margin-top:16px">YIELD STRESS</h3>
      <div class="slider-group">
        <label>σ_y <span class="val" id="pi-vy">200</span></label>
        <input type="range" id="pi-sy" min="50" max="300" step="1" value="200">
      </div>

      <div class="presets">
        <button data-s="200,0,0">Uniaxial tension</button>
        <button data-s="-200,0,0">Uniaxial compression</button>
        <button data-s="115,-115,0">Pure shear</button>
        <button data-s="200,200,0">Equibiaxial</button>
        <button data-s="100,50,-50">Mixed</button>
      </div>

      <div class="readouts">
        <div class="row"><span>σ_m (hydrostatic)</span><span id="pi-r-sm"></span></div>
        <div class="row"><span>σ_vm (Von Mises)</span><span id="pi-r-vm"></span></div>
        <div class="row"><span>σ_tresca (σ_max−σ_min)</span><span id="pi-r-tr"></span></div>
      </div>
      <div class="status" id="pi-status"></div>
    </div>

    <div class="plot-panel">
      <svg id="pi-svg-pi" viewBox="-245 -245 490 490"></svg>
      <div class="legend">
        <span><span class="swatch" style="background:var(--vm)"></span>Von Mises</span>
        <span><span class="swatch" style="background:var(--tresca)"></span>Tresca</span>
        <span><span class="swatch" style="background:var(--point)"></span>stress state</span>
      </div>
    </div>
  </div>

  <div class="note">
    The two criteria always agree exactly at the hexagon's corners (uniaxial-like states, where two
    principal stresses coincide) and diverge most at the corners' midpoints (pure-shear-like states),
    where Tresca is more conservative by a factor of 2/√3 ≈ 1.155. Motion purely along the hydrostatic
    axis (σ₁=σ₂=σ₃) doesn't move the point in this plane at all — both criteria are pressure-independent.
  </div>


<script>
(function(){
  const root = document.querySelector(".viz-pi");
  if (!root) return;
  const __q = (id) => root.querySelector("#" + id);

const els = {
  s1: __q('pi-s1'),
  s2: __q('pi-s2'),
  s3: __q('pi-s3'),
  sy: __q('pi-sy'),
};
const valEls = {
  s1: __q('pi-v1'),
  s2: __q('pi-v2'),
  s3: __q('pi-v3'),
  sy: __q('pi-vy'),
};

const SCALE = 0.55; // data units -> svg units

function project(s1, s2, s3) {
  const sm = (s1 + s2 + s3) / 3;
  const d1 = s1 - sm, d2 = s2 - sm, d3 = s3 - sm;
  const x = (2 * d1 - d2 - d3) / Math.sqrt(6);
  const y = (d2 - d3) / Math.sqrt(2);
  return { x, y, sm };
}

function hexagonPoints(Rvm) {
  const pts = [];
  for (let k = 0; k < 6; k++) {
    const theta = k * Math.PI / 3;
    pts.push([Rvm * Math.cos(theta) * SCALE, -Rvm * Math.sin(theta) * SCALE]);
  }
  return pts.map(p => p.join(',')).join(' ');
}

function update() {
  const s1 = parseFloat(els.s1.value);
  const s2 = parseFloat(els.s2.value);
  const s3 = parseFloat(els.s3.value);
  const sy = parseFloat(els.sy.value);

  valEls.s1.textContent = s1.toFixed(0);
  valEls.s2.textContent = s2.toFixed(0);
  valEls.s3.textContent = s3.toFixed(0);
  valEls.sy.textContent = sy.toFixed(0);

  const svm = Math.sqrt(0.5 * ((s1 - s2) ** 2 + (s2 - s3) ** 2 + (s3 - s1) ** 2));
  const stresca = Math.max(s1, s2, s3) - Math.min(s1, s2, s3);
  const { x, y, sm } = project(s1, s2, s3);

  __q('pi-r-sm').textContent = sm.toFixed(1);
  __q('pi-r-vm').textContent = svm.toFixed(1);
  __q('pi-r-tr').textContent = stresca.toFixed(1);

  const statusEl = __q('pi-status');
  const vmYield = svm >= sy;
  const trYield = stresca >= sy;
  if (vmYield && trYield) {
    statusEl.textContent = 'Outside both surfaces (yielded)';
    statusEl.style.background = 'rgba(193,68,14,0.18)';
    statusEl.style.color = '#C1440E';
  } else if (!vmYield && !trYield) {
    statusEl.textContent = 'Inside both surfaces (elastic)';
    statusEl.style.background = 'rgba(62,137,20,0.18)';
    statusEl.style.color = '#3E8914';
  } else {
    statusEl.textContent = 'Between criteria — Tresca yields, Von Mises doesn\'t (or vice versa)';
    statusEl.style.background = 'rgba(176,137,0,0.18)';
    statusEl.style.color = '#b08900';
  }

  const Rvm = Math.sqrt(2 / 3) * sy;
  const svg = __q('pi-svg-pi');
  const px = x * SCALE, py = -y * SCALE;

  // axis directions for σ1, σ2, σ3 projected (labels)
  const axisLen = 210;
  const axes = [0, 2 * Math.PI / 3, 4 * Math.PI / 3].map((theta, i) => {
    const ax = axisLen * Math.cos(theta), ay = -axisLen * Math.sin(theta);
    return { ax, ay, label: ['σ₁', 'σ₂', 'σ₃'][i] };
  });

  svg.innerHTML = `
    ${axes.map(a => `<line x1="0" y1="0" x2="${a.ax}" y2="${a.ay}" stroke="var(--grid)" stroke-width="1" stroke-dasharray="3,3"/>
      <text x="${a.ax * 1.06}" y="${a.ay * 1.06}" font-size="13" fill="var(--fg-muted)" text-anchor="middle">${a.label}</text>`).join('')}
    <circle cx="0" cy="0" r="${Rvm * SCALE}" fill="none" stroke="var(--vm)" stroke-width="2.5"/>
    <polygon points="${hexagonPoints(Rvm)}" fill="none" stroke="var(--tresca)" stroke-width="2.5"/>
    <line x1="0" y1="0" x2="${px}" y2="${py}" stroke="var(--point)" stroke-width="1.5" stroke-dasharray="4,3"/>
    <circle cx="${px}" cy="${py}" r="6" fill="var(--point)" stroke="var(--bg)" stroke-width="1.5"/>
  `;
}

Object.values(els).forEach(el => el.addEventListener('input', update));
root.querySelectorAll('.presets button').forEach(btn => {
  btn.addEventListener('click', () => {
    const [a, b, c] = btn.dataset.s.split(',').map(Number);
    els.s1.value = a; els.s2.value = b; els.s3.value = c;
    update();
  });
});

update();
})();
</script>
</div>
```
