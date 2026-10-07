```{=html}
<!--
  Core learning outcome: a rigid rotation gives E = 0 but eps != 0 (about -theta^2/2),
  and eps ~ E only while the displacement gradient H is small.
  Overload check: first load = one idea (stage 1, rotation). Stage 2 adds the error measure, stage 3 adds uniaxial + ln(lambda).
-->
<style>
.viz-lss2,
[data-bs-theme="light"] .viz-lss2,
body.quarto-light .viz-lss2 {
  --fg: #1f2328; --fg-muted: #59636e; --panel-bg: #f6f8fa; --border: #d0d7de;
  --grid: #dde3ea; --slider: #57606a;
  --disp: #0072B2; --ref: #6B7684; --ok: #00805E; --bad: #B8321A;
  --s2: #C98700; --s4: #CC79A7;
}
@media (prefers-color-scheme: dark) {
  .viz-lss2 {
    --fg: #e6edf3; --fg-muted: #9da7b3; --panel-bg: #1c2128; --border: #3d444d;
    --grid: #2f363e; --slider: #b1bac4;
    --disp: #56B4E9; --ref: #9AA4B0; --ok: #3CC9A0; --bad: #FF7B6B;
    --s2: #F0B030; --s4: #E3A5C7;
  }
}
[data-bs-theme="dark"] .viz-lss2,
body.quarto-dark .viz-lss2 {
  --fg: #e6edf3; --fg-muted: #9da7b3; --panel-bg: #1c2128; --border: #3d444d;
  --grid: #2f363e; --slider: #b1bac4;
  --disp: #56B4E9; --ref: #9AA4B0; --ok: #3CC9A0; --bad: #FF7B6B;
  --s2: #F0B030; --s4: #E3A5C7;
}

.viz-lss2 *, .viz-lss2 *::before, .viz-lss2 *::after { box-sizing: border-box; }
.viz-lss2 { font-family: inherit; color: var(--fg); line-height: 1.45; margin: 1.2em 0; }
.viz-lss2 [hidden] { display: none !important; }

.viz-lss2 .intro { margin: 0 0 .8em; font-size: .95em; }
.viz-lss2 .presets { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: .8em; }
.viz-lss2 .pbtn {
  font: inherit; font-size: .85em; padding: .3em .7em; cursor: pointer;
  border: 1px solid var(--border); border-radius: 6px;
  background: var(--panel-bg); color: var(--fg);
}
.viz-lss2 .pbtn:hover { border-color: var(--fg-muted); }
.viz-lss2 .pbtn:focus-visible, .viz-lss2 .stab:focus-visible, .viz-lss2 .qopt:focus-visible { outline: 2px solid var(--slider); outline-offset: 2px; }

.viz-lss2 .ctrls { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: .4em 1.2em; margin: 0 0 .9em; }
.viz-lss2 .ctl label { display: flex; justify-content: space-between; font-size: .9em; }
.viz-lss2 .val { font-variant-numeric: tabular-nums; color: var(--fg-muted); }
.viz-lss2 input[type=range] { width: 100%; accent-color: var(--slider); margin: .15em 0 0; }

.viz-lss2 .fig { border: 1px solid var(--border); border-radius: 8px; background: var(--panel-bg); padding: .5em .6em .6em; margin-bottom: .6em; }
.viz-lss2 .ftitle { font-size: .9em; font-weight: 600; margin-bottom: .2em; }
.viz-lss2 .fig > svg { display: block; width: 100%; height: auto; max-width: 460px; margin: 0 auto; }
.viz-lss2 .leg { display: flex; flex-wrap: wrap; gap: .2em .9em; font-size: .8em; color: var(--fg-muted); margin-top: .35em; }
.viz-lss2 .leg span { display: inline-flex; align-items: center; gap: .35em; }
.viz-lss2 .sw { width: 34px; height: 10px; flex: none; }

.viz-lss2 .stabs { display: flex; flex-wrap: wrap; gap: 6px; margin: 1em 0 .7em; }
.viz-lss2 .stab {
  font: inherit; font-size: .9em; padding: .35em .8em; cursor: pointer; color: var(--fg);
  border: 1px solid var(--border); border-radius: 6px; background: transparent;
}
.viz-lss2 .stab[aria-selected="true"] { background: var(--panel-bg); border: 2px solid var(--fg); font-weight: 600; padding: calc(.35em - 1px) calc(.8em - 1px); }
.viz-lss2 .stitle { margin: 0 0 .5em; font-weight: 600; }

.viz-lss2 .rt { display: grid; gap: .15em 1em; font-size: .88em; font-variant-numeric: tabular-nums; align-items: baseline; margin-bottom: .6em; }
.viz-lss2 .rt3 { grid-template-columns: auto repeat(2, minmax(0, 1fr)); }
.viz-lss2 .rt4 { grid-template-columns: auto repeat(3, minmax(0, 1fr)); }
.viz-lss2 .rt span { text-align: right; white-space: pre; }
.viz-lss2 .rt .hd { color: var(--fg-muted); }
.viz-lss2 .rt .rl { text-align: left; color: var(--fg-muted); }
.viz-lss2 .kcards { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-bottom: .7em; }
.viz-lss2 .kcard { border: 1px solid var(--border); border-radius: 8px; background: var(--panel-bg); padding: .5em .7em; }
.viz-lss2 .cl { font-size: .8em; color: var(--fg-muted); margin-bottom: .2em; }
.viz-lss2 .cv { font-size: 1.05em; font-variant-numeric: tabular-nums; white-space: pre; }
.viz-lss2 .line { font-size: .88em; font-variant-numeric: tabular-nums; margin: 0 0 .6em; color: var(--fg-muted); }
.viz-lss2 .verdict { margin: 0 0 .7em; padding: .5em .7em; border: 1px solid var(--border); border-radius: 6px; font-size: .9em; }
.viz-lss2 .verdict.ok { color: var(--ok); }
.viz-lss2 .verdict.bad { color: var(--bad); }

.viz-lss2 .gr { stroke: var(--grid); stroke-width: 1; fill: none; }
.viz-lss2 .zero { stroke: var(--fg-muted); stroke-width: 1.2; fill: none; }
.viz-lss2 .guide { stroke: var(--fg-muted); stroke-width: 1; stroke-dasharray: 2 3; fill: none; }
.viz-lss2 .tx { fill: var(--fg-muted); font-size: 11px; font-variant-numeric: tabular-nums; font-family: inherit; }
.viz-lss2 .sh-ref { fill: none; stroke: var(--ref); stroke-width: 1.8; stroke-dasharray: 7 4; }
.viz-lss2 .sh-act { fill: var(--disp); fill-opacity: .16; stroke: var(--disp); stroke-width: 2.2; }
.viz-lss2 .sh-grid { fill: none; stroke: var(--disp); stroke-width: 1; stroke-opacity: .4; }
.viz-lss2 .sh-eps { fill: none; stroke: var(--s2); stroke-width: 2.2; stroke-dasharray: 9 4; }
.viz-lss2 .mk-act { fill: var(--disp); stroke: var(--panel-bg); stroke-width: 1.5; }
.viz-lss2 .mk-eps { fill: none; stroke: var(--s2); stroke-width: 2.2; }
.viz-lss2 .cv-E { fill: none; stroke: var(--disp); stroke-width: 2.4; }
.viz-lss2 .cv-eps { fill: none; stroke: var(--s2); stroke-width: 2.4; stroke-dasharray: 9 4; }
.viz-lss2 .cv-ln { fill: none; stroke: var(--s4); stroke-width: 2.4; stroke-dasharray: 9 3 2 3; }
.viz-lss2 .cv-err { fill: none; stroke: var(--fg); stroke-width: 2.6; stroke-linejoin: round; }
.viz-lss2 .thr { stroke: var(--ref); stroke-width: 1.6; stroke-dasharray: 7 4; fill: none; }
.viz-lss2 .dE { fill: var(--disp); stroke: var(--panel-bg); stroke-width: 1.5; }
.viz-lss2 .dEps { fill: var(--s2); stroke: var(--panel-bg); stroke-width: 1.5; }
.viz-lss2 .dLn { fill: var(--s4); stroke: var(--panel-bg); stroke-width: 1.5; }
.viz-lss2 .dErr { fill: var(--fg); stroke: var(--panel-bg); stroke-width: 1.5; }
.viz-lss2 .dErr0 { fill: var(--panel-bg); stroke: var(--fg); stroke-width: 2; }
.viz-lss2 .lE { fill: var(--disp); font-size: 12px; font-weight: 600; font-family: inherit; }
.viz-lss2 .lEps { fill: var(--s2); font-size: 12px; font-weight: 600; font-family: inherit; }
.viz-lss2 .lLn { fill: var(--s4); font-size: 12px; font-weight: 600; font-family: inherit; }
.viz-lss2 .lRef { fill: var(--ref); font-size: 11px; font-family: inherit; }

.viz-lss2 .note { font-size: .85em; color: var(--fg-muted); margin-top: .6em; }
.viz-lss2 .note p { margin: 0 0 .45em; }

/* quiz (self-contained: delete this block, the .quiz divs and the quiz section of the script to remove it) */
.viz-lss2 .quiz { margin-top: .9em; border-top: 1px solid var(--border); padding-top: .6em; }
.viz-lss2 .qq { margin-bottom: .9em; }
.viz-lss2 .qp { margin: 0 0 .4em; font-size: .92em; font-weight: 600; }
.viz-lss2 .qopts { display: flex; flex-direction: column; gap: 6px; align-items: flex-start; }
.viz-lss2 .qopt {
  font: inherit; font-size: .88em; text-align: left; padding: .3em .7em; cursor: pointer;
  border: 1px solid var(--border); border-radius: 6px; background: var(--panel-bg); color: var(--fg);
}
.viz-lss2 .qopt:disabled { cursor: default; color: var(--fg); }
.viz-lss2 .qopt.right { border: 2px solid var(--ok); }
.viz-lss2 .qopt.wrong { border: 2px solid var(--bad); }
.viz-lss2 .qfb { margin-top: .45em; font-size: .86em; }
.viz-lss2 .qchk { display: block; color: var(--fg-muted); margin-top: .2em; }
</style>

<div class="viz-lss2">
  <p class="intro">Both strain measures are computed from one deformation gradient, <i>F</i> = <i>R</i>(&theta;)&middot;[[&lambda;, <i>k</i>],[0, 1]]:
  a stretch &lambda; and a shear <i>k</i>, followed by a rigid rotation &theta;. The small strain is &epsilon; = sym(<i>F</i> &minus; <i>I</i>) and the
  Green&ndash;Lagrange strain is <i>E</i> = &frac12;(<i>F</i><sup>T</sup><i>F</i> &minus; <i>I</i>). Work through the three stages below the figure.</p>

  <div class="presets" id="lss2-presets">
    <button type="button" class="pbtn" data-lam="1" data-k="0" data-th="30">Rigid rotation, 30&deg;</button>
    <button type="button" class="pbtn" data-lam="1.01" data-k="0" data-th="0">Small stretch, &lambda; = 1.01</button>
    <button type="button" class="pbtn" data-lam="1.5" data-k="0" data-th="0">Large stretch, &lambda; = 1.5</button>
    <button type="button" class="pbtn" data-lam="1" data-k="0.5" data-th="0">Simple shear, <i>k</i> = 0.5</button>
    <button type="button" class="pbtn" data-lam="1.1" data-k="0" data-th="20">Stretch 1.1 + rotation 20&deg;</button>
  </div>

  <div class="ctrls">
    <div class="ctl"><label for="lss2-lam">Stretch &lambda; (<i>x</i>&#8321;) <span class="val" id="lss2-lam-v"></span></label>
      <input type="range" id="lss2-lam" min="0.5" max="1.5" step="0.01" value="1"></div>
    <div class="ctl"><label for="lss2-k">Shear <i>k</i> (before rotation) <span class="val" id="lss2-k-v"></span></label>
      <input type="range" id="lss2-k" min="-0.6" max="0.6" step="0.01" value="0"></div>
    <div class="ctl"><label for="lss2-th">Rotation &theta; (counter-clockwise) <span class="val" id="lss2-th-v"></span></label>
      <input type="range" id="lss2-th" min="-90" max="90" step="1" value="30"></div>
  </div>

  <div class="fig">
    <div class="ftitle">Geometry</div>
    <svg id="lss2-geom" viewBox="-128 -128 256 256" role="img"
         aria-label="Reference square, actual deformed square, and the shape predicted by small strain">
      <g id="lss2-geom-g" transform="scale(1,-1)"></g>
    </svg>
    <div class="leg">
      <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-ref" x1="1" y1="5" x2="33" y2="5"/></svg>reference</span>
      <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-act" x1="1" y1="5" x2="33" y2="5"/></svg>actual, <i>x</i> = <i>F X</i></span>
      <span><svg class="sw" viewBox="0 0 34 10"><line class="sh-eps" x1="1" y1="5" x2="33" y2="5"/></svg>small strain, <i>x</i> = <i>X</i> + &epsilon;<i>X</i></span>
    </div>
  </div>

  <div class="stabs" role="tablist" aria-label="Stages">
    <button type="button" class="stab" role="tab" id="lss2-tab1" data-stage="1" aria-controls="lss2-st1">1 &middot; A rotation deforms nothing</button>
    <button type="button" class="stab" role="tab" id="lss2-tab2" data-stage="2" aria-controls="lss2-st2">2 &middot; How small is small?</button>
    <button type="button" class="stab" role="tab" id="lss2-tab3" data-stage="3" aria-controls="lss2-st3">3 &middot; Uniaxial stretch and ln &lambda;</button>
  </div>

  <div class="spanel" id="lss2-st1" role="tabpanel" aria-labelledby="lss2-tab1">
    <p class="stitle">Move &theta; and watch &epsilon;<sub>11</sub> and <i>E</i><sub>11</sub>.</p>
    <div class="rt rt3" aria-label="Strain components">
      <span></span><span class="hd">&epsilon; (small)</span><span class="hd"><i>E</i> (Green&ndash;Lagrange)</span>
      <span class="rl">11</span><span id="lss2-1-e11"></span><span id="lss2-1-E11"></span>
      <span class="rl">22</span><span id="lss2-1-e22"></span><span id="lss2-1-E22"></span>
      <span class="rl">12</span><span id="lss2-1-e12"></span><span id="lss2-1-E12"></span>
    </div>
    <p class="verdict" id="lss2-1-verdict"></p>
    <p class="line" id="lss2-1-quad" hidden></p>
    <div class="fig">
      <div class="ftitle">Normal strain along <i>x</i><sub>1</sub> against the rotation &theta;</div>
      <svg viewBox="-54 -184 340 218" role="img" aria-label="Small strain epsilon 11 and Green-Lagrange strain E 11 against rotation angle">
        <g id="lss2-p1-g" transform="scale(1,-1)"></g>
      </svg>
      <div class="leg">
        <span><svg class="sw" viewBox="0 0 34 10"><line class="cv-E" x1="1" y1="5" x2="33" y2="5"/></svg><i>E</i><sub>11</sub> (does not contain &theta;)</span>
        <span><svg class="sw" viewBox="0 0 34 10"><line class="cv-eps" x1="1" y1="5" x2="33" y2="5"/></svg>&epsilon;<sub>11</sub> = &lambda; cos &theta; &minus; 1</span>
      </div>
    </div>
    <div class="note">
      <p><i>E</i><sub>11</sub> = &frac12;(&lambda;&sup2; &minus; 1) has no &theta; in it, so its line is flat; &epsilon;<sub>11</sub> = &lambda; cos &theta; &minus; 1 does. The plot uses the current &lambda; and does not depend on <i>k</i>.
      Shear rows show the tensor component (&epsilon;<sub>12</sub>), which is half the engineering shear &gamma;<sub>12</sub> used in the Voigt vector.
      The dashed shape <i>X</i> + &epsilon;<i>X</i> drops the rotation, so it shows exactly the strain that &epsilon; reports.
      Here <i>E</i> is the Green&ndash;Lagrange tensor, not Young&rsquo;s modulus. Everything is 2D.</p>
    </div>
    <div class="quiz" id="lss2-quiz1"></div>
  </div>

  <div class="spanel" id="lss2-st2" role="tabpanel" aria-labelledby="lss2-tab2" hidden>
    <p class="stitle">Compare &epsilon; with <i>E</i>: how large is the difference?</p>
    <div class="rt rt4" aria-label="Strain components and their difference">
      <span></span><span class="hd">&epsilon;</span><span class="hd"><i>E</i></span><span class="hd"><i>E</i> &minus; &epsilon;</span>
      <span class="rl">11</span><span id="lss2-2-e11"></span><span id="lss2-2-E11"></span><span id="lss2-2-d11"></span>
      <span class="rl">22</span><span id="lss2-2-e22"></span><span id="lss2-2-E22"></span><span id="lss2-2-d22"></span>
      <span class="rl">12</span><span id="lss2-2-e12"></span><span id="lss2-2-E12"></span><span id="lss2-2-d12"></span>
      <span class="rl">norm</span><span id="lss2-2-ne"></span><span id="lss2-2-nE"></span><span id="lss2-2-nd"></span>
    </div>
    <p class="verdict" id="lss2-2-verdict"></p>
    <div class="fig">
      <div class="ftitle">Relative error against the stretch &lambda; (current <i>k</i> and &theta;)</div>
      <svg viewBox="-54 -184 340 218" role="img" aria-label="Relative difference between Green-Lagrange and small strain against stretch, with a 5 percent threshold">
        <g id="lss2-p2-g" transform="scale(1,-1)"></g>
      </svg>
      <div class="leg">
        <span><svg class="sw" viewBox="0 0 34 10"><line class="cv-err" x1="1" y1="5" x2="33" y2="5"/></svg>&Vert;<i>E</i> &minus; &epsilon;&Vert; / &Vert;<i>E</i>&Vert;</span>
        <span><svg class="sw" viewBox="0 0 34 10"><line class="thr" x1="1" y1="5" x2="33" y2="5"/></svg>5 % threshold</span>
        <span><svg class="sw" viewBox="0 0 34 10"><circle class="dErr0" cx="17" cy="5" r="3.5"/></svg>above 100 % (drawn on the top edge)</span>
      </div>
    </div>
    <div class="note">
      <p>The norm is the Frobenius norm of the tensor, &radic;(<i>A</i><sub>11</sub>&sup2; + <i>A</i><sub>22</sub>&sup2; + 2<i>A</i><sub>12</sub>&sup2;).
      With <i>H</i> = <i>F</i> &minus; <i>I</i>, the difference is <i>E</i> &minus; &epsilon; = &frac12;<i>H</i><sup>T</sup><i>H</i>, second order in <i>H</i>. It is small when <i>H</i> is small, and a rotation makes <i>H</i> large without making <i>E</i> large.
      The 5 % threshold is an arbitrary engineering choice. If <i>E</i> = 0 (a rigid rotation) the ratio is undefined and the verdict says so.
      The curve is broken where the ratio is undefined or above 100 %, and the readouts always show the true value. Nothing in the geometry is clamped.</p>
    </div>
    <div class="quiz" id="lss2-quiz2"></div>
  </div>

  <div class="spanel" id="lss2-st3" role="tabpanel" aria-labelledby="lss2-tab3" hidden>
    <p class="stitle">Uniaxial stretch: three strain measures at the current &lambda;.</p>
    <div class="kcards">
      <div class="kcard"><div class="cl">&epsilon; = &lambda; &minus; 1</div><div class="cv" id="lss2-3-eps"></div></div>
      <div class="kcard"><div class="cl"><i>E</i> = (&lambda;&sup2; &minus; 1)/2</div><div class="cv" id="lss2-3-E"></div></div>
      <div class="kcard"><div class="cl">ln &lambda; (logarithmic)</div><div class="cv" id="lss2-3-ln"></div></div>
    </div>
    <div class="fig">
      <div class="ftitle">Strain against the stretch &lambda;</div>
      <svg viewBox="-54 -214 340 248" role="img" aria-label="Small strain, Green-Lagrange strain and logarithmic strain versus stretch">
        <g id="lss2-p3-g" transform="scale(1,-1)"></g>
      </svg>
      <div class="leg">
        <span><svg class="sw" viewBox="0 0 34 10"><line class="cv-eps" x1="1" y1="5" x2="33" y2="5"/></svg>&epsilon; = &lambda; &minus; 1</span>
        <span><svg class="sw" viewBox="0 0 34 10"><line class="cv-E" x1="1" y1="5" x2="33" y2="5"/></svg><i>E</i> = (&lambda;&sup2; &minus; 1)/2</span>
        <span><svg class="sw" viewBox="0 0 34 10"><line class="cv-ln" x1="1" y1="5" x2="33" y2="5"/></svg>ln &lambda;</span>
      </div>
    </div>
    <div class="note">
      <p>This stage is uniaxial only (<i>F</i> = diag(&lambda;, 1)): the readouts and dots use the uniaxial formulas and ignore <i>k</i> and &theta;.
      With &epsilon; = &lambda; &minus; 1, <i>E</i> = &epsilon; + &epsilon;&sup2;/2 and ln &lambda; = &epsilon; &minus; &epsilon;&sup2;/2 + &epsilon;&sup3;/3 &minus; &hellip;, so the three agree to first order near &lambda; = 1.
      The logarithmic (Hencky) strain adds up over successive stretches, because ln(&lambda;<sub>1</sub>&lambda;<sub>2</sub>) = ln &lambda;<sub>1</sub> + ln &lambda;<sub>2</sub>; &epsilon; and <i>E</i> do not.
      Here &lambda; is the stretch, not a Lam&eacute; constant. Nothing is clamped.</p>
    </div>
    <div class="quiz" id="lss2-quiz3"></div>
  </div>

<script>
(function () {
  const root = (document.currentScript && document.currentScript.closest('.viz-lss2'))
            || document.querySelector('.viz-lss2');
  if (!root) return;
  const __q = (id) => root.querySelector('#' + id);

  const S = 90, NEG = '−', NB = ' ', DEG = Math.PI / 180, TOL = 1e-9;
  const $lam = __q('lss2-lam'), $k = __q('lss2-k'), $th = __q('lss2-th');
  let stage = 1;

  // ---------- formatting ----------
  function snap(v, d) { return Math.abs(v) < 0.5 * Math.pow(10, -d) ? 0 : v; }
  function fmt(v, d) {                    // signed, padded, never "-0.0000"
    if (!isFinite(v)) return '–';
    v = snap(v, d);
    return (v < 0 ? NEG : NB) + Math.abs(v).toFixed(d);
  }
  function fmtS(v, d) {                   // slider display, no padding
    v = snap(v, d);
    return (v < 0 ? NEG : '') + Math.abs(v).toFixed(d);
  }
  const f2 = (v) => v.toFixed(2);
  const nrm = (a, b, c) => Math.sqrt(a * a + b * b + 2 * c * c);
  const T = (x, y, s, cls, anchor) =>
    '<text class="' + (cls || 'tx') + '" transform="translate(' + f2(x) + ' ' + f2(y) + ') scale(1 -1)" text-anchor="' +
    (anchor || 'start') + '" dominant-baseline="central">' + s + '</text>';
  const PATH = (pts) => 'M' + pts.map((q) => f2(q[0]) + ' ' + f2(q[1])).join('L') + 'Z';

  // ---------- mechanics ----------
  function mech(lam, k, thDeg) {
    const th = thDeg * DEG, c = Math.cos(th), s = Math.sin(th);
    // F = R(theta) * [[lam, k],[0, 1]]
    const F11 = c * lam, F12 = c * k - s, F21 = s * lam, F22 = s * k + c;
    // small strain: sym(F - I)
    const e11 = F11 - 1, e22 = F22 - 1, e12 = 0.5 * (F12 + F21);
    // Green-Lagrange: (F^T F - I) / 2
    const C11 = F11 * F11 + F21 * F21, C22 = F12 * F12 + F22 * F22, C12 = F11 * F12 + F21 * F22;
    const E11 = 0.5 * (C11 - 1), E22 = 0.5 * (C22 - 1), E12 = 0.5 * C12;
    return {
      F11: F11, F12: F12, F21: F21, F22: F22,
      e11: e11, e22: e22, e12: e12, E11: E11, E22: E22, E12: E12,
      ne: nrm(e11, e22, e12), nE: nrm(E11, E22, E12), nD: nrm(E11 - e11, E22 - e22, E12 - e12)
    };
  }
  // relative error in percent; null where it is undefined (E = 0 but E != eps)
  function relErr(m) {
    if (m.nE < TOL) return m.nD < TOL ? 0 : null;
    return 100 * m.nD / m.nE;
  }

  // ---------- plot frame ----------
  function frame(o) {
    const px = (x) => (x - o.x0) / (o.x1 - o.x0) * o.W;
    const py = (y) => (y - o.y0) / (o.y1 - o.y0) * o.H;
    let g = '';
    o.yt.forEach(function (v) {
      const y = py(v);
      g += '<line class="' + (v === 0 && o.y0 < 0 ? 'zero' : 'gr') + '" x1="0" y1="' + f2(y) + '" x2="' + o.W + '" y2="' + f2(y) + '"/>';
      g += T(-7, y, o.yf(v), 'tx', 'end');
    });
    o.xt.forEach(function (v) {
      const x = px(v);
      g += '<line class="gr" x1="' + f2(x) + '" y1="0" x2="' + f2(x) + '" y2="' + o.H + '"/>';
      g += T(x, -12, o.xf(v), 'tx', 'middle');
    });
    g += T(o.W / 2, -29, o.xtitle, 'tx', 'middle') + T(-52, o.H + 10, o.ytitle, 'tx', 'start');
    return { g: g, px: px, py: py };
  }
  // polyline that lifts the pen at null points
  function pathOf(pts, px, py) {
    let d = '', pen = false;
    pts.forEach(function (p) {
      if (!p) { pen = false; return; }
      d += (pen ? 'L' : 'M') + f2(px(p[0])) + ' ' + f2(py(p[1]));
      pen = true;
    });
    return d;
  }
  const sgnLabel = (v, d) => (v < 0 ? NEG : '') + Math.abs(v).toFixed(d);

  // ---------- geometry (shared, above the stages) ----------
  function drawGeom(m) {
    const corners = [[-.5, -.5], [.5, -.5], [.5, .5], [-.5, .5]];
    const mapR = (p) => [S * p[0], S * p[1]];
    const mapF = (p) => [S * (m.F11 * p[0] + m.F12 * p[1]), S * (m.F21 * p[0] + m.F22 * p[1])];
    const mapE = (p) => [S * ((1 + m.e11) * p[0] + m.e12 * p[1]), S * (m.e12 * p[0] + (1 + m.e22) * p[1])];
    let grid = '';
    for (let i = 1; i <= 3; i++) {
      const t = -.5 + i / 4;
      const a = mapF([t, -.5]), b = mapF([t, .5]), c = mapF([-.5, t]), d = mapF([.5, t]);
      grid += 'M' + f2(a[0]) + ' ' + f2(a[1]) + 'L' + f2(b[0]) + ' ' + f2(b[1]);
      grid += 'M' + f2(c[0]) + ' ' + f2(c[1]) + 'L' + f2(d[0]) + ' ' + f2(d[1]);
    }
    const ca = mapF(corners[0]), ce = mapE(corners[0]);
    __q('lss2-geom-g').innerHTML =
      '<line class="gr" x1="-112" y1="0" x2="112" y2="0"/>' +
      '<line class="gr" x1="0" y1="-112" x2="0" y2="112"/>' +
      T(114, 0, 'x₁', 'tx', 'start') + T(0, 117, 'x₂', 'tx', 'middle') +
      '<path class="sh-ref" d="' + PATH(corners.map(mapR)) + '"/>' +
      '<path class="sh-act" d="' + PATH(corners.map(mapF)) + '"/>' +
      '<path class="sh-grid" d="' + grid + '"/>' +
      '<path class="sh-eps" d="' + PATH(corners.map(mapE)) + '"/>' +
      '<circle class="mk-act" cx="' + f2(ca[0]) + '" cy="' + f2(ca[1]) + '" r="3.5"/>' +
      '<circle class="mk-eps" cx="' + f2(ce[0]) + '" cy="' + f2(ce[1]) + '" r="6"/>';
  }

  // ---------- stage 1: eps11 and E11 against theta ----------
  function drawStage1(lam, k, thDeg, m) {
    const set = (id, v) => { __q('lss2-1-' + id).textContent = fmt(v, 4); };
    set('e11', m.e11); set('E11', m.E11); set('e22', m.e22); set('E22', m.E22); set('e12', m.e12); set('E12', m.E12);

    const vd = __q('lss2-1-verdict');
    let cls, txt;
    if (m.nE < TOL && m.ne < 1e-6) {
      cls = 'ok'; txt = '✓ Undeformed: ε = E = 0.';
    } else if (m.nE < TOL) {
      cls = 'bad'; txt = '✗ Rigid rotation: E = 0 (nothing is stretched or sheared), yet ε ≠ 0. The linear theory reports strain that is not there.';
    } else {
      cls = ''; txt = 'E ≠ 0, so the body is deformed. Move θ: E₁₁ stays put and ε₁₁ moves.';
    }
    vd.className = 'verdict ' + cls; vd.textContent = txt;

    const ql = __q('lss2-1-quad');
    if (Math.abs(lam - 1) < 1e-9 && Math.abs(k) < 1e-9) {
      const th = thDeg * DEG;
      ql.hidden = false;
      ql.textContent = 'ε₁₁ = cos θ − 1 = ' + fmt(Math.cos(th) - 1, 4).trim() +
        '   ≈   −θ²/2 = ' + fmt(-th * th / 2, 4).trim() + '   (θ in radians, small θ)';
    } else {
      ql.hidden = true;
    }

    const E = 0.5 * (lam * lam - 1);
    const fr = frame({
      W: 240, H: 170, x0: -90, x1: 90, xt: [-90, -45, 0, 45, 90], xf: (v) => sgnLabel(v, 0) + '°',
      y0: -1.1, y1: 0.8, yt: [-1, -0.5, 0, 0.5], yf: (v) => sgnLabel(v, 1),
      xtitle: 'rotation θ', ytitle: 'strain (–)'
    });
    const eps = [];
    for (let a = -90; a <= 90; a += 2) eps.push([a, lam * Math.cos(a * DEG) - 1]);
    let g = fr.g;
    g += '<line class="guide" x1="' + f2(fr.px(thDeg)) + '" y1="0" x2="' + f2(fr.px(thDeg)) + '" y2="170"/>';
    g += '<line class="cv-E" x1="0" y1="' + f2(fr.py(E)) + '" x2="240" y2="' + f2(fr.py(E)) + '"/>';
    g += '<path class="cv-eps" d="' + pathOf(eps, fr.px, fr.py) + '"/>';
    g += T(246, fr.py(E), 'E₁₁', 'lE', 'start');
    g += T(246, fr.py(lam * Math.cos(90 * DEG) - 1), 'ε₁₁', 'lEps', 'start');
    g += '<circle class="dE" cx="' + f2(fr.px(thDeg)) + '" cy="' + f2(fr.py(E)) + '" r="4.5"/>';
    const sx = fr.px(thDeg), sy = fr.py(m.e11);
    g += '<rect class="dEps" x="' + f2(sx - 4.5) + '" y="' + f2(sy - 4.5) + '" width="9" height="9"/>';
    __q('lss2-p1-g').innerHTML = g;
  }

  // ---------- stage 2: error against lambda ----------
  function drawStage2(lam, k, thDeg, m) {
    const set = (id, v) => { __q('lss2-2-' + id).textContent = fmt(v, 4); };
    set('e11', m.e11); set('E11', m.E11); set('d11', m.E11 - m.e11);
    set('e22', m.e22); set('E22', m.E22); set('d22', m.E22 - m.e22);
    set('e12', m.e12); set('E12', m.E12); set('d12', m.E12 - m.e12);
    set('ne', m.ne); set('nE', m.nE); set('nd', m.nD);

    const r = relErr(m);
    const vd = __q('lss2-2-verdict');
    let cls, txt;
    if (m.nE < TOL && m.ne < 1e-6) {
      cls = 'ok'; txt = '✓ Undeformed: ε = E = 0.';
    } else if (m.nE < TOL) {
      cls = 'bad'; txt = '✗ E = 0 (rigid rotation), so the relative error is undefined. ε reports ‖ε‖ = ' +
        fmt(m.ne, 4).trim() + ' for a body that is not deformed.';
    } else if (r < 5) {
      cls = 'ok'; txt = '✓ ε and E agree within ' + r.toFixed(1) + ' %. The small-strain approximation is adequate here.';
    } else {
      cls = 'bad'; txt = '✗ ε differs from E by ' + r.toFixed(0) + ' % (‖E − ε‖ / ‖E‖). Geometric nonlinearity matters here.';
    }
    vd.className = 'verdict ' + cls; vd.textContent = txt;

    const fr = frame({
      W: 240, H: 170, x0: 0.5, x1: 1.5, xt: [0.5, 0.75, 1, 1.25, 1.5], xf: (v) => v.toFixed(2),
      y0: 0, y1: 100, yt: [0, 25, 50, 75, 100], yf: (v) => v + ' %',
      xtitle: 'uniaxial stretch λ (at the current k and θ)', ytitle: 'relative error ‖E − ε‖ / ‖E‖'
    });
    const pts = [];
    let last = null;
    for (let i = 0; i <= 100; i++) {
      const l = (50 + i) / 100;
      const q = relErr(mech(l, k, thDeg));
      if (q === null || q > 100) { pts.push(null); continue; }
      pts.push([l, q]); last = [l, q];
    }
    let g = fr.g;
    g += '<line class="thr" x1="0" y1="' + f2(fr.py(5)) + '" x2="240" y2="' + f2(fr.py(5)) + '"/>';
    g += T(246, fr.py(5), '5 %', 'lRef', 'start');
    g += '<line class="guide" x1="' + f2(fr.px(lam)) + '" y1="0" x2="' + f2(fr.px(lam)) + '" y2="170"/>';
    g += '<path class="cv-err" d="' + pathOf(pts, fr.px, fr.py) + '"/>';
    if (r !== null) {
      if (r <= 100) g += '<circle class="dErr" cx="' + f2(fr.px(lam)) + '" cy="' + f2(fr.py(r)) + '" r="4.5"/>';
      else g += '<circle class="dErr0" cx="' + f2(fr.px(lam)) + '" cy="170" r="4.5"/>';
    }
    __q('lss2-p2-g').innerHTML = g;
  }

  // ---------- stage 3: uniaxial, three measures ----------
  function drawStage3(lam) {
    const fE = (l) => l - 1, fG = (l) => 0.5 * (l * l - 1), fL = (l) => Math.log(l);
    __q('lss2-3-eps').textContent = fmt(fE(lam), 4);
    __q('lss2-3-E').textContent = fmt(fG(lam), 4);
    __q('lss2-3-ln').textContent = fmt(fL(lam), 4);

    const fr = frame({
      W: 240, H: 200, x0: 0.5, x1: 1.5, xt: [0.5, 0.75, 1, 1.25, 1.5], xf: (v) => v.toFixed(2),
      y0: -0.75, y1: 0.75, yt: [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75], yf: (v) => sgnLabel(v, 2),
      xtitle: 'uniaxial stretch λ = L / L₀', ytitle: 'strain (–)'
    });
    const curve = (f) => {
      const pts = [];
      for (let i = 0; i <= 100; i++) { const l = (50 + i) / 100; pts.push([l, f(l)]); }
      return pathOf(pts, fr.px, fr.py);
    };
    let g = fr.g;
    g += '<line class="guide" x1="' + f2(fr.px(lam)) + '" y1="0" x2="' + f2(fr.px(lam)) + '" y2="200"/>';
    g += '<path class="cv-ln" d="' + curve(fL) + '"/>';
    g += '<path class="cv-eps" d="' + curve(fE) + '"/>';
    g += '<path class="cv-E" d="' + curve(fG) + '"/>';
    g += T(246, fr.py(fG(1.5)), 'E', 'lE', 'start') + T(246, fr.py(fE(1.5)), 'ε', 'lEps', 'start') + T(246, fr.py(fL(1.5)), 'ln λ', 'lLn', 'start');
    const dot = (cls, f) => '<circle class="' + cls + '" cx="' + f2(fr.px(lam)) + '" cy="' + f2(fr.py(f(lam))) + '" r="4.5"/>';
    g += dot('dLn', fL) + dot('dEps', fE) + dot('dE', fG);
    __q('lss2-p3-g').innerHTML = g;
  }

  // ---------- the one update() ----------
  function update() {
    const lam = parseFloat($lam.value), k = parseFloat($k.value), thDeg = parseFloat($th.value);
    __q('lss2-lam-v').textContent = fmtS(lam, 2);
    __q('lss2-k-v').textContent = fmtS(k, 2);
    __q('lss2-th-v').textContent = fmtS(thDeg, 0) + '°';

    for (let n = 1; n <= 3; n++) {
      __q('lss2-st' + n).hidden = (n !== stage);
      __q('lss2-tab' + n).setAttribute('aria-selected', n === stage ? 'true' : 'false');
      __q('lss2-tab' + n).setAttribute('tabindex', n === stage ? '0' : '-1');
    }

    const m = mech(lam, k, thDeg);
    drawGeom(m);
    if (stage === 1) drawStage1(lam, k, thDeg, m);
    else if (stage === 2) drawStage2(lam, k, thDeg, m);
    else drawStage3(lam);
  }

  // ---------- controls ----------
  [$lam, $k, $th].forEach((el) => el.addEventListener('input', update));
  root.querySelectorAll('#lss2-presets button').forEach(function (b) {
    b.addEventListener('click', function () {
      $lam.value = b.getAttribute('data-lam');
      $k.value = b.getAttribute('data-k');
      $th.value = b.getAttribute('data-th');
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
  makeQuiz(__q('lss2-quiz1'), [
    { q: 'Predict: a body is rotated by 30° with no stretch (λ = 1, k = 0). What do ε and E say?',
      o: ['ε = 0 and E = 0', 'ε ≠ 0 and E = 0', 'ε = 0 and E ≠ 0', 'ε ≠ 0 and E ≠ 0'], a: 1,
      why: 'Nothing is stretched or sheared, so E = 0. The linear ε gives ε₁₁ = ε₂₂ = cos 30° − 1 = −0.1340.',
      chk: 'click “Rigid rotation, 30°” and read the table.' },
    { q: 'Predict: with λ = 1 and k = 0, you increase the rotation from 10° to 20°. What happens to ε₁₁?',
      o: ['It stays the same, because a rotation stretches nothing', 'It roughly doubles', 'It grows roughly fourfold, because it scales like θ²'], a: 2,
      why: 'ε₁₁ = cos θ − 1 ≈ −θ²/2 goes from −0.0152 to −0.0603, a factor of about 4.',
      chk: 'set λ = 1, k = 0 and move θ to 10°, then 20°.' }
  ]);
  makeQuiz(__q('lss2-quiz2'), [
    { q: 'Predict: pure stretch with no rotation (k = 0, θ = 0). For which of λ = 1.05 and λ = 1.5 is ε within 5 % of E?',
      o: ['Both', 'Only λ = 1.05', 'Only λ = 1.5', 'Neither'], a: 1,
      why: 'The error is ½(λ − 1)² against E ≈ λ − 1, so the ratio is (λ − 1)/(λ + 1): 2.4 % at 1.05 and 20 % at 1.5.',
      chk: 'in stage 2 set k = 0, θ = 0 and read the verdict at λ = 1.05 and at λ = 1.5.' },
    { q: 'Predict: λ = 1.01, k = 0, θ = 0 is a 1 % stretch and ε agrees with E. You now add a 20° rotation. What does the verdict say?',
      o: ['They still agree: the strain is only 1 %', 'They disagree by far more than the 1 % strain itself'], a: 1,
      why: 'The stretch is unchanged, so E is unchanged, but ε now contains the rotation: ‖E − ε‖ / ‖E‖ is about 850 %.',
      chk: 'in stage 2 use the “Small stretch” preset, then move θ to 20°.' }
  ]);
  makeQuiz(__q('lss2-quiz3'), [
    { q: 'Predict: the body is compressed to half its length (λ = 0.5). Which of ε, E and ln λ has the largest magnitude?',
      o: ['ε = λ − 1', 'E = (λ² − 1)/2', 'ln λ'], a: 2,
      why: 'ε = −0.500, E = −0.375 and ln λ = −0.693. Under compression the logarithmic strain is the most negative.',
      chk: 'in stage 3 set λ = 0.5 and read the three cards.' }
  ]);

  update();
})();
</script>
</div>
```
