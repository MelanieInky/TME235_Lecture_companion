```{=html}
<style>
.viz-lss,
[data-bs-theme="light"] .viz-lss,
body.quarto-light .viz-lss {
  --fg: #1f2328;
  --fg-muted: #5b626b;
  --panel-bg: #f5f6f8;
  --border: #d5d8de;
  --grid: #cfd3d9;
  --slider: #57606a;
  --actual: #0072B2;
  --small: #D55E00;
  --ln: #009E73;
  --ok: #009E73;
}
@media (prefers-color-scheme: dark) {
  .viz-lss {
    --fg: #e6e8eb;
    --fg-muted: #a0a7b0;
    --panel-bg: #22262b;
    --border: #3a4048;
    --grid: #454c55;
    --slider: #9aa4af;
    --actual: #56B4E9;
    --small: #E69F00;
    --ln: #2FBF9B;
    --ok: #2FBF9B;
  }
}
[data-bs-theme="dark"] .viz-lss,
body.quarto-dark .viz-lss {
  --fg: #e6e8eb;
  --fg-muted: #a0a7b0;
  --panel-bg: #22262b;
  --border: #3a4048;
  --grid: #454c55;
  --slider: #9aa4af;
  --actual: #56B4E9;
  --small: #E69F00;
  --ln: #2FBF9B;
  --ok: #2FBF9B;
}

.viz-lss *, .viz-lss *::before, .viz-lss *::after { box-sizing: border-box; }
.viz-lss { font-family: inherit; color: var(--fg); margin: 1.2em 0; }
.viz-lss .subtitle { margin: 0 0 10px; color: var(--fg-muted); font-size: .92em; }

.viz-lss .presets { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
.viz-lss .presets button {
  font: inherit; font-size: .82em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 6px; padding: 4px 10px; cursor: pointer;
}
.viz-lss .presets button:hover { border-color: var(--fg-muted); }

.viz-lss .ctl {
  display: grid; grid-template-columns: minmax(150px, 220px) 1fr 4.2em;
  align-items: center; gap: 4px 10px; margin: 6px 0;
}
.viz-lss .ctl label { font-size: .9em; }
.viz-lss .ctl input[type=range] { width: 100%; accent-color: var(--slider); }
.viz-lss .ctl .val { font-variant-numeric: tabular-nums; text-align: right; font-size: .9em; }

.viz-lss .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; margin: 10px 0; }
.viz-lss .panel { background: var(--panel-bg); border: 1px solid var(--border); border-radius: 8px; padding: 10px; }
.viz-lss .panel h4 { margin: 0 0 6px; font-size: .9em; font-weight: 600; }

.viz-lss svg.fig { display: block; width: 100%; height: auto; max-width: 460px; margin: 0 auto; }

.viz-lss .ax { stroke: var(--grid); stroke-width: 1; fill: none; }
.viz-lss .zero { stroke: var(--fg-muted); stroke-width: 1; fill: none; }
.viz-lss .guide { stroke: var(--fg-muted); stroke-width: 1; stroke-dasharray: 1 3; fill: none; }
.viz-lss .tx { fill: var(--fg-muted); font-size: 10px; font-variant-numeric: tabular-nums; }

.viz-lss .sh-ref  { fill: none; stroke: var(--fg-muted); stroke-width: 1.5; stroke-dasharray: 2 4; }
.viz-lss .sh-act  { fill: var(--actual); fill-opacity: .18; stroke: var(--actual); stroke-width: 2; }
.viz-lss .sh-grid { fill: none; stroke: var(--actual); stroke-width: 1; stroke-opacity: .4; }
.viz-lss .sh-eps  { fill: none; stroke: var(--small); stroke-width: 2; stroke-dasharray: 7 4; }
.viz-lss .mk-act  { fill: var(--actual); stroke: var(--panel-bg); stroke-width: 1.5; }
.viz-lss .mk-eps  { fill: none; stroke: var(--small); stroke-width: 2; }

.viz-lss .cv-eps { fill: none; stroke: var(--small); stroke-width: 2; stroke-dasharray: 7 4; }
.viz-lss .cv-E   { fill: none; stroke: var(--actual); stroke-width: 2.2; }
.viz-lss .cv-ln  { fill: none; stroke: var(--ln); stroke-width: 2; stroke-dasharray: 1 4; stroke-linecap: round; }
.viz-lss .mp-eps { fill: var(--small);  stroke: var(--panel-bg); stroke-width: 1.5; }
.viz-lss .mp-E   { fill: var(--actual); stroke: var(--panel-bg); stroke-width: 1.5; }
.viz-lss .mp-ln  { fill: var(--ln);     stroke: var(--panel-bg); stroke-width: 1.5; }

.viz-lss .legend { display: flex; flex-wrap: wrap; gap: 4px 14px; margin-top: 8px; font-size: .8em; color: var(--fg-muted); }
.viz-lss .legend span { display: inline-flex; align-items: center; gap: 6px; }
.viz-lss .legend svg.sw { width: 28px; height: 10px; flex: none; }

.viz-lss .tbl-wrap { overflow-x: auto; }
.viz-lss table { width: 100%; border-collapse: collapse; font-size: .82em; font-variant-numeric: tabular-nums; }
.viz-lss th, .viz-lss td { padding: 4px 6px; text-align: right; border-bottom: 1px solid var(--border); white-space: nowrap; }
.viz-lss th { color: var(--fg-muted); font-weight: 500; }
.viz-lss th:first-child, .viz-lss td:first-child { text-align: left; }
.viz-lss th .sub { display: block; font-size: .85em; font-weight: 400; }

.viz-lss .verdict { margin-top: 10px; padding: 8px 10px; border-left: 4px solid var(--border); border-radius: 4px; font-size: .88em; }
.viz-lss .verdict.ok  { border-left-color: var(--ok); }
.viz-lss .verdict.bad { border-left-color: var(--small); }

.viz-lss .note { margin: 10px 0 0; font-size: .82em; color: var(--fg-muted); line-height: 1.5; }
.viz-lss .note p { margin: 0 0 6px; }

@media (max-width: 480px) {
  .viz-lss .ctl { grid-template-columns: 1fr 4.2em; }
  .viz-lss .ctl label { grid-column: 1 / -1; }
}
</style>

<div class="viz-lss">
  <p class="subtitle">
    Compare the linearised strain &epsilon; = sym(&nabla;u) with the Green&ndash;Lagrange strain
    E = &frac12;(F<sup>T</sup>F &minus; I). A rigid rotation is the cleanest test: E stays zero, &epsilon; does not.
  </p>

  <div class="presets">
    <button type="button" data-lam="1.01" data-k="0" data-th="0">Small stretch, &lambda; = 1.01</button>
    <button type="button" data-lam="1.5" data-k="0" data-th="0">Large stretch, &lambda; = 1.5</button>
    <button type="button" data-lam="1" data-k="0.5" data-th="0">Simple shear, k = 0.5</button>
    <button type="button" data-lam="1" data-k="0" data-th="30">Rigid rotation, 30&deg;</button>
    <button type="button" data-lam="1.1" data-k="0" data-th="20">Stretch 1.1 + rotation 20&deg;</button>
  </div>

  <div class="ctl">
    <label for="lss-lam">Stretch &lambda; (x-direction)</label>
    <input type="range" id="lss-lam" min="0.5" max="1.5" step="0.01" value="1.1">
    <span class="val" id="lss-lam-v"></span>
  </div>
  <div class="ctl">
    <label for="lss-k">Shear k (F<sub>12</sub> before rotation)</label>
    <input type="range" id="lss-k" min="-0.6" max="0.6" step="0.01" value="0">
    <span class="val" id="lss-k-v"></span>
  </div>
  <div class="ctl">
    <label for="lss-th">Rigid rotation &theta; (counter-clockwise)</label>
    <input type="range" id="lss-th" min="-90" max="90" step="1" value="20">
    <span class="val" id="lss-th-v"></span>
  </div>

  <div class="grid">
    <div class="panel">
      <h4>Geometry</h4>
      <svg class="fig" id="lss-geom" viewBox="-125 -125 250 250" role="img"
           aria-label="Reference square, actual deformed square, and the shape predicted by small strain">
        <g id="lss-geom-g" transform="scale(1,-1)"></g>
      </svg>
      <div class="legend">
        <span><svg class="sw" viewBox="0 0 28 10"><line class="sh-ref" x1="1" y1="5" x2="27" y2="5"/></svg>reference</span>
        <span><svg class="sw" viewBox="0 0 28 10"><line class="sh-act" x1="1" y1="5" x2="27" y2="5"/></svg>actual, x = F X</span>
        <span><svg class="sw" viewBox="0 0 28 10"><line class="sh-eps" x1="1" y1="5" x2="27" y2="5"/></svg>small-strain, x = X + &epsilon;X</span>
      </div>
    </div>

    <div class="panel">
      <h4>Strain measures</h4>
      <div class="tbl-wrap">
        <table>
          <thead>
            <tr>
              <th></th>
              <th>&epsilon;<span class="sub">small</span></th>
              <th>E<span class="sub">Green&ndash;Lagrange</span></th>
              <th>E &minus; &epsilon;</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>11</td><td id="lss-e11"></td><td id="lss-E11"></td><td id="lss-d11"></td></tr>
            <tr><td>22</td><td id="lss-e22"></td><td id="lss-E22"></td><td id="lss-d22"></td></tr>
            <tr><td>12</td><td id="lss-e12"></td><td id="lss-E12"></td><td id="lss-d12"></td></tr>
            <tr><td>&Delta;A/A<sub>0</sub> (2D)</td><td id="lss-eA"></td><td id="lss-EA"></td><td id="lss-dA"></td></tr>
            <tr><td>&Vert;&middot;&Vert;<sub>F</sub></td><td id="lss-en"></td><td id="lss-En"></td><td id="lss-dn"></td></tr>
          </tbody>
        </table>
      </div>
      <div class="verdict" id="lss-verdict"></div>
    </div>
  </div>

  <div class="panel">
    <h4>Uniaxial stretch: three strain measures vs &lambda;</h4>
    <svg class="fig" id="lss-plot" viewBox="-48 -222 300 254" role="img"
         aria-label="Small strain, Green-Lagrange strain and logarithmic strain versus stretch">
      <g id="lss-plot-g" transform="scale(1,-1)"></g>
    </svg>
    <div class="legend">
      <span><svg class="sw" viewBox="0 0 28 10"><line class="cv-eps" x1="1" y1="5" x2="27" y2="5"/></svg>&epsilon; = &lambda; &minus; 1</span>
      <span><svg class="sw" viewBox="0 0 28 10"><line class="cv-E" x1="1" y1="5" x2="27" y2="5"/></svg>E = (&lambda;&sup2; &minus; 1)/2</span>
      <span><svg class="sw" viewBox="0 0 28 10"><line class="cv-ln" x1="2" y1="5" x2="26" y2="5"/></svg>ln &lambda; (logarithmic)</span>
    </div>
  </div>

  <div class="note">
    <p>The deformation drawn is F = R(&theta;)&middot;[[&lambda;, k],[0, 1]], applied about the square's centre.
    &epsilon; = sym(F &minus; I) and E = &frac12;(F<sup>T</sup>F &minus; I) are both computed from that same F. Their difference is second order in &nabla;u,
    so it is invisible for small deformations and grows quickly once &nabla;u is not small (including rotation, which &epsilon; does not filter out).</p>
    <p>Shear rows show the tensor component (&epsilon;<sub>12</sub>), which is half the engineering shear &gamma;<sub>12</sub> used in the Voigt vector.
    The area row is 2D: the &epsilon; column is the linearised trace &epsilon;<sub>11</sub> + &epsilon;<sub>22</sub>, the E column is the exact det F &minus; 1
    (in 3D the linearised measure is the full trace &epsilon;<sub>kk</sub>).</p>
    <p>The dashed shape is what small-strain theory assigns to the current state; it has no rotation, so it can never match a rotated body.
    The plot is uniaxial only (k = 0, &theta; = 0) and does not depend on those two sliders; the dots mark the current &lambda;.
    All three curves agree to first order near &lambda; = 1. The verdict compares &Vert;E &minus; &epsilon;&Vert;/&Vert;E&Vert; against a 5% threshold.
    Nothing is clamped: the drawing stays inside its frame over the full slider range.</p>
  </div>

<script>
(function () {
  const root = document.querySelector('.viz-lss');
  if (!root) return;
  const __q = (id) => root.querySelector('#' + id);

  const S = 90;                       // drawing scale: unit square -> 90 user units
  const NEG = '\u2212', NB = '\u00A0';

  const $lam = __q('lss-lam'), $k = __q('lss-k'), $th = __q('lss-th');

  function snap(v, d) { return Math.abs(v) < 0.5 * Math.pow(10, -d) ? 0 : v; }
  function fmt(v, d) {                // signed, padded, no "-0.0000"
    v = snap(v, d);
    return (v < 0 ? NEG : NB) + Math.abs(v).toFixed(d);
  }
  function fmtS(v, d) {               // slider display, no padding
    v = snap(v, d);
    return (v < 0 ? NEG : '') + Math.abs(v).toFixed(d);
  }
  const nrm = (a, b, c) => Math.sqrt(a * a + b * b + 2 * c * c);
  const T = (x, y, s, a) =>
    '<text class="tx" transform="translate(' + x + ' ' + y + ') scale(1 -1)" text-anchor="' + (a || 'start') + '">' + s + '</text>';
  const P = (pts) => 'M' + pts.map((q) => q[0].toFixed(2) + ' ' + q[1].toFixed(2)).join('L') + 'Z';

  function update() {
    const lam = +$lam.value, k = +$k.value, th = +$th.value * Math.PI / 180;
    const c = Math.cos(th), s = Math.sin(th);

    // F = R(theta) * [[lam, k],[0, 1]]
    const F11 = c * lam, F12 = c * k - s, F21 = s * lam, F22 = s * k + c;

    // small strain: sym(F - I)
    const e11 = F11 - 1, e22 = F22 - 1, e12 = 0.5 * (F12 + F21);
    // Green-Lagrange: (F^T F - I) / 2
    const C11 = F11 * F11 + F21 * F21, C22 = F12 * F12 + F22 * F22, C12 = F11 * F12 + F21 * F22;
    const E11 = 0.5 * (C11 - 1), E22 = 0.5 * (C22 - 1), E12 = 0.5 * C12;
    const J = F11 * F22 - F12 * F21;
    const eA = e11 + e22, EA = J - 1;

    const ne = nrm(e11, e22, e12), nE = nrm(E11, E22, E12);
    const nD = nrm(E11 - e11, E22 - e22, E12 - e12);

    // ---- slider readouts
    __q('lss-lam-v').textContent = fmtS(lam, 2);
    __q('lss-k-v').textContent = fmtS(k, 2);
    __q('lss-th-v').textContent = fmtS(+$th.value, 0) + '\u00B0';

    // ---- table
    const row = (id, a, b, d) => {
      __q('lss-e' + id).textContent = fmt(a, 4);
      __q('lss-E' + id).textContent = fmt(b, 4);
      __q('lss-d' + id).textContent = fmt(d, 4);
    };
    row('11', e11, E11, E11 - e11);
    row('22', e22, E22, E22 - e22);
    row('12', e12, E12, E12 - e12);
    __q('lss-eA').textContent = fmt(eA, 4);
    __q('lss-EA').textContent = fmt(EA, 4);
    __q('lss-dA').textContent = fmt(EA - eA, 4);
    __q('lss-en').textContent = fmt(ne, 4);
    __q('lss-En').textContent = fmt(nE, 4);
    __q('lss-dn').textContent = fmt(nD, 4);

    // ---- verdict (reachable states only)
    const vd = __q('lss-verdict');
    let cls, txt;
    if (nE < 1e-9 && ne < 1e-6) {
      cls = 'ok';
      txt = 'Undeformed: \u03B5 = E = 0.';
    } else if (nE < 1e-9) {
      cls = 'bad';
      txt = 'Rigid-body rotation: E = 0 exactly (no material deformation), yet \u03B5 \u2260 0. Small-strain theory reports strain that is not there.';
    } else {
      const r = nD / nE;
      if (r < 0.05) {
        cls = 'ok';
        txt = '\u03B5 and E agree to within ' + (r * 100).toFixed(1) + '%. The small-strain approximation is adequate here.';
      } else {
        cls = 'bad';
        txt = '\u03B5 differs from E by ' + (r * 100).toFixed(0) + '% (\u2016E \u2212 \u03B5\u2016/\u2016E\u2016). Geometric nonlinearity matters here.';
      }
    }
    vd.className = 'verdict ' + cls;
    vd.textContent = txt;

    // ---- geometry (maths coordinates; the group flips y)
    const corners = [[-.5, -.5], [.5, -.5], [.5, .5], [-.5, .5]];
    const mapR = (p) => [S * p[0], S * p[1]];
    const mapF = (p) => [S * (F11 * p[0] + F12 * p[1]), S * (F21 * p[0] + F22 * p[1])];
    const mapE = (p) => [S * ((1 + e11) * p[0] + e12 * p[1]), S * (e12 * p[0] + (1 + e22) * p[1])];

    let grid = '';
    for (let i = 1; i <= 3; i++) {
      const t = -.5 + i / 4;
      const a = mapF([t, -.5]), b = mapF([t, .5]), c2 = mapF([-.5, t]), d = mapF([.5, t]);
      grid += 'M' + a[0].toFixed(2) + ' ' + a[1].toFixed(2) + 'L' + b[0].toFixed(2) + ' ' + b[1].toFixed(2);
      grid += 'M' + c2[0].toFixed(2) + ' ' + c2[1].toFixed(2) + 'L' + d[0].toFixed(2) + ' ' + d[1].toFixed(2);
    }
    const ca = mapF(corners[0]), ce = mapE(corners[0]);
    __q('lss-geom-g').innerHTML =
      '<line class="ax" x1="-110" y1="0" x2="110" y2="0"/>' +
      '<line class="ax" x1="0" y1="-110" x2="0" y2="110"/>' +
      T(113, -3, 'x') + T(4, 112, 'y') +
      '<path class="sh-ref" d="' + P(corners.map(mapR)) + '"/>' +
      '<path class="sh-act" d="' + P(corners.map(mapF)) + '"/>' +
      '<path class="sh-grid" d="' + grid + '"/>' +
      '<path class="sh-eps" d="' + P(corners.map(mapE)) + '"/>' +
      '<circle class="mk-act" cx="' + ca[0].toFixed(2) + '" cy="' + ca[1].toFixed(2) + '" r="3.5"/>' +
      '<circle class="mk-eps" cx="' + ce[0].toFixed(2) + '" cy="' + ce[1].toFixed(2) + '" r="6"/>';

    // ---- uniaxial plot: lambda in [0.5, 1.5], strain in [-0.75, 0.75]
    const W = 240, H = 200;
    const px = (l) => (l - 0.5) * W;
    const py = (v) => (v + 0.75) / 1.5 * H;
    let g = '';
    for (let i = -3; i <= 3; i++) {
      const v = i * 0.25, y = py(v);
      g += '<line class="' + (i === 0 ? 'zero' : 'ax') + '" x1="0" y1="' + y.toFixed(2) + '" x2="' + W + '" y2="' + y.toFixed(2) + '"/>';
      g += T(-6, (y - 3).toFixed(2), (i < 0 ? NEG : '') + Math.abs(v).toFixed(2), 'end');
    }
    for (let j = 0; j <= 4; j++) {
      const l = 0.5 + j * 0.25, x = px(l);
      g += '<line class="ax" x1="' + x.toFixed(2) + '" y1="0" x2="' + x.toFixed(2) + '" y2="' + H + '"/>';
      g += T(x.toFixed(2), -13, l.toFixed(2), 'middle');
    }
    g += T(W / 2, -28, 'uniaxial stretch \u03BB = L/L\u2080', 'middle');
    g += T(-46, H + 10, 'strain (\u2013)', 'start');

    const fE = (l) => l - 1, fG = (l) => 0.5 * (l * l - 1), fL = (l) => Math.log(l);
    const curve = (f) => {
      let d = '';
      for (let i = 0; i <= 50; i++) {
        const l = 0.5 + i * 0.02;
        d += (i ? 'L' : 'M') + px(l).toFixed(2) + ' ' + py(f(l)).toFixed(2);
      }
      return d;
    };
    g += '<line class="guide" x1="' + px(lam).toFixed(2) + '" y1="0" x2="' + px(lam).toFixed(2) + '" y2="' + H + '"/>';
    g += '<path class="cv-ln" d="' + curve(fL) + '"/>';
    g += '<path class="cv-eps" d="' + curve(fE) + '"/>';
    g += '<path class="cv-E" d="' + curve(fG) + '"/>';
    const dot = (cls, f) => '<circle class="' + cls + '" cx="' + px(lam).toFixed(2) + '" cy="' + py(f(lam)).toFixed(2) + '" r="4"/>';
    g += dot('mp-ln', fL) + dot('mp-eps', fE) + dot('mp-E', fG);
    __q('lss-plot-g').innerHTML = g;
  }

  [$lam, $k, $th].forEach((el) => el.addEventListener('input', update));
  root.querySelectorAll('.presets button').forEach((b) => {
    b.addEventListener('click', () => {
      $lam.value = b.dataset.lam;
      $k.value = b.dataset.k;
      $th.value = b.dataset.th;
      update();
    });
  });

  update();
})();
</script>
</div>
```
