```{=html}
<style>
.viz-fe,
[data-bs-theme="light"] .viz-fe,
body.quarto-light .viz-fe {
  --fg: #1f2328; --fg-muted: #5b636d; --panel-bg: #f6f7f9; --border: #d4d8de;
  --grid: #e3e6ea; --slider: #3b6ea8;
  --load: #00805e; --disp: #0072B2; --stress: #D55E00; --ref: #6b7684;
  --virtual: #CC79A7; --ok: #00805e; --bad: #b8321a;
}
@media (prefers-color-scheme: dark) {
  .viz-fe {
    --fg: #e6e8eb; --fg-muted: #a0a8b3; --panel-bg: #1e2227; --border: #3a414a;
    --grid: #2c323a; --slider: #7fb0e6;
    --load: #3cc9a0; --disp: #56B4E9; --stress: #FF8C42; --ref: #9aa4b0;
    --virtual: #E3A5C7; --ok: #3cc9a0; --bad: #ff7b6b;
  }
}
[data-bs-theme="dark"] .viz-fe,
body.quarto-dark .viz-fe {
  --fg: #e6e8eb; --fg-muted: #a0a8b3; --panel-bg: #1e2227; --border: #3a414a;
  --grid: #2c323a; --slider: #7fb0e6;
  --load: #3cc9a0; --disp: #56B4E9; --stress: #FF8C42; --ref: #9aa4b0;
  --virtual: #E3A5C7; --ok: #3cc9a0; --bad: #ff7b6b;
}

.viz-fe { color: var(--fg); font-family: inherit; }
.viz-fe *, .viz-fe *::before, .viz-fe *::after { box-sizing: border-box; }
.viz-fe .intro { color: var(--fg-muted); font-size: .95em; margin: 0 0 .8em; }
.viz-fe .controls {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .6em 1.2em;
  padding: .8em; background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 6px; margin-bottom: .8em;
}
.viz-fe .ctrl label { display: block; font-size: .88em; color: var(--fg-muted); margin-bottom: .2em; }
.viz-fe .ctrl .val { color: var(--fg); font-variant-numeric: tabular-nums; }
.viz-fe .hrow { display: flex; gap: .5em; align-items: center; flex-wrap: wrap; }
.viz-fe input[type="range"] { flex: 1; min-width: 6em; accent-color: var(--slider); }
.viz-fe input[type="number"] {
  width: 6em; font: inherit; font-size: .9em; font-variant-numeric: tabular-nums;
  color: var(--fg); background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 4px; padding: .15em .3em;
}
.viz-fe select {
  flex: 1; min-width: 0; font: inherit; font-size: .9em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 4px; padding: .2em .3em;
}
.viz-fe button {
  font: inherit; font-size: .85em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 4px; padding: .25em .6em; cursor: pointer;
}
.viz-fe button:hover, .viz-fe button:focus-visible { border-color: var(--slider); }
.viz-fe .ucontrols { grid-column: 1 / -1; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .5em 1.2em; }
.viz-fe .fig {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 6px;
  padding: .5em; margin-bottom: .8em;
}
.viz-fe svg { display: block; width: 100%; height: auto; max-width: 460px; margin: 0 auto; }
.viz-fe svg text { fill: var(--fg-muted); font-size: 11px; font-family: inherit; }
.viz-fe svg text.lbl { fill: var(--fg); }
.viz-fe table { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; font-size: .92em; }
.viz-fe td { padding: .3em .4em; border-bottom: 1px solid var(--grid); vertical-align: top; }
.viz-fe td.num { text-align: right; white-space: nowrap; }
.viz-fe td .eq { display: block; font-size: .88em; color: var(--fg-muted); }
.viz-fe td label { cursor: pointer; }
.viz-fe tr.sep td { border-top: 2px solid var(--border); }
.viz-fe .pass { color: var(--ok); }
.viz-fe .fail { color: var(--bad); }
.viz-fe .neutral { color: var(--fg-muted); }
.viz-fe .verdict { margin: .7em 0 .8em; font-weight: 600; }
.viz-fe .verdict.ok { color: var(--ok); }
.viz-fe .verdict.bad { color: var(--bad); }
.viz-fe .note { font-size: .88em; color: var(--fg-muted); margin-top: .9em; }
.viz-fe .note p { margin: 0 0 .5em; }
.viz-fe .quiz { padding: .8em; background: var(--panel-bg); border: 1px solid var(--border); border-radius: 6px; margin: .8em 0; }
.viz-fe .quiz .qhead { font-size: .85em; color: var(--fg-muted); }
.viz-fe .quiz .qtext { margin: .3em 0 .6em; font-weight: 600; }
.viz-fe .quiz .qopts { display: flex; flex-direction: column; gap: .35em; }
.viz-fe .quiz .qopt { text-align: left; }
.viz-fe .quiz .qopt:disabled { cursor: default; }
.viz-fe .quiz .qopt.correct { border-color: var(--ok); color: var(--ok); }
.viz-fe .quiz .qopt.wrong { border-color: var(--bad); color: var(--bad); }
.viz-fe .quiz .qfeedback, .viz-fe .quiz .qtry { margin: .6em 0 0; font-size: .92em; }
.viz-fe .quiz .qfeedback.ok { color: var(--ok); }
.viz-fe .quiz .qfeedback.bad { color: var(--bad); }
.viz-fe .quiz .qtry { color: var(--fg-muted); }
.viz-fe .quiz .qnav { display: flex; justify-content: space-between; margin-top: .7em; }
@media (max-width: 560px) {
  .viz-fe .controls, .viz-fe .ucontrols { grid-template-columns: 1fr; }
}
</style>

<div class="viz-fe">
  <p class="intro">Same bar, now solved for the displacement with finite elements. The trial
  u(x) is piecewise linear, the sum of u<sub>i</sub>·φ<sub>i</sub>(x) over hat functions
  φ<sub>i</sub>. Galerkin's method uses those same hats as test functions: each φ<sub>j</sub> gives
  one equation. Find the nodal values u<sub>i</sub> that make every hat test balance.</p>

  <div class="controls">
    <div class="ctrl">
      <label for="fe-n">Number of elements n = <span class="val" id="fe-n-val"></span></label>
      <input type="range" id="fe-n" min="1" max="6" step="1" value="3" style="width:100%">
    </div>
    <div class="ctrl">
      <label for="fe-load">Load case</label>
      <div class="hrow">
        <select id="fe-load">
          <option value="uniform">Uniform q</option>
          <option value="tri">Triangular q(x) = q₀·x/L</option>
        </select>
        <button type="button" id="fe-new">New loads</button>
      </div>
    </div>
    <div class="ctrl" style="grid-column: 1 / -1">
      <div class="hrow">
        <button type="button" id="fe-reset">Reset u to zero</button>
        <button type="button" id="fe-solve">Fill in the Galerkin solution</button>
        <button type="button" id="fe-reveal"></button>
      </div>
    </div>
    <div class="ucontrols" id="fe-ucontrols"></div>
  </div>

  <div class="fig">
    <svg viewBox="0 0 460 360" role="img" aria-label="Bar with nodes, FE displacement and axial force">
      <defs>
        <marker id="fe-ah" viewBox="0 0 10 10" refX="9" refY="5"
                markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="var(--load)"></path>
        </marker>
      </defs>
      <g id="fe-wall" stroke="var(--fg-muted)" stroke-width="1"></g>
      <rect x="60" y="38" width="320" height="12" fill="var(--grid)" stroke="var(--fg-muted)"></rect>
      <g id="fe-qarrows" stroke="var(--load)" stroke-width="1.5"></g>
      <g id="fe-nodes"></g>
      <text id="fe-q-lbl" class="lbl" x="70" y="18"></text>
      <line id="fe-parrow" y1="44" y2="44" stroke="var(--load)" stroke-width="2.5" marker-end="url(#fe-ah)"></line>
      <text id="fe-p-lbl" class="lbl" x="404" y="28" text-anchor="middle"></text>

      <text class="lbl" x="60" y="94">Displacement u(x) [mm]</text>
      <g class="fe-legend-exact">
        <line x1="320" y1="90" x2="336" y2="90" stroke="var(--ref)" stroke-width="2" stroke-dasharray="4 3"></line>
        <text x="340" y="94" style="font-size:10px">exact</text>
      </g>
      <g id="fe-uticks"></g>
      <g transform="translate(60,200) scale(1,-1)">
        <g id="fe-ugrid"></g>
        <path id="fe-uref" fill="none" stroke="var(--ref)" stroke-width="2" stroke-dasharray="4 3"></path>
        <path id="fe-upath" fill="none" stroke="var(--disp)" stroke-width="2.2"></path>
        <g id="fe-udots"></g>
      </g>

      <text class="lbl" x="60" y="228">Axial force N = EA·du/dx [kN]</text>
      <g class="fe-legend-exact">
        <line x1="320" y1="224" x2="336" y2="224" stroke="var(--ref)" stroke-width="2" stroke-dasharray="4 3"></line>
        <text x="340" y="228" style="font-size:10px">exact</text>
      </g>
      <g id="fe-nticks"></g>
      <g transform="translate(60,320) scale(1,-1)">
        <g id="fe-ngrid"></g>
        <path id="fe-nref" fill="none" stroke="var(--ref)" stroke-width="2" stroke-dasharray="4 3"></path>
        <path id="fe-npath" fill="none" stroke="var(--stress)" stroke-width="2.4"></path>
      </g>
      <g id="fe-xticks"></g>
      <text x="220" y="352" text-anchor="middle">x / L</text>
    </svg>
  </div>

  <table data-quarto-disable-processing="true" id="fe-table"></table>
  <div class="verdict" id="fe-verdict"></div>

  <div class="fig">
    <svg viewBox="0 0 460 150" role="img" aria-label="Selected test function">
      <text class="lbl" id="fe-t-title" x="60" y="16"></text>
      <g id="fe-tticks"></g>
      <g transform="translate(60,120) scale(1,-1)">
        <g id="fe-tgrid"></g>
        <path id="fe-tfill" fill="var(--virtual)" fill-opacity="0.15" stroke="none"></path>
        <path id="fe-tpath" fill="none" stroke="var(--virtual)" stroke-width="2"></path>
      </g>
      <g id="fe-txticks"></g>
    </svg>
  </div>

  <table data-quarto-disable-processing="true">
    <tr><td>L2 error of u, your nodal values (RMS over the bar)</td><td class="num"><span id="fe-eu"></span> mm</td><td class="num"><span id="fe-eu-rel"></span> %</td></tr>
    <tr><td>L2 error of N, your nodal values (RMS over the bar)</td><td class="num"><span id="fe-eN"></span> kN</td><td class="num"><span id="fe-eN-rel"></span> %</td></tr>
  </table>

  <div class="fig" style="margin-top:.8em">
    <label class="check" for="fe-quad" style="display:flex;gap:.4em;align-items:center;font-size:.88em;color:var(--fg-muted);margin:0 0 .4em .2em">
      <input type="checkbox" id="fe-quad" style="accent-color:var(--slider)">
      Also show quadratic elements (bonus, not covered in this course)
    </label>
    <svg viewBox="0 0 460 272" role="img" aria-label="L2 error against number of elements, log-log">
      <text class="lbl" x="60" y="16">L2 error of the Galerkin solution vs n (log–log)</text>
      <line x1="60" y1="30" x2="76" y2="30" stroke="var(--disp)" stroke-width="2"></line>
      <text id="fe-leg-u" x="80" y="34" style="font-size:10px"></text>
      <line x1="230" y1="30" x2="246" y2="30" stroke="var(--stress)" stroke-width="2"></line>
      <text id="fe-leg-N" x="250" y="34" style="font-size:10px"></text>
      <g id="fe-leg-q">
        <line id="fe-leg-qu-line" x1="60" y1="44" x2="76" y2="44" stroke="var(--disp)" stroke-width="2" stroke-dasharray="7 4"></line>
        <text id="fe-leg-qu" x="80" y="48" style="font-size:10px"></text>
        <line id="fe-leg-qN-line" x1="230" y1="44" x2="246" y2="44" stroke="var(--stress)" stroke-width="2" stroke-dasharray="7 4"></line>
        <text id="fe-leg-qN" x="250" y="48" style="font-size:10px"></text>
      </g>
      <g id="fe-cticks"></g>
      <g transform="translate(60,232) scale(1,-1)">
        <g id="fe-cgrid"></g>
        <path id="fe-cu" fill="none" stroke="var(--disp)" stroke-width="2"></path>
        <path id="fe-cN" fill="none" stroke="var(--stress)" stroke-width="2"></path>
        <path id="fe-cqu" fill="none" stroke="var(--disp)" stroke-width="2" stroke-dasharray="7 4"></path>
        <path id="fe-cqN" fill="none" stroke="var(--stress)" stroke-width="2" stroke-dasharray="7 4"></path>
        <g id="fe-cmarks"></g>
      </g>
      <text x="230" y="266" text-anchor="middle">number of elements n (log scale)</text>
    </svg>
  </div>

  <div class="quiz" id="fe-quiz"></div>

  <div class="note">
    <p>The bar has L = 1 m and EA = 1000 kN, so N [kN] equals du/dx [mm/m]. Node 0 is fixed
    (u<sub>0</sub> = 0), so φ<sub>0</sub> is not an admissible test function. Testing with
    φ<sub>j</sub> gives the Galerkin equation Σ<sub>i</sub> K<sub>ji</sub> u<sub>i</sub> = f<sub>j</sub>,
    with K<sub>ji</sub> = ∫ EA φ<sub>i</sub>′ φ<sub>j</sub>′ dx and f<sub>j</sub> = ∫ q φ<sub>j</sub> dx + P φ<sub>j</sub>(L).
    The equations are listed with coefficients in kN/mm and right-hand sides in kN; their rows form
    the global system K u = f. The residual of a test is W<sub>int</sub> − W<sub>ext</sub> for a
    virtual displacement of amplitude 1 mm, in J.</p>
    <p>Each hat test is the equilibrium of one node. In element forces N<sub>e</sub> = EA(u<sub>e</sub> − u<sub>e−1</sub>)/h,
    the equation reads N<sub>j</sub> − N<sub>j+1</sub> = f<sub>j</sub>, with the load share f<sub>j</sub>
    collected by that node. The last hat gives N<sub>n</sub> = f<sub>n</sub> directly, so you can work
    back to the wall and then integrate the displacements outward.</p>
    <p>Every combination Σ c<sub>j</sub> φ<sub>j</sub> is also in the space. Its residual is
    Σ c<sub>j</sub> × (residual of φ<sub>j</sub>), so once all hats balance, every test in the space
    balances; press "New coefficients" to try another. The sine is not in the space, so the
    Galerkin solution does not in general balance it. For a 1D bar with constant EA and consistently
    integrated loads, the nodal displacements are exact for any n. N, however, is only piecewise
    constant, equal to the exact N averaged over each element.</p>
    <p>Errors are L2 norms divided by √L, i.e. root-mean-square differences over the bar, computed
    with 5-point Gauss quadrature per element (exact for these polynomials); percentages are relative
    to the RMS of the exact field. The log–log plot runs the Galerkin solution from n = 1 to 64; the
    filled markers sit at the current n, the hollow squares show your own nodal values. The slopes
    in the legend are measured between n = 32 and 64: about 2 for u and 1 for N, i.e. halving h
    divides the u error by 4 and the N error by 2. For this problem Galerkin gives the smallest
    possible N error of any nodal values (it is the best approximation in the energy norm) — try
    beating it. The u error is not minimised the same way: the Galerkin u equals the nodal
    interpolant here, and other nodal values can give a slightly smaller L2 error in u.</p>
    <p><em>Bonus, not covered in this course:</em> quadratic elements add a midside node to each
    element, so u is piecewise quadratic and N piecewise linear. Their dashed curves are computed
    by the same Galerkin procedure (3×3 element stiffness, loads integrated by Gauss quadrature)
    and converge one order faster: slope about 3 for u and 2 for N. Under a uniform load the exact
    u is itself quadratic, so it lies in the quadratic space and the error is zero for every n —
    there is then nothing to plot. The hand-solving part above uses linear elements only.</p>
    <p>Hat tests count as balanced below 0.015 J, which covers typing nodal values to three
    decimals. The combination's threshold scales with Σ|c<sub>j</sub>|. Parts of N outside the
    plotted range are not drawn.</p>
  </div>

  <script>
  (function () {
    const root = (document.currentScript && document.currentScript.closest('.viz-fe')) || document.querySelector('.viz-fe');
    if (!root) return;
    const __q = (id) => root.querySelector('#' + id);
    const NS = 'http://www.w3.org/2000/svg';
    const TOL = 0.015, UMINV = -15, UMAXV = 35, USTEP = 0.001;
    const SUB = '₀₁₂₃₄₅₆₇₈₉';
    const sub = (i) => String(i).split('').map((d) => SUB[+d]).join('');

    // plot windows (maths coordinates inside flipped groups)
    const PW = 320, X = (xi) => PW * xi;
    const UMIN = -15, UMAX = 35, UH = 100, YU = (u) => (u - UMIN) * UH / (UMAX - UMIN);
    const NMIN = -20, NMAX = 50, NH = 86, YN = (N) => (N - NMIN) * NH / (NMAX - NMIN);
    const TMIN = -1.1, TMAX = 1.1, TH = 90, YT = (v) => (v - TMIN) * TH / (TMAX - TMIN);

    let n = 3, q = 10, P = 5, reveal = false, sel = 0, coef = [];
    const nIn = __q('fe-n'), loadSel = __q('fe-load');

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
    function fmt(v, d) {
      if (Math.abs(v) < 0.5 * Math.pow(10, -d)) v = 0;
      return (v < 0 ? '\u2212' : '\u00A0') + Math.abs(v).toFixed(d);
    }
    const clear = (g) => { while (g.firstChild) g.removeChild(g.firstChild); };

    // ---- static scaffolding ----
    (function build() {
      const wall = __q('fe-wall');
      el('line', { x1: 60, y1: 20, x2: 60, y2: 68, 'stroke-width': 2 }, wall);
      for (let y = 22; y <= 60; y += 8) el('line', { x1: 60, y1: y, x2: 52, y2: y + 8 }, wall);
      const qa = __q('fe-qarrows');
      for (let i = 0; i < 8; i++) el('line', { y1: 30, y2: 30, 'marker-end': 'url(#fe-ah)' }, qa);

      const ut = __q('fe-uticks');
      for (let u = UMIN + 5; u <= UMAX; u += 10) txt(ut, 54, 200 - YU(u) + 3.5, sgn(u), 'end');
      const nt = __q('fe-nticks');
      for (let N = NMIN; N <= NMAX; N += 10) if (N % 20 === 0) txt(nt, 54, 320 - YN(N) + 3.5, sgn(N), 'end');
      const tt = __q('fe-tticks');
      [-1, 0, 1].forEach((v) => txt(tt, 54, 120 - YT(v) + 3.5, sgn(v), 'end'));
      const xt = __q('fe-xticks'), txt2 = __q('fe-txticks');
      [0, 0.25, 0.5, 0.75, 1].forEach((xi) => {
        txt(xt, 60 + X(xi), 336, String(xi));
        txt(txt2, 60 + X(xi), 136, String(xi));
      });
    })();

    // ---- physics ----
    const tri = () => loadSel.value === 'tri';
    const qOf = (xi) => (tri() ? q * xi : q);
    function exactU(xi) { return tri() ? (P + q / 2) * xi - q * xi ** 3 / 6 : (P + q) * xi - q * xi * xi / 2; }
    function exactN(xi) { return tri() ? P + q * (1 - xi * xi) / 2 : P + q * (1 - xi); }
    function loads(nn) {          // consistent nodal loads f_1..f_nn (index 0 unused: reaction)
      const h = 1 / nn, f = new Array(nn + 1).fill(0);
      for (let e = 1; e <= nn; e++) {
        const qa = qOf((e - 1) * h), qb = qOf(e * h);
        f[e - 1] += h * (2 * qa + qb) / 6;
        f[e] += h * (qa + 2 * qb) / 6;
      }
      f[nn] += P;
      return f;
    }
    function galerkin(nn, f) {    // nodal equilibrium from the tip, then integrate outward
      const Ne = new Array(nn + 2).fill(0), u = new Array(nn + 1).fill(0);
      for (let e = nn; e >= 1; e--) Ne[e] = Ne[e + 1] + f[e];
      for (let i = 1; i <= nn; i++) u[i] = u[i - 1] + Ne[i] / nn;
      return u;
    }
    // RMS (L2 norm / √L) errors of u_h and N_h = EA u_h' against the exact solution.
    // 5-point Gauss per element: exact for the polynomial integrands here (degree ≤ 6).
    const GX = [0, -0.5384693101056831, 0.5384693101056831, -0.9061798459386640, 0.9061798459386640];
    const GW = [0.5688888888888889, 0.4786286704993665, 0.4786286704993665, 0.2369268850561891, 0.2369268850561891];
    function errNorms(u, nn) {
      const h = 1 / nn;
      let su = 0, sN = 0, nu = 0, nN = 0;
      for (let e = 1; e <= nn; e++) {
        const Nh = (u[e] - u[e - 1]) / h;
        for (let g = 0; g < 5; g++) {
          const s = (1 + GX[g]) / 2, xi = (e - 1 + s) * h, wg = GW[g] * h / 2;
          const uh = u[e - 1] + (u[e] - u[e - 1]) * s, ue = exactU(xi), Nex = exactN(xi);
          su += wg * (uh - ue) ** 2; sN += wg * (Nh - Nex) ** 2;
          nu += wg * ue * ue; nN += wg * Nex * Nex;
        }
      }
      return { eu: Math.sqrt(su), eN: Math.sqrt(sN), nu: Math.sqrt(nu), nN: Math.sqrt(nN) };
    }

    // ---- quadratic elements (convergence plot only). Nodes 0..2m, element e uses 2e-2, 2e-1, 2e ----
    const Q = [(s) => 2 * (s - 0.5) * (s - 1), (s) => 4 * s * (1 - s), (s) => 2 * s * (s - 0.5)];
    const DQ = [(s) => 4 * s - 3, (s) => 4 - 8 * s, (s) => 4 * s - 1];   // d/ds
    function galerkinQuad(m) {
      const h = 1 / m, N = 2 * m;                  // unknowns: nodes 1..2m
      const K = [], f = new Array(N + 1).fill(0);
      for (let i = 0; i <= N; i++) K.push(new Float64Array(N + 1));
      const ke = [[7, -8, 1], [-8, 16, -8], [1, -8, 7]];
      for (let e = 1; e <= m; e++) {
        const dofs = [2 * e - 2, 2 * e - 1, 2 * e];
        for (let a = 0; a < 3; a++) {
          for (let b = 0; b < 3; b++) K[dofs[a]][dofs[b]] += ke[a][b] / (3 * h);
          for (let g = 0; g < 5; g++) {
            const s = (1 + GX[g]) / 2;
            f[dofs[a]] += GW[g] * h / 2 * qOf((e - 1 + s) * h) * Q[a](s);
          }
        }
      }
      f[N] += P;
      // drop dof 0 (u0 = 0) and solve the SPD system by Gaussian elimination
      const A = [], bvec = [];
      for (let i = 1; i <= N; i++) { A.push(Array.from(K[i].slice(1))); bvec.push(f[i]); }
      for (let k = 0; k < N; k++) {
        for (let i = k + 1; i < Math.min(N, k + 3); i++) {   // bandwidth 2
          const r = A[i][k] / A[k][k];
          if (!r) continue;
          for (let j = k; j < Math.min(N, k + 3); j++) A[i][j] -= r * A[k][j];
          bvec[i] -= r * bvec[k];
        }
      }
      const u = new Array(N + 1).fill(0);
      for (let k = N - 1; k >= 0; k--) {
        let sum = bvec[k];
        for (let j = k + 1; j < Math.min(N, k + 3); j++) sum -= A[k][j] * u[j + 1];
        u[k + 1] = sum / A[k][k];
      }
      return u;
    }
    function errNormsQuad(u, m) {
      const h = 1 / m;
      let su = 0, sN = 0;
      for (let e = 1; e <= m; e++) {
        const ua = [u[2 * e - 2], u[2 * e - 1], u[2 * e]];
        for (let g = 0; g < 5; g++) {
          const s = (1 + GX[g]) / 2, xi = (e - 1 + s) * h, wg = GW[g] * h / 2;
          let uh = 0, Nh = 0;
          for (let a = 0; a < 3; a++) { uh += ua[a] * Q[a](s); Nh += ua[a] * DQ[a](s) / h; }
          su += wg * (uh - exactU(xi)) ** 2; sN += wg * (Nh - exactN(xi)) ** 2;
        }
      }
      return { eu: Math.sqrt(su), eN: Math.sqrt(sN) };
    }

    // Galerkin convergence curves depend only on the load case: cache them
    const NC = 64;
    let convKey = '', conv = null;
    function convergence() {
      const key = loadSel.value + '|' + q + '|' + P;
      if (key === convKey) return conv;
      const c = { eu1: [], eN1: [], eu2: [], eN2: [] };
      let ref = null;
      for (let m = 1; m <= NC; m++) {
        const E1 = errNorms(galerkin(m, loads(m)), m);
        if (!ref) ref = E1;
        c.eu1.push(E1.eu); c.eN1.push(E1.eN);
        const E2 = errNormsQuad(galerkinQuad(m), m);
        // round-off floor: errors below 1e-9 of the field's RMS are treated as exactly zero
        c.eu2.push(E2.eu > 1e-9 * ref.nu ? E2.eu : 0);
        c.eN2.push(E2.eN > 1e-9 * ref.nN ? E2.eN : 0);
      }
      convKey = key; conv = c;
      return c;
    }
    function newCoefs() {
      coef = [0];
      for (let j = 1; j <= n; j++) coef.push(Math.round((Math.random() * 2 - 1) * 10) / 10 || 0.5);
    }

    // ---- per-n structure (controls, table rows) ----
    function rebuild() {
      n = +nIn.value;
      sel = 0;
      newCoefs();
      const uc = __q('fe-ucontrols');
      uc.innerHTML = '';
      for (let i = 1; i <= n; i++) {
        const d = document.createElement('div');
        d.className = 'ctrl';
        d.innerHTML =
          '<label for="fe-u-' + i + '">u' + sub(i) + ' at x/L = ' + (i / n).toFixed(3).replace(/0+$/, '').replace(/\.$/, '') + ' [mm]</label>' +
          '<div class="hrow"><input type="range" id="fe-u-' + i + '" min="' + UMINV + '" max="' + UMAXV + '" step="' + USTEP + '" value="0">' +
          '<input type="number" id="fe-un-' + i + '" min="' + UMINV + '" max="' + UMAXV + '" step="' + USTEP + '" value="0" aria-label="u' + i + ' in mm"></div>';
        uc.appendChild(d);
        const r = d.querySelector('input[type="range"]'), num = d.querySelector('input[type="number"]');
        r.addEventListener('input', update);
        num.addEventListener('change', () => {
          let v = parseFloat(num.value);
          if (!isFinite(v)) v = +r.value;
          r.value = Math.min(UMAXV, Math.max(UMINV, v));
          update();
        });
      }
      const tb = __q('fe-table');
      tb.innerHTML = '';
      const rows = [];
      for (let j = 1; j <= n; j++) rows.push({ name: 'Hat φ' + sub(j), cls: '' });
      rows.push({ name: 'Combination Σ cⱼ φⱼ', cls: 'sep', combo: true });
      rows.push({ name: 'Sine sin(πx/2L), not in the space', cls: '' });
      rows.forEach((r, k) => {
        const tr = document.createElement('tr');
        if (r.cls) tr.className = r.cls;
        const id = 'fe-sel-' + k;
        tr.innerHTML =
          '<td><input type="radio" name="fe-sel" id="' + id + '"' + (k === 0 ? ' checked' : '') + '> ' +
          '<label for="' + id + '">' + r.name + '</label>' +
          (r.combo ? ' <button type="button" id="fe-newc">New coefficients</button>' : '') +
          '<span class="eq" id="fe-eq-' + k + '"></span></td>' +
          '<td class="num"><span id="fe-res-' + k + '"></span> J</td>';
        tb.appendChild(tr);
        tr.querySelector('input').addEventListener('change', () => { sel = k; update(); });
      });
      __q('fe-newc').addEventListener('click', () => { newCoefs(); update(); });
      update();
    }

    function readU() {
      const u = [0];
      for (let i = 1; i <= n; i++) u.push(+__q('fe-u-' + i).value);
      return u;
    }

    function update() {
      const h = 1 / n, u = readU(), f = loads(n);
      __q('fe-n-val').textContent = n;
      for (let i = 1; i <= n; i++) __q('fe-un-' + i).value = u[i].toFixed(3);

      // schematic
      const qa = __q('fe-qarrows').children;
      for (let i = 0; i < qa.length; i++) {
        const x0 = 72 + i * 38, xi = (x0 + 9 - 60) / 320, len = 18 * (tri() ? xi : 1);
        qa[i].setAttribute('x1', x0); qa[i].setAttribute('x2', x0 + len);
        qa[i].style.visibility = q > 0 && len >= 3 ? 'visible' : 'hidden';
      }
      __q('fe-q-lbl').textContent = tri() ? 'q(x) = ' + q + '·x/L kN/m' : 'q = ' + q + ' kN/m';
      const pa = __q('fe-parrow'), plen = 12 + 28 * Math.abs(P) / 20;
      pa.style.visibility = P !== 0 ? 'visible' : 'hidden';
      if (P > 0) { pa.setAttribute('x1', 382); pa.setAttribute('x2', 382 + plen); }
      else       { pa.setAttribute('x1', 382 + plen); pa.setAttribute('x2', 382); }
      __q('fe-p-lbl').textContent = 'P = ' + sgn(P) + ' kN';
      const nodes = __q('fe-nodes');
      clear(nodes);
      for (let i = 0; i <= n; i++) {
        el('circle', { cx: 60 + X(i * h), cy: 44, r: 3.2, fill: 'var(--fg)' }, nodes);
        txt(nodes, 60 + X(i * h) + (i === 0 ? 5 : 0), 66, String(i));
      }

      // grids depend on n
      const ug = __q('fe-ugrid'), ng = __q('fe-ngrid'), tg = __q('fe-tgrid');
      [ug, ng, tg].forEach(clear);
      for (let v = UMIN + 5; v <= UMAX; v += 10)
        el('line', { x1: 0, y1: YU(v), x2: PW, y2: YU(v), stroke: v === 0 ? 'var(--fg-muted)' : 'var(--grid)' }, ug);
      for (let v = NMIN; v <= NMAX; v += 10)
        el('line', { x1: 0, y1: YN(v), x2: PW, y2: YN(v), stroke: v === 0 ? 'var(--fg-muted)' : 'var(--grid)' }, ng);
      [-1, 0, 1].forEach((v) =>
        el('line', { x1: 0, y1: YT(v), x2: PW, y2: YT(v), stroke: v === 0 ? 'var(--fg-muted)' : 'var(--grid)' }, tg));
      for (let i = 0; i <= n; i++) {
        el('line', { x1: X(i * h), y1: 0, x2: X(i * h), y2: UH, stroke: 'var(--grid)' }, ug);
        el('line', { x1: X(i * h), y1: 0, x2: X(i * h), y2: NH, stroke: 'var(--grid)' }, ng);
        el('line', { x1: X(i * h), y1: 0, x2: X(i * h), y2: TH, stroke: 'var(--grid)' }, tg);
      }
      [[ug, UH], [ng, NH], [tg, TH]].forEach(([g, H]) =>
        el('rect', { x: 0, y: 0, width: PW, height: H, fill: 'none', stroke: 'var(--border)' }, g));

      // u plot
      let d = '';
      for (let i = 0; i <= n; i++) d += (i ? 'L' : 'M') + X(i * h).toFixed(2) + ',' + YU(u[i]).toFixed(2);
      __q('fe-upath').setAttribute('d', d);
      const dots = __q('fe-udots');
      clear(dots);
      for (let i = 1; i <= n; i++)
        el('circle', { cx: X(i * h), cy: YU(u[i]), r: 4, fill: 'var(--disp)', stroke: 'var(--panel-bg)', 'stroke-width': 1.5 }, dots);
      let de = '', dn = '', pen = false;
      for (let k = 0; k <= 200; k++) {
        const xi = k / 200;
        de += (k ? 'L' : 'M') + X(xi).toFixed(2) + ',' + YU(exactU(xi)).toFixed(2);
        dn += (k ? 'L' : 'M') + X(xi).toFixed(2) + ',' + YN(exactN(xi)).toFixed(2);
      }
      __q('fe-uref').setAttribute('d', reveal ? de : '');
      __q('fe-nref').setAttribute('d', reveal ? dn : '');
      root.querySelectorAll('.fe-legend-exact').forEach((g) => { g.style.visibility = reveal ? 'visible' : 'hidden'; });

      // N plot: constant per element, segments outside the window are skipped
      const Ne = [0];
      for (let e = 1; e <= n; e++) Ne.push((u[e] - u[e - 1]) / h);
      let dN = '', prevIn = false;
      for (let e = 1; e <= n; e++) {
        const inWin = Ne[e] >= NMIN && Ne[e] <= NMAX;
        if (!inWin) { prevIn = false; continue; }
        const y = YN(Ne[e]).toFixed(2);
        dN += (prevIn ? 'L' + X((e - 1) * h).toFixed(2) + ',' + y : 'M' + X((e - 1) * h).toFixed(2) + ',' + y) +
              'L' + X(e * h).toFixed(2) + ',' + y;
        prevIn = true;
      }
      __q('fe-npath').setAttribute('d', dN);

      // residuals of hat tests: (K u − f)_j
      const res = [0];
      for (let j = 1; j <= n; j++) {
        const Kuj = (j < n ? 2 * n * u[j] - n * u[j + 1] : n * u[j]) - n * u[j - 1];
        res.push(Kuj - f[j]);
      }
      let pass = 0;
      for (let j = 1; j <= n; j++) {
        const ok = Math.abs(res[j]) < TOL;
        if (ok) pass++;
        const r = __q('fe-res-' + (j - 1));
        r.textContent = (ok ? '\u2713 ' : '\u2717 ') + fmt(res[j], 3);
        r.className = ok ? 'pass' : 'fail';
        const terms = [];
        const c = (k) => (k === 1 ? '' : k + '\u2009');
        if (j > 1) terms.push('\u2212\u2009' + c(n) + 'u' + sub(j - 1));
        terms.push((terms.length ? '+\u2009' : '') + c(j < n ? 2 * n : n) + 'u' + sub(j));
        if (j < n) terms.push('\u2212\u2009' + c(n) + 'u' + sub(j + 1));
        __q('fe-eq-' + (j - 1)).textContent = terms.join(' ') + ' = ' + fmt(f[j], 3).trim();
      }
      // combination
      let rc = 0, cabs = 0;
      for (let j = 1; j <= n; j++) { rc += coef[j] * res[j]; cabs += Math.abs(coef[j]); }
      const rcEl = __q('fe-res-' + n);
      const okc = Math.abs(rc) < TOL * Math.max(1, cabs);
      rcEl.textContent = (okc ? '\u2713 ' : '\u2717 ') + fmt(rc, 3);
      rcEl.className = okc ? 'pass' : 'fail';
      __q('fe-eq-' + n).textContent = 'c = (' + coef.slice(1).map((v) => v.toFixed(1)).join(', ') + ')';
      // sine: W_int exact per element, W_ext analytic
      let wi = 0;
      for (let e = 1; e <= n; e++) wi += Ne[e] * (Math.sin(Math.PI * e * h / 2) - Math.sin(Math.PI * (e - 1) * h / 2));
      const we = (tri() ? q * 4 / (Math.PI * Math.PI) : q * 2 / Math.PI) + P;
      const rs = __q('fe-res-' + (n + 1));
      rs.textContent = fmt(wi - we, 3);
      rs.className = 'neutral';
      __q('fe-eq-' + (n + 1)).textContent = 'W_int = ' + fmt(wi, 3).trim() + ', W_ext = ' + fmt(we, 3).trim() + ' (no pass/fail: outside the space)';

      // selected test function
      let td = '', tname;
      if (sel < n) {
        const j = sel + 1;
        tname = 'hat φ' + sub(j);
        td = 'M0,' + YT(0);
        for (let i = 1; i <= n; i++) td += 'L' + X(i * h).toFixed(2) + ',' + YT(i === j ? 1 : 0).toFixed(2);
      } else if (sel === n) {
        tname = 'combination Σ cⱼ φⱼ';
        td = 'M0,' + YT(0);
        for (let i = 1; i <= n; i++) td += 'L' + X(i * h).toFixed(2) + ',' + YT(coef[i]).toFixed(2);
      } else {
        tname = 'sine (not in the FE space)';
        for (let k = 0; k <= 200; k++) td += (k ? 'L' : 'M') + X(k / 200).toFixed(2) + ',' + YT(Math.sin(Math.PI * k / 400)).toFixed(2);
      }
      __q('fe-tpath').setAttribute('d', td);
      __q('fe-tfill').setAttribute('d', td + 'L' + X(1) + ',' + YT(0) + 'L0,' + YT(0) + 'Z');
      __q('fe-t-title').textContent = 'Test function δu(x): ' + tname + ' [mm]';

      // errors of the current nodal values
      const E = errNorms(u, n);
      __q('fe-eu').textContent = fmt(E.eu, 4);
      __q('fe-eN').textContent = fmt(E.eN, 3);
      __q('fe-eu-rel').textContent = E.nu > 0 ? fmt(100 * E.eu / E.nu, 2) : '\u00A0\u2014';
      __q('fe-eN-rel').textContent = E.nN > 0 ? fmt(100 * E.eN / E.nN, 2) : '\u00A0\u2014';

      // convergence of the Galerkin solution, n = 1..64
      const C = convergence(), eu = C.eu1, eN = C.eN1, showQ = __q('fe-quad').checked;
      const all = eu.concat(eN, [E.eu, E.eN], showQ ? C.eu2.concat(C.eN2) : []).filter((v) => v > 1e-12);
      const cg = __q('fe-cgrid'), ct = __q('fe-cticks'), cm = __q('fe-cmarks');
      [cg, ct, cm].forEach(clear);
      const CW = 340, CH = 170;
      const CX = (m) => CW * Math.log2(m) / Math.log2(NC);
      let lo = 0, hi = 1;
      if (all.length) {
        lo = Math.floor(Math.log10(Math.min.apply(null, all)));
        hi = Math.ceil(Math.log10(Math.max.apply(null, all)));
        if (hi - lo < 1) hi = lo + 1;
      }
      const CY = (v) => (Math.log10(v) - lo) / (hi - lo) * CH;
      const sup = (k) => String(k).replace('-', '\u207B').split('').map((c) => '⁰¹²³⁴⁵⁶⁷⁸⁹'[+c] || c).join('');
      const step = hi - lo > 6 ? 2 : 1;
      for (let k = lo; k <= hi; k += step) {
        el('line', { x1: 0, y1: CY(Math.pow(10, k)), x2: CW, y2: CY(Math.pow(10, k)), stroke: 'var(--grid)' }, cg);
        txt(ct, 54, 232 - CY(Math.pow(10, k)) + 3.5, '10' + sup(k), 'end');
      }
      [1, 2, 4, 8, 16, 32, 64].forEach((m) => {
        el('line', { x1: CX(m), y1: 0, x2: CX(m), y2: CH, stroke: m === n ? 'var(--fg-muted)' : 'var(--grid)' }, cg);
        txt(ct, 60 + CX(m), 246, String(m));
      });
      el('rect', { x: 0, y: 0, width: CW, height: CH, fill: 'none', stroke: 'var(--border)' }, cg);
      function logPath(arr) {
        let d = '', pen = false;
        arr.forEach((v, k) => {
          if (!(v > 1e-12)) { pen = false; return; }
          d += (pen ? 'L' : 'M') + CX(k + 1).toFixed(2) + ',' + CY(v).toFixed(2);
          pen = true;
        });
        return d;
      }
      const endLabel = (arr, lbl, col) => {
        const v = arr[NC - 1];
        if (!(v > 1e-12)) return;
        const t = txt(ct, 60 + CW + 5, 232 - CY(v) + 3.5, lbl, 'start');
        t.setAttribute('style', 'fill:' + col + ';font-weight:600');
      };
      endLabel(eu, 'u', 'var(--disp)');
      endLabel(eN, 'N', 'var(--stress)');
      if (__q('fe-quad').checked) { endLabel(C.eu2, 'u', 'var(--disp)'); endLabel(C.eN2, 'N', 'var(--stress)'); }
      __q('fe-cu').setAttribute('d', logPath(eu));
      __q('fe-cN').setAttribute('d', logPath(eN));
      [[eu[n - 1], E.eu, 'var(--disp)'], [eN[n - 1], E.eN, 'var(--stress)']].forEach(([g, mine, col]) => {
        if (g > 1e-12) el('circle', { cx: CX(n), cy: CY(g), r: 4.5, fill: col, stroke: 'var(--panel-bg)', 'stroke-width': 1.5 }, cm);
        if (mine > 1e-12) el('rect', { x: CX(n) - 5, y: CY(mine) - 5, width: 10, height: 10, fill: 'none', stroke: col, 'stroke-width': 1.8 }, cm);
      });
      const slope = (arr) => (arr[31] > 1e-12 && arr[63] > 1e-12 ? Math.log2(arr[31] / arr[63]).toFixed(2) : '\u2014');
      __q('fe-leg-u').textContent = 'linear: u error, slope ' + slope(eu);
      __q('fe-leg-N').textContent = 'linear: N error, slope ' + slope(eN);
      __q('fe-cqu').setAttribute('d', showQ ? logPath(C.eu2) : '');
      __q('fe-cqN').setAttribute('d', showQ ? logPath(C.eN2) : '');
      __q('fe-leg-q').style.visibility = showQ ? 'visible' : 'hidden';
      const qExact = C.eu2.every((v) => v === 0) && C.eN2.every((v) => v === 0);
      __q('fe-leg-qu').textContent = qExact ? 'quadratic: zero error, the exact u is quadratic' : 'quadratic: u error, slope ' + slope(C.eu2);
      __q('fe-leg-qN').textContent = qExact ? '' : 'quadratic: N error, slope ' + slope(C.eN2);
      __q('fe-leg-qN-line').style.visibility = qExact ? 'hidden' : '';

      // verdict
      const v = __q('fe-verdict');
      if (pass === n) {
        v.className = 'verdict ok';
        v.textContent = 'All ' + n + ' hat tests balance: this is the Galerkin solution, and every test in the FE space balances. ' +
          'The sine test is outside the space, so its residual need not be zero.';
      } else {
        v.className = 'verdict bad';
        const hint = Math.abs(res[n]) >= TOL
          ? 'Start at the tip: the last hat gives N in the last element directly, ' + (n > 1 ? n + '(u' + sub(n) + ' − u' + sub(n - 1) + ')' : 'u' + sub(1)) + ' = f' + sub(n) + '.'
          : 'Work back toward the wall: hat j says Nⱼ − Nⱼ₊₁ = fⱼ, then u grows by N·h/EA across each element.';
        v.textContent = pass + ' of ' + n + ' hat tests balance. ' + hint;
      }
      __q('fe-reveal').textContent = reveal ? 'Hide exact solution' : 'Show exact solution';
    }

    // ---- events ----
    nIn.addEventListener('input', rebuild);
    loadSel.addEventListener('change', () => { reveal = false; update(); });
    __q('fe-new').addEventListener('click', () => {
      q = 4 + Math.floor(Math.random() * 17);
      P = -10 + Math.floor(Math.random() * 31);
      reveal = false;
      update();
    });
    __q('fe-reset').addEventListener('click', () => {
      for (let i = 1; i <= n; i++) __q('fe-u-' + i).value = 0;
      update();
    });
    __q('fe-solve').addEventListener('click', () => {
      const u = galerkin(n, loads(n));
      for (let i = 1; i <= n; i++) __q('fe-u-' + i).value = u[i];
      update();
    });
    __q('fe-reveal').addEventListener('click', () => { reveal = !reveal; update(); });
    __q('fe-quad').addEventListener('change', update);

    // ---- predict-first quiz ----
    const QUIZ = [
      { q: 'You double the number of elements. The L2 error of N will be roughly…',
        options: ['unchanged', 'halved', 'divided by 4', 'divided by 8'],
        answer: 1,
        explain: 'N is piecewise constant, so its error is first order in h: slope 1 on the log–log plot.',
        check: 'fill in the Galerkin solution at n = 3 and at n = 6 and compare the N error, or read the slope in the legend.' },
      { q: 'And the L2 error of u?',
        options: ['halved', 'divided by 4', 'divided by 8'],
        answer: 1,
        explain: 'u is piecewise linear, so its error is second order in h: slope 2.',
        check: 'same as before, with the u error.' },
      { q: 'How do the Galerkin nodal displacements compare with the exact solution at the nodes?',
        options: ['Slightly too small', 'Exactly equal', 'Slightly too large'],
        answer: 1,
        explain: 'For a 1D bar with constant EA and consistently integrated loads, the nodal values are exact for any n. The error lives between the nodes.',
        check: 'fill in the Galerkin solution and show the exact solution: the dots sit on the dashed curve.' },
      { q: 'At the Galerkin solution, does the sine test balance?',
        options: ['Yes, always', 'No in general, but its residual shrinks as n grows', 'No, and it gets worse as n grows'],
        answer: 1,
        explain: 'Galerkin only enforces the tests inside the FE space. The sine is outside, but the space approximates it better as the mesh is refined.',
        check: 'fill in the Galerkin solution at n = 1, 2, … 6 and watch the sine row.' },
      { q: 'In each element, the FE axial force N_h equals…',
        options: ['the exact N at the element centre', 'the average of the exact N over the element', 'the exact N at the left node'],
        answer: 1,
        explain: 'N_h = EA(u_e − u_(e−1))/h, the mean of EA u′ over the element; with exact nodal values that is the element average of the exact N. For a uniform load it also equals the centre value, because the exact N is linear.',
        check: 'use the triangular load, show the exact solution and compare each step with the dashed curve.' },
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
    makeQuiz(__q('fe-quiz'), QUIZ);

    rebuild();
  })();
  </script>
</div>
```
