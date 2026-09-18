```{=html}
<style>
.viz-lame-i {
  --bg: #ffffff; --fg: #1a1a1a; --fg-muted: #6b6b6b;
    --panel-bg: #f7f7f8; --border: #e2e2e4; --grid: #dcdcde;
    --mat: #2E86AB; --push: #C1440E; --pull: #3E8914; --wall: #6b6b6b;
}
@media (prefers-color-scheme: dark) {
  .viz-lame-i {
    --bg: #1c1c1e; --fg: #f0f0f0; --fg-muted: #a0a0a3;
      --panel-bg: #262628; --border: #3a3a3c; --grid: #38383a;
  }
}
.viz-lame-i *, .viz-lame-i *::before, .viz-lame-i *::after {
  box-sizing: border-box;
}
.viz-lame-i {
  background: var(--bg); color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    margin: 0; padding: 22px 16px 36px;
}
.viz-lame-i .wrap {
  max-width: 980px; margin: 0 auto;
}
.viz-lame-i h1 {
  font-size: 1.25rem; font-weight: 600; text-align: center; margin: 0 0 4px;
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
  width: 100%; accent-color: #555;
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
  display: block; margin: 0 auto; max-width: 100%; height: auto;
}
.viz-lame-i .panel .readout {
  margin-top: 10px; font-size: 0.85rem; font-variant-numeric: tabular-nums;
}
.viz-lame-i .panel .readout b {
  font-weight: 700;
}
.viz-lame-i .note {
  max-width: 760px; margin: 20px auto 0; font-size: 0.8rem; color: var(--fg-muted);
    line-height: 1.55; text-align: center;
}
.viz-lame-i svg { width: 100%; height: auto; max-width: 460px; }
.viz-lame-i .legend span { white-space: nowrap; }
.viz-lame-i { margin: 0 0 1.5rem; padding: 0; font-family: inherit; }
</style>

<div class="viz-lame-i">
<div class="subtitle">μ resists <i>shape</i> change; λ is the stress that shows up sideways when shape change is prevented</div>

  <div class="controls">
    <div class="slider-group">
      <label>μ (shear modulus) <span class="val" id="li-vMu">40 GPa</span></label>
      <input type="range" id="li-mu" min="5" max="100" step="1" value="40">
    </div>
    <div class="slider-group">
      <label>λ (Lamé's 1st parameter) <span class="val" id="li-vLambda">60 GPa</span></label>
      <input type="range" id="li-lambda" min="-20" max="150" step="1" value="60">
    </div>
  </div>

  <div class="panels">
    <div class="panel">
      <h2 style="color:var(--mat)">μ — resistance to shape change</h2>
      <div class="desc">Apply a shear strain γ; τ = μγ is the stress needed to hold it there</div>
      <svg id="li-svg-shear" viewBox="0 0 260 220"></svg>
      <div class="slider-group" style="margin:10px auto 0;">
        <label>Shear strain γ <span class="val" id="li-vGamma">0.25</span></label>
        <input type="range" id="li-gamma" min="0" max="0.5" step="0.01" value="0.25">
      </div>
      <div class="readout">τ = μγ = <b id="li-r-tau"></b></div>
    </div>

    <div class="panel">
      <h2 style="color:var(--push)">λ — sideways stress when confined</h2>
      <div class="desc">Squeeze/stretch a bar between rigid walls (ε_lateral locked at 0)</div>
      <svg id="li-svg-confined" viewBox="0 0 260 220"></svg>
      <div class="slider-group" style="margin:10px auto 0;">
        <label>Axial strain ε <span class="val" id="li-vEpsA">0.15</span></label>
        <input type="range" id="li-epsA" min="-0.3" max="0.3" step="0.01" value="0.15">
      </div>
      <div class="readout">σ_axial = (λ+2μ)ε = <b id="li-r-sigax"></b><br>σ_wall = λε = <b id="li-r-sigwall"></b></div>
    </div>
  </div>

  <div class="note">
    Left: shear an element with the walls free to move — no volume or lateral coupling involved, just μ
    fighting the change of angle. Right: pull/push a bar but clamp its sides so it <b>can't</b> bulge or
    neck sideways (ε_lateral = 0 by construction, not by Poisson relaxation) — the walls still feel a
    push or pull, and that reaction is exactly λε. λ isn't a "stiffness" you can feel directly in an
    unconstrained pull test (that's E); it only shows up once something stops the material from doing
    what its Poisson's ratio would otherwise let it do. Note λ+2μ = M, the constrained (uniaxial-strain)
    modulus — the same quantity that sets P-wave speed in geomechanics/seismology.
  </div>


<script>
(function(){
  const root = document.querySelector(".viz-lame-i");
  if (!root) return;
  const __q = (id) => root.querySelector("#" + id);

const els = {
  mu: __q('li-mu'),
  lambda: __q('li-lambda'),
  gamma: __q('li-gamma'),
  epsA: __q('li-epsA'),
};
const vals = {
  mu: __q('li-vMu'),
  lambda: __q('li-vLambda'),
  gamma: __q('li-vGamma'),
  epsA: __q('li-vEpsA'),
};

function drawShear(gamma) {
  const svg = __q('li-svg-shear');
  const S = 100, x0 = 80, y0 = 60; // top-left of undeformed square, size S
  // deformed: top edge shifts right by gamma*S, bottom fixed
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

  const wallColor = 'var(--wall)';
  const sigWall = lambda * epsA;
  const tensile = sigWall > 0.5;   // wall pulls bar outward (bar "wants" to neck, wall resists)
  const compressive = sigWall < -0.5; // wall pushes bar inward (bar "wants" to bulge, wall resists)
  const wallArrowColor = tensile ? '#3E8914' : (compressive ? '#C1440E' : '#8a8a8a');
  const axArrowColor = epsA > 0.002 ? '#3E8914' : (epsA < -0.002 ? '#C1440E' : '#8a8a8a');
  const axDir = epsA >= 0 ? 1 : -1;
  // dirSign=1 -> arrows point outward (tensile wall reaction), -1 -> inward (compressive)
  const dirSign = tensile ? 1 : (compressive ? -1 : 0);

  svg.innerHTML = `
    <rect x="${x0}" y="${y0orig}" width="${W}" height="${H0}" fill="none" stroke="var(--fg-muted)" stroke-width="1.2" stroke-dasharray="4,4"/>
    <rect x="${x0}" y="${y0}" width="${W}" height="${H}" fill="var(--mat)" fill-opacity="0.25" stroke="var(--mat)" stroke-width="2.2"/>

    <!-- rigid walls (hatched) -->
    <line x1="${x0-6}" y1="20" x2="${x0-6}" y2="200" stroke="${wallColor}" stroke-width="3"/>
    <line x1="${x0+W+6}" y1="20" x2="${x0+W+6}" y2="200" stroke="${wallColor}" stroke-width="3"/>

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
  const gamma = parseFloat(els.gamma.value);
  const epsA = parseFloat(els.epsA.value);

  vals.mu.textContent = `${mu} GPa`;
  vals.lambda.textContent = `${lambda} GPa`;
  vals.gamma.textContent = gamma.toFixed(2);
  vals.epsA.textContent = epsA.toFixed(2);

  const tau = mu * gamma;
  const sigAx = (lambda + 2*mu) * epsA;
  const sigWall = lambda * epsA;

  __q('li-r-tau').textContent = `${tau.toFixed(1)} GPa`;
  __q('li-r-sigax').textContent = `${sigAx.toFixed(1)} GPa`;
  __q('li-r-sigwall').textContent = `${sigWall.toFixed(1)} GPa`;

  drawShear(gamma);
  drawConfined(epsA, lambda);
}

Object.values(els).forEach(el => el.addEventListener('input', update));
update();
})();
</script>
</div>
```
