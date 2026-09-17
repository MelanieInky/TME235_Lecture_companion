```{=html}
<style>
.viz-strain {
  --bg: #ffffff;
    --fg: #1a1a1a;
    --fg-muted: #6b6b6b;
    --panel-bg: #f7f7f8;
    --border: #e2e2e4;
    --accent-sph: #2E86AB;
    --accent-dev: #C1440E;
    --accent-tot: #3E8914;
    --grid: #e8e8ea;
}
@media (prefers-color-scheme: dark) {
  .viz-strain {
    --bg: #1c1c1e;
      --fg: #f0f0f0;
      --fg-muted: #a0a0a3;
      --panel-bg: #262628;
      --border: #3a3a3c;
      --grid: #333335;
  }
}
.viz-strain *, .viz-strain *::before, .viz-strain *::after {
  box-sizing: border-box;
}
.viz-strain {
  background: var(--bg);
    color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 24px 16px 40px;
}
.viz-strain .wrap {
  max-width: 1080px; margin: 0 auto;
}
.viz-strain h1 {
  font-size: 1.3rem;
    font-weight: 600;
    text-align: center;
    margin: 0 0 4px;
}
.viz-strain .subtitle {
  text-align: center;
    color: var(--fg-muted);
    font-size: 0.9rem;
    margin-bottom: 24px;
}
.viz-strain .controls {
  display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    background: var(--panel-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px 20px;
    margin-bottom: 22px;
}
.viz-strain .slider-group {
  display: flex;
    flex-direction: column;
    min-width: 210px;
    flex: 1 1 210px;
    max-width: 300px;
}
.viz-strain .slider-group label {
  display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    margin-bottom: 6px;
}
.viz-strain .slider-group label .val {
  font-variant-numeric: tabular-nums;
    color: var(--fg-muted);
}
.viz-strain input[type="range"] {
  width: 100%;
    accent-color: #555;
}
.viz-strain .presets {
  display: flex;
    gap: 8px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 22px;
}
.viz-strain .presets button {
  font-size: 0.8rem;
    padding: 6px 12px;
    border-radius: 999px;
    border: 1px solid var(--border);
    background: var(--panel-bg);
    color: var(--fg);
    cursor: pointer;
}
.viz-strain .presets button:hover {
  border-color: var(--fg-muted);
}
.viz-strain .panels {
  display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}
@media (max-width: 720px) {
  .viz-strain .panels {
    grid-template-columns: 1fr;
  }
}
.viz-strain .panel {
  background: var(--panel-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px 12px 16px;
    text-align: center;
    overflow-x: auto;
}
.viz-strain .panel h2 {
  font-size: 0.92rem;
    font-weight: 600;
    margin: 4px 0 2px;
}
.viz-strain .panel .desc {
  font-size: 0.78rem;
    color: var(--fg-muted);
    margin-bottom: 8px;
}
.viz-strain .panel .area {
  font-size: 0.78rem;
    color: var(--fg-muted);
    margin-top: 6px;
}
.viz-strain svg {
  display: block; margin: 0 auto; max-width: 100%; height: auto;
}
.viz-strain .matrix-row {
  display: flex;
    justify-content: center;
    gap: 28px;
    flex-wrap: wrap;
    margin-top: 22px;
    font-size: 0.85rem;
}
.viz-strain .matrix-block {
  text-align: center;
}
.viz-strain .matrix-block .label {
  color: var(--fg-muted); margin-bottom: 4px; font-size: 0.78rem;
}
.viz-strain table.mat {
  border-collapse: collapse;
    margin: 0 auto;
}
.viz-strain table.mat td {
  padding: 2px 10px;
    font-variant-numeric: tabular-nums;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
}
.viz-strain table.mat tr:first-child td {
  border-top: 1.5px solid var(--fg-muted);
}
.viz-strain table.mat tr:last-child td {
  border-bottom: 1.5px solid var(--fg-muted);
}
.viz-strain .note {
  max-width: 640px;
    margin: 26px auto 0;
    font-size: 0.8rem;
    color: var(--fg-muted);
    line-height: 1.5;
    text-align: center;
}
.viz-strain svg { width: 100%; height: auto; max-width: 460px; }
.viz-strain .legend span { white-space: nowrap; }
.viz-strain { margin: 0 0 1.5rem; padding: 0; font-family: inherit; }
</style>

<div class="viz-strain">
<div class="subtitle">ε = ε<sub>sph</sub> + ε<sub>dev</sub> — drag the sliders to set ε₁₁, ε₂₂, ε₁₂</div>

  <div class="controls">
    <div class="slider-group">
      <label>ε₁₁ <span class="val" id="sd-v11">0.18</span></label>
      <input type="range" id="sd-e11" min="-0.4" max="0.4" step="0.01" value="0.18">
    </div>
    <div class="slider-group">
      <label>ε₂₂ <span class="val" id="sd-v22">-0.06</span></label>
      <input type="range" id="sd-e22" min="-0.4" max="0.4" step="0.01" value="-0.06">
    </div>
    <div class="slider-group">
      <label>ε₁₂ = ε₂₁ <span class="val" id="sd-v12">0.10</span></label>
      <input type="range" id="sd-e12" min="-0.4" max="0.4" step="0.01" value="0.10">
    </div>
  </div>

  <div class="presets">
    <button data-e="0.2,0.2,0">Pure dilation</button>
    <button data-e="0.2,-0.2,0">Pure deviatoric (uniaxial)</button>
    <button data-e="0,0,0.25">Pure shear</button>
    <button data-e="0.15,0.05,0.15">Mixed</button>
    <button data-e="0,0,0">Reset to zero</button>
  </div>

  <div class="panels">
    <div class="panel">
      <h2 style="color:var(--accent-sph)">Volumetric (spherical)</h2>
      <div class="desc">ε<sub>sph</sub> = ε<sub>v</sub> I — area change, no shape change</div>
      <svg id="sd-svg-sph" viewBox="-100 -100 200 200"></svg>
      <div class="area" id="sd-area-sph"></div>
    </div>
    <div class="panel">
      <h2 style="color:var(--accent-dev)">Deviatoric</h2>
      <div class="desc">ε<sub>dev</sub> = ε − ε<sub>v</sub> I — shape change, tr = 0</div>
      <svg id="sd-svg-dev" viewBox="-100 -100 200 200"></svg>
      <div class="area" id="sd-area-dev"></div>
    </div>
    <div class="panel">
      <h2 style="color:var(--accent-tot)">Total strain</h2>
      <div class="desc">ε = ε<sub>sph</sub> + ε<sub>dev</sub></div>
      <svg id="sd-svg-tot" viewBox="-100 -100 200 200"></svg>
      <div class="area" id="sd-area-tot"></div>
    </div>
  </div>

  <div class="matrix-row">
    <div class="matrix-block">
      <div class="label">ε</div>
      <table class="mat" id="sd-mat-full"></table>
    </div>
    <div class="matrix-block">
      <div class="label">ε<sub>sph</sub> = ε<sub>v</sub>I, ε<sub>v</sub> = ½tr(ε)</div>
      <table class="mat" id="sd-mat-sph"></table>
    </div>
    <div class="matrix-block">
      <div class="label">ε<sub>dev</sub> (tr = 0)</div>
      <table class="mat" id="sd-mat-dev"></table>
    </div>
  </div>

  <div class="note">
    Squares are drawn with the finite map x′ = (I + ε)x for visual clarity, not the strict
    infinitesimal linearization — so at large strain the "area-preserving" property of the
    deviatoric part is only approximate (visible as small drift in the reported areas).
  </div>


<script>
(function(){
  const root = document.querySelector(".viz-strain");
  if (!root) return;
  const __q = (id) => root.querySelector("#" + id);

const els = {
  e11: __q('sd-e11'),
  e22: __q('sd-e22'),
  e12: __q('sd-e12'),
};
const valEls = {
  e11: __q('sd-v11'),
  e22: __q('sd-v22'),
  e12: __q('sd-v12'),
};

const square = [[-50,-50],[50,-50],[50,50],[-50,50]];

function matVec(F, p) {
  return [F[0][0]*p[0] + F[0][1]*p[1], F[1][0]*p[0] + F[1][1]*p[1]];
}

function polygonArea(pts) {
  let a = 0;
  for (let i = 0; i < pts.length; i++) {
    const [x1,y1] = pts[i];
    const [x2,y2] = pts[(i+1) % pts.length];
    a += x1*y2 - x2*y1;
  }
  return Math.abs(a) / 2;
}

function drawPanel(svgId, e, color) {
  const svg = __q('sd-' + svgId);
  const F = [[1+e[0][0], e[0][1]], [e[1][0], 1+e[1][1]]];
  const defPts = square.map(p => matVec(F, p));
  const origPath = square.map(p => p.join(',')).join(' ');
  const defPath = defPts.map(p => p.join(',')).join(' ');

  svg.innerHTML = `
    <line x1="-100" y1="0" x2="100" y2="0" stroke="var(--grid)" stroke-width="1"/>
    <line x1="0" y1="-100" x2="0" y2="100" stroke="var(--grid)" stroke-width="1"/>
    <polygon points="${origPath}" fill="none" stroke="var(--fg-muted)" stroke-width="1.5" stroke-dasharray="5,4"/>
    <polygon points="${defPath}" fill="${color}" fill-opacity="0.22" stroke="${color}" stroke-width="2.5"/>
  `;
  return polygonArea(defPts) / polygonArea(square);
}

function fmt(x) {
  return (x >= 0 ? ' ' : '') + x.toFixed(3);
}

function matTable(id, m) {
  __q('sd-' + id).innerHTML = `
    <tr><td>${fmt(m[0][0])}</td><td>${fmt(m[0][1])}</td></tr>
    <tr><td>${fmt(m[1][0])}</td><td>${fmt(m[1][1])}</td></tr>
  `;
}

function update() {
  const e11 = parseFloat(els.e11.value);
  const e22 = parseFloat(els.e22.value);
  const e12 = parseFloat(els.e12.value);

  valEls.e11.textContent = e11.toFixed(2);
  valEls.e22.textContent = e22.toFixed(2);
  valEls.e12.textContent = e12.toFixed(2);

  const eps = [[e11, e12], [e12, e22]];
  const ev = 0.5 * (e11 + e22);
  const sph = [[ev, 0], [0, ev]];
  const dev = [[e11 - ev, e12], [e12, e22 - ev]];

  const aSph = drawPanel('svg-sph', sph, getComputedStyle(root).getPropertyValue('--accent-sph').trim());
  const aDev = drawPanel('svg-dev', dev, getComputedStyle(root).getPropertyValue('--accent-dev').trim());
  const aTot = drawPanel('svg-tot', eps, getComputedStyle(root).getPropertyValue('--accent-tot').trim());

  __q('sd-area-sph').textContent = `area = ${aSph.toFixed(3)} (orig. 1.000)`;
  __q('sd-area-dev').textContent = `area = ${aDev.toFixed(3)} (orig. 1.000)`;
  __q('sd-area-tot').textContent = `area = ${aTot.toFixed(3)} (orig. 1.000)`;

  matTable('mat-full', eps);
  matTable('mat-sph', sph);
  matTable('mat-dev', dev);
}

Object.values(els).forEach(el => el.addEventListener('input', update));

root.querySelectorAll('.presets button').forEach(btn => {
  btn.addEventListener('click', () => {
    const [a,b,c] = btn.dataset.e.split(',').map(Number);
    els.e11.value = a; els.e22.value = b; els.e12.value = c;
    update();
  });
});

update();
})();
</script>
</div>
```
