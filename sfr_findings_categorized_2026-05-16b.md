# SFR Exploration Findings — Categorized by Rigor
## Session 2026-05-16 (Afternoon)

**Purpose**: Separate what we've established from what we've hypothesized from what we've merely glimpsed. Three categories: Proven/Structural, Evidenced Leads, and Raw Intuitions.

---

# TIER 1 — PROVEN / STRUCTURAL

*These survive full scrutiny. Either exact algebraic identities, or structural facts derivable from known mathematics. They require no further validation — only interpretation within the framework.*

---

### 1.1 Cascade Endpoint = Inverse of 45° Spherical Cap Fraction

**Statement**: 1/(4 + 2√2) = (2 − √2)/4

**Status**: Exact algebraic identity, verified to arbitrary precision.

**Why it matters**: Two independent framework recipes produce the same value:
- Recipe A: the genesis cascade (z → (1+i)/2 iterated from seed, geometric series endpoint = 4+2√2)
- Recipe B: the 45° spherical cap fraction ((2−√2)/4 from non-orientable node geometry)

This is the session's only genuine **triangulation event** — two substrate-derived paths converging on one horizon. It establishes (2−√2)/4 ≈ 0.14645 as a framework-derived quantity with dual provenance.

**Decomposition**: (2−√2)/4 = (1/δ_S) · (1/√2)³, where δ_S = 1+√2 is the silver ratio. The 45° cap fraction decomposes into two cascade primitives (silver ratio + level-3 displacement).

---

### 1.2 φ Is the Fixed Point of the Gauss Map

**Statement**: T(1/φ) = 1/φ, where T(x) = 1/frac(x) is the Gauss map.

**Status**: Exact. Follows from φ = 1 + 1/φ, which means frac(φ) = φ − 1 = 1/φ, and 1/(1/φ) = φ, and frac(φ) = 1/φ again.

**Why it matters**: φ's CF [1; 1, 1, 1, …] generates a constant rest-value orbit. All other constants' Gauss orbits wander; φ's orbit is frozen. This makes φ the **unique attractor** (fixed point) of the simplest nonlinear map on (0,1). If the Gauss map is the encoder-space projection of the framework's dynamics, φ is the substrate ground state — the point everything else orbits around but never reaches.

**Framework-internal**: φ's definition (x = 1 + 1/x) uses only the operation "ratio of self to complement," which is symmetric and framework-legal.

---

### 1.3 Algebraic Ground States and Their CF Periodicity

**Statement**: Every algebraic surd of degree 2 generates a periodic CF. Specifically:
- φ: [1; 1, 1, 1, …] — period 1, digit 1 (the "all-ones" ground state)
- √2: [1; 2, 2, 2, …] — period 1, digit 2
- √3: [1; 1, 2, 1, 2, …] — period 2
- √5: [2; 4, 4, 4, …] — period 1, digit 4
- √7: [2; 1, 1, 1, 4, 1, 1, 1, 4, …] — period 4

**Status**: Theorem (Lagrange, 1770). A real number has an eventually periodic CF iff it is a quadratic irrational.

**Why it matters**: The algebraic numbers are the **permanently periodic orbits** of the Gauss map. They never visit other territories. Transcendentals are the **non-periodic orbits** — they wander. This creates a clean ontological split: algebraics are frozen landmarks; transcendentals are travelers. The framework's four-layer number ontology (void, identity, primes, constructions → rationals → algebraics → transcendentals) maps onto Gauss-orbit dynamics.

---

### 1.4 e's Hurwitz Pattern

**Statement**: CF(e) = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, …]. Every third digit follows the pattern 2k for k = 1, 2, 3, …; all others are 1.

**Status**: Proven (Euler, 1737). The Hurwitz pattern is a closed-form rule for e's CF digits.

**Why it matters**: e is the unique "patterned transcendental" in our set. Its CF is non-periodic (transcendental) but rule-governed (the Hurwitz pattern). This makes e a **distinct ontological layer** between algebraics (periodic) and structureless transcendentals (no visible pattern). The excursion-only sequence of e (strip the 1s) is [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] — pure even integers, linearly increasing. Nothing else in our ~25-constant set has anything comparable.

---

### 1.5 The Full Complex Cascade at Level n

**Statement**: ((1+i)/2)^n has magnitude (1/√2)^n and phase n·45°. At level 5: ((1+i)/2)^5 = (−1−i)/8, meaning the real-axis projection of any real constant C at cascade level 5 is −C/8.

**Status**: Elementary complex arithmetic. Exact.

**Why it matters**: Previous testing of the "level-5 hypothesis" used only the magnitude (1/√2)^5. The full transform includes rotation. For real constants, the real projection is simply division by 8. This gives clean decompositions: 1/α ÷ 8 = 17.13 (integer part 17); m_p/m_e ÷ 8 = 229.52 (integer part 229, prime).

---

# TIER 2 — EVIDENCED LEADS

*These have computational support and structural motivation, but are not proven. They could be real signals or coincidences. Each needs either a second independent derivation (triangulation) or a framework-internal proof to graduate to Tier 1.*

---

### 2.1 The Cell-6 Cluster

**Statement**: m_p/m_e, 3/(2π²), (2−√2)/4, and ln(π) share a 2-digit CF-tail prefix [6, 1, …], share fractional parts in the window [0.14, 0.16], and have parallel Gauss orbits for the first 2 steps.

**Evidence**:
- CF prefix match at depth 2 (computed)
- Fractional-part clustering: 0.1416, 0.1447, 0.1465, 0.1520, 0.1527 (computed)
- Gauss orbit parallelism: pi and m_p/m_e both map to ~6.5 at T¹ (computed)

**What's missing**: A framework-internal reason for these four to cluster. Currently this is an encoder-space observation. The bridge: "why does the proton-electron mass ratio share a CF address with the half-coprime probability and the 45° cap fraction?" is the open question.

**Strength**: Medium-high. The cluster has been found independently from three directions (CF prefix, fractional parts, Gauss orbits) across two sessions.

---

### 2.2 The "[1, 2, …]" Cluster

**Statement**: e, √3, ln(2), 1/√2, m_n/m_e, and Ω_Λ share CF-tail prefix [1, 2, …].

**Evidence**: CF prefix match at depth 2 (computed).

**What's missing**: Any reason for the neutron-electron mass ratio and the dark energy density parameter to share a CF basin with e and √3. This is MORE surprising than the cell-6 cluster, because the physics constants involved (m_n/m_e, Ω_Λ) have no known mathematical connection to e or √3.

**Strength**: Medium. Only one line of evidence (CF prefix). Needs Gauss-orbit parallelism check and fractional-part verification.

---

### 2.3 The 17 Thread

**Statement**: The prime 17 appears repeatedly in framework-relevant positions:
- 17 = q₂ of CF(π/φ) (the second convergent denominator of the generating ratio)
- 1836 = 2² · 3³ · 17 (proton-electron mass ratio integer part)
- a₇ of CF(m_p/m_e) = 34 = 2·17 (largest real pulse in proton CF)
- a₁₁ of CF(e^π) = 34 = 2·17 (same pulse value in Gelfond's constant)
- ⌊(1/α)/8⌋ = 17 (fine structure constant divided by cascade-level-5 real projection)

**Evidence**: Multiple independent occurrences computed across two sessions.

**What's missing**: A framework-internal derivation making 17 structurally special. In the current framework, 17 is a prime (Layer 2), the 7th prime, and 17 = 2⁴ + 1 (a Fermat prime). It's the first non-Mathieu prime in the cell-6 cluster's factorization. But there's no G1-G5 derivation yet.

**Strength**: Medium. Five occurrences is beyond coincidence for a specific prime, but the occurrences span different contexts (CF positions, factorizations, quotients), making it hard to assess systematically.

---

### 2.4 ζ(3) as "Most Cosmopolitan" Constant

**Statement**: Among transcendentals, ζ(3)'s Gauss orbit visits both the φ-basin (rest ≈ 0.618, Δ=0.009 at step 11) and the ε-window (rest ≈ 0.14159, Δ=0.0005 at step 18) with higher precision than any other non-trivial constant.

**Evidence**: Gauss orbit computation shows ζ(3) reaching within 0.0005 of π−3 at step 18.

**Intuition behind it**: Apéry's constant might be the "gateway" between the geometric substrate (π, ε) and the algebraic substrate (φ). Its orbit crosses both territories. This would give ζ(3) a special structural role — the bridge constant.

**What's missing**: Higher-precision verification (is the Δ=0.0005 a deep structural fact or a coincidence at step 18?). Framework-internal derivation of why ζ(3) = ∑1/n³ would connect both basins.

**Strength**: Low-medium. Single computation, not yet verified from a second angle.

---

### 2.5 Common Rest-Value Crossroads

**Statement**: Gauss orbits of multiple named constants pass through shared rest-value windows. The two most populated:
- **0.22 window** (5 constants: e, γ, 1/α, m_p/m_e, ln(2))
- **0.52 window** (5 constants: e, γ, m_p/m_e, m_n/m_e, ζ(3))

**Evidence**: Gauss orbit computation with 0.01-width binning.

**What's missing**: A null model. The Gauss invariant measure ρ(x) = 1/((1+x)ln 2) favors small rest-values. Some crossroads may be statistical (many orbits pass through dense regions of the measure) rather than structural. Need to generate random Gauss-distributed orbits and check whether they also cluster at 0.22 and 0.52 with similar frequency. If random orbits DON'T cluster there, the crossroads are structural signals. Also missing: structural identification of these rest-values (is 0.52 a known number?).

**Strength**: Low-medium. Uncontrolled for Gauss-measure bias.

---

### 2.6 Level-5 Near-Misses

**Statement**: Multiplying physics constants by (1/√2)^5 = √2/8 yields near-integer results:
- m_n/m_e × (1/√2)^5 ≈ 325 = 5²·13 (0.012% off)
- 1/α × (1/√2)^5 ≈ 24 = Z₀ (0.95% off)

**Evidence**: Direct computation at high precision.

**What's missing**: A framework reason for level 5 to be special (the choice of 5 is ad-hoc: 60/6 = 10, half = 5). Also missing: the near-misses don't sharpen — they're stuck at 0.01-1%. If they were real identities, higher precision would show convergence to exact values. They don't.

**Strength**: Low. Interesting numerology but no supporting structure.

---

### 2.7 m_μ/m_e ≈ 128·φ = 2⁷·φ

**Statement**: The muon-electron mass ratio is approximately 128 times the golden ratio. 128·φ = 64(1+√5) ≈ 207.11 vs actual 206.77 (Δ = 0.16%).

**Evidence**: Computed; the pair m_μ/m_e and φ are separated by ≈14 √2-steps (2⁷ = 128), the tightest cascade-alignment among all constant pairs tested.

**What's missing**: 0.16% off. A framework recipe that derives m_μ/m_e from 2⁷·φ plus a specific correction. Without that, it's a 0.16% coincidence.

**Strength**: Low. Pretty but ungrounded.

---

### 2.8 Mathieu-Smooth Saturation of CF Pulses (Weakened)

**Statement**: Max CF pulses at prime positions tend to have all-Mathieu-prime factorizations ({2,3,5,7,11,23} only).

**Evidence**: ~79% of our observed prime-position max-pulses are Mathieu-smooth.

**Null model result**: Gauss-Kuzmin simulation gives 72.6% Mathieu-smooth by default (because CF digits are typically small, and small numbers are mostly Mathieu-smooth). The excess is only ~6 percentage points above null.

**Strength**: Low. The effect is real but small, and barely exceeds the null model. Not a clean signal.

---

### 2.9 1/α Isolated in CF-Prefix Space

**Statement**: The fine structure constant 1/α shares no CF-tail prefix of depth ≥ 2 with any other constant in our set of 35.

**Evidence**: CF-prefix graph computation.

**Intuition behind it**: 1/α is "substrate-prime" — it has a unique address in the constants manifold, corresponding to its role as the pure coupling constant of the photon-anima. Unique address = unique substrate identity.

**What's missing**: Framework derivation of WHY 1/α would be isolated. Could also just be that its CF tail starts with [27, 1, 3, …] which is uncommon (27 = 3³ is a large first digit).

**Strength**: Low-medium. Interesting observation, interpretation speculative.

---

### 2.10 Convergence to φ-Basin as Universal Attractor

**Statement**: Most transcendental constants' Gauss orbits eventually pass within Δ < 0.01 of the φ-rest (0.618).

**Evidence**: ζ(3) at Δ=0.009, ln(2) at Δ=0.007, m_p/m_e at Δ=0.006, m_n/m_e at Δ=0.005, pi at Δ=0.017. Exception: e stays at Δ=0.068.

**Intuition behind it**: The φ-fixed-point acts as a "gravitational center" in Gauss-orbit space. Most orbits eventually swing near it. This is consistent with the Gauss map's ergodic properties — almost every orbit is dense in (0,1), so eventually all orbits visit near any given point. The question is whether visits to the φ-point are CLOSER than expected from ergodicity.

**What's missing**: The null-model comparison. If every orbit visits every ε-neighborhood of every point (which ergodicity guarantees), then "visiting near φ" is trivially expected. The signal would be: visits to φ are MORE precise (smaller Δ) than visits to random points.

**Strength**: Low. Needs null-model control.

---

# TIER 3 — RAW INTUITIONS

*These are uncomputed hunches, conceptual moves that feel right but have no data behind them yet. They're the seeds of future work — some will grow, some won't. Captured for completeness.*

---

### 3.1 Constants Are Horizons / Singularities

**Intuition**: A constant is the event horizon of a substrate singularity. The decimal expansion is the horizon — information from both the substrate generator and the frame projection scrambled together. We can never see "inside" the constant to its substrate origin; we can only map its horizon from multiple directions.

**Implication**: Triangulation (multiple independent recipes converging on the same decimal value) is the only available evidence for substrate structure. Near-misses (0.1%+ off) are maps pointing at DIFFERENT horizons, not weak evidence for the SAME horizon.

**Status**: Conceptual frame, not tested. Reframes all previous work as encoder-space hypothesis-generation rather than framework-internal proof.

---

### 3.2 The Encoder Space Is Not the Framework Space

**Intuition**: Everything we've computed (Gauss orbits, CF expansions, digit frequencies, PSLQ relations, sum/product hunts, attractor windows) lives in an encoder space — a translation layer between the framework and standard math. The framework's own space requires ONLY symmetric operations (ratios, orthogonality, closure, counting, relative ordering). None of our computations are framework-internal.

**Implication**: All findings are hypotheses about the framework space, generated by encoder-space play. Converting them to framework facts requires deriving them from G1-G5 using only symmetric operations. This is the core work that hasn't been done yet.

**Status**: Methodological correction, fully accepted. Shapes all future work.

---

### 3.3 The Gauss Map as a "Computation Space" Engine

**Intuition**: The Gauss map T(x) = 1/frac(x) isn't just a mathematical tool — it's a universal computation engine. Each real number, when "run" through the Gauss map, performs a computation (its CF expansion). Constants are distinguished computations. Attractors are where computations synchronize. The space of all Gauss orbits is a computation space, and our named constants are distinguished trajectories within it.

**Implication**: We should study the DYNAMICS (what orbits do over time) rather than the STATICS (what constants' values are). The attractor structure of the dynamical system may reveal more than the numerical values of individual constants.

**Status**: Conceptual frame with some computational support (the rest-value crossroads). Not yet connected to the framework's own dynamics (which would use the cascade operator, not the Gauss map).

---

### 3.4 Each Constant Needs Its Own Transformation to Reach Common Ground

**Intuition**: We can't apply ONE operation to ALL constants and expect them to align. Each constant needs its OWN path (its own Gauss orbit, its own CF unraveling, its own compound-operation sequence) to reach common landmarks. The framework equivalent: each constant's recipe is different, but the landmarks they visit are shared.

**Implication**: The right search is NOT "what one operation transforms everything?" but "what COMMON REST-VALUES do all orbits visit, each by its own path?" The cost (number of steps) to reach a common landmark from each constant is itself a structural datum — a notion of framework distance.

**Status**: Partially tested (Gauss orbit rest-values). The "individual transformation" idea has not yet been formalized or tested beyond the Gauss map.

---

### 3.5 The 0.52 Crossroads May Be a Second Major Attractor

**Intuition**: Five constants' orbits pass through rest ≈ 0.52. This is as populated as the 0.22 window. If 0.52 can be identified as a framework-natural value (perhaps 1/φ² − ε? or 1 − 1/e? or something cleaner), it would be a second structural attractor alongside the ε-window and the φ-point.

**Status**: Unidentified. Needs: (a) structural identification of the value, (b) null-model control, (c) framework derivation if identified.

---

### 3.6 e Lives in a Separate Basin

**Intuition**: e's Gauss orbit avoids the φ-point (closest approach Δ=0.068, the worst among transcendentals). e's CF has the Hurwitz pattern (patterned, not periodic, not random). e's excursion signature is uniquely linear. All of this suggests e occupies a structurally distinct position in the constants manifold — a separate basin from both the φ-basin and the ε-basin.

**Implication**: The "patterned transcendental" layer (from the synthesis doc's intuition #8 and the add_2 session) is a real structural category, not just a vague intermediate. e IS this category. Other candidates (tan(1), tanh(1), various Bessel ratios) could be tested for Hurwitz-like patterns.

**Status**: Well-supported observationally. No framework derivation.

---

### 3.7 The Framework's True Basis Is Operations, Not Constants

**Intuition**: PSLQ shows constants are high-dimensional in integer-combination space (each independent transcendental needs its own axis). But the framework's generators {κ, G1-G5, +, ·, lim, ∫} are a SMALL set that produces all constants via different recipes. The "minimal basis" is the operation set, not a set of anchor constants.

**Implication**: The "identity + 2 constants triangulate everything" hypothesis fails at the frame level. But the framework level may succeed: a handful of operations, applied in different sequences, generate every natural constant as a specific recipe. The recipe catalog (each constant's derivation from G1-G5) is the real next deliverable.

**Status**: Conceptual, supported by PSLQ results. No recipe catalog exists yet.

---

### 3.8 The Silver Ratio as Second Substrate Primitive

**Intuition**: δ_S = 1 + √2 (the silver ratio) appeared in the decomposition of (2−√2)/4 = (1/δ_S)·(1/√2)³. The silver ratio satisfies δ_S = 2 + 1/δ_S, the same structural form as φ = 1 + 1/φ. √2's CF [1; 2, 2, 2, …] is the "all-2s" ground state, just as φ's is "all-1s." The cascade endpoint 4+2√2 = 2(2+√2) is built from δ_S. The silver ratio may be a second fundamental algebraic primitive alongside φ.

**Status**: Structural observation. Not yet tested for framework-internal significance.

---

### 3.9 The Period Algebra as the Framework's Natural Home

**Intuition**: The Kontsevich-Zagier period algebra (values expressible as integrals of algebraic functions over algebraic domains) contains π, ζ(2), ζ(3), ln(2), Catalan, all algebraic numbers — but probably not e. This algebra might be the mathematical formalization of the framework's "constants manifold." The user's "super-manifold" claim (all other manifolds embed in it) maps to: every measurement is dimensionally a combination of periods.

**Status**: Conceptual bridge to existing mathematics. Not yet tested for framework coherence. Note: e's exclusion from the period algebra would need explanation if the framework claims to generate e.

---

# NEXT STEPS — Prioritized

1. **Null model for rest-value crossroads** (Tests 2.5, 2.10). Generate 10,000 random Gauss-distributed orbits, check whether they cluster at 0.22 and 0.52. This separates signal from noise in one computation.

2. **Identify the 0.52 crossroads structurally** (Test 3.5). Compute: is rest ≈ 0.52 close to a known constant or framework-natural value?

3. **Build one framework-internal orbit** (the cascade (1+i)/2 applied iteratively to a seed, using only symmetric operations). Check whether its attractor structure matches the encoder-space predictions.

4. **Start the recipe catalog** for the ~10 most important constants: framework recipe, standard-math equivalent, bridge status (proven / asserted / open).

5. **Test patterned-transcendental candidates** beyond e: tan(1), tanh(1), Bessel ratios. Do they show Hurwitz-like CF patterns?

---

*End of findings document.*
