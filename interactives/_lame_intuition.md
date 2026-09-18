```{=html}
<style>
/* Light tokens. The [data-bs-theme]/body.quarto-* selectors are ANCESTOR-scoped,
   so they only bite when Quarto's own theme toggle is present — they never apply
   unconditionally the way a bare [data-theme="dark"] rule would. */
.viz-lame-i,
[data-bs-theme="light"] .viz-lame-i,
body.quarto-light .viz-lame-i {
  --fg: #1a1a1a; --fg-muted: #6b6b6b;
  --panel-bg: #f7f7f8; --border: #e2e2e4; --grid: #dcdcde;
  --slider: #555;
  --mat: #2E86AB; --push: #C1440E; --pull: #3E8914; --wall: #6b6b6b;
}
@media (prefers-color-scheme: dark) {
  .viz-lame-i {
    --fg: #f0f0f0; --fg-muted: #a0a0a3;
    --panel-bg: #262628; --border: #3a3a3c; --grid: #38383a;
    --slider: #9a9a9d; --wall: #8a8a8d;
  }
}
[data-bs-theme="dark"] .viz-lame-i,
body.quarto-dark .viz-lame-i {
  --fg: #f0f0f0; --fg-muted: #a0a0a3;
  --panel-bg: #262628; --border: #3a3a3c; --grid: #38383a;
  --slider: #9a9a9d; --wall: #8a8a8d;
}

.viz-lame-i *, .viz-lame-i *::before, .viz-lame-i *::after {
  box-sizing: border-box;
}
.viz-lame-i {
  color: var(--fg);
  font-family: inherit;
  margin: 0 0 1.5rem;
  padding: 0;
}
.viz-lame-i .subtitle {
  text-align: center; color: var(--fg-muted); font-size: 0.88rem; margin-bottom: 18px;
}
.viz-lame-i .controls {
  display: flex; gap: 24px; flex-wrap: wrap; justify-content: center;
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 12px;
  padding: 14px 20px; margin-bottom: 20px;
}
.viz-lame-i .slider-group {
  min-width: 200px; flex: 1 1 200px; max-width: 260px;
}
.viz-lame-i .slider-group label {
  display: flex; justify-content: space-between; font-size: 0.83rem; margin-bottom: 4px;
}
.viz-lame-i .slider-group label .val {
  font-variant-numeric: tabular-nums; color: var(--fg-muted);
}
.viz-lame-i input[type="range"] {
  width: 100%; accent-color: var(--slider);
}
.viz-lame-i .panels {
  display: grid; grid-template-columns: 1fr 1fr; gap: 16px;
}
@media (max-width: 720px) {
  .viz-lame-i .panels {
    grid-template-columns: 1fr;
  }
}
.viz-lame-i .panel {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 12px; padding: 14px; text-align: center;
}
.viz-lame-i .panel h2 {
  font-size: 0.95rem; margin: 2px 0 2px;
}
.viz-lame-i .panel .desc {
  font-size: 0.78rem; color: var(--fg-muted); margin-bottom: 10px;
}
.viz-lame-i svg {
  display: block; margin: 0 auto; width: 100%; height: auto; max-width: 460px;
}
.viz-lame-i .panel .readout {
  margin-top: 10px; font-size: 0.85rem; font-variant-numeric: tabular-nums;
}
.viz-lame-i .panel .readout b {
  font-weight: 700;
}
.viz-lame-i .warning {
  text-align: center; font-size: 0.78rem; font-weight: 600; padding: 6px 10px;
  border-radius: 8px; margin: 0 auto 16px; max-width: 560px; display: none;
  background: rgba(193,68,14,0.18); color: var(--push);
}
.viz-lame-i .warning.show {
  display: block;
}
.viz-lame-i .note {
  max-width: 760px; margin: 20px auto 0; font-size: 0.8rem; color: var(--fg-muted);
  line-height: 1.55; text-align: center;
}
</style>

<div class="viz-lame-i">
<div class="subtitle">μ resists <i>shape</i> change; λ is the stress that shows up sideways when shape change is prevented</div>

  <div class="controls">
    <div class="slider-group">
      <label for="li-mu">μ (shear modulus) <span class="val" id="li-vMu">40 GPa</span></label>
      <input type="range" id="li-mu" min="5" max="100" step="1" value="40">
    </div>
    <div class="slider-group">
      <label for="li-lambda">λ (Lamé's 1st parameter) <span class="val" id="li-vLambda">60 GPa</span></label>
      <input type="range" id="li-lambda" min="-20" max="150" step="1" value="60">
    </div>
  </div>

  <div class="warning" id="li-warn">Unstable isotropic material: stability needs μ &gt; 0 <i>and</i> 3λ+2μ &gt; 0 (i.e. K &gt; 0). Strains are not reported here.</div>

  <div class="panels">
    <div class="panel">
      <h2 style="color:var(--mat)">μ — resistance to shape change</h2>
      <div class="desc">Set the shear stress τ; γ = τ/μ is the resulting shear strain</div>
      <svg id="li-svg-shear" viewBox="0 0 260 220"></svg>
      <div class="slider-group" style="margin:10px auto 0;">
        <label for="li-tau">Shear stress τ <span class="val" id="li-vTau">10.0 GPa</span></label>
        <input type="range" id="li-tau" min="0" max="50" step="0.5" value="10">
      </div>
      <div class="readout">γ = τ/μ = <b id="li-r-gamma"></b></div>
    </div>

    <div class="panel">
      <h2 style="color:var(--push)">λ — sideways stress when confined</h2>
      <div class="desc">Set the axial stress σ on a bar between rigid walls (ε_lateral locked at 0); ε_axial = σ/(λ+2μ)</div>
      <svg id="li-svg-confined" viewBox="0 0 260 220"></svg>
      <div class="slider-group" style="margin:10px auto 0;">
        <label for="li-sigax">Axial stress σ_axial <span class="val" id="li-vSigax">21 GPa</span></label>
        <input type="range" id="li-sigax" min="-50" max="100" step="1" value="21">
      </div>
      <div class="readout">ε_axial = σ/(λ+2μ) = <b id="li-r-epsax"></b><br>σ_wall = λε = <b id="li-r-sigwall"></b></div>
    </div>
  </div>

  <div class="note">
    Left: apply a shear stress τ and read off the resulting angle γ = τ/μ — no volume or lateral
    coupling involved, just μ resisting the change of shape. Right: apply an axial stress σ to a bar
    whose sides are clamped so it <b>can't</b> bulge or neck sideways (ε_lateral = 0 by construction,
    not by Poisson relaxation) — the walls still feel a push or pull, and that reaction is exactly λε.
    λ isn't a "stiffness" you can feel directly in an unconstrained pull test (that's E); it only shows
    up once something stops the material from doing what its Poisson's ratio would otherwise let it do.
    Note λ+2μ = M, the constrained (uniaxial-strain) modulus — the same quantity that sets P-wave speed
    in geomechanics/seismology. The outward (green) wall reaction assumes the bar is <i>bonded</i> to
    the walls: a smooth rigid wall can only push, and an unbonded bar under axial compression would
    simply separate from it. Isotropic stability requires μ &gt; 0 and 3λ+2μ &gt; 0; outside that
    window the strain readouts are suppressed rather than shown with a nonsense sign. The drawings
    saturate at a fixed deformation so the figure stays inside its box — the numbers above keep going.
  </div>


<script>
(function(){
  const root = document.querySelector(".viz-lame-i");
  if (!root) return;
  const __q = (id) => root.querySelector("#" + id);

const els = {
  mu: __q('li-mu'),
  lambda: __q('li-lambda'),
  tau: __q('li-tau'),
  sigAx: __q('li-sigax'),
};
const vals = {
  mu: __q('li-vMu'),
  lambda: __q('li-vLambda'),
  tau: __q('li-vTau'),
  sigAx: __q('li-vSigax'),
};

function drawShear(gamma) {
  const svg = __q('li-svg-shear');
  // x0 pulled left of the old 80 so the sheared square still fits at the draw clamp:
  // top-right reaches x0 + S + shift = 55 + 100 + 90 = 245 inside a 260-wide viewBox.
  const S = 100, x0 = 55, y0 = 60;
  const shift = gamma * S;
  const pts = [
    [x0, y0 + S],          // bottom-left
    [x0 + S, y0 + S],      // bottom-right
    [x0 + S + shift, y0],  // top-right
    [x0 + shift, y0],      // top-left
  ];
  const defPath = pts.map(p => p.join(',')).join(' ');
  const origPath = `${x0},${y0+S} ${x0+S},${y0+S} ${x0+S},${y0} ${x0},${y0}`;

  svg.innerHTML = `
    <polygon points="${origPath}" fill="none" stroke="var(--fg-muted)" stroke-width="1.2" stroke-dasharray="4,4"/>
    <polygon points="${defPath}" fill="var(--mat)" fill-opacity="0.25" stroke="var(--mat)" stroke-width="2.2"/>
    <line x1="${x0+shift}" y1="${y0-14}" x2="${x0+shift+40}" y2="${y0-14}" stroke="var(--fg)" stroke-width="1.6" marker-end="url(#li-arrH)"/>
    <line x1="${x0}" y1="${y0+S+14}" x2="${x0-40}" y2="${y0+S+14}" stroke="var(--fg)" stroke-width="1.6" marker-end="url(#li-arrH)"/>
    <text x="${x0+shift+20}" y="${y0-20}" font-size="9" fill="var(--fg)" text-anchor="middle">τ</text>
    <text x="${x0-20}" y="${y0+S+28}" font-size="9" fill="var(--fg)" text-anchor="middle">τ</text>
    <defs><marker id="li-arrH" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="var(--fg)"/></marker></defs>
  `;
}

function drawConfined(epsA, lambda) {
  const svg = __q('li-svg-confined');
  const W = 90, H0 = 100, x0 = 85, ycenter = 110;
  const H = H0 * (1 + epsA);
  const y0 = ycenter - H/2;
  const y0orig = ycenter - H0/2;

  const sigWall = lambda * epsA;
  const tensile = sigWall > 0.5;      // wall pulls bar outward (bar "wants" to neck, bonded wall resists)
  const compressive = sigWall < -0.5; // wall pushes bar inward (bar "wants" to bulge, wall resists)
  const wallArrowColor = tensile ? 'var(--pull)' : (compressive ? 'var(--push)' : 'var(--fg-muted)');
  const axArrowColor = epsA > 0.002 ? 'var(--pull)' : (epsA < -0.002 ? 'var(--push)' : 'var(--fg-muted)');
  const axDir = epsA >= 0 ? 1 : -1;
  // dirSign=1 -> arrows point outward (tensile wall reaction), -1 -> inward (compressive)
  const dirSign = tensile ? 1 : (compressive ? -1 : 0);

  svg.innerHTML = `
    <rect x="${x0}" y="${y0orig}" width="${W}" height="${H0}" fill="none" stroke="var(--fg-muted)" stroke-width="1.2" stroke-dasharray="4,4"/>
    <rect x="${x0}" y="${y0}" width="${W}" height="${H}" fill="var(--mat)" fill-opacity="0.25" stroke="var(--mat)" stroke-width="2.2"/>

    <!-- rigid walls -->
    <line x1="${x0-6}" y1="20" x2="${x0-6}" y2="200" stroke="var(--wall)" stroke-width="3"/>
    <line x1="${x0+W+6}" y1="20" x2="${x0+W+6}" y2="200" stroke="var(--wall)" stroke-width="3"/>

    <!-- wall reaction arrows -->
    <line x1="${x0-10}" y1="${ycenter}" x2="${x0-10 - 16*dirSign}" y2="${ycenter}" stroke="${wallArrowColor}" stroke-width="1.8" marker-end="url(#li-arrWall)"/>
    <line x1="${x0+W+10}" y1="${ycenter}" x2="${x0+W+10 + 16*dirSign}" y2="${ycenter}" stroke="${wallArrowColor}" stroke-width="1.8" marker-end="url(#li-arrWall)"/>

    <!-- axial arrows -->
    <line x1="${x0+W/2}" y1="${y0}" x2="${x0+W/2}" y2="${y0 - 20*axDir}" stroke="${axArrowColor}" stroke-width="1.8" marker-end="url(#li-arrAx)"/>
    <line x1="${x0+W/2}" y1="${y0+H}" x2="${x0+W/2}" y2="${y0+H + 20*axDir}" stroke="${axArrowColor}" stroke-width="1.8" marker-end="url(#li-arrAx)"/>

    <defs>
      <marker id="li-arrWall" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="${wallArrowColor}"/></marker>
      <marker id="li-arrAx" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="${axArrowColor}"/></marker>
    </defs>
  `;
}

function update() {
  const mu = parseFloat(els.mu.value);
  const lambda = parseFloat(els.lambda.value);
  const tau = parseFloat(els.tau.value);
  const sigAx = parseFloat(els.sigAx.value);

  vals.mu.textContent = `${mu} GPa`;
  vals.lambda.textContent = `${lambda} GPa`;
  vals.tau.textContent = `${tau.toFixed(1)} GPa`;
  vals.sigAx.textContent = `${sigAx} GPa`;

  const gamma = tau / mu;

  // Isotropic stability is mu > 0 AND 3*lambda + 2*mu > 0 (i.e. K > 0); M = lambda + 2*mu
  // follows from those but does not imply them — e.g. mu=30, lambda=-25 gives M=35 > 0
  // with K = -5, which the old M <= 0 test waved through.
  const M = lambda + 2*mu;         // constrained (uniaxial-strain) modulus
  const K = lambda + (2/3)*mu;     // bulk modulus
  const stable = mu > 0 && (3*lambda + 2*mu) > 0;
  const epsA = stable ? sigAx / M : 0;
  const sigWall = lambda * epsA;

  __q('li-warn').classList.toggle('show', !stable);

  __q('li-r-gamma').textContent = mu > 0 ? gamma.toFixed(3) : '— (μ ≤ 0)';
  __q('li-r-epsax').textContent = stable ? epsA.toFixed(3) : `— (K = ${K.toFixed(1)} GPa ≤ 0, unstable)`;
  __q('li-r-sigwall').textContent = stable ? `${sigWall.toFixed(1)} GPa` : '—';

  // Clamp only what's drawn, not the reported numbers: a stress-controlled slider
  // can push gamma or epsA well outside what a small fixed-size SVG box can depict.
  // Limits chosen so the geometry stays inside the 260x220 viewBox:
  // shear top-right = 55 + 100 + 0.9*100 = 245; bar height = 100*(1+0.7) = 170 plus arrows.
  const gammaDraw = Math.min(Math.max(gamma, 0), 0.9);
  const epsADraw = Math.min(Math.max(epsA, -0.7), 0.7);

  drawShear(gammaDraw);
  drawConfined(epsADraw, lambda);
}

Object.values(els).forEach(el => el.addEventListener('input', update));
update();
})();
</script>
</div>
```
