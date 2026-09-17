```{=html}
<style>
.viz-poisson {
  --bg: #ffffff; --fg: #1a1a1a; --fg-muted: #6b6b6b;
    --panel-bg: #f7f7f8; --border: #e2e2e4; --grid: #dcdcde;
    --mat: #2E86AB; --shrink: #C1440E; --grow: #3E8914;
}
@media (prefers-color-scheme: dark) {
  .viz-poisson {
    --bg: #1c1c1e; --fg: #f0f0f0; --fg-muted: #a0a0a3;
      --panel-bg: #262628; --border: #3a3a3c; --grid: #38383a;
  }
}
.viz-poisson *, .viz-poisson *::before, .viz-poisson *::after {
  box-sizing: border-box;
}
.viz-poisson {
  background: var(--bg); color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    margin: 0; padding: 22px 16px 36px;
}
.viz-poisson .wrap {
  max-width: 900px; margin: 0 auto;
}
.viz-poisson h1 {
  font-size: 1.25rem; font-weight: 600; text-align: center; margin: 0 0 4px;
}
.viz-poisson .subtitle {
  text-align: center; color: var(--fg-muted); font-size: 0.88rem; margin-bottom: 20px;
}
.viz-poisson .controls {
  display: flex; gap: 24px; flex-wrap: wrap; justify-content: center;
    background: var(--panel-bg); border: 1px solid var(--border); border-radius: 12px;
    padding: 16px 20px; margin-bottom: 14px;
}
.viz-poisson .slider-group {
  min-width: 240px; flex: 1 1 240px; max-width: 340px;
}
.viz-poisson .slider-group label {
  display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 5px;
}
.viz-poisson .slider-group label .val {
  font-variant-numeric: tabular-nums; color: var(--fg-muted);
}
.viz-poisson input[type="range"] {
  width: 100%; accent-color: #555;
}
.viz-poisson .presets {
  display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin-bottom: 18px;
}
.viz-poisson .presets button {
  font-size: 0.78rem; padding: 6px 12px; border-radius: 999px;
    border: 1px solid var(--border); background: var(--panel-bg); color: var(--fg); cursor: pointer;
}
.viz-poisson .presets button:hover {
  border-color: var(--fg-muted);
}
.viz-poisson .stage {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 12px;
    padding: 16px; text-align: center;
}
.viz-poisson svg {
  display: block; margin: 0 auto; max-width: 100%; height: auto;
}
.viz-poisson .readouts {
  display: flex; justify-content: center; gap: 26px; flex-wrap: wrap;
    margin-top: 14px; font-size: 0.85rem;
}
.viz-poisson .readouts .item {
  text-align: center;
}
.viz-poisson .readouts .item .label {
  color: var(--fg-muted); font-size: 0.75rem;
}
.viz-poisson .readouts .item .value {
  font-variant-numeric: tabular-nums; font-weight: 600; font-size: 1.0rem;
}
.viz-poisson .note {
  max-width: 680px; margin: 20px auto 0; font-size: 0.8rem; color: var(--fg-muted);
    line-height: 1.55; text-align: center;
}
.viz-poisson svg { width: 100%; height: auto; max-width: 460px; }
.viz-poisson .legend span { white-space: nowrap; }
.viz-poisson { margin: 0 0 1.5rem; padding: 0; font-family: inherit; }
</style>

<div class="viz-poisson">
<div class="subtitle">Pull a bar along its length — ν sets how much it shrinks (or grows) sideways</div>

  <div class="controls">
    <div class="slider-group">
      <label>Applied axial strain ε <span class="val" id="po-vEps">0.20</span></label>
      <input type="range" id="po-eps" min="0" max="0.4" step="0.01" value="0.20">
    </div>
    <div class="slider-group">
      <label>Poisson's ratio ν <span class="val" id="po-vNu">0.30</span></label>
      <input type="range" id="po-nu" min="-0.9" max="0.5" step="0.01" value="0.30">
    </div>
  </div>

  <div class="presets">
    <button data-nu="0.30">Typical metal (ν≈0.30)</button>
    <button data-nu="0.00">Cork (ν≈0.00)</button>
    <button data-nu="0.499">Rubber (ν≈0.499)</button>
    <button data-nu="0.50">Perfectly incompressible (ν=0.5)</button>
    <button data-nu="-0.50">Auxetic foam (ν≈−0.5)</button>
  </div>

  <div class="stage">
    <svg id="po-svg-bar" viewBox="0 0 480 260"></svg>
    <div class="readouts">
      <div class="item"><div class="label">Lateral strain ε_lat = −νε</div><div class="value" id="po-r-lat"></div></div>
      <div class="item"><div class="label">Length change</div><div class="value" id="po-r-len"></div></div>
      <div class="item"><div class="label">Width change</div><div class="value" id="po-r-wid"></div></div>
      <div class="item"><div class="label">Volume change ΔV/V₀</div><div class="value" id="po-r-vol"></div></div>
    </div>
  </div>

  <div class="note" id="po-explainer">
    Pull most ordinary materials and they get thinner as they get longer — that's a <b>positive</b>
    Poisson's ratio. ν=0 means no lateral response at all (like cork, which is why it's easy to push
    into a bottle without swelling out the sides). ν=0.5 means the material can't change volume — it
    must get thinner by exactly the amount needed to conserve volume (rubber, most fluids). Negative ν
    ("auxetic") materials do the opposite of intuition: pull them and they get <i>fatter</i>, not thinner.
  </div>


<script>
(function(){
  const root = document.querySelector(".viz-poisson");
  if (!root) return;
  const __q = (id) => root.querySelector("#" + id);

const epsEl = __q('po-eps');
const nuEl = __q('po-nu');
const vEps = __q('po-vEps');
const vNu = __q('po-vNu');

const L0 = 160, W0 = 70; // reference bar dimensions (svg units)
const cx = 240, cy = 130;

function update() {
  const eps = parseFloat(epsEl.value);
  const nu = parseFloat(nuEl.value);
  vEps.textContent = eps.toFixed(2);
  vNu.textContent = nu.toFixed(3);

  const epsLat = -nu * eps;
  const L = L0 * (1 + eps);
  const W = W0 * (1 + epsLat);

  const dV = (1 + eps) * (1 + epsLat) ** 2 - 1;

  __q('po-r-lat').textContent = `${(epsLat*100).toFixed(1)}%`;
  __q('po-r-len').textContent = `${(eps*100).toFixed(1)}%`;
  __q('po-r-wid').textContent = `${(epsLat*100).toFixed(1)}%`;
  const volEl = __q('po-r-vol');
  volEl.textContent = `${(dV*100).toFixed(1)}%`;
  volEl.style.color = Math.abs(dV) < 0.005 ? 'var(--fg)' : (dV > 0 ? 'var(--grow)' : 'var(--shrink)');

  const svg = __q('po-svg-bar');
  const origX = cx - L0/2, origY = cy - W0/2;
  const defX = cx - L/2, defY = cy - W/2;

  const widthColor = epsLat < -0.002 ? 'var(--shrink)' : (epsLat > 0.002 ? 'var(--grow)' : 'var(--fg-muted)');

  svg.innerHTML = `
    <rect x="${origX}" y="${origY}" width="${L0}" height="${W0}" fill="none" stroke="var(--fg-muted)" stroke-width="1.3" stroke-dasharray="5,4"/>
    <rect x="${defX}" y="${defY}" width="${L}" height="${W}" fill="var(--mat)" fill-opacity="0.28" stroke="var(--mat)" stroke-width="2.4"/>

    <line x1="${defX-22}" y1="${cy}" x2="${defX-6}" y2="${cy}" stroke="var(--fg)" stroke-width="1.6" marker-end="url(#po-arrow)"/>
    <line x1="${defX+L+6}" y1="${cy}" x2="${defX+L+22}" y2="${cy}" stroke="var(--fg)" stroke-width="1.6" marker-end="url(#po-arrow)"/>

    <line x1="${defX+L+34}" y1="${defY}" x2="${defX+L+34}" y2="${defY+W}" stroke="${widthColor}" stroke-width="1.3"/>
    <line x1="${defX+L+30}" y1="${defY}" x2="${defX+L+38}" y2="${defY}" stroke="${widthColor}" stroke-width="1.3"/>
    <line x1="${defX+L+30}" y1="${defY+W}" x2="${defX+L+38}" y2="${defY+W}" stroke="${widthColor}" stroke-width="1.3"/>
    <text x="${defX+L+42}" y="${cy+3}" font-size="10" fill="${widthColor}">width</text>

    <defs>
      <marker id="po-arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L6,3 L0,6 Z" fill="var(--fg)"/>
      </marker>
    </defs>
  `;
}

epsEl.addEventListener('input', update);
nuEl.addEventListener('input', update);
root.querySelectorAll('.presets button').forEach(btn => {
  btn.addEventListener('click', () => {
    nuEl.value = btn.dataset.nu;
    update();
  });
});

update();
})();
</script>
</div>
```
