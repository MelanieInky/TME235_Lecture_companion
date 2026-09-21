```{=html}
<style>
.viz-beamvib,
[data-bs-theme="light"] .viz-beamvib,
body.quarto-light .viz-beamvib {
  --fg: #1f2328;
  --fg-muted: #5b636e;
  --panel-bg: #f5f6f8;
  --border: #d5d9df;
  --grid: #e1e4e9;
  --slider: #3b6ea8;
  --curve: #2e6fb5;
  --drive: #c0392b;
  --load: #23784a;
}
@media (prefers-color-scheme: dark) {
  .viz-beamvib {
    --fg: #e6e8eb;
    --fg-muted: #a3aab4;
    --panel-bg: #1d2127;
    --border: #3a414b;
    --grid: #2c323a;
    --slider: #7fb0e6;
    --curve: #6aa8ef;
    --drive: #ef6b5b;
    --load: #5cc18a;
  }
}
[data-bs-theme="dark"] .viz-beamvib,
body.quarto-dark .viz-beamvib {
  --fg: #e6e8eb;
  --fg-muted: #a3aab4;
  --panel-bg: #1d2127;
  --border: #3a414b;
  --grid: #2c323a;
  --slider: #7fb0e6;
  --curve: #6aa8ef;
  --drive: #ef6b5b;
  --load: #5cc18a;
}

.viz-beamvib { color: var(--fg); font-family: inherit; }
.viz-beamvib *, .viz-beamvib *::before, .viz-beamvib *::after { box-sizing: border-box; }
.viz-beamvib .subtitle { color: var(--fg-muted); margin: 0 0 0.75rem; font-size: 0.95em; }

.viz-beamvib .controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 0.6rem 1rem;
  background: var(--panel-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem;
}
.viz-beamvib .ctrl label { display: block; font-size: 0.9em; }
.viz-beamvib .ctrl input[type="range"] { width: 100%; accent-color: var(--slider); }
.viz-beamvib .val { font-variant-numeric: tabular-nums; font-weight: 600; }

.viz-beamvib .presets {
  display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: center;
  margin: 0.6rem 0; font-size: 0.9em;
}
.viz-beamvib .presets button {
  font: inherit; font-size: 0.9em; color: var(--fg);
  background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 6px; padding: 0.2rem 0.6rem; cursor: pointer;
}
.viz-beamvib .presets button:hover,
.viz-beamvib .presets button:focus-visible { border-color: var(--slider); }

.viz-beamvib .panel {
  background: var(--panel-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.5rem 0.75rem;
  margin-top: 0.6rem;
}
.viz-beamvib .panel-title { font-weight: 600; font-size: 0.95em; margin-bottom: 0.25rem; }

.viz-beamvib svg { width: 100%; height: auto; max-width: 460px; display: block; margin: 0 auto; }
.viz-beamvib svg text { fill: var(--fg); font-size: 11px; font-family: inherit; font-variant-numeric: tabular-nums; }
.viz-beamvib svg text.muted { fill: var(--fg-muted); }
.viz-beamvib svg text.lbl-load { fill: var(--load); font-weight: 600; font-style: italic; font-size: 12px; }
.viz-beamvib svg text.lbl-mode { fill: var(--fg-muted); font-style: italic; }

.viz-beamvib .readouts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 0.4rem 1rem;
  margin-top: 0.6rem;
  font-size: 0.9em;
  font-variant-numeric: tabular-nums;
}
.viz-beamvib .readouts div { border-bottom: 1px solid var(--border); padding: 0.2rem 0; }
.viz-beamvib .note { color: var(--fg-muted); font-size: 0.88em; margin-top: 0.75rem; }
.viz-beamvib .note p { margin: 0 0 0.4rem; }
</style>

<div class="viz-beamvib">
  <p class="subtitle">
    Cantilever driven by a harmonic tip force <i>F</i> sin <i>ωt</i>. Solving
    <i>W</i>⁗ − β⁴<i>W</i> = 0 with β⁴ = ω²ρ<i>A</i>/<i>EI</i> and the clamp and tip
    conditions gives the tip amplitude at every frequency; the gain is that amplitude divided by
    the static tip deflection <i>FL</i>³/3<i>EI</i>.
  </p>

  <div class="controls">
    <div class="ctrl">
      <label for="bv-om">Drive frequency ω/ω₁ = <span class="val" id="bv-om-val"></span></label>
      <input type="range" id="bv-om" min="-1" max="1.5" step="any" value="0">
    </div>
    <div class="ctrl">
      <label for="bv-eta">Loss factor η = <span class="val" id="bv-eta-val"></span></label>
      <input type="range" id="bv-eta" min="-3" max="-1" step="0.1" value="-2">
    </div>
  </div>

  <div class="presets">
    <span>Drive at:</span>
    <button type="button" data-om="0.1">Quasi-static</button>
    <button type="button" data-om="1">Mode 1</button>
    <button type="button" data-om="4.385316">Tip anti-resonance</button>
    <button type="button" data-om="6.266893">Mode 2</button>
    <button type="button" data-om="17.547475">Mode 3</button>
  </div>

  <div class="panel">
    <div class="panel-title">Gain and phase of the tip response</div>
    <svg id="bv-plot" viewBox="0 0 460 352" role="img" aria-label="Gain and phase versus drive frequency">
      <g id="bv-grid"></g>
      <path id="bv-gain" fill="none" stroke="var(--curve)" stroke-width="1.8" stroke-linejoin="round"/>
      <path id="bv-phase" fill="none" stroke="var(--curve)" stroke-width="1.8" stroke-linejoin="round"/>
      <line id="bv-cur" stroke="var(--drive)" stroke-width="1.2" stroke-dasharray="3 3"/>
      <circle id="bv-cur-g" r="4.5" stroke="var(--drive)" stroke-width="2"/>
      <circle id="bv-cur-p" r="4.5" fill="var(--drive)" stroke="var(--drive)" stroke-width="2"/>
      <text x="12" y="106" text-anchor="middle" class="muted" transform="rotate(-90 12 106)">|W(L)| / W_static</text>
      <text x="12" y="267" text-anchor="middle" class="muted" transform="rotate(-90 12 267)">phase</text>
      <text x="249" y="347" text-anchor="middle" class="muted">ω / ω₁ (log scale)</text>
    </svg>
  </div>

  <div class="panel">
    <div class="panel-title">Forced shape <i>W</i>(<i>x</i>) at the drive frequency</div>
    <svg id="bv-shape" viewBox="0 0 460 140" role="img" aria-label="Forced vibration shape of the cantilever">
      <defs>
        <marker id="bv-arrow" viewBox="0 0 10 10" refX="10" refY="5"
                markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="var(--load)"/>
        </marker>
      </defs>
      <g transform="translate(0,70) scale(1,-1)">
        <rect x="28" y="-55" width="12" height="110" fill="var(--grid)" stroke="var(--fg-muted)"/>
        <path d="M28,-40 L40,-52 M28,-20 L40,-32 M28,0 L40,-12 M28,20 L40,8 M28,40 L40,28"
              stroke="var(--fg-muted)" stroke-width="1"/>
        <line x1="40" y1="0" x2="400" y2="0" stroke="var(--fg-muted)" stroke-dasharray="4 3"/>
        <path id="bv-mirror" fill="none" stroke="var(--fg-muted)" stroke-width="1.2" stroke-dasharray="5 4"/>
        <path id="bv-w" fill="none" stroke="var(--curve)" stroke-width="3" stroke-linecap="round"/>
        <g id="bv-nodes"></g>
        <circle id="bv-tip" r="4" fill="var(--curve)" stroke="var(--panel-bg)" stroke-width="1.5"/>
        <line x1="422" y1="-22" x2="422" y2="22" stroke="var(--load)" stroke-width="2.2"
              marker-start="url(#bv-arrow)" marker-end="url(#bv-arrow)"/>
      </g>
      <text x="430" y="74" class="lbl-load">F</text>
      <text x="48" y="136" class="muted">shape scaled to fit; amplitude is read off the gain plot</text>
    </svg>
  </div>

  <div class="readouts">
    <div>ω/ω₁ = <span class="val" id="bv-r-om"></span></div>
    <div>β<i>L</i> (undamped) = <span class="val" id="bv-r-bl"></span></div>
    <div>Tip gain = <span class="val" id="bv-r-g"></span></div>
    <div>Phase = <span class="val" id="bv-r-p"></span></div>
  </div>

  <div class="note">
    <p>
      ω₁ = 1.8751² √(<i>EI</i>/ρ<i>AL</i>⁴) is the first natural frequency; the dashed
      verticals are ω₁, ω₂ = 6.27 ω₁ and ω₃ = 17.55 ω₁, from 1 + cos β<i>L</i> cosh β<i>L</i> = 0.
      The gain dips between resonances at anti-resonances (tan β<i>L</i> = tanh β<i>L</i>),
      where the tip stands still while the rest of the beam vibrates. That dip is a property of
      driving and measuring at the same point; a response measured elsewhere has its dips
      at other frequencies.
    </p>
    <p>
      The equation on the page is undamped, so its resonance peaks are infinite. To keep them
      finite the bending stiffness is taken as <i>EI</i>(1 + iη) (hysteretic loss factor η);
      η → 0 recovers the undamped curve, and the static gain is 1/|1 + iη| ≈ 1. Phase runs from
      0° (tip in phase with the force) to −180° (in anti-phase), switching at each resonance and
      anti-resonance. A hollow marker means the current gain is outside the plotted window.
    </p>
    <p>
      The drawn shape is the real part of <i>W</i>(<i>x</i>) after removing one overall phase,
      shown with its mirror image (the other half-cycle); small circles are nodes. Euler–Bernoulli
      theory neglects shear deformation and rotary inertia, so the higher modes are only accurate
      while the wavelength stays long compared with the beam depth.
    </p>
  </div>

  <script>
  (function () {
    const root = document.querySelector('.viz-beamvib');
    if (!root) return;
    const __q = (id) => root.querySelector('#' + id);
    const NS = 'http://www.w3.org/2000/svg';
    const set = (el, attrs) => { for (const k in attrs) el.setAttribute(k, attrs[k]); };
    const mk = (tag, attrs) => { const el = document.createElementNS(NS, tag); set(el, attrs); return el; };

    // ---- complex arithmetic ----
    const C = (re, im = 0) => ({ re, im });
    const add = (p, q) => C(p.re + q.re, p.im + q.im);
    const sub = (p, q) => C(p.re - q.re, p.im - q.im);
    const mul = (p, q) => C(p.re * q.re - p.im * q.im, p.re * q.im + p.im * q.re);
    const div = (p, q) => { const d = q.re * q.re + q.im * q.im;
      return C((p.re * q.re + p.im * q.im) / d, (p.im * q.re - p.re * q.im) / d); };
    const neg = (p) => C(-p.re, -p.im);
    const abs = (p) => Math.hypot(p.re, p.im);
    const csin = (z) => C(Math.sin(z.re) * Math.cosh(z.im), Math.cos(z.re) * Math.sinh(z.im));
    const ccos = (z) => C(Math.cos(z.re) * Math.cosh(z.im), -Math.sin(z.re) * Math.sinh(z.im));
    const csinh = (z) => C(Math.sinh(z.re) * Math.cos(z.im), Math.cosh(z.re) * Math.sin(z.im));
    const ccosh = (z) => C(Math.cosh(z.re) * Math.cos(z.im), Math.sinh(z.re) * Math.sin(z.im));

    const LAM1 = 1.87510407;
    const MODES = [1, 6.266893, 17.547475];           // (λn/λ1)^2
    const OM_MIN = 0.1, OM_MAX = Math.pow(10, 1.5);

    // Nondimensional (L = 1, EI = 1, F = 1). W = a(sin βx − sinh βx) + b(cos βx − cosh βx)
    // satisfies W(0) = W'(0) = 0; solve W''(1) = 0 and EI*(1+iη) W'''(1) = −F.
    function solve(om, eta) {
      const x0 = LAM1 * Math.sqrt(om);
      const r = Math.pow(1 + eta * eta, -0.125), th = -Math.atan(eta) / 4;
      const x = C(x0 * r * Math.cos(th), x0 * r * Math.sin(th));
      const x3 = mul(x, mul(x, x));
      const sx = csin(x), cx = ccos(x), shx = csinh(x), chx = ccosh(x);
      const m11 = neg(add(sx, shx)), m12 = neg(add(cx, chx));
      const m21 = mul(x3, m12), m22 = mul(x3, sub(sx, shx));
      const g = div(C(-1), C(1, eta));
      const det = sub(mul(m11, m22), mul(m12, m21));
      const a = div(neg(mul(m12, g)), det), b = div(mul(m11, g), det);
      const W = (xi) => { const z = C(x.re * xi, x.im * xi);
        return add(mul(a, sub(csin(z), csinh(z))), mul(b, sub(ccos(z), ccosh(z)))); };
      const tip = W(1);
      return { W, gain: C(3 * tip.re, 3 * tip.im) };   // divided by static tip deflection 1/3
    }

    // ---- plot geometry ----
    const PX0 = 52, PX1 = 446;
    const GY0 = 16, GY1 = 196, GDEC_TOP = 3, GDEC_BOT = -3;
    const PY0 = 222, PY1 = 312;
    const xOf = (om) => PX0 + (Math.log10(om) - Math.log10(OM_MIN)) /
                              (Math.log10(OM_MAX) - Math.log10(OM_MIN)) * (PX1 - PX0);
    const yG = (g) => GY0 + (GDEC_TOP - Math.log10(g)) / (GDEC_TOP - GDEC_BOT) * (GY1 - GY0);
    const yP = (deg) => PY0 + (-deg) / 180 * (PY1 - PY0);

    // static grid, built once
    (function buildGrid() {
      const g = __q('bv-grid');
      const sup = { '-3': '10⁻³', '-2': '10⁻²', '-1': '10⁻¹', '0': '1', '1': '10', '2': '10²', '3': '10³' };
      for (let d = GDEC_BOT; d <= GDEC_TOP; d++) {
        const y = yG(Math.pow(10, d));
        g.appendChild(mk('line', { x1: PX0, y1: y, x2: PX1, y2: y, stroke: 'var(--grid)' }));
        const t = mk('text', { x: PX0 - 5, y: y, 'text-anchor': 'end', 'dominant-baseline': 'middle', class: 'muted' });
        t.textContent = sup[String(d)]; g.appendChild(t);
      }
      [0, -90, -180].forEach(p => {
        const y = yP(p);
        g.appendChild(mk('line', { x1: PX0, y1: y, x2: PX1, y2: y, stroke: 'var(--grid)' }));
        const t = mk('text', { x: PX0 - 5, y: y, 'text-anchor': 'end', 'dominant-baseline': 'middle', class: 'muted' });
        t.textContent = (p === 0 ? '0' : '\u2212' + (-p)) + '°'; g.appendChild(t);
      });
      [0.1, 0.3, 1, 3, 10, 30].forEach(om => {
        const x = xOf(om);
        g.appendChild(mk('line', { x1: x, y1: GY0, x2: x, y2: GY1, stroke: 'var(--grid)' }));
        g.appendChild(mk('line', { x1: x, y1: PY0, x2: x, y2: PY1, stroke: 'var(--grid)' }));
        const t = mk('text', { x: x, y: 328, 'text-anchor': 'middle', class: 'muted' });
        t.textContent = String(om); g.appendChild(t);
      });
      MODES.forEach((om, i) => {
        const x = xOf(om);
        g.appendChild(mk('line', { x1: x, y1: GY0, x2: x, y2: PY1, stroke: 'var(--fg-muted)',
                                   'stroke-dasharray': '2 4', 'stroke-width': 1 }));
        const t = mk('text', { x: x, y: 11, 'text-anchor': 'middle', class: 'lbl-mode' });
        t.textContent = 'ω' + '₁₂₃'[i]; g.appendChild(t);
      });
      g.appendChild(mk('rect', { x: PX0, y: GY0, width: PX1 - PX0, height: GY1 - GY0,
                                 fill: 'none', stroke: 'var(--border)' }));
      g.appendChild(mk('rect', { x: PX0, y: PY0, width: PX1 - PX0, height: PY1 - PY0,
                                 fill: 'none', stroke: 'var(--border)' }));
    })();

    function fmtG(v) {
      const a = Math.abs(v);
      if (a < 5e-13) return '0';
      if (a >= 1000) return v.toFixed(0);
      return v.toPrecision(3);
    }
    function phaseDeg(z) {
      let p = Math.atan2(z.im, z.re) * 180 / Math.PI;
      if (p > 0.5) p -= 360;                 // passive collocated response lives in (−180°, 0°]
      return Math.abs(p) < 0.05 ? 0 : p;
    }

    function update() {
      const om = Math.pow(10, +__q('bv-om').value);
      const eta = Math.pow(10, +__q('bv-eta').value);
      __q('bv-om-val').textContent = om.toPrecision(3);
      __q('bv-eta-val').textContent = eta.toPrecision(2);

      // --- frequency sweep: log grid plus refinement around each resonance ---
      const samples = [];
      const NB = 600, l0 = Math.log10(OM_MIN), l1 = Math.log10(OM_MAX);
      for (let i = 0; i <= NB; i++) samples.push(Math.pow(10, l0 + (l1 - l0) * i / NB));
      MODES.forEach(m => { for (let t = -8; t <= 8; t += 0.25) {
        const s = m * (1 + eta * t); if (s > OM_MIN && s < OM_MAX) samples.push(s); } });
      samples.sort((p, q) => p - q);

      let dG = '', dP = '', penG = false;
      for (const s of samples) {
        const G = solve(s, eta).gain;
        const g = abs(G), p = phaseDeg(G), x = xOf(s).toFixed(2);
        if (g >= Math.pow(10, GDEC_BOT) && g <= Math.pow(10, GDEC_TOP)) {
          dG += (penG ? ' L' : ' M') + x + ',' + yG(g).toFixed(2); penG = true;
        } else penG = false;                           // break the path, do not clamp
        dP += (dP ? ' L' : 'M') + x + ',' + yP(p).toFixed(2);   // damped: phase is continuous
      }
      __q('bv-gain').setAttribute('d', dG);
      __q('bv-phase').setAttribute('d', dP);

      // --- current drive point ---
      const cur = solve(om, eta);
      const g = abs(cur.gain), p = phaseDeg(cur.gain), xc = xOf(om);
      set(__q('bv-cur'), { x1: xc, y1: GY0, x2: xc, y2: PY1 });
      const inWin = g >= Math.pow(10, GDEC_BOT) && g <= Math.pow(10, GDEC_TOP);
      const gClamped = Math.min(Math.max(g, Math.pow(10, GDEC_BOT)), Math.pow(10, GDEC_TOP));
      set(__q('bv-cur-g'), { cx: xc, cy: yG(gClamped), fill: inWin ? 'var(--drive)' : 'var(--panel-bg)' });
      set(__q('bv-cur-p'), { cx: xc, cy: yP(p) });

      // --- forced shape ---
      const NX = 120, Wc = [];
      let iMax = 0, aMax = 0;
      for (let i = 0; i <= NX; i++) {
        const w = cur.W(i / NX); Wc.push(w);
        const a = abs(w); if (a > aMax) { aMax = a; iMax = i; }
      }
      const ph = Math.atan2(Wc[iMax].im, Wc[iMax].re);
      const rot = C(Math.cos(-ph), Math.sin(-ph));
      const real = Wc.map(w => mul(w, rot).re);
      const rMax = Math.max(...real.map(Math.abs)) || 1;
      const sc = 50 / rMax, XB0 = 40, XB1 = 400;
      const xs = (i) => XB0 + (XB1 - XB0) * i / NX;
      let dW = '', dM = '';
      real.forEach((v, i) => {
        const y = v * sc;
        dW += (i ? ' L' : 'M') + xs(i).toFixed(2) + ',' + y.toFixed(2);
        dM += (i ? ' L' : 'M') + xs(i).toFixed(2) + ',' + (-y).toFixed(2);
      });
      __q('bv-w').setAttribute('d', dW);
      __q('bv-mirror').setAttribute('d', dM);
      set(__q('bv-tip'), { cx: XB1, cy: real[NX] * sc });

      const nodes = __q('bv-nodes');
      while (nodes.firstChild) nodes.removeChild(nodes.firstChild);
      for (let i = 3; i < NX; i++) {             // skip the clamp, where W = 0 by construction
        const v0 = real[i], v1 = real[i + 1];
        if (v0 === 0 || v0 * v1 < 0) {
          const t = v0 === 0 ? 0 : v0 / (v0 - v1);
          nodes.appendChild(mk('circle', { cx: xs(i + t), cy: 0, r: 3.5, fill: 'none',
                                          stroke: 'var(--drive)', 'stroke-width': 1.5 }));
        }
      }

      // --- readouts ---
      __q('bv-r-om').textContent = om.toPrecision(3);
      __q('bv-r-bl').textContent = (LAM1 * Math.sqrt(om)).toFixed(3);
      __q('bv-r-g').textContent = fmtG(g);
      __q('bv-r-p').textContent = (p < 0 ? '\u2212' : '\u00A0') + Math.abs(p).toFixed(1) + '°';
    }

    __q('bv-om').addEventListener('input', update);
    __q('bv-eta').addEventListener('input', update);
    root.querySelectorAll('.presets button[data-om]').forEach(btn => {
      btn.addEventListener('click', () => {
        __q('bv-om').value = Math.log10(+btn.dataset.om);
        update();
      });
    });

    update();
  })();
  </script>
</div>
```
