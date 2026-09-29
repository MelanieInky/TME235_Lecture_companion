```{=html}
<style>
.viz-vw,
[data-bs-theme="light"] .viz-vw,
body.quarto-light .viz-vw {
  --fg: #1f2328; --fg-muted: #5b636d; --panel-bg: #f6f7f9; --border: #d4d8de;
  --grid: #e3e6ea; --slider: #3b6ea8;
  --load: #00805E; --stress: #D55E00; --ref: #6B7684; --virtual: #CC79A7;
  --ok: #00805E; --bad: #B8321A;
}
@media (prefers-color-scheme: dark) {
  .viz-vw {
    --fg: #e6e8eb; --fg-muted: #a0a8b3; --panel-bg: #1e2227; --border: #3a414a;
    --grid: #2c323a; --slider: #7fb0e6;
    --load: #3CC9A0; --stress: #FF8C42; --ref: #9AA4B0; --virtual: #E3A5C7;
    --ok: #3CC9A0; --bad: #FF7B6B;
  }
}
[data-bs-theme="dark"] .viz-vw,
body.quarto-dark .viz-vw {
  --fg: #e6e8eb; --fg-muted: #a0a8b3; --panel-bg: #1e2227; --border: #3a414a;
  --grid: #2c323a; --slider: #7fb0e6;
  --load: #3CC9A0; --stress: #FF8C42; --ref: #9AA4B0; --virtual: #E3A5C7;
  --ok: #3CC9A0; --bad: #FF7B6B;
}

.viz-vw { color: var(--fg); font-family: inherit; }
.viz-vw *, .viz-vw *::before, .viz-vw *::after { box-sizing: border-box; }
.viz-vw .intro { color: var(--fg-muted); font-size: .95em; margin: 0 0 .8em; }
.viz-vw .controls {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .6em 1.2em;
  padding: .8em; background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 6px; margin-bottom: .6em;
}
.viz-vw .ctrl label { display: block; font-size: .88em; color: var(--fg-muted); margin-bottom: .2em; }
.viz-vw .ctrl .val { color: var(--fg); font-variant-numeric: tabular-nums; }
.viz-vw input[type="range"] { width: 100%; accent-color: var(--slider); }
.viz-vw input[type="range"]:disabled { opacity: .35; }
.viz-vw select {
  width: 100%; font: inherit; font-size: .9em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 4px; padding: .2em .3em;
}
.viz-vw .presets { display: flex; flex-wrap: wrap; gap: .4em; margin-bottom: .8em; }
.viz-vw .presets button {
  font: inherit; font-size: .85em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 4px; padding: .25em .6em; cursor: pointer;
}
.viz-vw .presets button:hover, .viz-vw .presets button:focus-visible { border-color: var(--slider); }
.viz-vw .fig {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 6px;
  padding: .5em; margin-bottom: .8em;
}
.viz-vw svg { display: block; width: 100%; height: auto; max-width: 460px; margin: 0 auto; }
.viz-vw svg text { fill: var(--fg-muted); font-size: 11px; font-family: inherit; }
.viz-vw svg text.lbl { fill: var(--fg); }
.viz-vw table { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; font-size: .92em; }
.viz-vw td { padding: .25em .4em; border-bottom: 1px solid var(--grid); }
.viz-vw td.num { text-align: right; white-space: nowrap; }
.viz-vw .verdict { margin-top: .6em; font-weight: 600; }
.viz-vw .verdict.ok { color: var(--ok); }
.viz-vw .verdict.bad { color: var(--bad); }
.viz-vw .note { font-size: .88em; color: var(--fg-muted); margin-top: .9em; }
.viz-vw .note p { margin: 0 0 .5em; }
@media (max-width: 560px) {
  .viz-vw .controls { grid-template-columns: 1fr; }
}
</style>

<div class="viz-vw">
  <p class="intro">A bar of length L = 1 m, fixed at x = 0, carries a uniform axial load q and a
  tip load P. Pick a force field N(x) and a virtual displacement δu(x) (amplitude δ = 1 mm), and
  compare internal and external virtual work.</p>

  <div class="controls">
    <div class="ctrl">
      <label for="vw-nsel">Axial force field N(x)</label>
      <select id="vw-nsel">
        <option value="exact">Equilibrium solution: P + q(L − x)</option>
        <option value="constant">Constant: P + qL/2</option>
        <option value="offset">Shifted: P + q(L − x) + 10 kN</option>
      </select>
    </div>
    <div class="ctrl">
      <label for="vw-vsel">Virtual displacement δu(x)</label>
      <select id="vw-vsel">
        <option value="linear">Linear: δ·x/L</option>
        <option value="quad">Quadratic: δ·(x/L)²</option>
        <option value="sine">Sine: δ·sin(πx/2L)</option>
        <option value="bump">Local bump at x = a (zero at both ends)</option>
        <option value="shift">Rigid shift: δ everywhere (inadmissible)</option>
      </select>
    </div>
    <div class="ctrl">
      <label for="vw-q">Distributed load q = <span class="val" id="vw-q-val"></span> kN/m</label>
      <input type="range" id="vw-q" min="0" max="20" step="1" value="10">
    </div>
    <div class="ctrl">
      <label for="vw-p">Tip load P = <span class="val" id="vw-p-val"></span> kN</label>
      <input type="range" id="vw-p" min="-10" max="20" step="1" value="5">
    </div>
    <div class="ctrl">
      <label for="vw-a">Bump centre a/L = <span class="val" id="vw-a-val"></span></label>
      <input type="range" id="vw-a" min="0.15" max="0.85" step="0.01" value="0.5">
    </div>
  </div>

  <div class="presets">
    <button type="button" data-n="constant" data-v="linear">Constant N passes the linear test</button>
    <button type="button" data-n="constant" data-v="quad">…and fails the quadratic one</button>
    <button type="button" data-n="offset" data-v="bump">Shifted N passes every bump</button>
    <button type="button" data-n="offset" data-v="linear">Linear δu catches the tip condition</button>
    <button type="button" data-n="exact" data-v="shift">Why δu(0) must be 0</button>
  </div>

  <div class="fig">
    <svg id="vw-svg" viewBox="0 0 460 546" role="img"
         aria-label="Bar under axial load, with plots of N(x), the virtual displacement and the virtual work densities">
      <defs>
        <marker id="vw-ah-load" viewBox="0 0 10 10" refX="9" refY="5"
                markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="var(--load)"></path>
        </marker>
        <pattern id="vw-hatch" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
          <line x1="0" y1="0" x2="0" y2="5" stroke="var(--load)" stroke-width="2"></line>
        </pattern>
      </defs>

      <!-- schematic -->
      <g id="vw-wall" stroke="var(--fg-muted)" stroke-width="1"></g>
      <rect x="60" y="38" width="320" height="12" fill="var(--grid)" stroke="var(--fg-muted)"></rect>
      <g id="vw-qarrows" stroke="var(--load)" stroke-width="1.5"></g>
      <text id="vw-q-lbl" class="lbl" x="70" y="18"></text>
      <line id="vw-parrow" y1="44" y2="44" stroke="var(--load)" stroke-width="2.5"
            marker-end="url(#vw-ah-load)"></line>
      <text id="vw-p-lbl" class="lbl" x="404" y="28" text-anchor="middle"></text>

      <!-- N plot -->
      <text class="lbl" x="60" y="94">Axial force N(x) [kN]</text>
      <line x1="252" y1="90" x2="268" y2="90" stroke="var(--stress)" stroke-width="2"></line>
      <text x="272" y="94" style="font-size:10px">selected</text>
      <line x1="320" y1="90" x2="336" y2="90" stroke="var(--ref)" stroke-width="2"
            stroke-dasharray="4 3"></line>
      <text x="340" y="94" style="font-size:10px">equilibrium</text>
      <g id="vw-nticks"></g>
      <g transform="translate(60,212) scale(1,-1)">
        <g id="vw-ngrid"></g>
        <path id="vw-nref" fill="none" stroke="var(--ref)" stroke-width="2"
              stroke-dasharray="4 3"></path>
        <path id="vw-npath" fill="none" stroke="var(--stress)" stroke-width="2"></path>
        <circle id="vw-ptarget" cx="320" r="4.5" fill="none" stroke="var(--load)" stroke-width="2"></circle>
      </g>

      <!-- δu plot -->
      <text class="lbl" x="60" y="246">Virtual displacement δu(x) [mm]</text>
      <g id="vw-uticks"></g>
      <g transform="translate(60,340) scale(1,-1)">
        <g id="vw-ugrid"></g>
        <path id="vw-ufill" fill="var(--virtual)" fill-opacity="0.14" stroke="none"></path>
        <path id="vw-upath" fill="none" stroke="var(--virtual)" stroke-width="2"></path>
        <circle id="vw-bcflag" cx="0" r="5" fill="none" stroke="var(--bad)" stroke-width="2"></circle>
      </g>
      <g id="vw-xticks"></g>

      <!-- virtual work densities and totals -->
      <text class="lbl" x="60" y="392">Work densities along the bar [J/m]</text>
      <line x1="258" y1="388" x2="274" y2="388" stroke="var(--stress)" stroke-width="2"></line>
      <text x="278" y="392" style="font-size:10px">N δε</text>
      <line x1="312" y1="388" x2="328" y2="388" stroke="var(--load)" stroke-width="2" stroke-dasharray="7 4"></line>
      <text x="332" y="392" style="font-size:10px">q δu</text>
      <text x="422" y="403" text-anchor="middle" style="font-size:10px">totals</text>
      <g id="vw-dticks"></g>
      <g transform="translate(60,504) scale(1,-1)">
        <g id="vw-dgrid"></g>
        <path id="vw-dext-fill" fill="var(--load)" fill-opacity="0.18" stroke="none"></path>
        <path id="vw-dint-fill" fill="var(--stress)" fill-opacity="0.18" stroke="none"></path>
        <path id="vw-dext" fill="none" stroke="var(--load)" stroke-width="2" stroke-dasharray="7 4"></path>
        <path id="vw-dint" fill="none" stroke="var(--stress)" stroke-width="2"></path>
      </g>
      <g transform="translate(392,504) scale(1,-1)">
        <line id="vw-bzero" x1="0" x2="60" stroke="var(--fg-muted)"></line>
        <rect id="vw-bint" x="4" width="20" fill="var(--stress)" fill-opacity="0.7"></rect>
        <rect id="vw-bdist" x="34" width="20" fill="var(--load)" fill-opacity="0.45"></rect>
        <rect id="vw-btip" x="34" width="20" fill="url(#vw-hatch)" stroke="var(--load)" stroke-width="1"></rect>
      </g>
      <text x="406" y="520" text-anchor="middle">int</text>
      <text x="436" y="520" text-anchor="middle">ext</text>
      <g id="vw-dxticks"></g>
      <text x="220" y="538" text-anchor="middle">x / L</text>
    </svg>
  </div>

  <table data-quarto-disable-processing="true">
    <tr><td>Internal virtual work ∫ N δε dx</td><td class="num"><span id="vw-wint"></span> J</td></tr>
    <tr><td>External virtual work ∫ q δu dx + P δu(L)</td><td class="num"><span id="vw-wext"></span> J</td></tr>
    <tr><td>Difference W<sub>int</sub> − W<sub>ext</sub></td><td class="num"><span id="vw-diff"></span> J</td></tr>
    <tr><td>Support reaction work R δu(0), with R = −N(0)</td><td class="num"><span id="vw-wreac"></span> J</td></tr>
  </table>
  <div class="verdict" id="vw-verdict"></div>

  <div class="note">
    <p>The principle of virtual work: N(x) is in equilibrium with q and P if and only if
    ∫ N δε dx = ∫ q δu dx + P δu(L) for <em>every</em> admissible δu, i.e. every δu with
    δu(0) = 0 where the displacement is prescribed. Integrating by parts, the difference is
    −∫ (dN/dx + q) δu dx + [N(L) − P] δu(L). A bump that vanishes at both ends therefore tests
    only the field equation dN/dx + q = 0; any δu with δu(L) ≠ 0 also tests the natural
    boundary condition N(L) = P, shown as the hollow marker on the N plot.</p>
    <p>One passing test proves nothing. The constant field passes the linear δu because that
    test only sees the total load (∫ q δu dx = qL/2 for every field), and the shifted field
    passes every bump because it satisfies dN/dx + q = 0 everywhere — it only fails at the tip.
    With q = 0 the constant field coincides with the equilibrium solution.</p>
    <p>The rigid shift violates δu(0) = 0, so the wall reaction does virtual work and
    W<sub>int</sub> ≠ W<sub>ext</sub> even for the true N; the gap equals R δu(0). In a real problem
    R is unknown, which is why admissible δu must vanish on the supported boundary. For admissible
    fields that row is zero.</p>
    <p>The bottom plot draws the works as areas. The solid curve is the internal density N δε,
    whose area is W<sub>int</sub>; the dashed curve is the external density q δu, whose area is the
    distributed part of W<sub>ext</sub>. The tip load adds P δu(L) at a single point, so it has no
    density and appears only as the hatched part of the "ext" bar. The bars show the totals on their
    own scale; the numbers are in the table. The densities do not have to agree point by point,
    even for the equilibrium field: with the linear δu, N δε = N(x) while q δu = q x/L. Only the
    totals must match. A bump makes the internal work pile up on the bump's flanks, where δε is
    large.</p>
    <p>Virtual displacements are infinitesimal; δ = 1 mm is only a scale, so works are in
    kN·mm = J. EA never enters: the principle is a statement about equilibrium, not about the
    material. Integrals are evaluated with Simpson's rule (600 intervals); values below
    0.0005 J are shown as zero.</p>
  </div>

  <script>
  (function () {
    const root = (document.currentScript && document.currentScript.closest('.viz-vw')) || document.querySelector('.viz-vw');
    if (!root) return;
    const __q = (id) => root.querySelector('#' + id);
    const NS = 'http://www.w3.org/2000/svg';

    const L = 1;          // m
    const HW = 0.15;      // bump half-width, x/L
    const OFFSET = 10;    // kN, shifted field
    const NINT = 600;     // Simpson intervals (even)
    const TOL = 1e-4;     // J

    // plot geometry (maths coordinates inside flipped groups)
    const PW = 320;
    const NMIN = -10, NMAX = 50, NH = 110, SN = NH / (NMAX - NMIN);
    const UMIN = -0.1, UMAX = 1.1, UH = 86, SU = UH / (UMAX - UMIN);
    const NBASE = 212, UBASE = 340;   // screen y of the flipped origins
    const X = (xi) => PW * xi;
    const YN = (N) => (N - NMIN) * SN;
    const YU = (u) => (u - UMIN) * SU;

    const fields = {
      exact:    (x, q, P) => P + q * (L - x),
      constant: (x, q, P) => P + q * L / 2,
      offset:   (x, q, P) => P + q * (L - x) + OFFSET,
    };
    // returns [δu in mm, dδu/dx in mm/m] at xi = x/L
    const virt = {
      linear: (xi) => [xi, 1 / L],
      quad:   (xi) => [xi * xi, 2 * xi / L],
      sine:   (xi) => [Math.sin(Math.PI * xi / 2), (Math.PI / (2 * L)) * Math.cos(Math.PI * xi / 2)],
      bump:   (xi, a) => {
        const d = xi - a;
        if (Math.abs(d) >= HW) return [0, 0];
        const th = Math.PI * d / (2 * HW);
        return [Math.cos(th) ** 2, -Math.sin(2 * th) * Math.PI / (2 * HW * L)];
      },
      shift:  () => [1, 0],
    };

    const qIn = __q('vw-q'), pIn = __q('vw-p'), aIn = __q('vw-a');
    const nSel = __q('vw-nsel'), vSel = __q('vw-vsel');

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

    // ---- static scaffolding (built once) ----
    (function build() {
      const wall = __q('vw-wall');
      el('line', { x1: 60, y1: 20, x2: 60, y2: 68, 'stroke-width': 2 }, wall);
      for (let y = 22; y <= 60; y += 8) el('line', { x1: 60, y1: y, x2: 52, y2: y + 8 }, wall);

      const qa = __q('vw-qarrows');
      for (let i = 0; i < 8; i++) {
        const x0 = 72 + i * 38;
        el('line', { x1: x0, y1: 30, x2: x0 + 18, y2: 30, 'marker-end': 'url(#vw-ah-load)' }, qa);
      }

      const ng = __q('vw-ngrid'), nt = __q('vw-nticks');
      for (let N = NMIN; N <= NMAX; N += 10) {
        el('line', { x1: 0, y1: YN(N), x2: PW, y2: YN(N),
                     stroke: N === 0 ? 'var(--fg-muted)' : 'var(--grid)', 'stroke-width': 1 }, ng);
        txt(nt, 54, NBASE - YN(N) + 3.5, N < 0 ? '\u2212' + (-N) : String(N), 'end');
      }
      const ug = __q('vw-ugrid'), ut = __q('vw-uticks');
      [0, 0.5, 1].forEach((u) => {
        el('line', { x1: 0, y1: YU(u), x2: PW, y2: YU(u),
                     stroke: u === 0 ? 'var(--fg-muted)' : 'var(--grid)', 'stroke-width': 1 }, ug);
        txt(ut, 54, UBASE - YU(u) + 3.5, String(u), 'end');
      });
      const xt = __q('vw-xticks');
      [0, 0.25, 0.5, 0.75, 1].forEach((xi) => {
        el('line', { x1: X(xi), y1: 0, x2: X(xi), y2: NH, stroke: 'var(--grid)' }, ng);
        el('line', { x1: X(xi), y1: 0, x2: X(xi), y2: UH, stroke: 'var(--grid)' }, ug);
        txt(xt, 60 + X(xi), 356, String(xi));
        txt(__q('vw-dxticks'), 60 + X(xi), 520, String(xi));
      });
      el('rect', { x: 0, y: 0, width: PW, height: NH, fill: 'none', stroke: 'var(--border)' }, ng);
      el('rect', { x: 0, y: 0, width: PW, height: UH, fill: 'none', stroke: 'var(--border)' }, ug);
    })();

    function simpson(f) {
      const h = L / NINT;
      let s = f(0) + f(L);
      for (let i = 1; i < NINT; i++) s += (i % 2 ? 4 : 2) * f(i * h);
      return s * h / 3;
    }
    function fmt(v, d) {
      if (Math.abs(v) < 0.5 * Math.pow(10, -d)) v = 0;
      const s = Math.abs(v).toFixed(d);
      return (v < 0 ? '\u2212' : '\u00A0') + s;
    }
    function pathOf(fn, n) {
      let d = '';
      for (let i = 0; i <= n; i++) {
        const xi = i / n, p = fn(xi);
        d += (i ? 'L' : 'M') + X(xi).toFixed(2) + ',' + p.toFixed(2);
      }
      return d;
    }

    const clearG = (g) => { while (g.firstChild) g.removeChild(g.firstChild); };
    function niceRange(lo, hi) {            // expand [lo, hi] to round ticks, about 4 intervals
      if (hi - lo < 1e-9) { lo = -1; hi = 1; }
      const raw = (hi - lo) / 4, p = Math.pow(10, Math.floor(Math.log10(raw))), m = raw / p;
      const step = (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p;
      return [Math.floor(lo / step + 1e-9) * step, Math.ceil(hi / step - 1e-9) * step, step];
    }

    function update() {
      const q = +qIn.value, P = +pIn.value, a = +aIn.value;
      const nKey = nSel.value, vKey = vSel.value;
      aIn.disabled = vKey !== 'bump';
      __q('vw-q-val').textContent = q.toFixed(0);
      __q('vw-p-val').textContent = (P < 0 ? '\u2212' : '') + Math.abs(P).toFixed(0);
      __q('vw-a-val').textContent = a.toFixed(2);

      const Nf = (x) => fields[nKey](x, q, P);
      const Ne = (x) => fields.exact(x, q, P);
      const V = (x) => virt[vKey](x / L, a);

      // work
      const Wint = simpson((x) => Nf(x) * V(x)[1]);
      const Wext = simpson((x) => q * V(x)[0]) + P * V(L)[0];
      const du0 = V(0)[0];
      const Wreac = -Nf(0) * du0;
      const diff = Wint - Wext;

      // schematic
      __q('vw-qarrows').style.visibility = q > 0 ? 'visible' : 'hidden';
      __q('vw-q-lbl').textContent = 'q = ' + q + ' kN/m';
      const pa = __q('vw-parrow');
      const len = 12 + 28 * Math.abs(P) / 20;
      pa.style.visibility = P !== 0 ? 'visible' : 'hidden';
      if (P > 0) { pa.setAttribute('x1', 382); pa.setAttribute('x2', 382 + len); }
      else       { pa.setAttribute('x1', 382 + len); pa.setAttribute('x2', 382); }
      __q('vw-p-lbl').textContent = 'P = ' + (P < 0 ? '\u2212' : '') + Math.abs(P) + ' kN';

      // plots
      __q('vw-nref').setAttribute('d', pathOf((xi) => YN(Ne(xi * L)), 100));
      __q('vw-npath').setAttribute('d', pathOf((xi) => YN(Nf(xi * L)), 100));
      __q('vw-ptarget').setAttribute('cy', YN(P));
      const ud = pathOf((xi) => YU(virt[vKey](xi, a)[0]), 200);
      __q('vw-upath').setAttribute('d', ud);
      __q('vw-ufill').setAttribute('d', ud + 'L' + X(1) + ',' + YU(0) + 'L' + X(0) + ',' + YU(0) + 'Z');
      const flag = __q('vw-bcflag');
      flag.setAttribute('cy', YU(du0));
      flag.style.visibility = Math.abs(du0) > 1e-12 ? 'visible' : 'hidden';

      // work densities: internal N·δε and external q·δu, with auto-scaled, labelled axis
      const NS_ = 400, fi = [], fe = [];
      for (let k = 0; k <= NS_; k++) {
        const x = k / NS_ * L, v = V(x);
        fi.push(Nf(x) * v[1]); fe.push(q * v[0]);
      }
      const DH = 96;
      const [dlo, dhi, dstep] = niceRange(Math.min(0, ...fi, ...fe), Math.max(0, ...fi, ...fe));
      const YD = (v) => (v - dlo) / (dhi - dlo) * DH;
      const dg = __q('vw-dgrid'), dt = __q('vw-dticks');
      clearG(dg); clearG(dt);
      const dec = dstep >= 1 ? 0 : Math.ceil(-Math.log10(dstep) - 1e-9);
      for (let v = dlo; v <= dhi + 1e-9; v += dstep) {
        const vv = Math.abs(v) < dstep * 1e-6 ? 0 : v;
        el('line', { x1: 0, y1: YD(vv), x2: PW, y2: YD(vv), stroke: vv === 0 ? 'var(--fg-muted)' : 'var(--grid)' }, dg);
        txt(dt, 54, 504 - YD(vv) + 3.5, (vv < 0 ? '\u2212' : '') + Math.abs(vv).toFixed(dec), 'end');
      }
      [0, 0.25, 0.5, 0.75, 1].forEach((xi) => el('line', { x1: X(xi), y1: 0, x2: X(xi), y2: DH, stroke: 'var(--grid)' }, dg));
      el('rect', { x: 0, y: 0, width: PW, height: DH, fill: 'none', stroke: 'var(--border)' }, dg);
      const dpath = (arr) => arr.map((v, k) => (k ? 'L' : 'M') + X(k / NS_).toFixed(2) + ',' + YD(v).toFixed(2)).join('');
      const close = 'L' + X(1) + ',' + YD(0) + 'L' + X(0) + ',' + YD(0) + 'Z';
      const pi_ = dpath(fi), pe_ = dpath(fe);
      __q('vw-dint').setAttribute('d', pi_); __q('vw-dint-fill').setAttribute('d', pi_ + close);
      __q('vw-dext').setAttribute('d', pe_); __q('vw-dext-fill').setAttribute('d', pe_ + close);

      // totals as bars on their own scale: int | distributed + tip (hatched)
      const Wdist = simpson((x) => q * V(x)[0]), Wtip = P * V(L)[0];
      const [blo, bhi] = niceRange(Math.min(0, Wint, Wdist, Wdist + Wtip), Math.max(0, Wint, Wdist, Wdist + Wtip));
      const YB = (v) => (v - blo) / (bhi - blo) * DH;
      const bar = (id, a, b) => {
        const r = __q(id);
        r.setAttribute('y', Math.min(YB(a), YB(b)));
        r.setAttribute('height', Math.abs(YB(b) - YB(a)));
      };
      bar('vw-bint', 0, Wint); bar('vw-bdist', 0, Wdist); bar('vw-btip', Wdist, Wdist + Wtip);
      __q('vw-bzero').setAttribute('y1', YB(0)); __q('vw-bzero').setAttribute('y2', YB(0));

      // readouts
      __q('vw-wint').textContent = fmt(Wint, 3);
      __q('vw-wext').textContent = fmt(Wext, 3);
      __q('vw-diff').textContent = fmt(diff, 3);
      __q('vw-wreac').textContent = fmt(Wreac, 3);

      const v = __q('vw-verdict');
      if (Math.abs(du0) > 1e-12) {
        v.className = 'verdict bad';
        v.textContent = 'Inadmissible δu: δu(0) ≠ 0, so the support reaction does work and ' +
          'W_int ≠ W_ext even for the equilibrium field. Choose a δu with δu(0) = 0.';
      } else if (Math.abs(diff) < TOL) {
        v.className = 'verdict ok';
        v.textContent = 'W_int = W_ext for this δu. Equilibrium requires this for every admissible δu — try another.';
      } else {
        v.className = 'verdict bad';
        v.textContent = 'W_int ≠ W_ext: this N(x) is not in equilibrium with the applied loads.';
      }
    }

    [qIn, pIn, aIn].forEach((e) => e.addEventListener('input', update));
    [nSel, vSel].forEach((e) => e.addEventListener('change', update));
    root.querySelectorAll('.presets button').forEach((b) => {
      b.addEventListener('click', () => {
        nSel.value = b.dataset.n;
        vSel.value = b.dataset.v;
        qIn.value = 10; pIn.value = 5; aIn.value = 0.5;
        update();
      });
    });

    update();
  })();
  </script>
</div>
```
