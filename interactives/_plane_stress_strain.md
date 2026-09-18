```{=html}
<style>
/* ---- tokens: light, media-dark, attribute-dark (GUIDELINES §2 order) ---- */
.viz-planestress,
[data-bs-theme="light"] .viz-planestress,
body.quarto-light .viz-planestress {
  --ps-fg: #1a1a1a;
  --ps-fg-muted: #6b6b6b;
  --ps-panel-bg: #f4f4f6;
  --ps-border: #d8d8d8;
  --ps-slider: #6b3fa0;
  --ps-block-fill: rgba(90, 130, 200, 0.14);
  --ps-block-stroke: #3a3a3a;
  --ps-wall: #8a8a8a;
  --ps-tension: #c0392b;
  --ps-compression: #2166ac;
  --ps-accent: #6b3fa0;
}

@media (prefers-color-scheme: dark) {
  .viz-planestress {
    --ps-fg: #e8e8e8;
    --ps-fg-muted: #a0a0a0;
    --ps-panel-bg: #26272b;
    --ps-border: #3a3b3e;
    --ps-slider: #b18fd6;
    --ps-block-fill: rgba(120, 160, 230, 0.18);
    --ps-block-stroke: #cfcfcf;
    --ps-wall: #9a9a9a;
    --ps-tension: #e07a6e;
    --ps-compression: #6fa8dc;
    --ps-accent: #b18fd6;
  }
}

[data-bs-theme="dark"] .viz-planestress,
body.quarto-dark .viz-planestress {
  --ps-fg: #e8e8e8;
  --ps-fg-muted: #a0a0a0;
  --ps-panel-bg: #26272b;
  --ps-border: #3a3b3e;
  --ps-slider: #b18fd6;
  --ps-block-fill: rgba(120, 160, 230, 0.18);
  --ps-block-stroke: #cfcfcf;
  --ps-wall: #9a9a9a;
  --ps-tension: #e07a6e;
  --ps-compression: #6fa8dc;
  --ps-accent: #b18fd6;
}

/* ---- layout ---- */
.viz-planestress {
  font-family: inherit;
  color: var(--ps-fg);
  font-variant-numeric: tabular-nums;
}
.viz-planestress *,
.viz-planestress *::before,
.viz-planestress *::after { box-sizing: border-box; }

.viz-planestress .ps-subtitle {
  font-size: 0.85rem;
  color: var(--ps-fg-muted);
  margin: 0 0 0.9rem;
}

.viz-planestress .ps-controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0.9rem 1.4rem;
  padding: 0.9rem 1rem;
  background: var(--ps-panel-bg);
  border: 1px solid var(--ps-border);
  border-radius: 10px;
  margin-bottom: 0.8rem;
}
.viz-planestress .ps-control label {
  display: flex;
  justify-content: space-between;
  gap: 0.5rem;
  font-size: 0.85rem;
  margin-bottom: 0.25rem;
  cursor: pointer;
}
.viz-planestress .ps-control label .ps-val {
  color: var(--ps-accent);
  font-weight: 600;
}
.viz-planestress .ps-control input[type="range"] {
  width: 100%;
  accent-color: var(--ps-slider);
}

.viz-planestress .ps-presets {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.1rem;
}
.viz-planestress .ps-presets button {
  font: inherit;
  font-size: 0.78rem;
  color: var(--ps-fg);
  background: var(--ps-panel-bg);
  border: 1px solid var(--ps-border);
  border-radius: 999px;
  padding: 0.25rem 0.7rem;
  cursor: pointer;
}
.viz-planestress .ps-presets button:hover {
  border-color: var(--ps-accent);
  color: var(--ps-accent);
}

.viz-planestress .ps-panels {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
  justify-content: center;
}
.viz-planestress .ps-panel {
  flex: 1 1 300px;
  max-width: 400px;
  border: 1px solid var(--ps-border);
  border-radius: 10px;
  padding: 0.8rem 0.9rem 0.9rem;
}
.viz-planestress .ps-panel h4 {
  margin: 0 0 0.15rem;
  font-size: 0.95rem;
}
.viz-planestress .ps-panel .ps-sub {
  margin: 0 0 0.5rem;
  font-size: 0.78rem;
  color: var(--ps-fg-muted);
}
.viz-planestress svg {
  width: 100%;
  height: auto;
  max-width: 460px;
  display: block;
  margin: 0 auto;
}
.viz-planestress .ps-block {
  fill: var(--ps-block-fill);
  stroke: var(--ps-block-stroke);
  stroke-width: 2;
}
.viz-planestress .ps-wallhatch {
  stroke: var(--ps-wall);
  stroke-width: 2;
}
.viz-planestress .ps-thickbar {
  fill: var(--ps-block-fill);
  stroke: var(--ps-block-stroke);
  stroke-width: 1.5;
}
.viz-planestress .ps-readout {
  margin-top: 0.4rem;
  font-size: 0.86rem;
  text-align: center;
}
.viz-planestress .ps-readout .ps-eqline {
  font-weight: 600;
  color: var(--ps-accent);
}
.viz-planestress .ps-note {
  margin-top: 1rem;
  font-size: 0.78rem;
  color: var(--ps-fg-muted);
  line-height: 1.55;
}
</style>

<div class="viz-planestress">

  <p class="ps-subtitle">
    The same in-plane stress state, under two different assumptions about the third
    direction. Plane stress lets the out-of-plane direction move freely; plane strain
    holds it fixed. Drag the sliders and watch what each one gives up.
  </p>

  <div class="ps-controls">
    <div class="ps-control">
      <label for="ps-s11"><span>&sigma;<sub>11</sub></span> <span class="ps-val"><span id="ps-s11-val">100</span> MPa</span></label>
      <input type="range" id="ps-s11" min="-100" max="100" step="5" value="100">
    </div>
    <div class="ps-control">
      <label for="ps-s22"><span>&sigma;<sub>22</sub></span> <span class="ps-val"><span id="ps-s22-val">0</span> MPa</span></label>
      <input type="range" id="ps-s22" min="-100" max="100" step="5" value="0">
    </div>
    <div class="ps-control">
      <label for="ps-nu"><span>&nu;</span> <span class="ps-val" id="ps-nu-val">0.30</span></label>
      <input type="range" id="ps-nu" min="0" max="0.49" step="0.01" value="0.30">
    </div>
    <div class="ps-control">
      <label for="ps-e"><span>E</span> <span class="ps-val"><span id="ps-e-val">200</span> GPa</span></label>
      <input type="range" id="ps-e" min="10" max="300" step="5" value="200">
    </div>
  </div>

  <div class="ps-presets">
    <button type="button" id="ps-preset-1">Uniaxial, &nu; = 0.3</button>
    <button type="button" id="ps-preset-2">&nu; = 0</button>
    <button type="button" id="ps-preset-3">&sigma;<sub>11</sub> + &sigma;<sub>22</sub> = 0</button>
    <button type="button" id="ps-preset-4">Equibiaxial, &nu; = 0.49</button>
    <button type="button" id="ps-preset-5">Uniaxial, E = 70 GPa</button>
  </div>

  <div class="ps-panels">

    <!-- ============ PLANE STRESS ============ -->
    <div class="ps-panel">
      <h4>Plane stress</h4>
      <p class="ps-sub">thin plate, stress-free faces (&sigma;<sub>33</sub> = 0)</p>
      <svg viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <marker id="ps-a-tip-t" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="var(--ps-tension)"></path>
          </marker>
          <marker id="ps-a-tip-c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="var(--ps-compression)"></path>
          </marker>
        </defs>
        <rect class="ps-block" x="60" y="50" width="80" height="80"></rect>
        <line id="ps-a-arrow-left"   x1="60"  y1="90"  x2="30"  y2="90"  stroke-width="3"></line>
        <line id="ps-a-arrow-right"  x1="140" y1="90"  x2="170" y2="90"  stroke-width="3"></line>
        <line id="ps-a-arrow-top"    x1="100" y1="50"  x2="100" y2="20"  stroke-width="3"></line>
        <line id="ps-a-arrow-bottom" x1="100" y1="130" x2="100" y2="160" stroke-width="3"></line>
        <text x="100" y="190" text-anchor="middle" font-size="8.5" fill="var(--ps-fg-muted)">out-of-plane thickness (exaggerated)</text>
        <rect id="ps-thickbar" class="ps-thickbar" x="70" y="200" width="60" height="12"></rect>
        <text id="ps-a-clampflag" x="100" y="232" text-anchor="middle" font-size="8" fill="var(--ps-accent)"></text>
      </svg>
      <div class="ps-readout">
        &epsilon;<sub>33</sub> = <span class="ps-eqline" id="ps-eps33-val">0</span> &times;10<sup>&minus;6</sup>
      </div>
    </div>

    <!-- ============ PLANE STRAIN ============ -->
    <div class="ps-panel">
      <h4>Plane strain</h4>
      <p class="ps-sub">long body, axially restrained (&epsilon;<sub>33</sub> = 0)</p>
      <svg viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <marker id="ps-b-tip-t" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="var(--ps-tension)"></path>
          </marker>
          <marker id="ps-b-tip-c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="var(--ps-compression)"></path>
          </marker>
        </defs>
        <rect class="ps-block" x="60" y="50" width="80" height="80"></rect>
        <line id="ps-b-arrow-left"   x1="60"  y1="90"  x2="30"  y2="90"  stroke-width="3"></line>
        <line id="ps-b-arrow-right"  x1="140" y1="90"  x2="170" y2="90"  stroke-width="3"></line>
        <line id="ps-b-arrow-top"    x1="100" y1="50"  x2="100" y2="20"  stroke-width="3"></line>
        <line id="ps-b-arrow-bottom" x1="100" y1="130" x2="100" y2="160" stroke-width="3"></line>
        <g transform="translate(100,90)">
          <circle r="12" fill="none" stroke="var(--ps-block-stroke)" stroke-width="1.5"></circle>
          <circle id="ps-out-dot" r="3.5" fill="var(--ps-tension)"></circle>
          <g id="ps-out-cross" stroke="var(--ps-compression)" stroke-width="2">
            <line x1="-6" y1="-6" x2="6" y2="6"></line>
            <line x1="-6" y1="6"  x2="6" y2="-6"></line>
          </g>
        </g>
        <text x="100" y="158" text-anchor="middle" font-size="8" fill="var(--ps-fg-muted)">&#8857; out of page &nbsp;/&nbsp; &#8855; into page</text>

        <text x="100" y="170" text-anchor="middle" font-size="8.5" fill="var(--ps-fg-muted)">side view along the axis</text>
        <rect id="ps-sv-ghost" x="40" y="176" width="120" height="8" fill="none"
              stroke="var(--ps-fg-muted)" stroke-width="1.2" stroke-dasharray="4,3"></rect>
        <g class="ps-wallhatch">
          <line x1="36" y1="188" x2="36" y2="216"></line>
          <line x1="30" y1="192" x2="36" y2="188"></line>
          <line x1="30" y1="201" x2="36" y2="197"></line>
          <line x1="30" y1="210" x2="36" y2="206"></line>
          <line x1="164" y1="188" x2="164" y2="216"></line>
          <line x1="170" y1="192" x2="164" y2="188"></line>
          <line x1="170" y1="201" x2="164" y2="197"></line>
          <line x1="170" y1="210" x2="164" y2="206"></line>
        </g>
        <rect class="ps-thickbar" x="40" y="191" width="120" height="22"></rect>
        <line id="ps-sv-reaction-l" x1="95"  y1="202" x2="75"  y2="202" stroke-width="2.5"></line>
        <line id="ps-sv-reaction-r" x1="105" y1="202" x2="125" y2="202" stroke-width="2.5"></line>
        <text x="100" y="226" text-anchor="middle" font-size="7.5" fill="var(--ps-fg-muted)">dashed = length it would take if free to move axially</text>
        <text id="ps-b-clampflag" x="100" y="234" text-anchor="middle" font-size="8" fill="var(--ps-accent)"></text>
      </svg>
      <div class="ps-readout">
        &sigma;<sub>33</sub> = <span class="ps-eqline" id="ps-sig33-val">0</span> MPa
      </div>
    </div>

  </div>

  <p class="ps-note">
    <strong>Notes.</strong>
    Linearised (small-strain) elasticity throughout: &epsilon;<sub>33</sub> =
    &minus;(&nu;/E)(&sigma;<sub>11</sub>+&sigma;<sub>22</sub>) and
    &sigma;<sub>33</sub> = &nu;(&sigma;<sub>11</sub>+&sigma;<sub>22</sub>), with no shear
    component in either panel.
    Both out-of-plane effects are drawn at &times;1000 exaggeration &mdash; real strains here are
    of order 10<sup>&minus;4</sup> and would be invisible at true scale.
    The thickness bar and the dashed free length are <em>drawn</em> within a fixed box; when a
    state runs past it the figure says so and switches to a dashed outline, but the readouts
    below always report the true value.
    The dashed length is the same material at the same in-plane stress with the axial
    constraint released &mdash; a thought experiment, not a second physical body.
    The restraint is idealised as bonded: it both pushes and pulls, so
    &sigma;<sub>33</sub> can be tensile. A smooth rigid wall could only push.
  </p>

<script>
(function () {
  const root = document.querySelector('.viz-planestress');
  if (!root) return;
  const __q = (id) => root.querySelector('#' + id);

  const s11In = __q('ps-s11');
  const s22In = __q('ps-s22');
  const nuIn  = __q('ps-nu');
  const eIn   = __q('ps-e');

  const K = 1000;                       // drawing exaggeration, stated in the .note
  // ONE draw factor shared by both panels, so they saturate at the same state.
  // Bounds set by whichever figure runs out of room first (the ghost strip).
  const FAC_LO = 0.35, FAC_HI = 1.45;

  // snap -0 and float dust to a clean zero (GUIDELINES §7)
  const snap = (x, eps) => (Math.abs(x) < eps ? 0 : x);
  // pad positives with U+00A0 so the sign column does not drift
  const signed = (x, dp) => (x > 0 ? '\u00A0' : '') + x.toFixed(dp);

  function setArrow(panel, side, stress) {
    const el = __q('ps-' + panel + '-arrow-' + side);
    if (!el) return;
    if (stress === 0) { el.style.display = 'none'; return; }
    el.style.display = '';
    const tension = stress > 0;
    const len = 10 + 30 * Math.min(Math.abs(stress) / 100, 1);
    el.setAttribute('stroke', tension ? 'var(--ps-tension)' : 'var(--ps-compression)');
    el.setAttribute('marker-end', 'url(#ps-' + panel + '-tip-' + (tension ? 't' : 'c') + ')');
    let x1, y1, x2, y2;
    if (side === 'left')        { [x1,y1,x2,y2] = tension ? [60,90,60-len,90]   : [60-len,90,60,90]; }
    else if (side === 'right')  { [x1,y1,x2,y2] = tension ? [140,90,140+len,90] : [140+len,90,140,90]; }
    else if (side === 'top')    { [x1,y1,x2,y2] = tension ? [100,50,100,50-len] : [100,50-len,100,50]; }
    else                        { [x1,y1,x2,y2] = tension ? [100,130,100,130+len] : [100,130+len,100,130]; }
    el.setAttribute('x1', x1); el.setAttribute('y1', y1);
    el.setAttribute('x2', x2); el.setAttribute('y2', y2);
  }

  function update() {
    const s11   = parseFloat(s11In.value);
    const s22   = parseFloat(s22In.value);
    const nu    = parseFloat(nuIn.value);
    const E_GPa = parseFloat(eIn.value);
    const E_MPa = E_GPa * 1000;

    __q('ps-s11-val').textContent = s11.toFixed(0);
    __q('ps-s22-val').textContent = s22.toFixed(0);
    __q('ps-nu-val').textContent  = nu.toFixed(2);
    __q('ps-e-val').textContent   = E_GPa.toFixed(0);

    ['a', 'b'].forEach((p) => {
      setArrow(p, 'left', s11);  setArrow(p, 'right', s11);
      setArrow(p, 'top', s22);   setArrow(p, 'bottom', s22);
    });

    /* ---- plane stress: eps33 = -(nu/E)(s11+s22) ---- */
    const eps33 = snap(-(nu / E_MPa) * (s11 + s22), 1e-12);
    __q('ps-eps33-val').textContent = signed(eps33 * 1e6, 1);

    let fac = 1 + K * eps33;
    const facSat = (fac < FAC_LO || fac > FAC_HI);
    fac = Math.max(FAC_LO, Math.min(FAC_HI, fac));
    const bar = __q('ps-thickbar');
    const h = 14 * fac;
    bar.setAttribute('y', 206 - h / 2);
    bar.setAttribute('height', h);
    bar.setAttribute('fill', facSat ? 'none'
      : (eps33 < 0 ? 'var(--ps-compression)'
      : (eps33 > 0 ? 'var(--ps-tension)' : 'var(--ps-block-fill)')));
    bar.setAttribute('stroke-dasharray', facSat ? '4,3' : 'none');
    bar.setAttribute('stroke', facSat ? 'var(--ps-accent)' : 'var(--ps-block-stroke)');
    __q('ps-a-clampflag').textContent = facSat ? 'drawing saturated \u2014 readout is exact' : '';

    /* ---- plane strain: sig33 = nu*(s11+s22) ---- */
    const sig33 = snap(nu * (s11 + s22), 1e-12);
    __q('ps-sig33-val').textContent = signed(sig33, 1);

    const dot = __q('ps-out-dot'), cross = __q('ps-out-cross');
    if (sig33 === 0) { dot.style.display = 'none'; cross.style.display = 'none'; }
    else if (sig33 > 0) {
      dot.style.display = ''; cross.style.display = 'none';
      dot.setAttribute('r', 2 + Math.min(Math.abs(sig33) / 50, 1) * 4);
    } else { dot.style.display = 'none'; cross.style.display = ''; }

    // dashed ghost = free axial length, from the SAME fac as the thickness bar
    const ghost = __q('ps-sv-ghost');
    const gw = 120 * fac;
    ghost.setAttribute('width', gw);
    ghost.setAttribute('x', 100 - gw / 2);
    ghost.setAttribute('stroke', facSat ? 'var(--ps-accent)' : 'var(--ps-fg-muted)');
    __q('ps-b-clampflag').textContent = facSat ? 'drawing saturated \u2014 readout is exact' : '';

    // clamp reactions
    const rl = __q('ps-sv-reaction-l'), rr = __q('ps-sv-reaction-r');
    if (sig33 === 0) { rl.style.display = 'none'; rr.style.display = 'none'; }
    else {
      rl.style.display = ''; rr.style.display = '';
      const rLen = 6 + Math.min(Math.abs(sig33) / 50, 1) * 22;
      const t = sig33 > 0;
      const col = t ? 'var(--ps-tension)' : 'var(--ps-compression)';
      const mk  = 'url(#ps-b-tip-' + (t ? 't' : 'c') + ')';
      [rl, rr].forEach((el) => { el.setAttribute('stroke', col); el.setAttribute('marker-end', mk); });
      rl.setAttribute('x1', t ? 95 : 95 - rLen);  rl.setAttribute('x2', t ? 95 - rLen : 95);
      rr.setAttribute('x1', t ? 105 : 105 + rLen); rr.setAttribute('x2', t ? 105 + rLen : 105);
    }
  }

  [s11In, s22In, nuIn, eIn].forEach((el) => el.addEventListener('input', update));

  // presets set values and call update(); they never duplicate drawing logic
  const PRESETS = {
    'ps-preset-1': [100,   0, 0.30, 200],
    'ps-preset-2': [100, -40, 0.00, 200],
    'ps-preset-3': [ 60, -60, 0.30, 200],
    'ps-preset-4': [100, 100, 0.49, 200],
    'ps-preset-5': [100,   0, 0.30,  70]
  };
  Object.keys(PRESETS).forEach((id) => {
    const btn = __q(id);
    if (!btn) return;
    btn.addEventListener('click', () => {
      const [a, b, n, e] = PRESETS[id];
      s11In.value = a; s22In.value = b; nuIn.value = n; eIn.value = e;
      update();
    });
  });

  update();
})();
</script>
</div>
```
