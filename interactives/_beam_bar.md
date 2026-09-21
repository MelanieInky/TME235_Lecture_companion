```{=html}
<style>
.viz-beambar,
[data-bs-theme="light"] .viz-beambar,
body.quarto-light .viz-beambar {
  --fg: #1f2328;
  --fg-muted: #5b636e;
  --panel-bg: #f5f6f8;
  --border: #d5d9df;
  --grid: #e1e4e9;
  --slider: #3b6ea8;
  --member: #9aabbd;
  --load: #23784a;
  --tension: #c0392b;
  --compression: #2e6fb5;
}
@media (prefers-color-scheme: dark) {
  .viz-beambar {
    --fg: #e6e8eb;
    --fg-muted: #a3aab4;
    --panel-bg: #1d2127;
    --border: #3a414b;
    --grid: #2c323a;
    --slider: #7fb0e6;
    --member: #62778d;
    --load: #5cc18a;
    --tension: #ef6b5b;
    --compression: #6aa8ef;
  }
}
[data-bs-theme="dark"] .viz-beambar,
body.quarto-dark .viz-beambar {
  --fg: #e6e8eb;
  --fg-muted: #a3aab4;
  --panel-bg: #1d2127;
  --border: #3a414b;
  --grid: #2c323a;
  --slider: #7fb0e6;
  --member: #62778d;
  --load: #5cc18a;
  --tension: #ef6b5b;
  --compression: #6aa8ef;
}

.viz-beambar { color: var(--fg); font-family: inherit; }
.viz-beambar *, .viz-beambar *::before, .viz-beambar *::after { box-sizing: border-box; }
.viz-beambar .subtitle { color: var(--fg-muted); margin: 0 0 0.75rem; font-size: 0.95em; }

.viz-beambar .controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 0.6rem 1rem;
  background: var(--panel-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem;
}
.viz-beambar .ctrl label { display: block; font-size: 0.9em; }
.viz-beambar .ctrl input[type="range"] { width: 100%; accent-color: var(--slider); }
.viz-beambar .val { font-variant-numeric: tabular-nums; font-weight: 600; }

.viz-beambar .presets {
  display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: center;
  margin: 0.6rem 0; font-size: 0.9em;
}
.viz-beambar .presets button {
  font: inherit; font-size: 0.9em; color: var(--fg);
  background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 6px; padding: 0.2rem 0.6rem; cursor: pointer;
}
.viz-beambar .presets button:hover,
.viz-beambar .presets button:focus-visible { border-color: var(--slider); }
.viz-beambar .toggle { display: flex; gap: 0.4rem; align-items: center; margin-left: auto; }
.viz-beambar .toggle input { accent-color: var(--slider); }

.viz-beambar .row {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr);
  gap: 0.5rem 0.75rem;
  align-items: center;
  background: var(--panel-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.5rem 0.75rem;
  margin-top: 0.6rem;
}
.viz-beambar .rowtitle { grid-column: 1 / -1; font-weight: 600; font-size: 0.95em; }
@media (max-width: 560px) {
  .viz-beambar .row { grid-template-columns: 1fr; }
  .viz-beambar .toggle { margin-left: 0; }
}

.viz-beambar svg { width: 100%; height: auto; max-width: 460px; display: block; margin: 0 auto; }
.viz-beambar svg.sect { max-width: 220px; }
.viz-beambar svg text { fill: var(--fg); font-size: 12px; font-family: inherit; font-variant-numeric: tabular-nums; }
.viz-beambar svg text.muted { fill: var(--fg-muted); font-size: 11px; }
.viz-beambar svg text.lbl-load { fill: var(--load); font-weight: 600; font-style: italic; }
.viz-beambar .ghost { fill: none; stroke: var(--fg-muted); stroke-dasharray: 4 3; stroke-width: 1; }

.viz-beambar .readout-wrap { overflow-x: auto; margin-top: 0.75rem; }
.viz-beambar table.readout {
  width: 100%; border-collapse: collapse; font-size: 0.9em;
  font-variant-numeric: tabular-nums;
}
.viz-beambar table.readout th,
.viz-beambar table.readout td { padding: 0.25rem 0.5rem; border-bottom: 1px solid var(--border); }
.viz-beambar table.readout th { text-align: right; font-weight: 600; }
.viz-beambar table.readout th:first-child,
.viz-beambar table.readout td:first-child { text-align: left; }
.viz-beambar table.readout td { text-align: right; }
.viz-beambar .slender { font-size: 0.9em; margin: 0.5rem 0 0; font-variant-numeric: tabular-nums; }
.viz-beambar .warn { color: var(--tension); font-size: 0.9em; margin: 0.4rem 0 0; }
.viz-beambar .warn[hidden] { display: none; }
.viz-beambar .note { color: var(--fg-muted); font-size: 0.88em; margin-top: 0.75rem; }
.viz-beambar .note p { margin: 0 0 0.4rem; }
</style>

<div class="viz-beambar">
  <p class="subtitle">
    One cantilever, one force <i>F</i>: applied along the axis it acts as a bar,
    applied across it the same member acts as a beam. Rectangular section
    <i>b</i> × <i>h</i>, clamped at <i>x</i> = 0; stress profiles are taken at the clamped root.
  </p>

  <div class="controls">
    <div class="ctrl">
      <label for="bb-L">Length <i>L</i> = <span class="val" id="bb-L-val"></span> mm</label>
      <input type="range" id="bb-L" min="200" max="1000" step="10" value="600">
    </div>
    <div class="ctrl">
      <label for="bb-h">Depth <i>h</i> = <span class="val" id="bb-h-val"></span> mm</label>
      <input type="range" id="bb-h" min="10" max="50" step="1" value="20">
    </div>
    <div class="ctrl">
      <label for="bb-F">Load <i>F</i> = <span class="val" id="bb-F-val"></span> N</label>
      <input type="range" id="bb-F" min="0" max="200" step="1" value="100">
    </div>
  </div>

  <div class="presets">
    <span>Presets:</span>
    <button type="button" data-len="200" data-h="50">Stocky (L/h = 4)</button>
    <button type="button" data-len="400" data-h="40">Moderate (L/h = 10)</button>
    <button type="button" data-len="1000" data-h="20">Slender (L/h = 50)</button>
    <button type="button" data-len="1000" data-h="10">Very slender (L/h = 100)</button>
    <label class="toggle" for="bb-shared">
      <input type="checkbox" id="bb-shared" checked> Same drawing scale for bar and beam
    </label>
  </div>

  <!-- Bar row -->
  <div class="row">
    <div class="rowtitle">Bar: axial load, <i>u</i>(<i>x</i>) only</div>
    <svg id="bb-bar-svg" viewBox="0 0 460 110" role="img" aria-label="Axially loaded bar, deformed and undeformed">
      <defs>
        <marker id="bb-arrow-bar" viewBox="0 0 10 10" refX="10" refY="5"
                markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">
          <path d="M0,0 L10,5 L0,10 z" fill="var(--load)"/>
        </marker>
      </defs>
      <g transform="translate(0,55) scale(1,-1)">
        <rect x="28" y="-50" width="12" height="100" fill="var(--grid)" stroke="var(--fg-muted)"/>
        <path d="M28,-35 L40,-47 M28,-15 L40,-27 M28,5 L40,-7 M28,25 L40,13 M28,45 L40,33"
              stroke="var(--fg-muted)" stroke-width="1"/>
        <rect id="bb-bar-body" fill="var(--member)" stroke="var(--fg)" stroke-width="1"/>
        <rect id="bb-bar-ghost" class="ghost"/>
        <line id="bb-bar-arrow" stroke="var(--load)" stroke-width="2.5" marker-end="url(#bb-arrow-bar)"/>
      </g>
      <text id="bb-bar-F" class="lbl-load" y="55" dominant-baseline="middle">F</text>
      <text id="bb-bar-mag" class="muted" x="48" y="106"></text>
    </svg>
    <svg class="sect" id="bb-bar-sect" viewBox="0 0 220 202" role="img" aria-label="Axial stress through the depth at the root">
      <g transform="translate(110,95) scale(1,-1)">
        <line x1="-80" y1="75" x2="80" y2="75" stroke="var(--grid)"/>
        <line x1="-80" y1="-75" x2="80" y2="-75" stroke="var(--grid)"/>
        <polygon id="bb-bar-sig" fill="var(--tension)" fill-opacity="0.3" stroke="var(--tension)" stroke-width="1.5"/>
        <line x1="0" y1="-80" x2="0" y2="80" stroke="var(--fg-muted)"/>
        <line x1="-75" y1="-88" x2="75" y2="-88" stroke="var(--fg-muted)"/>
        <path d="M-75,-88 v-4 M0,-88 v-4 M75,-88 v-4" stroke="var(--fg-muted)"/>
      </g>
      <text x="110" y="12" text-anchor="middle" class="muted">σ<tspan baseline-shift="sub" font-size="8">xx</tspan> at root [MPa]</text>
      <text x="2" y="24" class="muted">+h/2</text>
      <text x="2" y="174" class="muted">−h/2</text>
      <text id="bb-bar-tlo" x="35" y="197" text-anchor="middle" class="muted"></text>
      <text x="110" y="197" text-anchor="middle" class="muted">0</text>
      <text id="bb-bar-thi" x="185" y="197" text-anchor="middle" class="muted"></text>
    </svg>
  </div>

  <!-- Beam row -->
  <div class="row">
    <div class="rowtitle">Beam (Euler–Bernoulli): transverse load, <i>w</i>(<i>x</i>) and rotation −<i>w</i>′</div>
    <svg id="bb-beam-svg" viewBox="0 0 460 215" role="img" aria-label="Cantilever beam, deflected and undeformed">
      <defs>
        <marker id="bb-arrow-beam" viewBox="0 0 10 10" refX="10" refY="5"
                markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">
          <path d="M0,0 L10,5 L0,10 z" fill="var(--load)"/>
        </marker>
      </defs>
      <g transform="translate(0,95) scale(1,-1)">
        <rect x="28" y="-50" width="12" height="100" fill="var(--grid)" stroke="var(--fg-muted)"/>
        <path d="M28,-35 L40,-47 M28,-15 L40,-27 M28,5 L40,-7 M28,25 L40,13 M28,45 L40,33"
              stroke="var(--fg-muted)" stroke-width="1"/>
        <path id="bb-beam-body" fill="var(--member)" stroke="var(--fg)" stroke-width="1"/>
        <rect id="bb-beam-ghost" class="ghost"/>
        <line id="bb-beam-arrow" stroke="var(--load)" stroke-width="2.5" marker-end="url(#bb-arrow-beam)"/>
      </g>
      <text id="bb-beam-F" class="lbl-load" dominant-baseline="middle">F</text>
      <text id="bb-beam-mag" class="muted" x="48" y="14"></text>
    </svg>
    <svg class="sect" id="bb-beam-sect" viewBox="0 0 220 202" role="img" aria-label="Bending stress through the depth at the root">
      <g transform="translate(110,95) scale(1,-1)">
        <line x1="-80" y1="75" x2="80" y2="75" stroke="var(--grid)"/>
        <line x1="-80" y1="-75" x2="80" y2="-75" stroke="var(--grid)"/>
        <polygon id="bb-beam-sigT" fill="var(--tension)" fill-opacity="0.3" stroke="var(--tension)" stroke-width="1.5"/>
        <polygon id="bb-beam-sigC" fill="var(--compression)" fill-opacity="0.3" stroke="var(--compression)" stroke-width="1.5"/>
        <line x1="0" y1="-80" x2="0" y2="80" stroke="var(--fg-muted)"/>
        <line x1="-75" y1="-88" x2="75" y2="-88" stroke="var(--fg-muted)"/>
        <path d="M-75,-88 v-4 M0,-88 v-4 M75,-88 v-4" stroke="var(--fg-muted)"/>
      </g>
      <text x="110" y="12" text-anchor="middle" class="muted">σ<tspan baseline-shift="sub" font-size="8">xx</tspan> at root [MPa]</text>
      <text x="2" y="24" class="muted">+h/2</text>
      <text x="2" y="174" class="muted">−h/2</text>
      <text id="bb-beam-tlo" x="35" y="197" text-anchor="middle" class="muted"></text>
      <text x="110" y="197" text-anchor="middle" class="muted">0</text>
      <text id="bb-beam-thi" x="185" y="197" text-anchor="middle" class="muted"></text>
    </svg>
  </div>

  <p class="slender">Slenderness <i>L</i>/<i>h</i> = <span class="val" id="bb-slender"></span></p>
  <p class="warn" id="bb-warn" hidden></p>

  <div class="readout-wrap">
    <table class="readout">
      <thead>
        <tr><th></th><th>Bar</th><th>Beam</th><th>Beam / bar</th></tr>
      </thead>
      <tbody>
        <tr><td>Tip stiffness <i>k</i> [N/mm]</td>
            <td id="bb-k-bar"></td><td id="bb-k-beam"></td><td></td></tr>
        <tr><td>Tip displacement [mm]</td>
            <td id="bb-d-bar"></td><td id="bb-d-beam"></td><td id="bb-d-ratio"></td></tr>
        <tr><td>Max |σ<sub>xx</sub>| at root [MPa]</td>
            <td id="bb-s-bar"></td><td id="bb-s-beam"></td><td id="bb-s-ratio"></td></tr>
      </tbody>
    </table>
  </div>

  <div class="note">
    <p>
      Linear elasticity, <i>E</i> = 70 GPa (aluminium), <i>b</i> = 20 mm fixed.
      Bar: <i>k</i> = <i>EA</i>/<i>L</i>, σ = <i>F</i>/<i>A</i>, uniform over the section.
      Beam: <i>k</i> = 3<i>EI</i>/<i>L</i>³, σ<sub>xx</sub> = −<i>E y w</i>″, linear through
      the depth with a neutral axis at <i>y</i> = 0. The ratio column is
      4(<i>L</i>/<i>h</i>)² for displacement and 6<i>L</i>/<i>h</i> for stress: it depends only
      on slenderness, not on <i>E</i>, <i>b</i> or <i>F</i>.
    </p>
    <p>
      Displacements are drawn magnified by the factor shown (fixed per geometry so the drawing
      tracks <i>F</i>). With “same drawing scale” on, the bar’s extension is usually below a
      pixel. That is the result, not a rendering bug; untick it to see the bar at its own scale.
      Stress profiles share a horizontal scale under the same switch. Red is tension (right),
      blue compression (left); the downward tip load puts the top fibre in tension at the root.
    </p>
    <p>
      Idealisations the figure does not show: the bar ignores lateral (Poisson) contraction and
      compressive buckling; the beam ignores shear deformation, which matters once
      <i>L</i>/<i>h</i> drops below about 10; both are small-deflection theories, so numbers are
      flagged once the tip deflection exceeds 10 % of <i>L</i>. The root stress is the
      beam-theory value; near the clamp the true 3D field differs (Saint-Venant). No yield check.
    </p>
  </div>

  <script>
  (function () {
    const root = document.querySelector('.viz-beambar');
    if (!root) return;
    const __q = (id) => root.querySelector('#' + id);
    const set = (el, attrs) => { for (const k in attrs) el.setAttribute(k, attrs[k]); };

    const E = 70000;    // MPa = N/mm^2
    const B = 20;       // mm, section width
    const FMAX = 200;   // N, slider max: sets the fixed drawing magnification
    const X0 = 40, LD = 300;         // drawn root position and length
    const BEAM_REF = 75, BAR_REF = 60, SIG_REF = 75;  // drawn size at F = FMAX

    function fmt(v) {
      if (!isFinite(v)) return '—';
      const a = Math.abs(v);
      if (a < 5e-13) return '0';
      if (a >= 10000) return Math.round(v).toLocaleString('en-US');
      let d;
      if (a >= 1000) d = 0;
      else if (a >= 100) d = 1;
      else if (a >= 1) d = 2;
      else d = Math.min(6, 2 - Math.floor(Math.log10(a)));
      return v.toFixed(d);
    }
    function fmtMag(n) {
      if (n >= 100) {
        const p = Math.pow(10, Math.floor(Math.log10(n)) - 1);
        return (Math.round(n / p) * p).toLocaleString('en-US');
      }
      return n.toPrecision(2);
    }
    const pts = (arr) => arr.map(p => p[0].toFixed(2) + ',' + p[1].toFixed(2)).join(' ');

    function update() {
      const L = +__q('bb-L').value;
      const h = +__q('bb-h').value;
      const F = +__q('bb-F').value;
      const shared = __q('bb-shared').checked;

      __q('bb-L-val').textContent = L;
      __q('bb-h-val').textContent = h;
      __q('bb-F-val').textContent = F;

      const A = B * h;
      const I = B * h * h * h / 12;
      const kBar = E * A / L;
      const kBeam = 3 * E * I / (L * L * L);
      const dBar = F / kBar;
      const wTip = F / kBeam;
      const sBar = F / A;
      const sBeam = F * L * (h / 2) / I;      // = 6FL/(b h^2)

      // drawing scale (true aspect ratio) and fixed-per-geometry magnifications
      const s = LD / L;
      const hd = h * s;
      const nBeam = BEAM_REF / ((FMAX / kBeam) * s);
      const nBar = shared ? nBeam : BAR_REF / ((FMAX / kBar) * s);

      // --- bar ---
      const e = dBar * s * nBar;
      const xe = X0 + LD + e;
      set(__q('bb-bar-body'), { x: X0, y: -hd / 2, width: LD + e, height: hd });
      set(__q('bb-bar-ghost'), { x: X0, y: -hd / 2, width: LD, height: hd });
      const barArrow = __q('bb-bar-arrow');
      set(barArrow, { x1: xe + 4, y1: 0, x2: xe + 34, y2: 0, visibility: F > 0 ? 'visible' : 'hidden' });
      set(__q('bb-bar-F'), { x: xe + 38, visibility: F > 0 ? 'visible' : 'hidden' });
      __q('bb-bar-mag').textContent = 'extension drawn ×' + fmtMag(nBar) +
        (shared ? ' (beam scale)' : ' (own scale)');

      // --- beam: downward tip load, w = -F x^2 (3L - x) / (6EI) ---
      const N = 48, upper = [], lower = [];
      for (let i = 0; i <= N; i++) {
        const xi = i / N, x = xi * L;
        const w = -F * x * x * (3 * L - x) / (6 * E * I);
        const yd = w * s * nBeam;
        upper.push([X0 + xi * LD, yd + hd / 2]);
        lower.push([X0 + xi * LD, yd - hd / 2]);
      }
      const yTop = upper[N][1];
      __q('bb-beam-body').setAttribute('d',
        'M' + pts(upper).replace(/ /g, ' L') + ' L' + pts(lower.slice().reverse()).replace(/ /g, ' L') + ' Z');
      set(__q('bb-beam-ghost'), { x: X0, y: -hd / 2, width: LD, height: hd });
      set(__q('bb-beam-arrow'), {
        x1: X0 + LD, y1: yTop + 40, x2: X0 + LD, y2: yTop + 2,
        visibility: F > 0 ? 'visible' : 'hidden'
      });
      set(__q('bb-beam-F'), { x: X0 + LD + 8, y: 95 - (yTop + 28), visibility: F > 0 ? 'visible' : 'hidden' });
      __q('bb-beam-mag').textContent = 'deflection drawn ×' + fmtMag(nBeam);

      // --- stress profiles at the root ---
      const refBeam = FMAX * L * (h / 2) / I;
      const refBar = shared ? refBeam : FMAX / A;
      const pxBeam = SIG_REF / refBeam, pxBar = SIG_REF / refBar;
      const xb = sBar * pxBar, xm = sBeam * pxBeam;
      __q('bb-bar-sig').setAttribute('points', pts([[0, -75], [xb, -75], [xb, 75], [0, 75]]));
      __q('bb-beam-sigT').setAttribute('points', pts([[0, 0], [0, 75], [xm, 75]]));
      __q('bb-beam-sigC').setAttribute('points', pts([[0, 0], [0, -75], [-xm, -75]]));
      __q('bb-bar-tlo').textContent = '\u2212' + fmt(refBar);
      __q('bb-bar-thi').textContent = '+' + fmt(refBar);
      __q('bb-beam-tlo').textContent = '\u2212' + fmt(refBeam);
      __q('bb-beam-thi').textContent = '+' + fmt(refBeam);

      // --- readouts ---
      __q('bb-k-bar').textContent = fmt(kBar);
      __q('bb-k-beam').textContent = fmt(kBeam);
      __q('bb-d-bar').textContent = fmt(dBar);
      __q('bb-d-beam').textContent = fmt(wTip);
      __q('bb-d-ratio').textContent = fmt(kBar / kBeam);   // 4 (L/h)^2
      __q('bb-s-bar').textContent = fmt(sBar);
      __q('bb-s-beam').textContent = fmt(sBeam);
      __q('bb-s-ratio').textContent = fmt(6 * L / h);
      __q('bb-slender').textContent = fmt(L / h);

      // --- validity flags ---
      const msgs = [];
      if (L / h < 10) {
        msgs.push('L/h < 10: shear deformation is no longer negligible, so Euler–Bernoulli ' +
                  'under-predicts the beam deflection (Timoshenko theory needed).');
      }
      if (wTip / L > 0.1) {
        msgs.push('Tip deflection is ' + fmt(100 * wTip / L) + ' % of L: outside the ' +
                  'small-deflection range, the linear beam numbers are no longer accurate.');
      }
      const warn = __q('bb-warn');
      warn.textContent = msgs.join(' ');
      warn.hidden = msgs.length === 0;
    }

    ['bb-L', 'bb-h', 'bb-F'].forEach(id => __q(id).addEventListener('input', update));
    __q('bb-shared').addEventListener('change', update);
    root.querySelectorAll('.presets button[data-len]').forEach(btn => {
      btn.addEventListener('click', () => {
        __q('bb-L').value = btn.dataset.len;
        __q('bb-h').value = btn.dataset.h;
        update();
      });
    });

    update();
  })();
  </script>
</div>
```
