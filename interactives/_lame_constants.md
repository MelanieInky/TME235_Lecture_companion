```{=html}
<style>
/* Light tokens. The [data-bs-theme]/body.quarto-* selectors are ANCESTOR-scoped,
   so they only bite when Quarto's own theme toggle is present — they never apply
   unconditionally the way a bare [data-theme="dark"] rule would. */
.viz-lame-c,
[data-bs-theme="light"] .viz-lame-c,
body.quarto-light .viz-lame-c {
  --fg: #1a1a1a; --fg-muted: #6b6b6b;
  --panel-bg: #f7f7f8; --border: #e2e2e4; --grid: #dcdcde;
  --slider: #555;
  --pos: #2E86AB; --neg: #C1440E; --accent: #3E8914;
}
@media (prefers-color-scheme: dark) {
  .viz-lame-c {
    --fg: #f0f0f0; --fg-muted: #a0a0a3;
    --panel-bg: #262628; --border: #3a3a3c; --grid: #38383a;
    --slider: #9a9a9d;
  }
}
[data-bs-theme="dark"] .viz-lame-c,
body.quarto-dark .viz-lame-c {
  --fg: #f0f0f0; --fg-muted: #a0a0a3;
  --panel-bg: #262628; --border: #3a3a3c; --grid: #38383a;
  --slider: #9a9a9d;
}

.viz-lame-c *, .viz-lame-c *::before, .viz-lame-c *::after {
  box-sizing: border-box;
}
.viz-lame-c {
  color: var(--fg);
  font-family: inherit;
  margin: 0 0 1.5rem;
  padding: 0;
}
.viz-lame-c .subtitle {
  text-align: center; color: var(--fg-muted); font-size: 0.88rem; margin-bottom: 20px;
}
.viz-lame-c .controls {
  display: flex; gap: 24px; flex-wrap: wrap; justify-content: center;
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 12px;
  padding: 16px 20px; margin-bottom: 18px;
}
.viz-lame-c .slider-group {
  min-width: 240px; flex: 1 1 240px; max-width: 360px;
}
.viz-lame-c .slider-group label {
  display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 5px;
}
.viz-lame-c .slider-group label .val {
  font-variant-numeric: tabular-nums; color: var(--fg-muted);
}
.viz-lame-c input[type="range"] {
  width: 100%; accent-color: var(--slider);
}
.viz-lame-c .warning {
  text-align: center; font-size: 0.78rem; font-weight: 600; padding: 6px 10px;
  border-radius: 8px; margin: 0 auto 18px; max-width: 520px; display: none;
}
.viz-lame-c .warning.show {
  display: block; background: rgba(193,68,14,0.18); color: var(--neg);
}
.viz-lame-c .layout {
  display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 18px; align-items: start;
}
@media (max-width: 760px) {
  .viz-lame-c .layout {
    grid-template-columns: 1fr;
  }
}
.viz-lame-c .panel {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 12px; padding: 14px 16px;
}
.viz-lame-c .panel h3 {
  font-size: 0.85rem; margin: 0 0 10px; color: var(--fg-muted); font-weight: 600;
}
.viz-lame-c .readouts {
  font-size: 0.86rem; line-height: 1.9;
}
.viz-lame-c .readouts .row {
  display: flex; justify-content: space-between; border-bottom: 1px dashed var(--border); padding: 2px 0;
}
.viz-lame-c .readouts .row span:last-child {
  font-variant-numeric: tabular-nums;
}
.viz-lame-c .formula {
  font-size: 0.75rem; color: var(--fg-muted); margin-top: 10px; line-height: 1.6;
}
.viz-lame-c svg {
  display: block; margin: 0 auto; width: 100%; height: auto; max-width: 460px;
}
.viz-lame-c .heat-label {
  font-size: 9px; fill: var(--fg-muted);
}
.viz-lame-c .heat-val {
  font-size: 9.5px; font-weight: 600;
}
.viz-lame-c .note {
  max-width: 720px; margin: 20px auto 0; font-size: 0.78rem; color: var(--fg-muted);
  line-height: 1.5; text-align: center;
}
</style>

<div class="viz-lame-c">
<div class="subtitle">Live isotropic elasticity conversion and 6×6 Voigt stiffness matrix (order 11,22,33,23,13,12)</div>

  <div class="controls">
    <div class="slider-group">
      <label for="lc-E">E (Young's modulus) <span class="val" id="lc-vE">70 GPa</span></label>
      <input type="range" id="lc-E" min="10" max="300" step="1" value="70">
    </div>
    <div class="slider-group">
      <label for="lc-nu">ν (Poisson's ratio) <span class="val" id="lc-vNu">0.330</span></label>
      <input type="range" id="lc-nu" min="-0.90" max="0.49" step="0.005" value="0.33">
    </div>
  </div>

  <div class="warning" id="lc-warn">Approaching the incompressible limit (ν → 0.5): λ and K diverge. Common for rubber-like materials; not physical for most metals/alloys.</div>

  <div class="layout">
    <div class="panel">
      <h3>DERIVED CONSTANTS</h3>
      <div class="readouts">
        <div class="row"><span>λ (Lamé's first parameter)</span><span id="lc-r-lambda"></span></div>
        <div class="row"><span>μ = G (shear modulus)</span><span id="lc-r-mu"></span></div>
        <div class="row"><span>K (bulk modulus)</span><span id="lc-r-K"></span></div>
      </div>
      <div class="formula">
        μ = E / [2(1+ν)] &nbsp;·&nbsp; λ = Eν / [(1+ν)(1−2ν)] &nbsp;·&nbsp; K = E / [3(1−2ν)] = λ + 2μ/3
      </div>

      <h3 style="margin-top:18px">λ(ν) AT FIXED E — SINGULARITY AT ν=0.5</h3>
      <svg id="lc-svg-curve" viewBox="0 0 320 180"></svg>
    </div>

    <div class="panel">
      <h3>ISOTROPIC STIFFNESS MATRIX C (VOIGT)</h3>
      <svg id="lc-svg-heat" viewBox="0 0 300 300"></svg>
    </div>
  </div>

  <div class="note">
    C relates Voigt stress and (engineering-shear) strain vectors: σ_V = C·ε_V, with the diagonal shear
    terms equal to μ (not 2μ) because γ_ij = 2ε_ij already carries the factor of two. Off-diagonal 4-5-6
    blocks are zero for an isotropic material — normal and shear response never couple. λ is linear in E
    at fixed ν, so moving the E slider rescales the λ(ν) curve without changing its shape — watch the
    axis numbers, not the outline.
  </div>


<script>
(function(){
  const root = document.querySelector(".viz-lame-c");
  if (!root) return;
  const __q = (id) => root.querySelector("#" + id);

const Eel = __q('lc-E');
const nuEl = __q('lc-nu');
const vE = __q('lc-vE');
const vNu = __q('lc-vNu');

function computeConstants(E, nu) {
  const mu = E / (2 * (1 + nu));
  const lambda = (E * nu) / ((1 + nu) * (1 - 2 * nu));
  const K = E / (3 * (1 - 2 * nu));
  return { mu, lambda, K };
}

function lambdaOf(E, nu) {
  return (E * nu) / ((1 + nu) * (1 - 2 * nu));
}

// Alpha-blended fill rather than blending toward a hard-coded light background:
// the old version mixed toward #f7f7f8, so in dark mode small-magnitude cells came
// out near-white behind light --fg text.
function colorFor(val, maxAbs) {
  if (val === 0) return 'none';
  const t = Math.min(Math.abs(val) / maxAbs, 1);
  const base = val > 0 ? '46,134,171' : '193,68,14'; // pos blue, neg red
  return `rgba(${base},${(0.12 + 0.88 * t).toFixed(3)})`;
}

function drawHeatmap(lambda, mu) {
  const M = [
    [lambda+2*mu, lambda, lambda, 0,0,0],
    [lambda, lambda+2*mu, lambda, 0,0,0],
    [lambda, lambda, lambda+2*mu, 0,0,0],
    [0,0,0, mu,0,0],
    [0,0,0,0, mu,0],
    [0,0,0,0,0, mu],
  ];
  const maxAbs = Math.max(Math.abs(lambda+2*mu), Math.abs(lambda), Math.abs(mu), 1e-6);
  const cell = 44, pad = 30;
  const svg = __q('lc-svg-heat');
  let html = '';
  const labels = ['11','22','33','23','13','12'];

  for (let i = 0; i < 6; i++) {
    html += `<text x="${pad - 6}" y="${pad + i*cell + cell/2 + 3}" text-anchor="end" class="heat-label">${labels[i]}</text>`;
    html += `<text x="${pad + i*cell + cell/2}" y="${pad - 10}" text-anchor="middle" class="heat-label">${labels[i]}</text>`;
  }

  for (let i = 0; i < 6; i++) {
    for (let j = 0; j < 6; j++) {
      const val = M[i][j];
      const x = pad + j*cell, y = pad + i*cell;
      html += `<rect x="${x}" y="${y}" width="${cell-2}" height="${cell-2}" fill="${colorFor(val, maxAbs)}" stroke="var(--border)" stroke-width="0.5"/>`;
      const textColor = Math.abs(val)/maxAbs > 0.55 ? '#fff' : 'var(--fg)';
      const label = val === 0 ? '0' : (Math.abs(val) >= 100 ? val.toFixed(0) : val.toFixed(1));
      html += `<text x="${x + (cell-2)/2}" y="${y + (cell-2)/2 + 3}" text-anchor="middle" class="heat-val" fill="${textColor}">${label}</text>`;
    }
  }
  svg.innerHTML = html;
}

function drawCurve(E, nu) {
  const svg = __q('lc-svg-curve');
  const W = 320, H = 180, ml = 44, mr = 10, mt = 12, mb = 26;
  const nuMin = -0.9, nuMax = 0.49;
  const yCap = 4 * E; // display window; scales with E, so the axis numbers carry the E dependence

  const xScale = (v) => ml + (v - nuMin) / (nuMax - nuMin) * (W - ml - mr);
  const yScale = (v) => H - mb - (v + yCap) / (2 * yCap) * (H - mt - mb);

  // Break the path where lambda leaves the window instead of clamping it: clamping
  // drew flat horizontal runs at +/-yCap that read as a plateau rather than a blow-up.
  const N = 400;
  let path = '', pen = false;
  for (let k = 0; k <= N; k++) {
    const nv = nuMin + (nuMax - nuMin) * k / N;
    const lam = lambdaOf(E, nv);
    if (!isFinite(lam) || Math.abs(lam) > yCap) { pen = false; continue; }
    path += `${pen ? ' L' : ' M'} ${xScale(nv).toFixed(1)} ${yScale(lam).toFixed(1)}`;
    pen = true;
  }

  const lamNow = lambdaOf(E, nu);
  const inView = Math.abs(lamNow) <= yCap;
  const cx = xScale(nu), cy = yScale(Math.max(-yCap, Math.min(yCap, lamNow)));
  const zeroY = yScale(0);
  const asymptoteX = xScale(0.5);
  const zeroNuX = xScale(0);
  const capLabel = yCap >= 100 ? yCap.toFixed(0) : yCap.toFixed(1);

  svg.innerHTML = `
    <line x1="${ml}" y1="${zeroY}" x2="${W-mr}" y2="${zeroY}" stroke="var(--grid)" stroke-width="1"/>
    <line x1="${zeroNuX}" y1="${mt}" x2="${zeroNuX}" y2="${H-mb}" stroke="var(--grid)" stroke-width="1"/>
    <line x1="${asymptoteX}" y1="${mt}" x2="${asymptoteX}" y2="${H-mb}" stroke="var(--neg)" stroke-width="1" stroke-dasharray="3,3"/>
    <text x="${asymptoteX}" y="${mt+8}" font-size="8.5" fill="var(--neg)" text-anchor="middle">ν=0.5</text>
    <path d="${path.trim()}" fill="none" stroke="var(--accent)" stroke-width="2"/>
    <circle cx="${cx}" cy="${cy}" r="4" fill="${inView ? 'var(--accent)' : 'none'}" stroke="var(--accent)" stroke-width="1.6"/>
    <text x="${ml - 4}" y="${mt + 8}" font-size="8.5" fill="var(--fg-muted)" text-anchor="end">${capLabel}</text>
    <text x="${ml - 4}" y="${zeroY + 3}" font-size="8.5" fill="var(--fg-muted)" text-anchor="end">0</text>
    <text x="${ml - 4}" y="${H - mb}" font-size="8.5" fill="var(--fg-muted)" text-anchor="end">−${capLabel}</text>
    <text x="4" y="${mt + 8}" font-size="8.5" fill="var(--fg-muted)">λ</text>
    <text x="4" y="${mt + 18}" font-size="7.5" fill="var(--fg-muted)">GPa</text>
    <text x="${ml}" y="${H-6}" font-size="8.5" fill="var(--fg-muted)">ν=${nuMin}</text>
    <text x="${zeroNuX}" y="${H-6}" font-size="8.5" fill="var(--fg-muted)" text-anchor="middle">0</text>
    <text x="${W-mr}" y="${H-6}" font-size="8.5" fill="var(--fg-muted)" text-anchor="end">ν=0.49</text>
  `;
}

function update() {
  const E = parseFloat(Eel.value);
  const nu = parseFloat(nuEl.value);
  vE.textContent = `${E} GPa`;
  vNu.textContent = nu.toFixed(3);

  const { mu, lambda, K } = computeConstants(E, nu);

  __q('lc-r-lambda').textContent = `${lambda.toFixed(1)} GPa`;
  __q('lc-r-mu').textContent = `${mu.toFixed(1)} GPa`;
  __q('lc-r-K').textContent = `${K.toFixed(1)} GPa`;

  const warn = __q('lc-warn');
  warn.classList.toggle('show', nu > 0.45);

  drawHeatmap(lambda, mu);
  drawCurve(E, nu);
}

Eel.addEventListener('input', update);
nuEl.addEventListener('input', update);
update();
})();
</script>
</div>
```
