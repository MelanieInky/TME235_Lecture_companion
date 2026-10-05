```{=html}
<style>
.viz-polar,
[data-bs-theme="light"] .viz-polar,
body.quarto-light .viz-polar {
  --fg: #1f2328; --fg-muted: #59636e; --panel-bg: #f6f8fa; --border: #d0d7de;
  --grid: #dde3ea; --slider: #57606a;
  --disp: #0072B2; --ref: #6B7684; --bad: #B8321A;
  --s2: #C98700; --s4: #CC79A7; --s5: #56B4E9;
}
@media (prefers-color-scheme: dark) {
  .viz-polar {
    --fg: #e6edf3; --fg-muted: #9da7b3; --panel-bg: #1c2128; --border: #3d444d;
    --grid: #2f363e; --slider: #b1bac4;
    --disp: #56B4E9; --ref: #9AA4B0; --bad: #FF7B6B;
    --s2: #F0B030; --s4: #E3A5C7; --s5: #A6DCF7;
  }
}
[data-bs-theme="dark"] .viz-polar,
body.quarto-dark .viz-polar {
  --fg: #e6edf3; --fg-muted: #9da7b3; --panel-bg: #1c2128; --border: #3d444d;
  --grid: #2f363e; --slider: #b1bac4;
  --disp: #56B4E9; --ref: #9AA4B0; --bad: #FF7B6B;
  --s2: #F0B030; --s4: #E3A5C7; --s5: #A6DCF7;
}

.viz-polar *, .viz-polar *::before, .viz-polar *::after { box-sizing: border-box; }
.viz-polar { font-family: inherit; color: var(--fg); line-height: 1.45; margin: 1.2em 0; }

.viz-polar .intro { margin: 0 0 .8em; font-size: .95em; }
.viz-polar .presets { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: .8em; }
.viz-polar .pbtn {
  font: inherit; font-size: .85em; padding: .3em .7em; cursor: pointer;
  border: 1px solid var(--border); border-radius: 6px;
  background: var(--panel-bg); color: var(--fg);
}
.viz-polar .pbtn:hover { border-color: var(--fg-muted); }
.viz-polar .pbtn:focus-visible { outline: 2px solid var(--slider); outline-offset: 2px; }

.viz-polar .ctrls { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .4em 1.2em; margin-bottom: .6em; }
.viz-polar .ctl label { display: flex; justify-content: space-between; font-size: .9em; }
.viz-polar .val { font-variant-numeric: tabular-nums; color: var(--fg-muted); }
.viz-polar input[type=range] { width: 100%; accent-color: var(--slider); margin: .15em 0 0; }

.viz-polar .stagebar { margin: .5em 0 .9em; padding: .6em .8em; border: 1px solid var(--border); border-radius: 8px; background: var(--panel-bg); }
.viz-polar .stagebar label { display: flex; justify-content: space-between; gap: 1em; font-size: .9em; }
.viz-polar .stg { color: var(--fg-muted); font-variant-numeric: tabular-nums; text-align: right; }
.viz-polar .hrow { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin-top: .5em; }

.viz-polar .warn { color: var(--bad); font-weight: 600; font-size: .9em; margin: 0 0 .7em; }
.viz-polar .warn:empty { display: none; }

.viz-polar .figs { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; margin-bottom: .9em; }
.viz-polar .fig { border: 1px solid var(--border); border-radius: 8px; background: var(--panel-bg); padding: .5em .6em .6em; }
.viz-polar .ftitle { font-size: .9em; font-weight: 600; margin-bottom: .2em; }
.viz-polar .fig > svg { display: block; width: 100%; height: auto; max-width: 460px; margin: 0 auto; }
.viz-polar .leg { display: flex; flex-wrap: wrap; gap: .2em .9em; font-size: .8em; color: var(--fg-muted); margin-top: .35em; }
.viz-polar .leg span { display: inline-flex; align-items: center; gap: .35em; }
.viz-polar .sw { width: 34px; height: 10px; flex: none; }

.viz-polar .gr { stroke: var(--grid); stroke-width: 1.2; }
.viz-polar .sh-ref { fill: none; stroke: var(--ref); stroke-width: 2.2; stroke-dasharray: 7 4; }
.viz-polar .sh-cur { fill: var(--disp); fill-opacity: .12; stroke: var(--disp); stroke-width: 2.6; }
.viz-polar .sh-ell { fill: none; stroke: var(--disp); stroke-width: 1.8; }
.viz-polar .sh-grid { stroke: var(--disp); stroke-opacity: .35; stroke-width: 1; }
.viz-polar .sh-u { fill: none; stroke: var(--s5); stroke-width: 2.2; stroke-dasharray: 2 3; }
.viz-polar .ax { stroke: var(--fg-muted); stroke-width: 1.3; }
.viz-polar .gain { fill: var(--s2); fill-opacity: .30; stroke: var(--s2); stroke-opacity: .30; stroke-width: .8; }
.viz-polar .loss { fill: var(--s5); fill-opacity: .38; stroke: var(--s5); stroke-opacity: .38; stroke-width: .8; }
.viz-polar .crv { fill: none; stroke: var(--s2); stroke-width: 2.6; stroke-linejoin: round; }
.viz-polar .pr { stroke: var(--fg); stroke-width: 3; stroke-linecap: round; }
.viz-polar .pv { stroke: var(--fg); stroke-width: 1.3; stroke-dasharray: 4 3; }
.viz-polar .pt0 { fill: var(--panel-bg); stroke: var(--fg); stroke-width: 2; }
.viz-polar .zl { stroke: var(--fg-muted); stroke-width: 1.4; }
.viz-polar .probe { margin: .6em 0 .4em; }
.viz-polar .probe label { display: flex; justify-content: space-between; font-size: .9em; }
.viz-polar .pt { fill: var(--fg); }
.viz-polar .lbl { fill: var(--fg); font-size: 15px; font-family: inherit; }
.viz-polar .lbl2 { fill: var(--fg-muted); font-size: 12px; font-family: inherit; }

.viz-polar .mats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: .9em; }
.viz-polar .mcard { border: 1px solid var(--border); border-radius: 8px; background: var(--panel-bg); padding: .5em .7em; }
.viz-polar .cl { font-size: .8em; color: var(--fg-muted); margin-bottom: .3em; }
.viz-polar .mat {
  display: grid; grid-template-columns: repeat(2, auto); justify-content: center; gap: .1em 1em;
  padding: .1em .5em; border-left: 2px solid var(--fg-muted); border-right: 2px solid var(--fg-muted); border-radius: 6px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: .85em;
  font-variant-numeric: tabular-nums; text-align: right; white-space: pre;
}
.viz-polar .kv { display: grid; grid-template-columns: auto 1fr; gap: .1em .8em; font-size: .85em; font-variant-numeric: tabular-nums; white-space: pre; }
.viz-polar .kv span:nth-child(even) { text-align: right; }

.viz-polar .note { font-size: .85em; color: var(--fg-muted); }
.viz-polar .note p { margin: 0 0 .45em; }
</style>

<div class="viz-polar">
  <p class="intro">Every deformation gradient with det <i>F</i> &gt; 0 splits as <b><i>F</i> = <i>R U</i></b>: first the pure stretch
  <i>U</i> = √(<i>F</i><sup>T</sup><i>F</i>) along the principal directions <i>N</i><sub>i</sub>, then the rigid rotation <i>R</i>.
  Set <i>F</i>, then scrub <i>s</i> (or press Play) to watch the two steps. The left figures show how the strain tensors
  <i>C</i> = <i>F</i><sup>T</sup><i>F</i> and <i>E</i> = ½(<i>C</i> − <i>I</i>) assign a normal strain to every direction in the reference configuration; the probe slider picks one direction.</p>

  <div class="presets" id="pd-presets">
    <button type="button" class="pbtn" data-f="1,0,0,1">Identity</button>
    <button type="button" class="pbtn" data-f="1.5,0,0,1">Uniaxial stretch</button>
    <button type="button" class="pbtn" data-f="0.6,0,0,1">Uniaxial compression</button>
    <button type="button" class="pbtn" data-f="1,0.8,0,1">Simple shear (γ = 0.8)</button>
    <button type="button" class="pbtn" data-f="0.6,-0.8,0.8,0.6">Rigid rotation (53.1°)</button>
    <button type="button" class="pbtn" data-f="0.9,-0.8,1.2,0.6">Rotation 53.1° after stretch 1.5</button>
  </div>

  <div class="ctrls">
    <div class="ctl"><label for="pd-f11">F₁₁ <span class="val" id="pd-f11-v"></span></label>
      <input type="range" id="pd-f11" min="-1" max="1.8" step="0.05" value="0.9"></div>
    <div class="ctl"><label for="pd-f12">F₁₂ <span class="val" id="pd-f12-v"></span></label>
      <input type="range" id="pd-f12" min="-1" max="1.8" step="0.05" value="-0.8"></div>
    <div class="ctl"><label for="pd-f21">F₂₁ <span class="val" id="pd-f21-v"></span></label>
      <input type="range" id="pd-f21" min="-1" max="1.8" step="0.05" value="1.2"></div>
    <div class="ctl"><label for="pd-f22">F₂₂ <span class="val" id="pd-f22-v"></span></label>
      <input type="range" id="pd-f22" min="-1" max="1.8" step="0.05" value="0.6"></div>
  </div>

  <div class="stagebar">
    <label for="pd-s">Stage <i>s</i> <span class="stg" id="pd-stage"></span></label>
    <input type="range" id="pd-s" min="0" max="2" step="0.02" value="2">
    <div class="hrow">
      <button type="button" class="pbtn" data-s="0">0 · reference</button>
      <button type="button" class="pbtn" data-s="1">1 · after U</button>
      <button type="button" class="pbtn" data-s="2">2 · after R U = F</button>
      <button type="button" class="pbtn" id="pd-play">▶ Play</button>
    </div>
  </div>

  <p class="warn" id="pd-warn"></p>

  <div class="figs">
    <div class="fig">
      <div class="ftitle">Reference: normal strain E(φ) of a line in direction φ</div>
      <svg id="pd-svgP" viewBox="-50 -140 560 280" role="img" aria-label="Normal Green-Lagrange strain as a function of direction, with its maximum and minimum at the principal directions">
        <g id="pd-gP" transform="scale(1,-1)"></g>
      </svg>
      <div class="leg">
        <span><svg class="sw" viewBox="0 0 34 10"><rect class="gain" x="1" y="1" width="32" height="8"/></svg>lengthened (E &gt; 0)</span>
        <span><svg class="sw" viewBox="0 0 34 10"><rect class="loss" x="1" y="1" width="32" height="8"/></svg>shortened (E &lt; 0)</span>
        <span><svg class="sw" viewBox="0 0 34 10"><line class="pr" x1="3" y1="5" x2="31" y2="5"/></svg>probe line (right figure)</span>
      </div>
      <div class="probe">
        <label for="pd-phi">Probe direction φ <span class="val" id="pd-phi-v"></span></label>
        <input type="range" id="pd-phi" min="0" max="180" step="0.5" value="30">
        <div class="hrow">
          <button type="button" class="pbtn" id="pd-toN1">φ = N₁</button>
          <button type="button" class="pbtn" id="pd-toN2">φ = N₂</button>
        </div>
        <div class="kv" id="pd-pkv"></div>
      </div>
    </div>
    <div class="fig">
      <div class="ftitle">Deformation at stage <i>s</i></div>
      <svg id="pd-svgB" viewBox="-260 -260 520 520" role="img" aria-label="Unit square and circle at the current stage of the polar decomposition">
        <g id="pd-gB" transform="scale(1,-1)"></g>
      </svg>
      <div class="leg">
        <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-ref" x1="1" y1="5" x2="33" y2="5"/></svg>reference</span>
        <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-cur" x1="1" y1="5" x2="33" y2="5"/></svg>current</span>
        <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-u" x1="1" y1="5" x2="33" y2="5"/></svg>after U (before R)</span>
      </div>
    </div>
  </div>

  <div class="mats">
    <div class="mcard"><div class="cl">F</div><div class="mat" id="pd-m-F"></div></div>
    <div class="mcard"><div class="cl">R (rotation)</div><div class="mat" id="pd-m-R"></div></div>
    <div class="mcard"><div class="cl">U (stretch)</div><div class="mat" id="pd-m-U"></div></div>
    <div class="mcard"><div class="cl">C = FᵀF</div><div class="mat" id="pd-m-C"></div></div>
    <div class="mcard"><div class="cl">E = ½(C − I)</div><div class="mat" id="pd-m-E"></div></div>
    <div class="mcard"><div class="cl">Scalars</div><div class="kv" id="pd-kv"></div></div>
  </div>

  <div class="note">
    <p><b>Order.</b> <i>F</i> = <i>R U</i> is the right (material) polar decomposition: stretch first, in the reference configuration, then rotate.
    The other order, <i>F</i> = <i>V R</i>, stretches along <b>n</b><sub>i</sub> = <i>R</i> <b>N</b><sub>i</sub> after rotating and is not drawn here.
    From <i>s</i> = 0 to 1 the figure blends <i>I</i> → <i>U</i> linearly and from 1 to 2 it rotates by a fraction of θ. The in-between frames are an illustration; the endpoints are exact.</p>
    <p><b>Left figure.</b> <i>E</i> is a tensor, so it gives a normal strain for every direction. For a material line along
    <b>N</b> = (cos φ, sin φ) in the reference, E(φ) = <b>N</b>·<i>E</i> <b>N</b> = ½(λ² − 1), where λ is the stretch of that line and λ² = <b>N</b>·<i>C</i> <b>N</b>.
    The plot shows E(φ) against φ (measured from <i>x</i>₁, counter-clockwise): amber where lines lengthen, blue where they shorten.
    Its maximum and minimum are the eigenvalues E₁ and E₂, reached along the principal directions <b>N</b><sub>1</sub>, <b>N</b><sub>2</sub>, which are also principal for <i>U</i> and <i>C</i>.
    Shear components are not drawn. <i>E</i> is the finite Green–Lagrange strain, not the linearised ε.
    In the right figure ● marks the material point (1, 1) and the black segment is the probe line carried along by the deformation. <i>x</i>₁ points right, <i>x</i>₂ up.</p>
    <p><b>Limits.</b> Figures are rescaled uniformly when they would leave the frame; “view ×k” says by how much, and the readouts are never rescaled.
    If λ₁ = λ₂ every direction is principal, and the axes in the right figure are drawn along <i>x</i>₁, <i>x</i>₂. This is 2D: <i>J</i> = det <i>F</i> = λ₁λ₂ is an area ratio.
    For det <i>F</i> ≤ 0 there is no proper rotation <i>R</i>, so figures and derived tensors are suppressed.</p>
  </div>

<script>
(function () {
  const root = (document.currentScript && document.currentScript.closest('.viz-polar'))
            || document.querySelector('.viz-polar');
  if (!root) return;
  const __q = (id) => root.querySelector('#' + id);

  const S = 100, NB = '\u00A0', EPS = 1e-9, RAD = 180 / Math.PI;
  const gB = __q('pd-gB'), gP = __q('pd-gP');
  const phS = __q('pd-phi'), phV = __q('pd-phi-v');
  const sl = { a: __q('pd-f11'), b: __q('pd-f12'), c: __q('pd-f21'), d: __q('pd-f22') };
  const vl = { a: __q('pd-f11-v'), b: __q('pd-f12-v'), c: __q('pd-f21-v'), d: __q('pd-f22-v') };
  const sS = __q('pd-s'), stgEl = __q('pd-stage'), warnEl = __q('pd-warn');
  const playBtn = __q('pd-play');
  let raf = 0;

  // ---------- formatting ----------
  function fmt(x, d) {
    d = (d === undefined) ? 3 : d;
    if (!isFinite(x)) return '–';
    let v = +x.toFixed(d);
    if (v === 0) v = 0;                       // kills -0
    const s = v.toFixed(d);
    return s[0] === '-' ? s : NB + s;
  }

  // ---------- SVG string helpers (viewBox units; y is flipped by the parent <g>) ----------
  const f1 = (v) => v.toFixed(1);
  const toV = (p, k) => [p[0] * S * k, p[1] * S * k];
  const lineV = (x1, y1, x2, y2, cls) =>
    '<line class="' + cls + '" x1="' + f1(x1) + '" y1="' + f1(y1) + '" x2="' + f1(x2) + '" y2="' + f1(y2) + '"/>';
  const polyV = (arr, cls) =>
    '<polygon class="' + cls + '" points="' + arr.map((p) => f1(p[0]) + ',' + f1(p[1])).join(' ') + '"/>';
  const dotV = (x, y, r, cls) =>
    '<circle class="' + cls + '" cx="' + f1(x) + '" cy="' + f1(y) + '" r="' + r + '"/>';
  const textV = (x, y, s, cls, anchor) =>
    '<text class="' + (cls || 'lbl') + '" transform="translate(' + f1(x) + ' ' + f1(y) + ') scale(1 -1)" text-anchor="' +
    (anchor || 'middle') + '" dominant-baseline="central">' + s + '</text>';
  const FRAME = lineV(-245, 0, 245, 0, 'gr') + lineV(0, -245, 0, 245, 'gr');

  const CORN = [[-1, -1], [1, -1], [1, 1], [-1, 1]];
  const CIRC = Array.from({ length: 96 }, (_, i) => [Math.cos(2 * Math.PI * i / 96), Math.sin(2 * Math.PI * i / 96)]);
  const ap = (M, p) => [M[0][0] * p[0] + M[0][1] * p[1], M[1][0] * p[0] + M[1][1] * p[1]];
  const mul = (A, B) => [
    [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
    [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]];

  // ---------- mechanics ----------
  function compute(a, b, c, d) {
    const th = Math.atan2(c - b, a + d), ct = Math.cos(th), st = Math.sin(th);
    const R = [[ct, -st], [st, ct]];
    // U = R^T F, symmetrised (exactly symmetric for the maximising angle)
    const u11 = ct * a + st * c, u22 = -st * b + ct * d;
    const u12 = 0.5 * ((ct * b + st * d) + (-st * a + ct * c));
    const U = [[u11, u12], [u12, u22]];
    const mean = 0.5 * (u11 + u22), rad = Math.hypot(0.5 * (u11 - u22), u12);
    const iso = rad < EPS;
    const al = iso ? 0 : 0.5 * Math.atan2(2 * u12, u11 - u22);
    const l1 = mean + rad, l2 = mean - rad;
    const C = [[a * a + c * c, a * b + c * d], [a * b + c * d, b * b + d * d]];
    const E = [[0.5 * (C[0][0] - 1), 0.5 * C[0][1]], [0.5 * C[0][1], 0.5 * (C[1][1] - 1)]];
    return {
      F: [[a, b], [c, d]], R: R, U: U, C: C, E: E, th: th, al: al, iso: iso,
      l1: l1, l2: l2, e1: 0.5 * (l1 * l1 - 1), e2: 0.5 * (l2 * l2 - 1),
      N1: [Math.cos(al), Math.sin(al)], N2: [-Math.sin(al), Math.cos(al)], J: a * d - b * c
    };
  }

  function stageM(m, s) {
    if (s <= 1) {
      return [[1 + s * (m.U[0][0] - 1), s * m.U[0][1]], [s * m.U[1][0], 1 + s * (m.U[1][1] - 1)]];
    }
    const ph = m.th * (s - 1), cp = Math.cos(ph), sp = Math.sin(ph);
    return mul([[cp, -sp], [sp, cp]], m.U);
  }

  // ---------- figures ----------
  const quad = (M, n) => n[0] * (M[0][0] * n[0] + M[0][1] * n[1]) + n[1] * (M[1][0] * n[0] + M[1][1] * n[1]);
  const dir = (phi) => [Math.cos(phi), Math.sin(phi)];
  const plineV = (arr, cls) =>
    '<polyline class="' + cls + '" points="' + arr.map((p) => f1(p[0]) + ',' + f1(p[1])).join(' ') + '"/>';
  const umin = (x) => (x < 0 ? '−' : '+') + Math.abs(x).toString();

  function drawP(m, phi) {
    const W = 480, H = 110;
    const emax = Math.max(Math.abs(m.e1), Math.abs(m.e2));
    const yw = [0.25, 0.5, 1, 2, 4, 8, 16].find((v) => v >= 1.1 * emax) || 16;
    const X = (deg) => deg * W / 180, Y = (e) => e * H / yw;
    const es = [];
    for (let i = 0; i <= 180; i++) es.push(quad(m.E, dir(i / RAD)));
    let h = lineV(0, H, W, H, 'gr') + lineV(0, -H, W, -H, 'gr') + lineV(0, -H, 0, H, 'gr');
    for (let i = 0; i < 180; i++) {
      const sgn = es[i] + es[i + 1];
      if (Math.abs(sgn) < 1e-12) continue;
      h += polyV([[X(i), 0], [X(i), Y(es[i])], [X(i + 1), Y(es[i + 1])], [X(i + 1), 0]], sgn > 0 ? 'gain' : 'loss');
    }
    h += lineV(0, 0, W, 0, 'zl');
    h += plineV(es.map((e, i) => [X(i), Y(e)]), 'crv');
    [0, 45, 90, 135, 180].forEach((d) => { h += textV(X(d), -H - 16, d + '°', 'lbl2'); });
    h += textV(-8, H, umin(yw), 'lbl2', 'end') + textV(-8, 0, '0', 'lbl2', 'end') + textV(-8, -H, umin(-yw), 'lbl2', 'end');
    if (!m.iso) {
      const p1 = (((m.al * RAD) % 180) + 180) % 180, p2 = (p1 + 90) % 180;
      h += dotV(X(p1), Y(m.e1), 5, 'pt') + textV(X(p1), Y(m.e1) + (m.e1 >= 0 ? 15 : -15), 'E₁', 'lbl');
      h += dotV(X(p2), Y(m.e2), 5, 'pt') + textV(X(p2), Y(m.e2) + (m.e2 >= 0 ? 15 : -15), 'E₂', 'lbl');
    } else {
      h += textV(W / 2, H - 12, 'isotropic: E(φ) is constant', 'lbl2');
    }
    const ph = phi * RAD;
    h += lineV(X(ph), -H, X(ph), H, 'pv');
    h += dotV(X(ph), Y(quad(m.E, dir(phi))), 5, 'pt');
    gP.innerHTML = h;
  }

  function drawB(m, s, phi) {
    const M = stageM(m, s);
    const vn = CORN.map((p) => Math.hypot.apply(null, ap(m.F, p)));
    const ext = Math.max.apply(null, [Math.SQRT2, 1.2 * m.l1].concat(vn));
    const k = Math.min(1, 2.1 / ext);
    let h = FRAME;
    h += polyV(CIRC.map((p) => toV(p, k)), 'sh-ref');
    h += polyV(CORN.map((p) => toV(p, k)), 'sh-ref');
    if (s > 1) h += polyV(CORN.map((p) => toV(ap(m.U, p), k)), 'sh-u');
    [-0.5, 0, 0.5].forEach(function (g) {
      [[[g, -1], [g, 1]], [[-1, g], [1, g]]].forEach(function (pq) {
        const a = toV(ap(M, pq[0]), k), b = toV(ap(M, pq[1]), k);
        h += lineV(a[0], a[1], b[0], b[1], 'sh-grid');
      });
    });
    h += polyV(CORN.map((p) => toV(ap(M, p), k)), 'sh-cur');
    h += polyV(CIRC.map((p) => toV(ap(M, p), k)), 'sh-ell');
    const final = s >= 2 - 1e-9;
    [[m.N1, final ? 'n₁' : 'N₁'], [m.N2, final ? 'n₂' : 'N₂']].forEach(function (z) {
      const n = ap(M, z[0]), len = Math.hypot(n[0], n[1]);
      const dx = n[0] / len, dy = n[1] / len;
      const tip = Math.max(1.25, 1.15 * len) * S * k;
      h += lineV(-tip * dx, -tip * dy, tip * dx, tip * dy, 'ax');
      h += textV((tip + 16) * dx, (tip + 16) * dy, z[1], 'lbl');
    });
    const q = toV(ap(M, dir(phi)), k);
    h += lineV(0, 0, q[0], q[1], 'pr') + dotV(q[0], q[1], 5, 'pt');
    const P = toV(ap(M, [1, 1]), k);
    h += dotV(P[0], P[1], 5, 'pt');
    if (k < 0.9995) h += textV(-250, -243, 'view ×' + k.toFixed(2), 'lbl2', 'start');
    gB.innerHTML = h;
  }

  // ---------- readouts ----------
  function setMat(key, A) {
    const el = __q('pd-m-' + key);
    if (!A) { el.innerHTML = '<span>–</span><span>–</span><span>–</span><span>–</span>'; return; }
    el.innerHTML = '<span>' + fmt(A[0][0]) + '</span><span>' + fmt(A[0][1]) + '</span><span>' +
                   fmt(A[1][0]) + '</span><span>' + fmt(A[1][1]) + '</span>';
  }
  function setKV(rows) {
    __q('pd-kv').innerHTML = rows.map((r) => '<span>' + r[0] + '</span><span>' + r[1] + '</span>').join('');
  }

  function update() {
    const v = {};
    ['a', 'b', 'c', 'd'].forEach(function (key) {
      v[key] = parseFloat(sl[key].value);
      vl[key].textContent = fmt(v[key], 2);
    });
    const s = parseFloat(sS.value);
    const phiD = parseFloat(phS.value), phi = phiD / RAD;
    phV.textContent = fmt(phiD, 1) + '°';
    if (s < 1) stgEl.textContent = 'applying U · ' + (100 * s).toFixed(0) + ' %';
    else if (s === 1) stgEl.textContent = 'U applied';
    else stgEl.textContent = 'applying R';

    const J = v.a * v.d - v.b * v.c;
    setMat('F', [[v.a, v.b], [v.c, v.d]]);
    if (!(J > EPS)) {
      warnEl.textContent = '✗ det F = ' + J.toFixed(3) + ' ≤ 0: no proper rotation R exists. Figures and derived tensors are suppressed.';
      ['R', 'U', 'C', 'E'].forEach((key) => setMat(key, null));
      setKV([['J = det F', fmt(J)]]);
      gB.innerHTML = textV(0, 0, 'no figure: det F ≤ 0', 'lbl');
      gP.innerHTML = textV(240, 0, 'no figure: det F ≤ 0', 'lbl');
      __q('pd-pkv').innerHTML = '';
      return;
    }
    warnEl.textContent = '';
    const m = compute(v.a, v.b, v.c, v.d);
    if (s > 1) stgEl.textContent = 'applying R · ' + (RAD * m.th * (s - 1)).toFixed(1) + '° of ' + (RAD * m.th).toFixed(1) + '°';
    setMat('R', m.R); setMat('U', m.U); setMat('C', m.C); setMat('E', m.E);
    setKV([
      ['J = det F', fmt(m.J)],
      ['θ (of R)', fmt(RAD * m.th, 1) + '°'],
      ['λ₁', fmt(m.l1)],
      ['λ₂', fmt(m.l2)],
      ['E₁', fmt(m.e1)],
      ['E₂', fmt(m.e2)],
      ['N₁ from x₁', m.iso ? 'any' : fmt(RAD * m.al, 1) + '°']
    ]);
    const nn = dir(phi), l2n = quad(m.C, nn);
    __q('pd-pkv').innerHTML = [
      ['λ(φ)', fmt(Math.sqrt(Math.max(0, l2n)))],
      ['N·C N = λ²', fmt(l2n)],
      ['N·E N', fmt(quad(m.E, nn))]
    ].map((r) => '<span>' + r[0] + '</span><span>' + r[1] + '</span>').join('');
    drawP(m, phi);
    drawB(m, s, phi);
  }

  // ---------- controls ----------
  function stopPlay() {
    if (raf) { cancelAnimationFrame(raf); raf = 0; }
    playBtn.textContent = '▶ Play';
  }
  function startPlay() {
    stopPlay();
    playBtn.textContent = '⏸ Pause';
    const t0 = performance.now(), DUR = 3200;
    const step = function (t) {
      const x = Math.min(1, (t - t0) / DUR);
      sS.value = (2 * x).toFixed(2);
      update();
      if (x < 1) raf = requestAnimationFrame(step);
      else { raf = 0; playBtn.textContent = '▶ Play'; }
    };
    raf = requestAnimationFrame(step);
  }

  ['a', 'b', 'c', 'd'].forEach((key) => sl[key].addEventListener('input', function () { stopPlay(); update(); }));
  sS.addEventListener('input', function () { stopPlay(); update(); });
  phS.addEventListener('input', function () { update(); });
  function toAxis(i) {
    const a = parseFloat(sl.a.value), b = parseFloat(sl.b.value), c = parseFloat(sl.c.value), d = parseFloat(sl.d.value);
    if (!(a * d - b * c > EPS)) return;
    const m = compute(a, b, c, d);
    const deg = ((((m.al * RAD) + 90 * i) % 180) + 180) % 180;
    phS.value = (Math.round(deg * 2) / 2) % 180;
    update();
  }
  __q('pd-toN1').addEventListener('click', function () { toAxis(0); });
  __q('pd-toN2').addEventListener('click', function () { toAxis(1); });
  playBtn.addEventListener('click', function () { if (raf) stopPlay(); else startPlay(); });
  root.querySelectorAll('[data-s]').forEach(function (btn) {
    btn.addEventListener('click', function () { stopPlay(); sS.value = btn.getAttribute('data-s'); update(); });
  });
  root.querySelectorAll('#pd-presets [data-f]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      stopPlay();
      const f = btn.getAttribute('data-f').split(',');
      ['a', 'b', 'c', 'd'].forEach((key, i) => { sl[key].value = f[i]; });
      update();
    });
  });

  update();
})();
</script>
</div>
```
