```{=html}
<style>
.viz-fls,
[data-bs-theme="light"] .viz-fls,
body.quarto-light .viz-fls {
  --fg: #1f2328; --fg-muted: #5b636d; --panel-bg: #f6f7f9; --border: #d4d8de;
  --grid: #e3e6ea; --slider: #3b6ea8;
  --disp: #0072B2; --ref: #6B7684; --ok: #00805E; --bad: #B8321A;
  --s1: #0072B2; --s2: #C98700; --s4: #CC79A7;
}
@media (prefers-color-scheme: dark) {
  .viz-fls {
    --fg: #e6e8eb; --fg-muted: #a0a8b3; --panel-bg: #1e2227; --border: #3a414a;
    --grid: #2c323a; --slider: #7fb0e6;
    --disp: #56B4E9; --ref: #9AA4B0; --ok: #3CC9A0; --bad: #FF7B6B;
    --s1: #5AA0F0; --s2: #F0B030; --s4: #E3A5C7;
  }
}
[data-bs-theme="dark"] .viz-fls,
body.quarto-dark .viz-fls {
  --fg: #e6e8eb; --fg-muted: #a0a8b3; --panel-bg: #1e2227; --border: #3a414a;
  --grid: #2c323a; --slider: #7fb0e6;
  --disp: #56B4E9; --ref: #9AA4B0; --ok: #3CC9A0; --bad: #FF7B6B;
  --s1: #5AA0F0; --s2: #F0B030; --s4: #E3A5C7;
}

.viz-fls { color: var(--fg); font-family: inherit; }
.viz-fls *, .viz-fls *::before, .viz-fls *::after { box-sizing: border-box; }
.viz-fls .intro { color: var(--fg-muted); font-size: .95em; margin: 0 0 .8em; }
.viz-fls .panel {
  padding: .8em; background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 6px; margin-bottom: .8em;
}
.viz-fls .controls { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .6em 1.2em; }
.viz-fls .ctrl label { display: block; font-size: .88em; color: var(--fg-muted); margin-bottom: .2em; }
.viz-fls .ctrl .val { color: var(--fg); font-variant-numeric: tabular-nums; }
.viz-fls .hrow { display: flex; gap: .5em; align-items: center; flex-wrap: wrap; }
.viz-fls input[type="range"] { flex: 1; min-width: 6em; accent-color: var(--slider); }
.viz-fls input[type="number"] {
  width: 6em; font: inherit; font-size: .9em; font-variant-numeric: tabular-nums;
  color: var(--fg); background: var(--panel-bg); border: 1px solid var(--border);
  border-radius: 4px; padding: .15em .3em;
}
.viz-fls select {
  flex: 1; min-width: 0; font: inherit; font-size: .9em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 4px; padding: .2em .3em;
}
.viz-fls button {
  font: inherit; font-size: .85em; color: var(--fg); background: var(--panel-bg);
  border: 1px solid var(--border); border-radius: 4px; padding: .25em .6em; cursor: pointer;
}
.viz-fls button:hover, .viz-fls button:focus-visible { border-color: var(--slider); }
.viz-fls button:disabled { opacity: .4; cursor: default; }
.viz-fls .steps { display: flex; gap: .3em; flex-wrap: wrap; margin-bottom: .6em; }
.viz-fls .steps button.on { border-color: var(--fg); font-weight: 600; }
.viz-fls .eqrow { display: flex; flex-wrap: wrap; gap: .5em 1.4em; align-items: center; justify-content: center; margin: .4em 0; }
.viz-fls .sys { display: flex; align-items: center; gap: .45em; }
.viz-fls .caption { font-size: .85em; color: var(--fg-muted); text-align: center; margin-bottom: .2em; }
.viz-fls table.mat {
  border-collapse: separate; border-spacing: 0; font-variant-numeric: tabular-nums;
  border-left: 2px solid var(--fg); border-right: 2px solid var(--fg); border-radius: 5px;
}
.viz-fls table.mat td { padding: .15em .5em; text-align: right; white-space: nowrap; border: none; }
.viz-fls table.mat td.struck { color: var(--fg-muted); text-decoration: line-through; opacity: .6; }
.viz-fls .e1 { color: var(--s1); font-weight: 600; }
.viz-fls .e2 { color: var(--s2); font-weight: 600; }
.viz-fls .steptxt { font-size: .92em; margin: .6em 0 0; }
.viz-fls .fig {
  background: var(--panel-bg); border: 1px solid var(--border); border-radius: 6px;
  padding: .5em; margin-bottom: .8em;
}
.viz-fls svg { display: block; width: 100%; height: auto; max-width: 460px; margin: 0 auto; }
.viz-fls svg text { fill: var(--fg-muted); font-size: 11px; font-family: inherit; }
.viz-fls #fls-handle { touch-action: none; cursor: grab; }
.viz-fls table.res { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; font-size: .92em; }
.viz-fls table.res td { padding: .3em .4em; border-bottom: 1px solid var(--grid); }
.viz-fls td.num { text-align: right; white-space: nowrap; }
.viz-fls .pass { color: var(--ok); }
.viz-fls .fail { color: var(--bad); }
.viz-fls .verdict { margin: .7em 0 .5em; font-weight: 600; }
.viz-fls .verdict.ok { color: var(--ok); }
.viz-fls .quiz { padding: .8em; background: var(--panel-bg); border: 1px solid var(--border); border-radius: 6px; margin: .8em 0; }
.viz-fls .quiz .qhead { font-size: .85em; color: var(--fg-muted); }
.viz-fls .quiz .qtext { margin: .3em 0 .6em; font-weight: 600; }
.viz-fls .quiz .qopts { display: flex; flex-direction: column; gap: .35em; }
.viz-fls .quiz .qopt { text-align: left; }
.viz-fls .quiz .qopt:disabled { cursor: default; opacity: 1; }
.viz-fls .quiz .qopt.correct { border-color: var(--ok); color: var(--ok); }
.viz-fls .quiz .qopt.wrong { border-color: var(--bad); color: var(--bad); }
.viz-fls .quiz .qfeedback, .viz-fls .quiz .qtry { margin: .6em 0 0; font-size: .92em; }
.viz-fls .quiz .qfeedback.ok { color: var(--ok); }
.viz-fls .quiz .qfeedback.bad { color: var(--bad); }
.viz-fls .quiz .qtry { color: var(--fg-muted); }
.viz-fls .quiz .qnav { display: flex; justify-content: space-between; margin-top: .7em; }
.viz-fls .note { font-size: .88em; color: var(--fg-muted); margin-top: .9em; }
.viz-fls .note p { margin: 0 0 .5em; }
@media (max-width: 560px) {
  .viz-fls .controls { grid-template-columns: 1fr; }
}
</style>

<div class="viz-fls">
  <p class="intro">The bar with two linear elements, solved the way an FE program does it:
  build the element matrices, assemble them, apply the support, eliminate, back-substitute.
  Step through the solve on the left; the plane below shows the same equations as lines.</p>

  <div class="panel">
    <div class="controls">
      <div class="ctrl">
        <label for="fls-load">Load case</label>
        <div class="hrow">
          <select id="fls-load">
            <option value="uniform">Uniform q</option>
            <option value="tri">Triangular q(x) = q₀·x/L</option>
          </select>
          <button type="button" id="fls-new">New loads</button>
        </div>
      </div>
      <div class="ctrl">
        <label>Current loads</label>
        <div class="val" id="fls-loadtxt"></div>
      </div>
    </div>
  </div>

  <div class="panel">
    <div class="steps" id="fls-steps"></div>
    <div id="fls-matrix"></div>
    <p class="steptxt" id="fls-steptxt"></p>
    <div class="hrow" style="justify-content:space-between;margin-top:.6em">
      <button type="button" id="fls-prev">Previous step</button>
      <button type="button" id="fls-next">Next step</button>
    </div>
  </div>

  <div class="fig">
    <svg id="fls-svg" viewBox="0 0 460 404" role="img"
         aria-label="The two equations of the reduced system as lines in the u1-u2 plane">
      <text x="8" y="14">u₂ [mm]</text>
      <g id="fls-ticks"></g>
      <g transform="translate(70,360) scale(1,-1)">
        <rect id="fls-bg" x="0" y="0" width="340" height="340" fill="transparent"></rect>
        <g id="fls-grid"></g>
        <line id="fls-l1" stroke="var(--s1)" stroke-width="2.4"></line>
        <line id="fls-l2" stroke="var(--s2)" stroke-width="2.4" stroke-dasharray="9 4"></line>
        <line id="fls-l2e" stroke="var(--s2)" stroke-width="2.4" stroke-dasharray="2 3"></line>
        <circle id="fls-sol" r="8" fill="none" stroke="var(--ref)" stroke-width="2" stroke-dasharray="3 2"></circle>
        <circle id="fls-pt" r="6" fill="var(--disp)" stroke="var(--panel-bg)" stroke-width="2"></circle>
        <circle id="fls-handle" r="18" fill="transparent" pointer-events="all"></circle>
      </g>
      <g id="fls-labels"></g>
      <text x="240" y="398" text-anchor="middle">u₁ [mm]</text>
    </svg>
  </div>

  <div class="panel">
    <div class="controls">
      <div class="ctrl">
        <label for="fls-u1">Trial u₁ [mm]</label>
        <div class="hrow">
          <input type="range" id="fls-u1" step="0.001">
          <input type="number" id="fls-u1-num" step="0.001" aria-label="u1 in mm">
        </div>
      </div>
      <div class="ctrl">
        <label for="fls-u2">Trial u₂ [mm]</label>
        <div class="hrow">
          <input type="range" id="fls-u2" step="0.001">
          <input type="number" id="fls-u2-num" step="0.001" aria-label="u2 in mm">
        </div>
      </div>
    </div>
    <table data-quarto-disable-processing="true" class="res" style="margin-top:.6em">
      <tr><td>Equation 1 residual (hat test φ₁): 4u₁ − 2u₂ − f₁</td><td class="num"><span id="fls-r1"></span> J</td></tr>
      <tr><td>Equation 2 residual (hat test φ₂): −2u₁ + 2u₂ − f₂</td><td class="num"><span id="fls-r2"></span> J</td></tr>
    </table>
    <div class="verdict" id="fls-verdict"></div>
  </div>

  <div class="quiz" id="fls-quiz"></div>

  <div class="note">
    <p>The bar has L = 1 m, EA = 1000 kN and two elements of length h = 0.5 m, so each element
    stiffness is EA/h = 2 kN/mm. Loads are integrated consistently, f<sub>j</sub> = ∫ q φ<sub>j</sub> dx,
    plus P at the tip. Each row of K u = f is one hat test: row j says the virtual work of
    φ<sub>j</sub> balances. In the plane, row j is a line, and a trial point lies on it exactly
    when that test balances; the solution is where the lines cross.</p>
    <p>Assembled without the support, K is singular: moving every node by the same amount stretches
    nothing, so K·(1, 1, 1) = 0. The support u₀ = 0 removes that rigid-body motion. Its row and
    column are struck out; the struck row is not lost, it gives the unknown reaction R once u is
    known.</p>
    <p>Forward elimination replaces equation 2 by equation 2 + ½·equation 1. That is a different
    line through the same intersection, one that no longer involves u₁, so u₂ can be read off
    directly; back-substitution then gives u₁. For n elements K is tridiagonal and the same two
    sweeps solve it in a number of operations proportional to n. This direct solve is what FE codes
    do for linear problems; iterative solvers and Newton's method for nonlinear problems are beyond
    this course. The same intersection is also where the potential energy ½uᵀKu − fᵀu is smallest.</p>
    <p>Nodal values move in steps of 0.001 mm; a residual counts as zero below 0.015 J. Drag the
    point or tap the plane to move it.</p>
  </div>

  <script>
  (function () {
    const root = (document.currentScript && document.currentScript.closest('.viz-fls')) || document.querySelector('.viz-fls');
    if (!root) return;
    const __q = (id) => root.querySelector('#' + id);
    const NS = 'http://www.w3.org/2000/svg';
    const TOL = 0.015, H = 15, PS = 340, SC = PS / (2 * H);
    const k = 2;                              // EA/h in kN/mm for h = 0.5 m
    const STEPS = ['Element matrices', 'Assemble', 'Apply u₀ = 0', 'Eliminate', 'Back-substitute'];
    let q = 10, P = 5, step = 0, lo1 = 0, lo2 = 0;
    const loadSel = __q('fls-load');
    const U1 = __q('fls-u1'), U2 = __q('fls-u2'), N1 = __q('fls-u1-num'), N2 = __q('fls-u2-num');

    function el(tag, attrs, parent) {
      const e = document.createElementNS(NS, tag);
      for (const a in attrs) e.setAttribute(a, attrs[a]);
      if (parent) parent.appendChild(e);
      return e;
    }
    function txt(parent, x, y, s, anchor) {
      const t = el('text', { x: x, y: y, 'text-anchor': anchor || 'middle' }, parent);
      t.textContent = s;
      return t;
    }
    const clear = (g) => { while (g.firstChild) g.removeChild(g.firstChild); };
    const sgn = (v) => (v < 0 ? '\u2212' + (-v) : String(v));
    function fmt(v, d) {
      if (Math.abs(v) < 0.5 * Math.pow(10, -d)) v = 0;
      return (v < 0 ? '\u2212' : '\u00A0') + Math.abs(v).toFixed(d);
    }
    function num(v) {                          // compact number for matrix entries
      if (Math.abs(v) < 5e-4) v = 0;
      let s = Math.abs(v).toFixed(3).replace(/0+$/, '').replace(/\.$/, '');
      return (v < 0 ? '\u2212' : '') + s;
    }

    // ---- element data ----
    function elements() {
      const tri = loadSel.value === 'tri', h = 0.5, qOf = (x) => (tri ? q * x : q);
      return [1, 2].map((e) => {
        const qa = qOf((e - 1) * h), qb = qOf(e * h);
        return { nodes: [e - 1, e], f: [h * (2 * qa + qb) / 6, h * (qa + 2 * qb) / 6] };
      });
    }
    function system() {
      const E = elements();
      const f0 = E[0].f[0], f1 = E[0].f[1] + E[1].f[0], f2 = E[1].f[1] + P;
      // reduced system [[2k, -k], [-k, k]] u = [f1, f2]
      const f2e = f2 + 0.5 * f1;               // row 2 + ½ row 1 → k/2 · u2 ... with k = 2: 1·u2
      const u2 = f2e / (k - k / 2);
      const u1 = (f1 + k * u2) / (2 * k);
      const R = -k * u1 - f0;                  // struck row 0: k u0 − k u1 = f0 + R, u0 = 0
      return { E: E, f0: f0, f1: f1, f2: f2, f2e: f2e, u1: u1, u2: u2, R: R };
    }

    // ---- matrix panel ----
    const C1 = (s) => '<span class="e1">' + s + '</span>';
    const C2 = (s) => '<span class="e2">' + s + '</span>';
    function mat(rows, struck) {
      return '<table data-quarto-disable-processing="true" class="mat">' + rows.map((r, i) => '<tr>' + r.map((c, j) =>
        '<td' + (struck && (i === 0 || j === 0) ? ' class="struck"' : '') + '>' + c + '</td>').join('') + '</tr>').join('') + '</table>';
    }
    const sys = (K, u, f, caption, struck) =>
      '<div><div class="caption">' + caption + '</div><div class="sys">' + mat(K, struck) + mat(u.map((x) => [x]), struck) +
      '<span>=</span>' + mat(f.map((x) => [x]), struck) + '</div></div>';

    function renderMatrix(S) {
      const m = __q('fls-matrix'), t = __q('fls-steptxt');
      const kk = String(k), mk = '\u2212' + k;
      const [a, b] = [S.E[0].f, S.E[1].f];
      if (step === 0) {
        m.innerHTML = '<div class="eqrow">' +
          sys([[C1(kk), C1(mk)], [C1(mk), C1(kk)]], ['u₀', 'u₁'], [C1(num(a[0])), C1(num(a[1]))], 'Element 1, nodes 0–1') +
          sys([[C2(kk), C2(mk)], [C2(mk), C2(kk)]], ['u₁', 'u₂'], [C2(num(b[0])), C2(num(b[1]))], 'Element 2, nodes 1–2') + '</div>';
        t.textContent = 'Each element has stiffness EA/h = 2 kN/mm and shares its load between its two nodes. ' +
          'Both matrices are the same; only the node numbers differ.';
      } else if (step === 1 || step === 2) {
        const K = [[C1(kk) + '⁽¹⁾', C1(mk) + '⁽¹⁾', '0'],
                   [C1(mk) + '⁽¹⁾', C1(kk) + '⁽¹⁾ + ' + C2(kk) + '⁽²⁾', C2(mk) + '⁽²⁾'],
                   ['0', C2(mk) + '⁽²⁾', C2(kk) + '⁽²⁾']];
        const f = [C1(num(a[0])) + ' + R', C1(num(a[1])) + ' + ' + C2(num(b[0])), C2(num(b[1])) + ' + P'];
        m.innerHTML = '<div class="eqrow">' + sys(K, ['u₀', 'u₁', 'u₂'], f, step === 1 ? 'Assembled system' : 'Support at node 0: u₀ = 0', step === 2) + '</div>';
        t.textContent = step === 1
          ? 'Entries are added where the elements share node 1 (superscripts show the element). R is the unknown support reaction. ' +
            'This K is singular: moving all nodes together, u = (1, 1, 1), gives K u = 0, a rigid-body motion with no stretch.'
          : 'u₀ = 0 is known, so row 0 and column 0 leave the system. The 2×2 system that remains is solvable; ' +
            'its two rows are the two lines in the plane. Row 0 is kept aside for the reaction.';
      } else if (step === 3) {
        m.innerHTML = '<div class="eqrow">' +
          sys([['4', mk], [mk, kk]], ['u₁', 'u₂'], [num(S.f1), num(S.f2)], 'Reduced system') +
          sys([['4', mk], ['0', '1']], ['u₁', 'u₂'], [num(S.f1), num(S.f2e)], 'After row 2 ← row 2 + ½·row 1') + '</div>';
        t.textContent = 'Adding half of equation 1 to equation 2 removes u₁ from it. In the plane, the dashed line is replaced by ' +
          'the dotted one: a different line through the same intersection, now horizontal.';
      } else {
        m.innerHTML = '<div class="eqrow">' +
          sys([['4', mk], ['0', '1']], [num(S.u1), num(S.u2)], [num(S.f1), num(S.f2e)], 'Solved') + '</div>';
        t.textContent = 'Back-substitution: u₂ = ' + num(S.u2) + ' mm from the last row, then u₁ = (' + num(S.f1) + ' + 2·' + num(S.u2) +
          ') / 4 = ' + num(S.u1) + ' mm. The struck row 0 now gives the reaction: R = −2u₁ − f₀ = ' + num(S.R) +
          ' kN, which balances the total load (P + ∫q dx = ' + num(-S.R) + ' kN).';
      }
      __q('fls-steps').querySelectorAll('button').forEach((b, i) => b.classList.toggle('on', i === step));
      __q('fls-prev').disabled = step === 0;
      __q('fls-next').disabled = step === STEPS.length - 1;
    }

    // ---- plane ----
    const X = (u1) => (u1 - lo1) * SC, Y = (u2) => (u2 - lo2) * SC;
    function setWindow(S) {
      lo1 = Math.round(S.u1 / 5) * 5 - H;
      lo2 = Math.round(S.u2 / 5) * 5 - H;
      [[U1, N1, lo1], [U2, N2, lo2]].forEach(([r, n, lo]) => { r.min = n.min = lo; r.max = n.max = lo + 2 * H; });
    }
    function clip(a, b, c) {                   // line a·u1 + b·u2 = c inside the window
      const pts = [], A0 = lo1, A1 = lo1 + 2 * H, B0 = lo2, B1 = lo2 + 2 * H;
      if (Math.abs(b) > 1e-12) [A0, A1].forEach((u1) => { const u2 = (c - a * u1) / b; if (u2 >= B0 - 1e-9 && u2 <= B1 + 1e-9) pts.push([u1, u2]); });
      if (Math.abs(a) > 1e-12) [B0, B1].forEach((u2) => { const u1 = (c - b * u2) / a; if (u1 >= A0 - 1e-9 && u1 <= A1 + 1e-9) pts.push([u1, u2]); });
      if (pts.length < 2) return null;
      let best = [pts[0], pts[1]], dmax = -1;
      for (let i = 0; i < pts.length; i++) for (let j = i + 1; j < pts.length; j++) {
        const d = (pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2;
        if (d > dmax) { dmax = d; best = [pts[i], pts[j]]; }
      }
      return best;
    }
    function drawLine(id, seg, show, label, lab) {
      const l = __q(id);
      if (!seg || !show) { l.style.visibility = 'hidden'; return; }
      l.style.visibility = 'visible';
      l.setAttribute('x1', X(seg[0][0])); l.setAttribute('y1', Y(seg[0][1]));
      l.setAttribute('x2', X(seg[1][0])); l.setAttribute('y2', Y(seg[1][1]));
      const e = seg[0][0] > seg[1][0] ? seg[0] : seg[1], o = e === seg[0] ? seg[1] : seg[0];
      const len = Math.hypot(X(e[0]) - X(o[0]), Y(e[1]) - Y(o[1])) || 1;
      const px = X(e[0]) - (X(e[0]) - X(o[0])) / len * 30, py = Y(e[1]) - (Y(e[1]) - Y(o[1])) / len * 30;
      const t = txt(lab, 70 + px, 360 - py - 7, label.text, 'end');
      t.setAttribute('style', 'fill:' + label.color + ';font-weight:600');
    }

    function update() {
      const S = system(), u = [+U1.value, +U2.value];
      N1.value = u[0].toFixed(3); N2.value = u[1].toFixed(3);
      __q('fls-loadtxt').textContent = (loadSel.value === 'tri' ? 'q₀ = ' : 'q = ') + q + ' kN/m, P = ' + sgn(P) + ' kN';
      renderMatrix(S);

      const g = __q('fls-grid'), tk = __q('fls-ticks'), lab = __q('fls-labels');
      clear(g); clear(tk); clear(lab);
      for (let t = 0; t <= 2 * H; t += 5) {
        el('line', { x1: t * SC, y1: 0, x2: t * SC, y2: PS, stroke: 'var(--grid)' }, g);
        el('line', { x1: 0, y1: t * SC, x2: PS, y2: t * SC, stroke: 'var(--grid)' }, g);
        txt(tk, 70 + t * SC, 376, sgn(lo1 + t));
        txt(tk, 64, 360 - t * SC + 3.5, sgn(lo2 + t), 'end');
      }
      el('rect', { x: 0, y: 0, width: PS, height: PS, fill: 'none', stroke: 'var(--border)' }, g);

      const lines = step >= 2;
      drawLine('fls-l1', clip(4, -2, S.f1), lines, { text: 'eq. 1 (φ₁)', color: 'var(--s1)' }, lab);
      drawLine('fls-l2', clip(-2, 2, S.f2), lines, { text: step >= 3 ? 'eq. 2 before' : 'eq. 2 (φ₂)', color: 'var(--s2)' }, lab);
      drawLine('fls-l2e', clip(0, 1, S.f2e), step >= 3, { text: 'eq. 2 after elimination', color: 'var(--s2)' }, lab);
      __q('fls-l2').setAttribute('stroke-opacity', step >= 3 ? 0.45 : 1);
      const so = __q('fls-sol');
      so.setAttribute('cx', X(S.u1)); so.setAttribute('cy', Y(S.u2));
      so.style.visibility = step >= 4 ? 'visible' : 'hidden';
      if (!lines) txt(lab, 240, 190, 'The two equations appear here once u₀ = 0 is applied (step 3).');

      ['fls-pt', 'fls-handle'].forEach((id) => { __q(id).setAttribute('cx', X(u[0])); __q(id).setAttribute('cy', Y(u[1])); });

      const r = [4 * u[0] - 2 * u[1] - S.f1, -2 * u[0] + 2 * u[1] - S.f2];
      r.forEach((v, i) => {
        const ok = Math.abs(v) < TOL, e = __q('fls-r' + (i + 1));
        e.textContent = (ok ? '\u2713 ' : '\u2717 ') + fmt(v, 3);
        e.className = ok ? 'pass' : 'fail';
      });
      const both = r.every((v) => Math.abs(v) < TOL), vd = __q('fls-verdict');
      vd.className = both ? 'verdict ok' : 'verdict';
      vd.textContent = both ? 'The point lies on both lines: it solves K u = f, and both hat tests balance.'
        : Math.abs(r[0]) < TOL ? 'On line 1 only: test φ₁ balances, φ₂ does not.'
        : Math.abs(r[1]) < TOL ? 'On line 2 only: test φ₂ balances, φ₁ does not.'
        : 'On neither line: neither hat test balances.';
    }

    // ---- interaction ----
    STEPS.forEach((name, i) => {
      const b = document.createElement('button');
      b.type = 'button'; b.textContent = (i + 1) + '. ' + name;
      b.addEventListener('click', () => { step = i; update(); });
      __q('fls-steps').appendChild(b);
    });
    __q('fls-prev').addEventListener('click', () => { step = Math.max(0, step - 1); update(); });
    __q('fls-next').addEventListener('click', () => { step = Math.min(STEPS.length - 1, step + 1); update(); });

    const svg = __q('fls-svg'), handle = __q('fls-handle');
    function moveTo(evt) {
      const pt = svg.createSVGPoint();
      pt.x = evt.clientX; pt.y = evt.clientY;
      const p = pt.matrixTransform(svg.getScreenCTM().inverse());
      U1.value = lo1 + (p.x - 70) / SC;
      U2.value = lo2 + (360 - p.y) / SC;
      update();
    }
    let dragging = false;
    handle.addEventListener('pointerdown', (e) => { dragging = true; handle.setPointerCapture(e.pointerId); e.preventDefault(); });
    handle.addEventListener('pointermove', (e) => { if (dragging) moveTo(e); });
    handle.addEventListener('pointerup', () => { dragging = false; });
    handle.addEventListener('pointercancel', () => { dragging = false; });
    __q('fls-bg').addEventListener('click', moveTo);
    [U1, U2].forEach((r) => r.addEventListener('input', update));
    [[U1, N1], [U2, N2]].forEach(([r, n]) => n.addEventListener('change', () => {
      const v = parseFloat(n.value);
      if (isFinite(v)) r.value = v;
      update();
    }));
    function newCase() {
      const S = system();
      setWindow(S);
      U1.value = Math.round(S.u1) + 4;
      U2.value = Math.round(S.u2) - 3;
      update();
    }
    loadSel.addEventListener('change', newCase);
    __q('fls-new').addEventListener('click', () => {
      q = 4 + Math.floor(Math.random() * 17);
      P = -10 + Math.floor(Math.random() * 31);
      newCase();
    });

    // ---- predict-first quiz ----
    const QUIZ = [
      { q: 'Before the support is applied, the assembled 3×3 K is singular. Why?',
        options: ['Rounding errors in the entries', 'Without a support the bar can move as a rigid body, which costs no strain energy', 'The loads have not been added yet'],
        answer: 1,
        explain: 'Moving all nodes by the same amount stretches no element, so K·(1, 1, 1) = 0. Fixing u₀ removes that motion.',
        check: 'on step 2, add up each row of K: every row sums to zero.' },
      { q: 'The trial point lies on the line of equation 1 but not on equation 2. Which hat test balances?',
        options: ['φ₁ only', 'φ₂ only', 'Both', 'Neither'],
        answer: 0,
        explain: 'Row j of K u = f is the virtual-work balance of the hat test φⱼ, so lying on line j means test j balances.',
        check: 'from step 3 on, drag the point onto one line and read the two residuals.' },
      { q: 'Forward elimination replaces equation 2 with equation 2 + ½·equation 1. Does the solution move?',
        options: ['Yes, a little', 'No: the new line passes through the same intersection', 'Only for the triangular load'],
        answer: 1,
        explain: 'Any point satisfying both original equations also satisfies their combination. Elimination changes the lines, never the solution.',
        check: 'go to step 4: the dotted line crosses the others at the same point.' },
      { q: 'You press "New loads". What changes in the linear system?',
        options: ['K and f', 'Only f, and with it the solution', 'Only K'],
        answer: 1,
        explain: 'K depends on EA and the mesh only. In the plane the lines keep their slopes and just shift.',
        check: 'on step 3 or 4, press "New loads" and compare the matrices and line directions.' },
      { q: 'What does the struck-out row 0 give once u is known?',
        options: ['Nothing, it is discarded', 'The support reaction R', 'The tip load P'],
        answer: 1,
        explain: 'Row 0 still holds: 2u₀ − 2u₁ = f₀ + R. With u known it gives R, which balances the total applied load.',
        check: 'step 5 shows R next to P + ∫q dx.' },
    ];
    function makeQuiz(box, Q) {
      const chosen = Q.map(() => -1);
      let i = 0;
      function render() {
        const it = Q[i], c = chosen[i];
        let html = '<div class="qhead">Predict first: question ' + (i + 1) + ' of ' + Q.length + '</div>' +
          '<p class="qtext">' + it.q + '</p><div class="qopts">';
        it.options.forEach((o, j) => {
          let cls = '', mark = '';
          if (c >= 0 && j === it.answer) { cls = ' correct'; mark = '\u2713 '; }
          else if (c >= 0 && j === c) { cls = ' wrong'; mark = '\u2717 '; }
          html += '<button type="button" class="qopt' + cls + '" data-i="' + j + '"' + (c >= 0 ? ' disabled' : '') + '>' + mark + o + '</button>';
        });
        html += '</div>';
        if (c >= 0) {
          html += '<p class="qfeedback ' + (c === it.answer ? 'ok' : 'bad') + '">' + (c === it.answer ? 'Right. ' : 'Not quite. ') + it.explain + '</p>' +
                  '<p class="qtry">Check it: ' + it.check + '</p>';
        }
        html += '<div class="qnav"><button type="button" data-nav="-1"' + (i === 0 ? ' disabled' : '') + '>Previous</button>' +
                '<button type="button" data-nav="1"' + (i === Q.length - 1 ? ' disabled' : '') + '>Next question</button></div>';
        box.innerHTML = html;
        box.querySelectorAll('.qopt').forEach((b) => b.addEventListener('click', () => { chosen[i] = +b.dataset.i; render(); }));
        box.querySelectorAll('[data-nav]').forEach((b) => b.addEventListener('click', () => { i += +b.dataset.nav; render(); }));
      }
      render();
    }
    makeQuiz(__q('fls-quiz'), QUIZ);

    newCase();
  })();
  </script>
</div>
```
