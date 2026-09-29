```{=html}
<style>
.viz-vws,
[data-bs-theme="light"] .viz-vws,
body.quarto-light .viz-vws {
  --fg: #1f2328; --fg-muted: #5b636d; --panel-bg: #f6f7f9; --border: #d4d8de;
  --grid: #e3e6ea; --slider: #3b6ea8;
  --load: #00805E; --stress: #D55E00; --ref: #6B7684; --ok: #00805E; --bad: #B8321A;
  --s1: #0072B2; --s2: #C98700; --s3: #00805E; --s4: #CC79A7; --s5: #56B4E9;
}
@media (prefers-color-scheme: dark) {
  .viz-vws {
    --fg: #e6e8eb; --fg-muted: #a0a8b3; --panel-bg: #1e2227; --border: #3a414a;
    --grid: #2c323a; --slider: #7fb0e6;
    --load: #3CC9A0; --stress: #FF8C42; --ref: #9AA4B0; --ok: #3CC9A0; --bad: #FF7B6B;
    --s1: #5AA0F0; --s2: #F0B030; --s3: #3CC9A0; --s4: #E3A5C7; --s5: #A6DCF7;
  }
}
[data-bs-theme="dark"] .viz-vws,
body.quarto-dark .viz-vws {
  --fg: #e6e8eb; --fg-muted: #a0a8b3; --panel-bg: #1e2227; --border: #3a414a;
  --grid: #2c323a; --slider: #7fb0e6;
  --load: #3CC9A0; --stress: #FF8C42; --ref: #9AA4B0; --ok: #3CC9A0; --bad: #FF7B6B;
  --s1: #5AA0F0; --s2: #F0B030; --s3: #3CC9A0; --s4: #E3A5C7; --s5: #A6DCF7;
}

.viz-vws { color: var(--fg); font-family: inherit; }
.viz-vws *, .viz-vws *::before, .viz-vws *::after { box-sizing: border-box; }
.viz-vws .intro { color: var(--fg-muted); font-size: .95em; margin: 0 0 .8em; }
.viz-vws .controls {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .6em 1.2em;
  padding: .8em; background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 6px; margin-bottom: .8em;
}
.viz-vws .ctrl label { display: block; font-size: .88em; color: var(--fg-muted); margin-bottom: .2em; }
.viz-vws .ctrl .hrow { display: flex; gap: .5em; align-items: center; }
.viz-vws input[type="range"] { flex: 1; min-width: 0; accent-color: var(--slider); }
.viz-vws input[type="checkbox"] { accent-color: var(--slider); }
.viz-vws input:disabled { opacity: .35; }
.viz-vws input[type="number"] {
  width: 5.2em; font: inherit; font-size: .9em; font-variant-numeric: tabular-nums;
  color: var(--fg); background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 4px; padding: .15em .3em;
}
.viz-vws select {
  flex: 1; min-width: 0; font: inherit; font-size: .9em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 4px; padding: .2em .3em;
}
.viz-vws button {
  font: inherit; font-size: .85em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 4px; padding: .25em .6em; cursor: pointer;
}
.viz-vws button:hover, .viz-vws button:focus-visible { border-color: var(--slider); }
.viz-vws .check { display: flex; gap: .4em; align-items: center; font-size: .88em; color: var(--fg-muted); }
.viz-vws .fig {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 6px;
  padding: .5em; margin-bottom: .8em;
}
.viz-vws svg { display: block; width: 100%; height: auto; max-width: 460px; margin: 0 auto; }
.viz-vws svg text { fill: var(--fg-muted); font-size: 11px; font-family: inherit; }
.viz-vws svg text.lbl { fill: var(--fg); }
.viz-vws table { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; font-size: .92em; }
.viz-vws td { padding: .3em .4em; border-bottom: 1px solid var(--grid); vertical-align: top; }
.viz-vws td.num { text-align: right; white-space: nowrap; }
.viz-vws td .eq { display: block; font-size: .85em; color: var(--fg-muted); }
.viz-vws td label { cursor: pointer; }
.viz-vws svg.swatch { display: inline-block; width: 22px; height: 8px; max-width: none; margin: 0 .35em 0 0; vertical-align: .05em; }
.viz-vws .pass { color: var(--ok); }
.viz-vws .fail { color: var(--bad); }
.viz-vws .verdict { margin: .7em 0 .5em; font-weight: 600; }
.viz-vws .verdict.ok { color: var(--ok); }
.viz-vws .verdict.bad { color: var(--bad); }
.viz-vws .note { font-size: .88em; color: var(--fg-muted); margin-top: .9em; }
.viz-vws .note p { margin: 0 0 .5em; }
.viz-vws .quiz { padding: .8em; background: var(--panel-bg); border: 1px solid var(--border); border-radius: 6px; margin: .8em 0; }
.viz-vws .quiz .qhead { font-size: .85em; color: var(--fg-muted); }
.viz-vws .quiz .qtext { margin: .3em 0 .6em; font-weight: 600; }
.viz-vws .quiz .qopts { display: flex; flex-direction: column; gap: .35em; }
.viz-vws .quiz .qopt { text-align: left; }
.viz-vws .quiz .qopt:disabled { cursor: default; }
.viz-vws .quiz .qopt.correct { border-color: var(--ok); color: var(--ok); }
.viz-vws .quiz .qopt.wrong { border-color: var(--bad); color: var(--bad); }
.viz-vws .quiz .qfeedback, .viz-vws .quiz .qtry { margin: .6em 0 0; font-size: .92em; }
.viz-vws .quiz .qfeedback.ok { color: var(--ok); }
.viz-vws .quiz .qfeedback.bad { color: var(--bad); }
.viz-vws .quiz .qtry { color: var(--fg-muted); }
.viz-vws .quiz .qnav { display: flex; justify-content: space-between; margin-top: .7em; }
@media (max-width: 560px) {
  .viz-vws .controls { grid-template-columns: 1fr; }
}
</style>

<div class="viz-vws">
  <p class="intro">Find the axial force in the bar using only the principle of virtual work.
  Guess N(x) = A + B·(x/L) + C·(x/L)², then check it against five test functions δu. Adjust A, B
  and C until every test balances.</p>

  <div class="controls">
    <div class="ctrl">
      <label for="vws-load">Load case</label>
      <div class="hrow">
        <select id="vws-load">
          <option value="uniform">Uniform q</option>
          <option value="tri">Triangular q(x) = q₀·x/L</option>
        </select>
        <button type="button" id="vws-new">New loads</button>
      </div>
    </div>
    <div class="ctrl">
      <label class="check" for="vws-usec"><input type="checkbox" id="vws-usec"> Include the (x/L)² term</label>
      <button type="button" id="vws-reset" style="margin-top:.3em">Reset guess to zero</button>
    </div>
    <div class="ctrl">
      <label for="vws-A">A = N(0) [kN]</label>
      <div class="hrow">
        <input type="range" id="vws-A" min="-20" max="50" step="0.5" value="0">
        <input type="number" id="vws-A-num" min="-20" max="50" step="0.5" value="0" aria-label="A in kN">
      </div>
    </div>
    <div class="ctrl">
      <label for="vws-B">B [kN]</label>
      <div class="hrow">
        <input type="range" id="vws-B" min="-30" max="10" step="0.5" value="0">
        <input type="number" id="vws-B-num" min="-30" max="10" step="0.5" value="0" aria-label="B in kN">
      </div>
    </div>
    <div class="ctrl">
      <label for="vws-C">C [kN]</label>
      <div class="hrow">
        <input type="range" id="vws-C" min="-15" max="5" step="0.5" value="0">
        <input type="number" id="vws-C-num" min="-15" max="5" step="0.5" value="0" aria-label="C in kN">
      </div>
    </div>
  </div>

  <div class="fig">
    <svg id="vws-svg1" viewBox="0 0 460 380" role="img"
         aria-label="Loaded bar, trial axial force and selected test function">
      <defs>
        <marker id="vws-ah" viewBox="0 0 10 10" refX="9" refY="5"
                markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="var(--load)"></path>
        </marker>
      </defs>
      <g id="vws-wall" stroke="var(--fg-muted)" stroke-width="1"></g>
      <rect x="60" y="38" width="320" height="12" fill="var(--grid)" stroke="var(--fg-muted)"></rect>
      <g id="vws-qarrows" stroke="var(--load)" stroke-width="1.5"></g>
      <text id="vws-q-lbl" class="lbl" x="70" y="18"></text>
      <line id="vws-parrow" y1="44" y2="44" stroke="var(--load)" stroke-width="2.5"
            marker-end="url(#vws-ah)"></line>
      <text id="vws-p-lbl" class="lbl" x="404" y="28" text-anchor="middle"></text>

      <text class="lbl" x="60" y="94">Trial axial force N(x) [kN]</text>
      <g id="vws-legend-exact" style="visibility:hidden">
        <line x1="320" y1="90" x2="336" y2="90" stroke="var(--ref)" stroke-width="2" stroke-dasharray="4 3"></line>
        <text x="340" y="94" style="font-size:10px">equilibrium</text>
      </g>
      <g id="vws-nticks"></g>
      <g transform="translate(60,212) scale(1,-1)">
        <g id="vws-ngrid"></g>
        <path id="vws-nref" fill="none" stroke="var(--ref)" stroke-width="2" stroke-dasharray="4 3"></path>
        <path id="vws-npath" fill="none" stroke="var(--stress)" stroke-width="2.2"></path>
      </g>

      <text class="lbl" id="vws-u-title" x="60" y="246"></text>
      <g id="vws-uticks"></g>
      <g transform="translate(60,340) scale(1,-1)">
        <g id="vws-ugrid"></g>
        <path id="vws-ufill" fill-opacity="0.15" stroke="none"></path>
        <path id="vws-upath" fill="none" stroke-width="2"></path>
      </g>
      <g id="vws-xticks"></g>
      <text x="220" y="374" text-anchor="middle">x / L</text>
    </svg>
  </div>

  <table data-quarto-disable-processing="true" id="vws-table"></table>

  <div class="verdict" id="vws-verdict"></div>
  <button type="button" id="vws-reveal">Show the equilibrium solution</button>

  <div class="fig" style="margin-top:.8em">
    <svg id="vws-svg2" viewBox="0 0 460 330" role="img"
         aria-label="Zero-residual lines of each test in the A-B plane">
      <text class="lbl" x="60" y="18">Where each test balances, in the (A, B) plane</text>
      <text x="14" y="34">B [kN]</text>
      <text id="vws-cslice" x="420" y="34" text-anchor="end"></text>
      <g id="vws-pticks"></g>
      <g transform="translate(60,290) scale(1,-1)">
        <g id="vws-pgrid"></g>
        <g id="vws-plines"></g>
        <circle id="vws-pexact" r="7" fill="none" stroke="var(--ref)" stroke-width="2" stroke-dasharray="3 2"></circle>
        <circle id="vws-pcur" r="5" fill="var(--fg)" stroke="var(--panel-bg)" stroke-width="2"></circle>
      </g>
      <text x="240" y="324" text-anchor="middle">A [kN]</text>
    </svg>
  </div>

  <div class="quiz" id="vws-quiz"></div>

  <div class="note">
    <p>The bar has length L = 1 m and is fixed at x = 0. For an admissible δu, one with δu(0) = 0,
    the principle of virtual work requires ∫ N δε dx = ∫ q δu dx + P δu(L). Your guess is linear in
    A, B and C, so each test becomes one linear equation, shown under its name. The residual
    W<sub>int</sub> − W<sub>ext</sub> equals −∫ (dN/dx + q) δu dx + [N(L) − P] δu(L). The two
    bumps vanish at both ends, so they test only the field equation dN/dx + q = 0. The other three
    tests also test the tip condition N(L) = P.</p>
    <p>With two unknowns, two independent tests fix A and B, and the rest are checks. In the plane
    below, each test is the line on which it balances. When your trial function can represent the
    equilibrium solution, all five lines meet at a single point. For a triangular load, dN/dx = −q(x)
    varies, so a linear guess cannot satisfy every test. The lines then fail to meet until the
    (x/L)² term is included and C is right. The plane is a slice at the current C. Choosing a finite
    set of test functions from the same family as the trial function is the Galerkin method, the
    starting point of the finite element method.</p>
    <p>Virtual displacements have amplitude δ = 1 mm, so works are in kN·mm = J. A test counts as
    balanced when |W<sub>int</sub> − W<sub>ext</sub>| &lt; 0.01 J. Integrals use Simpson's rule
    with 600 intervals. Parts of N(x) outside the plotted range are not drawn.</p>
  </div>

  <script>
  (function () {
    const root = (document.currentScript && document.currentScript.closest('.viz-vws')) || document.querySelector('.viz-vws');
    if (!root) return;
    const __q = (id) => root.querySelector('#' + id);
    const NS = 'http://www.w3.org/2000/svg';

    const L = 1, HW = 0.15, NINT = 600, TOL = 0.01;

    // ---- test functions: [δu (mm), dδu/dξ] at ξ = x/L ----
    const bump = (a) => (xi) => {
      const d = xi - a;
      if (Math.abs(d) >= HW) return [0, 0];
      const th = Math.PI * d / (2 * HW);
      return [Math.cos(th) ** 2, -Math.sin(2 * th) * Math.PI / (2 * HW)];
    };
    const TESTS = [
      { name: 'Linear δ·x/L',           f: (xi) => [xi, 1] },
      { name: 'Quadratic δ·(x/L)²',     f: (xi) => [xi * xi, 2 * xi] },
      { name: 'Sine δ·sin(πx/2L)',      f: (xi) => [Math.sin(Math.PI * xi / 2), Math.PI / 2 * Math.cos(Math.PI * xi / 2)] },
      { name: 'Bump at x/L = 0.3',      f: bump(0.3) },
      { name: 'Bump at x/L = 0.7',      f: bump(0.7) },
    ];
    function simpson(g) {
      const h = 1 / NINT;
      let s = g(0) + g(1);
      for (let i = 1; i < NINT; i++) s += (i % 2 ? 4 : 2) * g(i * h);
      return s * h / 3;
    }
    // with L = 1: W_int = a·A + b·B + c·C, W_ext = q·I0 (uniform) or q0·I1 (triangular) + P·uL
    TESTS.forEach((t, i) => {
      t.a = simpson((x) => t.f(x)[1]);
      t.b = simpson((x) => x * t.f(x)[1]);
      t.c = simpson((x) => x * x * t.f(x)[1]);
      t.I0 = simpson((x) => t.f(x)[0]);
      t.I1 = simpson((x) => x * t.f(x)[0]);
      t.uL = t.f(1)[0];
      t.color = 'var(--s' + (i + 1) + ')';
      t.dash = ['none', '9 4', '2 3', '9 3 2 3', '14 4 4 4'][i];
    });

    // ---- state not held in controls ----
    let q = 10, P = 5, reveal = false, sel = 0;

    const loadSel = __q('vws-load'), useC = __q('vws-usec');
    const S = {};
    ['A', 'B', 'C'].forEach((k) => { S[k] = { r: __q('vws-' + k), n: __q('vws-' + k + '-num') }; });

    // ---- plot geometry (maths coordinates inside flipped groups) ----
    const PW = 320;
    const NMIN = -20, NMAX = 50, NH = 110, SN = NH / (NMAX - NMIN);
    const UMIN = -0.1, UMAX = 1.1, UH = 86, SU = UH / (UMAX - UMIN);
    const X = (xi) => PW * xi, YN = (N) => (N - NMIN) * SN, YU = (u) => (u - UMIN) * SU;
    const AMIN = -20, AMAX = 50, BMIN = -30, BMAX = 10, PPW = 360, PPH = 250;
    const PA = (A) => (A - AMIN) * PPW / (AMAX - AMIN), PB = (B) => (B - BMIN) * PPH / (BMAX - BMIN);

    function el(tag, attrs, parent) {
      const e = document.createElementNS(NS, tag);
      for (const k in attrs) e.setAttribute(k, attrs[k]);
      if (parent) parent.appendChild(e);
      return e;
    }
    function txt(parent, x, y, s, anchor) {
      const t = el('text', { x: x, y: y, 'text-anchor': anchor || 'middle' }, parent);
      t.textContent = s;
      return t;
    }
    const sgn = (v) => (v < 0 ? '\u2212' + (-v) : String(v));

    // ---- static scaffolding ----
    (function build() {
      const wall = __q('vws-wall');
      el('line', { x1: 60, y1: 20, x2: 60, y2: 68, 'stroke-width': 2 }, wall);
      for (let y = 22; y <= 60; y += 8) el('line', { x1: 60, y1: y, x2: 52, y2: y + 8 }, wall);

      const ng = __q('vws-ngrid'), nt = __q('vws-nticks');
      for (let N = NMIN; N <= NMAX; N += 10) {
        el('line', { x1: 0, y1: YN(N), x2: PW, y2: YN(N), stroke: N === 0 ? 'var(--fg-muted)' : 'var(--grid)' }, ng);
        txt(nt, 54, 212 - YN(N) + 3.5, sgn(N), 'end');
      }
      const ug = __q('vws-ugrid'), ut = __q('vws-uticks');
      [0, 0.5, 1].forEach((u) => {
        el('line', { x1: 0, y1: YU(u), x2: PW, y2: YU(u), stroke: u === 0 ? 'var(--fg-muted)' : 'var(--grid)' }, ug);
        txt(ut, 54, 340 - YU(u) + 3.5, String(u), 'end');
      });
      const xt = __q('vws-xticks');
      [0, 0.25, 0.5, 0.75, 1].forEach((xi) => {
        el('line', { x1: X(xi), y1: 0, x2: X(xi), y2: NH, stroke: 'var(--grid)' }, ng);
        el('line', { x1: X(xi), y1: 0, x2: X(xi), y2: UH, stroke: 'var(--grid)' }, ug);
        txt(xt, 60 + X(xi), 356, String(xi));
      });
      el('rect', { x: 0, y: 0, width: PW, height: NH, fill: 'none', stroke: 'var(--border)' }, ng);
      el('rect', { x: 0, y: 0, width: PW, height: UH, fill: 'none', stroke: 'var(--border)' }, ug);

      const pg = __q('vws-pgrid'), pt = __q('vws-pticks');
      for (let A = AMIN; A <= AMAX; A += 10) {
        el('line', { x1: PA(A), y1: 0, x2: PA(A), y2: PPH, stroke: A === 0 ? 'var(--fg-muted)' : 'var(--grid)' }, pg);
        txt(pt, 60 + PA(A), 306, sgn(A));
      }
      for (let B = BMIN; B <= BMAX; B += 10) {
        el('line', { x1: 0, y1: PB(B), x2: PPW, y2: PB(B), stroke: B === 0 ? 'var(--fg-muted)' : 'var(--grid)' }, pg);
        txt(pt, 54, 290 - PB(B) + 3.5, sgn(B), 'end');
      }
      el('rect', { x: 0, y: 0, width: PPW, height: PPH, fill: 'none', stroke: 'var(--border)' }, pg);

      const qa = __q('vws-qarrows');
      for (let i = 0; i < 8; i++) el('line', { y1: 30, y2: 30, 'marker-end': 'url(#vws-ah)' }, qa);

      const pl = __q('vws-plines');
      TESTS.forEach((t) => { t.line = el('line', { stroke: t.color, 'stroke-width': 2, 'stroke-dasharray': t.dash }, pl); });

      // table
      const tb = __q('vws-table');
      TESTS.forEach((t, i) => {
        const tr = document.createElement('tr');
        const id = 'vws-sel-' + i;
        tr.innerHTML =
          '<td><input type="radio" name="vws-sel" id="' + id + '" value="' + i + '"' + (i === 0 ? ' checked' : '') + '> ' +
          '<label for="' + id + '"><svg class="swatch" viewBox="0 0 22 8" aria-hidden="true"><line x1="0" y1="4" x2="22" y2="4" stroke="' + t.color + '" stroke-width="2.5" stroke-dasharray="' + t.dash + '"></line></svg>' + t.name + '</label>' +
          '<span class="eq" id="vws-eq-' + i + '"></span></td>' +
          '<td class="num"><span id="vws-res-' + i + '"></span> J</td>';
        tb.appendChild(tr);
        tr.querySelector('input').addEventListener('change', () => { sel = i; update(); });
      });
    })();

    function fmt(v, d) {
      if (Math.abs(v) < 0.5 * Math.pow(10, -d)) v = 0;
      return (v < 0 ? '\u2212' : '\u00A0') + Math.abs(v).toFixed(d);
    }
    function snap(k, v) {
      const r = S[k].r, lo = +r.min, hi = +r.max, st = +r.step;
      if (!isFinite(v)) v = +r.value;
      v = Math.min(hi, Math.max(lo, v));
      return lo + Math.round((v - lo) / st) * st;
    }
    function term(coef, name, first) {
      if (Math.abs(coef) < 5e-4) return '';
      const s = Math.abs(coef).toFixed(3) + (name ? '\u2009' + name : '');
      if (first) return (coef < 0 ? '\u2212' : '') + s;
      return (coef < 0 ? ' \u2212 ' : ' + ') + s;
    }
    function exactABC(tri) {
      return tri ? [P + q / 2, 0, -q / 2] : [P + q, -q, 0];
    }

    function update() {
      const tri = loadSel.value === 'tri';
      const withC = useC.checked;
      S.C.r.disabled = S.C.n.disabled = !withC;
      const A = +S.A.r.value, B = +S.B.r.value, C = withC ? +S.C.r.value : 0;
      ['A', 'B', 'C'].forEach((k) => { S[k].n.value = (+S[k].r.value).toFixed(1); });

      // schematic
      const qa = __q('vws-qarrows').children;
      for (let i = 0; i < qa.length; i++) {
        const x0 = 72 + i * 38, xi = (x0 + 9 - 60) / 320;
        const len = 18 * (tri ? xi : 1);
        qa[i].setAttribute('x1', x0); qa[i].setAttribute('x2', x0 + len);
        qa[i].style.visibility = q > 0 && len >= 3 ? 'visible' : 'hidden';
      }
      __q('vws-q-lbl').textContent = tri ? 'q(x) = ' + q + '·x/L kN/m' : 'q = ' + q + ' kN/m';
      const pa = __q('vws-parrow'), len = 12 + 28 * Math.abs(P) / 20;
      pa.style.visibility = P !== 0 ? 'visible' : 'hidden';
      if (P > 0) { pa.setAttribute('x1', 382); pa.setAttribute('x2', 382 + len); }
      else       { pa.setAttribute('x1', 382 + len); pa.setAttribute('x2', 382); }
      __q('vws-p-lbl').textContent = 'P = ' + sgn(P) + ' kN';

      // N plot, pen lifted outside the window
      const Nt = (xi) => A + B * xi + C * xi * xi;
      const [Ae, Be, Ce] = exactABC(tri);
      const Ne = (xi) => Ae + Be * xi + Ce * xi * xi;
      function curve(fn) {
        let d = '', pen = false;
        for (let i = 0; i <= 200; i++) {
          const xi = i / 200, v = fn(xi);
          if (v < NMIN || v > NMAX) { pen = false; continue; }
          d += (pen ? 'L' : 'M') + X(xi).toFixed(2) + ',' + YN(v).toFixed(2);
          pen = true;
        }
        return d;
      }
      __q('vws-npath').setAttribute('d', curve(Nt));
      __q('vws-nref').setAttribute('d', reveal ? curve(Ne) : '');
      __q('vws-legend-exact').style.visibility = reveal ? 'visible' : 'hidden';

      // selected test function
      const T = TESTS[sel];
      let ud = '';
      for (let i = 0; i <= 200; i++) {
        const xi = i / 200;
        ud += (i ? 'L' : 'M') + X(xi).toFixed(2) + ',' + YU(T.f(xi)[0]).toFixed(2);
      }
      const up = __q('vws-upath'), uf = __q('vws-ufill');
      up.setAttribute('d', ud); up.setAttribute('stroke', T.color); up.setAttribute('stroke-dasharray', T.dash);
      uf.setAttribute('d', ud + 'L' + X(1) + ',' + YU(0) + 'L' + X(0) + ',' + YU(0) + 'Z');
      uf.setAttribute('fill', T.color);
      __q('vws-u-title').textContent = 'Test function δu(x): ' + T.name + ' [mm]';

      // residuals, equations, lines
      let pass = 0, bumpsPass = true;
      TESTS.forEach((t, i) => {
        const f = q * (tri ? t.I1 : t.I0) + P * t.uL;
        const res = t.a * A + t.b * B + t.c * C - f;
        const ok = Math.abs(res) < TOL;
        if (ok) pass++;
        if (i >= 3 && !ok) bumpsPass = false;
        const r = __q('vws-res-' + i);
        r.textContent = (ok ? '\u2713 ' : '\u2717 ') + fmt(res, 3);
        r.className = ok ? 'pass' : 'fail';
        let lhs = term(t.a, 'A', true);
        lhs += term(t.b, 'B', !lhs);
        if (withC) lhs += term(t.c, 'C', !lhs);
        __q('vws-eq-' + i).textContent = (lhs || '0') + ' = ' + fmt(f, 3).trim();

        // line a·A + b·B = f − c·C, clipped to the plane
        const g = f - t.c * C, pts = [];
        if (Math.abs(t.b) > 1e-9) [AMIN, AMAX].forEach((Av) => {
          const Bv = (g - t.a * Av) / t.b;
          if (Bv >= BMIN - 1e-9 && Bv <= BMAX + 1e-9) pts.push([Av, Bv]);
        });
        if (Math.abs(t.a) > 1e-9) [BMIN, BMAX].forEach((Bv) => {
          const Av = (g - t.b * Bv) / t.a;
          if (Av >= AMIN - 1e-9 && Av <= AMAX + 1e-9) pts.push([Av, Bv]);
        });
        if (pts.length >= 2) {
          let best = [pts[0], pts[1]], dmax = -1;
          for (let m = 0; m < pts.length; m++) for (let n = m + 1; n < pts.length; n++) {
            const dd = (pts[m][0] - pts[n][0]) ** 2 + (pts[m][1] - pts[n][1]) ** 2;
            if (dd > dmax) { dmax = dd; best = [pts[m], pts[n]]; }
          }
          t.line.setAttribute('x1', PA(best[0][0])); t.line.setAttribute('y1', PB(best[0][1]));
          t.line.setAttribute('x2', PA(best[1][0])); t.line.setAttribute('y2', PB(best[1][1]));
          t.line.style.visibility = 'visible';
        } else {
          t.line.style.visibility = 'hidden';
        }
        t.line.setAttribute('stroke-width', i === sel ? 3.5 : 1.8);
      });

      const cur = __q('vws-pcur');
      cur.setAttribute('cx', PA(A)); cur.setAttribute('cy', PB(B));
      const pe = __q('vws-pexact');
      pe.setAttribute('cx', PA(Ae)); pe.setAttribute('cy', PB(Be));
      pe.style.visibility = reveal ? 'visible' : 'hidden';
      __q('vws-cslice').textContent = withC ? 'slice at C = ' + fmt(C, 1).trim() + ' kN' : 'C = 0';

      // verdict
      const v = __q('vws-verdict');
      if (pass === TESTS.length) {
        v.className = 'verdict ok';
        v.textContent = 'All five tests balance. N(x) = ' + fmt(A, 1).trim() +
          (B ? (B < 0 ? ' \u2212 ' : ' + ') + Math.abs(B).toFixed(1) + '·x/L' : '') +
          (C ? (C < 0 ? ' \u2212 ' : ' + ') + Math.abs(C).toFixed(1) + '·(x/L)²' : '') +
          ' kN is in equilibrium with the loads.';
      } else {
        v.className = 'verdict bad';
        let hint;
        if (tri && !withC) hint = 'A linear N has a constant slope, but dN/dx = −q(x) varies along the bar. Include the (x/L)² term.';
        else if (bumpsPass) hint = 'Both bumps balance, so dN/dx + q = 0 is satisfied. The remaining tests also involve the tip, where N(L) must equal P.';
        else hint = 'Start with the bumps. They vanish at both ends, so they test only dN/dx + q = 0.';
        v.textContent = pass + ' of 5 tests balance. ' + hint;
      }
      __q('vws-reveal').textContent = reveal ? 'Hide the equilibrium solution' : 'Show the equilibrium solution';
    }

    // ---- events ----
    ['A', 'B', 'C'].forEach((k) => {
      S[k].r.addEventListener('input', update);
      S[k].n.addEventListener('change', () => { S[k].r.value = snap(k, parseFloat(S[k].n.value)); update(); });
    });
    useC.addEventListener('change', update);
    loadSel.addEventListener('change', () => { reveal = false; update(); });
    __q('vws-new').addEventListener('click', () => {
      q = 4 + Math.floor(Math.random() * 17);     // 4..20
      P = -10 + Math.floor(Math.random() * 31);   // -10..20
      reveal = false;
      update();
    });
    __q('vws-reset').addEventListener('click', () => {
      ['A', 'B', 'C'].forEach((k) => { S[k].r.value = 0; });
      update();
    });
    __q('vws-reveal').addEventListener('click', () => { reveal = !reveal; update(); });

    // ---- predict-first quiz ----
    const QUIZ = [
      { q: 'A bump test vanishes at both ends of the bar. Which condition can it check?',
        options: ['The field equation dN/dx + q = 0', 'The tip condition N(L) = P', 'Both', 'Neither'],
        answer: 0,
        explain: 'Its residual is −∫(dN/dx + q)δu dx; the boundary term [N(L) − P]δu(L) drops out because δu(L) = 0.',
        check: 'with the (x/L)² term off, the bump equations under the test names contain only B, never A.' },
      { q: 'You guess the constant field N = P + qL/2 (B = 0). Does the linear test δu = δ·x/L balance?',
        options: ['Yes', 'No', 'Only if P = 0'],
        answer: 0,
        explain: 'The linear test only sees the total load: W_int = N(L)·δ and W_ext = (qL/2 + P)·δ. The quadratic, sine and bump tests expose the guess.',
        check: 'with q = 10 and P = 5, set A = 10 and B = 0 and read the five residuals.' },
      { q: 'With the (x/L)² term off, how many tests do you need to pin down A and B?',
        options: ['One', 'Two independent ones', 'All five'],
        answer: 1,
        explain: 'Two unknowns need two independent equations; the others are checks. The two bumps are not independent of each other: both only fix B.',
        check: 'in the (A, B) plane, any two non-parallel lines meet at the solution; the two bump lines are parallel.' },
      { q: 'Triangular load, (x/L)² term off. Can you make all five tests balance?',
        options: ['Yes, with the right A and B', 'No, a linear N cannot satisfy dN/dx = −q(x)'],
        answer: 1,
        explain: 'The two bumps ask for different slopes, B = −0.3q₀ and B = −0.7q₀: their lines are parallel and never meet. Adding the (x/L)² term fixes it.',
        check: 'choose the triangular load and look at the two horizontal bump lines in the (A, B) plane.' },
    ];
    function makeQuiz(box, Q) {
      const chosen = Q.map(() => -1);
      let k = 0;
      function render() {
        const it = Q[k], c = chosen[k];
        let html = '<div class="qhead">Predict first: question ' + (k + 1) + ' of ' + Q.length + '</div>' +
          '<p class="qtext">' + it.q + '</p><div class="qopts">';
        it.options.forEach((o, i) => {
          let cls = '', mark = '';
          if (c >= 0 && i === it.answer) { cls = ' correct'; mark = '\u2713 '; }
          else if (c >= 0 && i === c) { cls = ' wrong'; mark = '\u2717 '; }
          html += '<button type="button" class="qopt' + cls + '" data-i="' + i + '"' + (c >= 0 ? ' disabled' : '') + '>' + mark + o + '</button>';
        });
        html += '</div>';
        if (c >= 0) {
          html += '<p class="qfeedback ' + (c === it.answer ? 'ok' : 'bad') + '">' + (c === it.answer ? 'Right. ' : 'Not quite. ') + it.explain + '</p>' +
                  '<p class="qtry">Check it: ' + it.check + '</p>';
        }
        html += '<div class="qnav"><button type="button" data-nav="-1"' + (k === 0 ? ' disabled' : '') + '>Previous</button>' +
                '<button type="button" data-nav="1"' + (k === Q.length - 1 ? ' disabled' : '') + '>Next question</button></div>';
        box.innerHTML = html;
        box.querySelectorAll('.qopt').forEach((b) => b.addEventListener('click', () => { chosen[k] = +b.dataset.i; render(); }));
        box.querySelectorAll('[data-nav]').forEach((b) => b.addEventListener('click', () => { k += +b.dataset.nav; render(); }));
      }
      render();
    }
    makeQuiz(__q('vws-quiz'), QUIZ);

    update();
  })();
  </script>
</div>
```
