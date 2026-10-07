```{=html}
<!--
  Core learning outcome: F = R U. U carries all the shape change (stretch along N1, N2); R only reorients.
  Overload check: first load = one idea (stage 1, the decomposition). Stage 2 adds the strain tensors C, E and E(phi).
  The animation parameter is called t (progress) so that it cannot be confused with the stage tabs.
-->
<style>
.viz-polar2,
[data-bs-theme="light"] .viz-polar2,
body.quarto-light .viz-polar2 {
  --fg: #1f2328; --fg-muted: #59636e; --panel-bg: #f6f8fa; --border: #d0d7de;
  --grid: #dde3ea; --slider: #57606a;
  --disp: #0072B2; --ref: #6B7684; --ok: #00805E; --bad: #B8321A;
  --s2: #C98700; --s4: #CC79A7; --s5: #56B4E9;
}
@media (prefers-color-scheme: dark) {
  .viz-polar2 {
    --fg: #e6edf3; --fg-muted: #9da7b3; --panel-bg: #1c2128; --border: #3d444d;
    --grid: #2f363e; --slider: #b1bac4;
    --disp: #56B4E9; --ref: #9AA4B0; --ok: #3CC9A0; --bad: #FF7B6B;
    --s2: #F0B030; --s4: #E3A5C7; --s5: #A6DCF7;
  }
}
[data-bs-theme="dark"] .viz-polar2,
body.quarto-dark .viz-polar2 {
  --fg: #e6edf3; --fg-muted: #9da7b3; --panel-bg: #1c2128; --border: #3d444d;
  --grid: #2f363e; --slider: #b1bac4;
  --disp: #56B4E9; --ref: #9AA4B0; --ok: #3CC9A0; --bad: #FF7B6B;
  --s2: #F0B030; --s4: #E3A5C7; --s5: #A6DCF7;
}

.viz-polar2 *, .viz-polar2 *::before, .viz-polar2 *::after { box-sizing: border-box; }
.viz-polar2 { font-family: inherit; color: var(--fg); line-height: 1.45; margin: 1.2em 0; }
.viz-polar2 [hidden] { display: none !important; }

.viz-polar2 .intro { margin: 0 0 .8em; font-size: .95em; }
.viz-polar2 .presets { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: .8em; }
.viz-polar2 .pbtn {
  font: inherit; font-size: .85em; padding: .3em .7em; cursor: pointer;
  border: 1px solid var(--border); border-radius: 6px;
  background: var(--panel-bg); color: var(--fg);
}
.viz-polar2 .pbtn:hover { border-color: var(--fg-muted); }
.viz-polar2 .pbtn:focus-visible, .viz-polar2 .stab:focus-visible, .viz-polar2 .qopt:focus-visible { outline: 2px solid var(--slider); outline-offset: 2px; }

.viz-polar2 .ctrls { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .4em 1.2em; margin-bottom: .6em; }
.viz-polar2 .ctl label { display: flex; justify-content: space-between; font-size: .9em; }
.viz-polar2 .val { font-variant-numeric: tabular-nums; color: var(--fg-muted); }
.viz-polar2 input[type=range] { width: 100%; accent-color: var(--slider); margin: .15em 0 0; }

.viz-polar2 .pbar { margin: .5em 0 .9em; padding: .6em .8em; border: 1px solid var(--border); border-radius: 8px; background: var(--panel-bg); }
.viz-polar2 .pbar label { display: flex; justify-content: space-between; gap: 1em; font-size: .9em; }
.viz-polar2 .prog { color: var(--fg-muted); font-variant-numeric: tabular-nums; text-align: right; }
.viz-polar2 .hrow { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin-top: .5em; }

.viz-polar2 .warn { color: var(--bad); font-weight: 600; font-size: .9em; margin: 0 0 .7em; }
.viz-polar2 .warn:empty { display: none; }

.viz-polar2 .fig { border: 1px solid var(--border); border-radius: 8px; background: var(--panel-bg); padding: .5em .6em .6em; margin-bottom: .8em; }
.viz-polar2 .ftitle { font-size: .9em; font-weight: 600; margin-bottom: .2em; }
.viz-polar2 .fig > svg { display: block; width: 100%; height: auto; max-width: 460px; margin: 0 auto; }
.viz-polar2 .leg { display: flex; flex-wrap: wrap; gap: .2em .9em; font-size: .8em; color: var(--fg-muted); margin-top: .35em; }
.viz-polar2 .leg span { display: inline-flex; align-items: center; gap: .35em; }
.viz-polar2 .sw { width: 34px; height: 10px; flex: none; }

.viz-polar2 .stabs { display: flex; flex-wrap: wrap; gap: 6px; margin: 1em 0 .7em; }
.viz-polar2 .stab {
  font: inherit; font-size: .9em; padding: .35em .8em; cursor: pointer; color: var(--fg);
  border: 1px solid var(--border); border-radius: 6px; background: transparent;
}
.viz-polar2 .stab[aria-selected="true"] { background: var(--panel-bg); border: 2px solid var(--fg); font-weight: 600; padding: calc(.35em - 1px) calc(.8em - 1px); }
.viz-polar2 .stitle { margin: 0 0 .5em; font-weight: 600; }

.viz-polar2 .gr { stroke: var(--grid); stroke-width: 1.2; }
.viz-polar2 .sh-ref { fill: none; stroke: var(--ref); stroke-width: 2.2; stroke-dasharray: 7 4; }
.viz-polar2 .sh-cur { fill: var(--disp); fill-opacity: .12; stroke: var(--disp); stroke-width: 2.6; }
.viz-polar2 .sh-ell { fill: none; stroke: var(--disp); stroke-width: 1.8; }
.viz-polar2 .sh-grid { stroke: var(--disp); stroke-opacity: .35; stroke-width: 1; }
.viz-polar2 .sh-u { fill: none; stroke: var(--s5); stroke-width: 2.4; stroke-dasharray: 14 4 4 4; }
.viz-polar2 .ax { stroke: var(--fg-muted); stroke-width: 1.3; }
.viz-polar2 .gain { fill: var(--s2); fill-opacity: .30; stroke: var(--s2); stroke-opacity: .30; stroke-width: .8; }
.viz-polar2 .loss { fill: var(--s4); fill-opacity: .38; stroke: var(--s4); stroke-opacity: .38; stroke-width: .8; }
.viz-polar2 .crv { fill: none; stroke: var(--s2); stroke-width: 2.6; stroke-linejoin: round; }
.viz-polar2 .pr { stroke: var(--fg); stroke-width: 3; stroke-linecap: round; }
.viz-polar2 .pv { stroke: var(--fg); stroke-width: 1.3; stroke-dasharray: 4 3; }
.viz-polar2 .zl { stroke: var(--fg-muted); stroke-width: 1.4; }
.viz-polar2 .probe { margin: .2em 0 .8em; }
.viz-polar2 .probe label { display: flex; justify-content: space-between; font-size: .9em; }
.viz-polar2 .pt { fill: var(--fg); }
.viz-polar2 .lbl { fill: var(--fg); font-size: 17px; font-family: inherit; }
.viz-polar2 .lbl2 { fill: var(--fg-muted); font-size: 13px; font-family: inherit; }

.viz-polar2 .mats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: .9em; }
.viz-polar2 .mcard { border: 1px solid var(--border); border-radius: 8px; background: var(--panel-bg); padding: .5em .7em; }
.viz-polar2 .cl { font-size: .8em; color: var(--fg-muted); margin-bottom: .3em; }
.viz-polar2 .mat {
  display: grid; grid-template-columns: repeat(2, auto); justify-content: center; gap: .1em 1em;
  padding: .1em .5em; border-left: 2px solid var(--fg-muted); border-right: 2px solid var(--fg-muted); border-radius: 6px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: .85em;
  font-variant-numeric: tabular-nums; text-align: right; white-space: pre;
}
.viz-polar2 .kv { display: grid; grid-template-columns: auto 1fr; gap: .1em .8em; font-size: .85em; font-variant-numeric: tabular-nums; white-space: pre; }
.viz-polar2 .kv span:nth-child(even) { text-align: right; }

.viz-polar2 .note { font-size: .85em; color: var(--fg-muted); }
.viz-polar2 .note p { margin: 0 0 .45em; }

/* quiz (self-contained: delete this block, the .quiz divs and the quiz section of the script to remove it) */
.viz-polar2 .quiz { margin-top: .9em; border-top: 1px solid var(--border); padding-top: .6em; }
.viz-polar2 .qq { margin-bottom: .9em; }
.viz-polar2 .qp { margin: 0 0 .4em; font-size: .92em; font-weight: 600; }
.viz-polar2 .qopts { display: flex; flex-direction: column; gap: 6px; align-items: flex-start; }
.viz-polar2 .qopt {
  font: inherit; font-size: .88em; text-align: left; padding: .3em .7em; cursor: pointer;
  border: 1px solid var(--border); border-radius: 6px; background: var(--panel-bg); color: var(--fg);
}
.viz-polar2 .qopt:disabled { cursor: default; color: var(--fg); }
.viz-polar2 .qopt.right { border: 2px solid var(--ok); }
.viz-polar2 .qopt.wrong { border: 2px solid var(--bad); }
.viz-polar2 .qfb { margin-top: .45em; font-size: .86em; }
.viz-polar2 .qchk { display: block; color: var(--fg-muted); margin-top: .2em; }
</style>

<div class="viz-polar2">
  <p class="intro">Every deformation gradient with det <i>F</i> &gt; 0 splits as <b><i>F</i> = <i>R U</i></b>: first the pure stretch
  <i>U</i> = &radic;(<i>F</i><sup>T</sup><i>F</i>) along the principal directions <i>N</i><sub>i</sub>, then the rigid rotation <i>R</i>.
  Set <i>F</i>, then drag the progress <i>t</i> (or press Play) to watch the two steps. Stage 1 reads off <i>R</i> and <i>U</i>;
  stage 2 shows what the strain tensors say about the same deformation.</p>

  <div class="presets" id="pd2-presets">
    <button type="button" class="pbtn" data-f="1,0,0,1">Identity</button>
    <button type="button" class="pbtn" data-f="1.5,0,0,1">Uniaxial stretch</button>
    <button type="button" class="pbtn" data-f="0.6,0,0,1">Uniaxial compression</button>
    <button type="button" class="pbtn" data-f="1,0.8,0,1">Simple shear (&gamma; = 0.8)</button>
    <button type="button" class="pbtn" data-f="0.6,-0.8,0.8,0.6">Rigid rotation (53.1&deg;)</button>
    <button type="button" class="pbtn" data-f="0.9,-0.8,1.2,0.6">Rotation 53.1&deg; after stretch 1.5</button>
  </div>

  <div class="ctrls">
    <div class="ctl"><label for="pd2-f11"><i>F</i>&#8321;&#8321; <span class="val" id="pd2-f11-v"></span></label>
      <input type="range" id="pd2-f11" min="-1" max="1.8" step="0.05" value="0.9"></div>
    <div class="ctl"><label for="pd2-f12"><i>F</i>&#8321;&#8322; <span class="val" id="pd2-f12-v"></span></label>
      <input type="range" id="pd2-f12" min="-1" max="1.8" step="0.05" value="-0.8"></div>
    <div class="ctl"><label for="pd2-f21"><i>F</i>&#8322;&#8321; <span class="val" id="pd2-f21-v"></span></label>
      <input type="range" id="pd2-f21" min="-1" max="1.8" step="0.05" value="1.2"></div>
    <div class="ctl"><label for="pd2-f22"><i>F</i>&#8322;&#8322; <span class="val" id="pd2-f22-v"></span></label>
      <input type="range" id="pd2-f22" min="-1" max="1.8" step="0.05" value="0.6"></div>
  </div>

  <div class="pbar">
    <label for="pd2-t">Progress <i>t</i> <span class="prog" id="pd2-prog"></span></label>
    <input type="range" id="pd2-t" min="0" max="2" step="0.02" value="0">
    <div class="hrow">
      <button type="button" class="pbtn" data-t="0">0 &middot; reference</button>
      <button type="button" class="pbtn" data-t="1">1 &middot; after <i>U</i></button>
      <button type="button" class="pbtn" data-t="2">2 &middot; after <i>R U</i> = <i>F</i></button>
      <button type="button" class="pbtn" id="pd2-play">&#9654; Play</button>
    </div>
  </div>

  <p class="warn" id="pd2-warn"></p>

  <div class="fig">
    <div class="ftitle">Deformation at progress <i>t</i></div>
    <svg id="pd2-svgB" viewBox="-240 -240 480 480" role="img" aria-label="Unit square and circle at the current progress of the polar decomposition">
      <g id="pd2-gB" transform="scale(1,-1)"></g>
    </svg>
    <div class="leg">
      <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-ref" x1="1" y1="5" x2="33" y2="5"/></svg>reference</span>
      <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-cur" x1="1" y1="5" x2="33" y2="5"/></svg>current</span>
      <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-u" x1="1" y1="5" x2="33" y2="5"/></svg>after <i>U</i> (before <i>R</i>)</span>
    </div>
  </div>

  <div class="stabs" role="tablist" aria-label="Stages">
    <button type="button" class="stab" role="tab" id="pd2-tab1" data-stage="1" aria-controls="pd2-st1">1 &middot; <i>F</i> = <i>R U</i></button>
    <button type="button" class="stab" role="tab" id="pd2-tab2" data-stage="2" aria-controls="pd2-st2">2 &middot; Strain tensors and <i>E</i>(&phi;)</button>
  </div>

  <div class="spanel" id="pd2-st1" role="tabpanel" aria-labelledby="pd2-tab1">
    <p class="stitle">Read off the rotation and the stretch.</p>
    <div class="mats">
      <div class="mcard"><div class="cl"><i>F</i></div><div class="mat" id="pd2-m-F"></div></div>
      <div class="mcard"><div class="cl"><i>R</i> (rotation)</div><div class="mat" id="pd2-m-R"></div></div>
      <div class="mcard"><div class="cl"><i>U</i> (stretch)</div><div class="mat" id="pd2-m-U"></div></div>
      <div class="mcard"><div class="cl">Scalars</div><div class="kv" id="pd2-kv"></div></div>
    </div>
    <div class="note">
      <p><b>Order.</b> <i>F</i> = <i>R U</i> is the right (material) polar decomposition: stretch first, in the reference configuration, then rotate.
      The other order, <i>F</i> = <i>V R</i>, stretches along <b>n</b><sub>i</sub> = <i>R</i> <b>N</b><sub>i</sub> after rotating and is not drawn here.
      From <i>t</i> = 0 to 1 the figure blends <i>I</i> &rarr; <i>U</i> linearly and from 1 to 2 it rotates by a fraction of &theta;. The in-between frames are an illustration; the endpoints are exact.
      &bull; marks the material point (1, 1); <i>x</i>&#8321; points right, <i>x</i>&#8322; up.</p>
      <p><b>Limits.</b> The figure is rescaled uniformly when it would leave the frame; &ldquo;view &times;k&rdquo; says by how much, and the readouts are never rescaled.
      If &lambda;&#8321; = &lambda;&#8322; every direction is principal, and the axes are drawn along <i>x</i>&#8321;, <i>x</i>&#8322;. This is 2D: <i>J</i> = det <i>F</i> = &lambda;&#8321;&lambda;&#8322; is an area ratio.
      For det <i>F</i> &le; 0 there is no proper rotation <i>R</i>, so the figure and the derived tensors are suppressed.</p>
    </div>
    <div class="quiz" id="pd2-quiz1"></div>
  </div>

  <div class="spanel" id="pd2-st2" role="tabpanel" aria-labelledby="pd2-tab2" hidden>
    <p class="stitle">Which lines does the deformation lengthen, and which does it shorten?</p>
    <div class="fig">
      <div class="ftitle">Reference: normal strain <i>E</i>(&phi;) of a line in direction &phi;</div>
      <svg id="pd2-svgP" viewBox="-56 -164 380 328" role="img" aria-label="Normal Green-Lagrange strain as a function of direction, with its maximum and minimum at the principal directions">
        <g id="pd2-gP" transform="scale(1,-1)"></g>
      </svg>
      <div class="leg">
        <span><svg class="sw" viewBox="0 0 34 10"><rect class="gain" x="1" y="1" width="32" height="8"/></svg>lengthened (<i>E</i> &gt; 0)</span>
        <span><svg class="sw" viewBox="0 0 34 10"><rect class="loss" x="1" y="1" width="32" height="8"/></svg>shortened (<i>E</i> &lt; 0)</span>
        <span><svg class="sw" viewBox="0 0 34 10"><line class="pr" x1="3" y1="5" x2="31" y2="5"/></svg>probe line (in the figure above)</span>
      </div>
      <div class="probe">
        <label for="pd2-phi">Probe direction &phi; <span class="val" id="pd2-phi-v"></span></label>
        <input type="range" id="pd2-phi" min="0" max="180" step="0.5" value="30">
        <div class="hrow">
          <button type="button" class="pbtn" id="pd2-toN1">&phi; = <i>N</i>&#8321;</button>
          <button type="button" class="pbtn" id="pd2-toN2">&phi; = <i>N</i>&#8322;</button>
        </div>
        <div class="kv" id="pd2-pkv"></div>
      </div>
    </div>
    <div class="mats">
      <div class="mcard"><div class="cl"><i>C</i> = <i>F</i><sup>T</sup><i>F</i></div><div class="mat" id="pd2-m-C"></div></div>
      <div class="mcard"><div class="cl"><i>E</i> = &frac12;(<i>C</i> &minus; <i>I</i>)</div><div class="mat" id="pd2-m-E"></div></div>
      <div class="mcard"><div class="cl">Principal strains</div><div class="kv" id="pd2-kv2"></div></div>
    </div>
    <div class="note">
      <p><i>E</i> is a tensor, so it gives a normal strain for every direction. For a material line along
      <b>N</b> = (cos &phi;, sin &phi;) in the reference, <i>E</i>(&phi;) = <b>N</b>&middot;<i>E</i> <b>N</b> = &frac12;(&lambda;&sup2; &minus; 1), where &lambda; is the stretch of that line and &lambda;&sup2; = <b>N</b>&middot;<i>C</i> <b>N</b>.
      The plot shows <i>E</i>(&phi;) against &phi; (measured from <i>x</i>&#8321;, counter-clockwise): amber where lines lengthen, pink where they shorten.
      Its maximum and minimum are the principal strains <i>E</i>&#8321; and <i>E</i>&#8322;, reached along <b>N</b><sub>1</sub> and <b>N</b><sub>2</sub>, which are also principal for <i>U</i> and <i>C</i>.
      The black segment in the figure above is the probe line carried along by the deformation.
      Matrix entries are tensor components (the off-diagonal <i>E</i>&#8321;&#8322; is half the engineering shear &gamma;&#8321;&#8322; used in the Voigt vector); shear components are not drawn.
      <i>E</i> is the finite Green&ndash;Lagrange strain, not the linearised &epsilon;.</p>
    </div>
    <div class="quiz" id="pd2-quiz2"></div>
  </div>

<script>
(function () {
  const root = (document.currentScript && document.currentScript.closest('.viz-polar2'))
            || document.querySelector('.viz-polar2');
  if (!root) return;
  const __q = (id) => root.querySelector('#' + id);

  const S = 100, NB = ' ', EPS = 1e-9, RAD = 180 / Math.PI;
  const gB = __q('pd2-gB'), gP = __q('pd2-gP');
  const phS = __q('pd2-phi'), phV = __q('pd2-phi-v');
  const sl = { a: __q('pd2-f11'), b: __q('pd2-f12'), c: __q('pd2-f21'), d: __q('pd2-f22') };
  const vl = { a: __q('pd2-f11-v'), b: __q('pd2-f12-v'), c: __q('pd2-f21-v'), d: __q('pd2-f22-v') };
  const tS = __q('pd2-t'), progEl = __q('pd2-prog'), warnEl = __q('pd2-warn');
  const playBtn = __q('pd2-play');
  const reduced = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  let raf = 0, stage = 1;

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
  const FRAME = lineV(-236, 0, 236, 0, 'gr') + lineV(0, -236, 0, 236, 'gr');

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

  function progressM(m, t) {
    if (t <= 1) {
      return [[1 + t * (m.U[0][0] - 1), t * m.U[0][1]], [t * m.U[1][0], 1 + t * (m.U[1][1] - 1)]];
    }
    const ph = m.th * (t - 1), cp = Math.cos(ph), sp = Math.sin(ph);
    return mul([[cp, -sp], [sp, cp]], m.U);
  }

  // ---------- figures ----------
  const quad = (M, n) => n[0] * (M[0][0] * n[0] + M[0][1] * n[1]) + n[1] * (M[1][0] * n[0] + M[1][1] * n[1]);
  const dir = (phi) => [Math.cos(phi), Math.sin(phi)];
  const plineV = (arr, cls) =>
    '<polyline class="' + cls + '" points="' + arr.map((p) => f1(p[0]) + ',' + f1(p[1])).join(' ') + '"/>';
  const umin = (x) => (x < 0 ? '−' : '+') + Math.abs(x).toString();

  function drawP(m, phi) {
    const W = 300, H = 130;
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
    [0, 45, 90, 135, 180].forEach((d) => { h += textV(X(d), -H - 18, d + '°', 'lbl2'); });
    h += textV(-8, H, umin(yw), 'lbl2', 'end') + textV(-8, 0, '0', 'lbl2', 'end') + textV(-8, -H, umin(-yw), 'lbl2', 'end');
    if (!m.iso) {
      const p1 = (((m.al * RAD) % 180) + 180) % 180, p2 = (p1 + 90) % 180;
      h += dotV(X(p1), Y(m.e1), 5, 'pt') + textV(X(p1), Y(m.e1) + (m.e1 >= 0 ? 17 : -17), 'E₁', 'lbl');
      h += dotV(X(p2), Y(m.e2), 5, 'pt') + textV(X(p2), Y(m.e2) + (m.e2 >= 0 ? 17 : -17), 'E₂', 'lbl');
    } else {
      h += textV(W / 2, H - 14, 'isotropic: E(φ) is constant', 'lbl2');
    }
    const ph = phi * RAD;
    h += lineV(X(ph), -H, X(ph), H, 'pv');
    h += dotV(X(ph), Y(quad(m.E, dir(phi))), 5, 'pt');
    gP.innerHTML = h;
  }

  function drawB(m, t, phi, withProbe) {
    const M = progressM(m, t);
    const vn = CORN.map((p) => Math.hypot.apply(null, ap(m.F, p)));
    const ext = Math.max.apply(null, [Math.SQRT2, 1.2 * m.l1].concat(vn));
    const k = Math.min(1, 2.1 / ext);
    let h = FRAME;
    h += polyV(CIRC.map((p) => toV(p, k)), 'sh-ref');
    h += polyV(CORN.map((p) => toV(p, k)), 'sh-ref');
    if (t > 1) h += polyV(CORN.map((p) => toV(ap(m.U, p), k)), 'sh-u');
    [-0.5, 0, 0.5].forEach(function (g) {
      [[[g, -1], [g, 1]], [[-1, g], [1, g]]].forEach(function (pq) {
        const a = toV(ap(M, pq[0]), k), b = toV(ap(M, pq[1]), k);
        h += lineV(a[0], a[1], b[0], b[1], 'sh-grid');
      });
    });
    h += polyV(CORN.map((p) => toV(ap(M, p), k)), 'sh-cur');
    h += polyV(CIRC.map((p) => toV(ap(M, p), k)), 'sh-ell');
    const final = t >= 2 - 1e-9;
    [[m.N1, final ? 'n₁' : 'N₁'], [m.N2, final ? 'n₂' : 'N₂']].forEach(function (z) {
      const n = ap(M, z[0]), len = Math.hypot(n[0], n[1]);
      const dx = n[0] / len, dy = n[1] / len;
      const tip = Math.max(1.25, 1.15 * len) * S * k;
      h += lineV(-tip * dx, -tip * dy, tip * dx, tip * dy, 'ax');
      h += textV((tip + 16) * dx, (tip + 16) * dy, z[1], 'lbl');
    });
    if (withProbe) {
      const q = toV(ap(M, dir(phi)), k);
      h += lineV(0, 0, q[0], q[1], 'pr') + dotV(q[0], q[1], 5, 'pt');
    }
    const P = toV(ap(M, [1, 1]), k);
    h += dotV(P[0], P[1], 5, 'pt');
    if (k < 0.9995) h += textV(-234, -226, 'view ×' + k.toFixed(2), 'lbl2', 'start');
    gB.innerHTML = h;
  }

  // ---------- readouts ----------
  function setMat(key, A) {
    const el = __q('pd2-m-' + key);
    if (!A) { el.innerHTML = '<span>–</span><span>–</span><span>–</span><span>–</span>'; return; }
    el.innerHTML = '<span>' + fmt(A[0][0]) + '</span><span>' + fmt(A[0][1]) + '</span><span>' +
                   fmt(A[1][0]) + '</span><span>' + fmt(A[1][1]) + '</span>';
  }
  const kvHtml = (rows) => rows.map((r) => '<span>' + r[0] + '</span><span>' + r[1] + '</span>').join('');

  function update() {
    const v = {};
    ['a', 'b', 'c', 'd'].forEach(function (key) {
      v[key] = parseFloat(sl[key].value);
      vl[key].textContent = fmt(v[key], 2);
    });
    const t = parseFloat(tS.value);
    const phiD = parseFloat(phS.value), phi = phiD / RAD;
    phV.textContent = fmt(phiD, 1) + '°';

    for (let n = 1; n <= 2; n++) {
      __q('pd2-st' + n).hidden = (n !== stage);
      __q('pd2-tab' + n).setAttribute('aria-selected', n === stage ? 'true' : 'false');
    }

    const J = v.a * v.d - v.b * v.c;
    setMat('F', [[v.a, v.b], [v.c, v.d]]);
    if (!(J > EPS)) {
      warnEl.textContent = '✗ det F = ' + J.toFixed(3) + ' ≤ 0: no proper rotation R exists. Figures and derived tensors are suppressed.';
      ['R', 'U', 'C', 'E'].forEach((key) => setMat(key, null));
      progEl.textContent = 'undefined for det F ≤ 0';
      __q('pd2-kv').innerHTML = kvHtml([['J = det F', fmt(J)]]);
      __q('pd2-kv2').innerHTML = '';
      __q('pd2-pkv').innerHTML = '';
      gB.innerHTML = textV(0, 0, 'no figure: det F ≤ 0', 'lbl');
      gP.innerHTML = textV(W_MID, 0, 'no figure: det F ≤ 0', 'lbl');
      return;
    }
    warnEl.textContent = '';
    const m = compute(v.a, v.b, v.c, v.d);
    if (t === 0) progEl.textContent = 'reference';
    else if (t < 1) progEl.textContent = 'applying U · ' + (100 * t).toFixed(0) + ' %';
    else if (t === 1) progEl.textContent = 'U applied';
    else if (t < 2) progEl.textContent = 'applying R · ' + (RAD * m.th * (t - 1)).toFixed(1) + '° of ' + (RAD * m.th).toFixed(1) + '°';
    else progEl.textContent = 'R U = F';

    setMat('R', m.R); setMat('U', m.U); setMat('C', m.C); setMat('E', m.E);
    __q('pd2-kv').innerHTML = kvHtml([
      ['J = det F', fmt(m.J)],
      ['θ (of R)', fmt(RAD * m.th, 1) + '°'],
      ['λ₁', fmt(m.l1)],
      ['λ₂', fmt(m.l2)],
      ['N₁ from x₁', m.iso ? 'any' : fmt(RAD * m.al, 1) + '°']
    ]);
    __q('pd2-kv2').innerHTML = kvHtml([['E₁', fmt(m.e1)], ['E₂', fmt(m.e2)]]);
    const nn = dir(phi), l2n = quad(m.C, nn);
    __q('pd2-pkv').innerHTML = kvHtml([
      ['λ(φ)', fmt(Math.sqrt(Math.max(0, l2n)))],
      ['E(φ)', fmt(quad(m.E, nn))]
    ]);
    if (stage === 2) drawP(m, phi);
    drawB(m, t, phi, stage === 2);
  }
  const W_MID = 150;

  // ---------- controls ----------
  function stopPlay() {
    if (raf) { cancelAnimationFrame(raf); raf = 0; }
    playBtn.innerHTML = '▶ Play';
  }
  function startPlay() {
    stopPlay();
    if (reduced) {                            // no animation: step through the key frames instead
      const cur = parseFloat(tS.value);
      tS.value = cur < 1 - 1e-9 ? '1' : (cur < 2 - 1e-9 ? '2' : '0');
      update();
      return;
    }
    playBtn.innerHTML = '⏸ Pause';
    const cur = parseFloat(tS.value);
    const from = cur >= 2 - 1e-9 ? 0 : cur / 2;   // resume from where Pause left it
    const t0 = performance.now(), DUR = 3200;
    const step = function (now) {
      const x = Math.min(1, from + (now - t0) / DUR);
      tS.value = (2 * x).toFixed(2);
      update();
      if (x < 1) raf = requestAnimationFrame(step);
      else { raf = 0; playBtn.innerHTML = '▶ Play'; }
    };
    raf = requestAnimationFrame(step);
  }

  ['a', 'b', 'c', 'd'].forEach((key) => sl[key].addEventListener('input', function () { stopPlay(); update(); }));
  tS.addEventListener('input', function () { stopPlay(); update(); });
  phS.addEventListener('input', function () { update(); });
  function toAxis(i) {
    const a = parseFloat(sl.a.value), b = parseFloat(sl.b.value), c = parseFloat(sl.c.value), d = parseFloat(sl.d.value);
    if (!(a * d - b * c > EPS)) return;
    const m = compute(a, b, c, d);
    const deg = ((((m.al * RAD) + 90 * i) % 180) + 180) % 180;
    phS.value = (Math.round(deg * 2) / 2) % 180;
    update();
  }
  __q('pd2-toN1').addEventListener('click', function () { toAxis(0); });
  __q('pd2-toN2').addEventListener('click', function () { toAxis(1); });
  playBtn.addEventListener('click', function () { if (raf) stopPlay(); else startPlay(); });
  root.querySelectorAll('[data-t]').forEach(function (btn) {
    btn.addEventListener('click', function () { stopPlay(); tS.value = btn.getAttribute('data-t'); update(); });
  });
  root.querySelectorAll('#pd2-presets [data-f]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      stopPlay();
      const f = btn.getAttribute('data-f').split(',');
      ['a', 'b', 'c', 'd'].forEach((key, i) => { sl[key].value = f[i]; });
      update();
    });
  });
  root.querySelectorAll('.stab').forEach(function (b) {
    b.addEventListener('click', function () { stage = parseInt(b.getAttribute('data-stage'), 10); update(); });
  });

  // ---------- predict-first quiz (self-contained) ----------
  function makeQuiz(box, items) {
    items.forEach(function (it) {
      const q = document.createElement('div'); q.className = 'qq';
      const p = document.createElement('p'); p.className = 'qp'; p.textContent = it.q;
      const opts = document.createElement('div'); opts.className = 'qopts';
      const fb = document.createElement('div'); fb.className = 'qfb'; fb.hidden = true; fb.setAttribute('role', 'status');
      it.o.forEach(function (txt, oi) {
        const b = document.createElement('button'); b.type = 'button'; b.className = 'qopt'; b.textContent = txt;
        b.addEventListener('click', function () {
          if (q.getAttribute('data-done')) return;
          q.setAttribute('data-done', '1');
          const bs = opts.children;
          for (let j = 0; j < bs.length; j++) {
            bs[j].disabled = true;
            if (j === it.a) { bs[j].classList.add('right'); bs[j].textContent = '✓ ' + it.o[j]; }
          }
          if (oi !== it.a) { b.classList.add('wrong'); b.textContent = '✗ ' + txt; }
          fb.innerHTML = '<b>' + (oi === it.a ? '✓ Right. ' : '✗ Not quite. ') + '</b>' + it.why +
            '<span class="qchk">Check it: ' + it.chk + '</span>';
          fb.hidden = false;
        });
        opts.appendChild(b);
      });
      q.appendChild(p); q.appendChild(opts); q.appendChild(fb); box.appendChild(q);
    });
  }
  makeQuiz(__q('pd2-quiz1'), [
    { q: 'Predict: F is a pure rigid rotation. What is the stretch U?',
      o: ['U = R', 'U = I, so all of F is the rotation', 'U has eigenvalues 0.6 and 0.8'], a: 1,
      why: 'A rigid rotation changes no lengths, so there is nothing to stretch: U = I and R = F.',
      chk: 'click “Rigid rotation (53.1°)” and read the <i>U</i> card.' },
    { q: 'Predict: simple shear with γ = 0.8, F = [[1, 0.8],[0, 1]]. What does the decomposition say about R?',
      o: ['R = I: a shear has no rotation', 'R is a clockwise rotation of about 22°', 'R is a counter-clockwise rotation of about 22°'], a: 1,
      why: 'The shear tilts the material lines on average, so part of it is rotation. θ = atan2(F₂₁ − F₁₂, F₁₁ + F₂₂) = atan2(−0.8, 2) = −21.8°, which is clockwise.',
      chk: 'click “Simple shear (γ = 0.8)” and read θ in the scalars.' },
    { q: 'Predict: for “Rotation 53.1° after stretch 1.5”, what are the principal stretches λ₁ and λ₂?',
      o: ['1.5 and 0.6', '1.5 and 1.0', '0.9 and 0.6'], a: 1,
      why: 'F = R U with U = diag(1.5, 1): the rotation after the stretch does not change the stretches.',
      chk: 'click that preset and read λ₁, λ₂ in the scalars.' }
  ]);
  makeQuiz(__q('pd2-quiz2'), [
    { q: 'Predict: uniaxial stretch 1.5 along x₁. In which direction φ is the line strain E(φ) largest?',
      o: ['φ = 0°, along x₁', 'φ = 45°', 'φ = 90°, along x₂'], a: 0,
      why: 'E(φ) = ½(λ² − 1) with λ² = 2.25 cos²φ + sin²φ: 0.625 at 0°, 0.3125 at 45° and 0 at 90°.',
      chk: 'click “Uniaxial stretch”, open stage 2 and press φ = <i>N</i>₁, then move φ to 45° and 90°.' },
    { q: 'Predict: uniaxial compression to 0.6 along x₁. Which statement is true?',
      o: ['The lines along x₂ (φ = 90°) are shortened too', 'No line is lengthened, and the lines along x₂ are unchanged', 'The lines at 45° are lengthened'], a: 1,
      why: 'E(φ) = −0.32 cos²φ is never positive and is exactly 0 at 90°.',
      chk: 'click “Uniaxial compression”, open stage 2 and sweep φ from 0° to 180°.' }
  ]);

  update();
})();
</script>
</div>
```
