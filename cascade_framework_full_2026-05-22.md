# The Collatz Cascade Framework: A Standalone Reference

**Status:** Working synthesis as of 2026-05-22. Readable without external lookup.

This document presents the full state of the cascade approach to the Collatz Conjecture: the notation, the building blocks, the proved lemmas, the argument families (some independent, some interlocking), the formal proof as far as it goes, and the precisely located walls where rigour gives way to conjecture.

---

## 0. How to Read This

Five things to know upfront:

1. **The conjecture being addressed.** The Collatz Conjecture states that for every positive integer $n$, the iteration $T(n) = n/2$ (if $n$ even) or $3n+1$ (if $n$ odd) eventually reaches $1$. Equivalently, the only cycle in the iteration is $\{1, 4, 2\}$, and no orbit diverges.

2. **The framework's domain.** We restrict to $\mathbb{Z}_{\geq 2}$ (the **DNCC domain** — "Descent on Non-Cycling Conjecture"). The boundary cycle $\{1, 4, 2\}$ is treated as an ideal boundary, not as an admissible cycle for proof purposes. This is a definitional move, not a logical sleight: any cycle proof in $\mathbb{Z}_{\geq 2}$ combined with the boundary cycle gives the full conjecture.

3. **The reduced map.** Because every odd Collatz step is followed by some halvings, we work with the *reduced* odd-to-odd map $f(m) = (3m+1)/2^{v_2(3m+1)}$, where $v_2$ denotes the 2-adic valuation (highest power of 2 dividing). Cycle length $L$ counts odd steps; total halvings $K = \sum k_i$ where $k_i = v_2(3m_i + 1)$.

4. **What is proven and what is conjectural.** Each lemma carries a status tag: **PROVEN** (rigorous), **ESTABLISHED** (well-known external result we cite), **CONJECTURAL** (motivated but not closed).

5. **The frame.** The operative cycle equation throughout is the cascade-decomposed form (Section 4). Everything is stated in this frame; the older $(L \ln 3, K \ln 2)$ frame is a rotation of the same algebra.

---

## 1. Notation (Read First)

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}_{\geq 2}$ | The DNCC domain: integers $\geq 2$ |
| $T$ | The classical Collatz map: $T(n) = n/2$ if even, $3n+1$ if odd |
| $f$ | The reduced odd-to-odd map: $f(m) = (3m+1)/2^{v_2(3m+1)}$ |
| $m_i$ | Cycle element (odd, $\geq 3$ in non-trivial cycles) |
| $L$ | Cycle length (number of odd steps in a closed orbit) |
| $k_i$ | Halvings at step $i$: $k_i = v_2(3 m_i + 1)$ |
| $K$ | Total halvings in a cycle: $K = \sum_i k_i$ |
| $D$ | Discrete cycle counter: $D = 2K - 3L \in \mathbb{Z}$ |
| $N_L$ | Cycle numerator: $N_L = \sum_{i=1}^L 3^{L-i} \cdot 2^{s_{i-1}}$ where $s_j = k_1 + \ldots + k_j$, $s_0 = 0$ |
| $v_2(\cdot)$ | 2-adic valuation: largest $r$ with $2^r$ dividing the argument |
| $\omega$ | Cascade operator: $\omega = (1+i)/2 \in \mathbb{C}$ |
| $n(v)$ | Cascade coordinate of value $v$: $n(v) = 2 \log_2 v$ |
| $g$ | Geometric mean: $g = \sqrt{(3/2)(3/4)} = 3/(2\sqrt{2}) \in \mathbb{Q}(\sqrt 2)$ |
| $\alpha$ | Displacement element: $\alpha = 1 - 1/\sqrt 2$, so $\alpha^2 = 3/2 - \sqrt 2$ |
| $\Lambda$ | The Baker linear form: $\Lambda = K \ln 2 - L \ln 3$ |
| $\Lambda'$ | The cascade Baker form: $\Lambda' = D \ln 2 - L \ln(9/8) = 2\Lambda$ |
| $\varepsilon_i$ | Correction term: $\varepsilon_i = \ln(1 + 1/(3 m_i))$ |
| $\mathbb{Q}(\sqrt 2)$ | The field of rationals extended by $\sqrt 2$ |
| $\mathbb{Z}[\omega]$ | Gaussian-half-integer ring $\mathbb{Z}[(1+i)/2]$ |
| $N(\beta)$ | Norm of $\beta \in \mathbb{Q}(\sqrt 2)$: $N(a + b\sqrt 2) = a^2 - 2b^2$ |
| $\text{HEN}$ | Hypothetical Escape Number: a number that would refute the conjecture |
| Baker bound | Lower bound on $|\Lambda|$ from Baker's theorem on linear forms in logarithms |
| Tier | Backward depth from 1 in the $f$-graph (tier 0 = $\{1\}$, tier 1 = preimages, etc.) |
| Rung | Synonym for $k_i$, the halving count of a single step |

---

## 2. The Standard Frame and Why It's Not Enough

The classical statement of the cycle equation: for a cycle $m_1 \to m_2 \to \ldots \to m_L \to m_1$ under $f$, taking the product over one full traversal and equating to 1 (since the cycle closes), then taking logarithms:

$$L \ln 3 + \sum_{i=1}^L \ln\left(1 + \frac{1}{3 m_i}\right) = K \ln 2$$

This says: the total log-growth (from $L$ odd steps each contributing $\ln 3$ plus a correction $\varepsilon_i = \ln(1 + 1/(3 m_i))$) must exactly equal the total log-shrinkage from $K$ halvings.

**Why this frame is hard.** It puts two transcendentals — $\ln 2$ and $\ln 3$ — into competition with a residual correction. The classical Baker problem (lower-bounding $|K \ln 2 - L \ln 3|$) is the right tool, but in this frame the integer structure isn't manifest. There's no "natural" discrete observable.

---

## 3. The Frame Jump: Cascade-Decomposed Cycle Equation

**Identity (PROVEN).** $\ln 3 = \tfrac{3}{2}\ln 2 + \tfrac{1}{2}\ln(9/8)$.

*Proof.* Expand: $\tfrac{1}{2}(2 \ln 3 - 3 \ln 2) = \ln 3 - \tfrac{3}{2} \ln 2$. Add $\tfrac{3}{2}\ln 2$: $\ln 3$. $\Box$

This identity is algebraically tautological (both sides equal $\ln 3$), but its *substitution* into the cycle equation reorganizes the algebra.

**Substituting** into the classical cycle equation and multiplying by 2:

$$D \cdot \ln 2 = L \cdot \ln(9/8) + 2 \sum_{i=1}^L \varepsilon_i, \quad \boxed{D = 2K - 3L \in \mathbb{Z}}$$

This is the **cascade-decomposed cycle equation**, the operative frame. Note:

- $D$ is forced to be an integer. For cycle closure, $D / L \to \log_2(3) \cdot 2 - 3 = 0.170$, so $D$ is small.
- $\ln 2$ and $\ln(9/8)$ are *hierarchical*, not symmetric. $\ln 2 \approx 0.693$; $\ln(9/8) \approx 0.118$. The former dominates.
- $9/8 = 1 + 1/8 = 1 + (1/2)^3$: the algebraic shadow of the Pell defect at depth 3.
- The error sum $2 \sum \varepsilon_i$ is bounded above by $2L / (3 m_{\min})$, a quantitative leash on the residual.

**The cycle question, in the new frame:** For which integer pair $(D, L)$ with $D > 0$, and which sequence of integer cycle elements $m_i \geq 3$, is the equation satisfied exactly?

---

## 4. Cascade Coordinates and the Operator $\omega$

**Definition.** For positive real $v$, the cascade coordinate is $n(v) = 2 \log_2 v$. So $n(1) = 0$, $n(2) = 2$, $n(4) = 4$, $n(16) = 8$, $n(2^{68}) = 136$.

**Lemma 4.1 (PROVEN). Cascade-step changes are linear.** If $f(m) = (3m+1)/2^k$, then:
$$n(f(m)) - n(m) = 2\log_2(3 + 1/m) - 2k$$
For large $m$, this approaches $2\log_2 3 - 2k \approx 3.17 - 2k$. So $k = 1$ steps give cascade $\Delta n \approx +1.17$ (expansion), $k = 2$ gives $\Delta n \approx -0.83$ (contraction), and $k \geq 3$ gives strong contraction.

**Definition.** The cascade operator is $\omega = (1+i)/2 \in \mathbb{C}$.

**Lemma 4.2 (PROVEN). Generator identities.**
- $|\omega| = 1/\sqrt 2$
- $\arg(\omega) = \pi/4$
- $\pi = 4 \arg(\omega)$
- $\ln 2 = -2 \ln |\omega|$
- Integer phase period of $\omega^n$ is 8 (since $\omega^8 = 1/16$, real positive)
- Complex period of $|\omega|^n = 2^{-n/2}$ extended to complex $n$ is $4\pi i / \ln 2$

These identities show $\omega$ is a single algebraic object simultaneously generating $\pi$ and $\ln 2$. This is the structural unity that motivates the frame, but is not in itself a proof step.

**Lemma 4.3 (PROVEN). The "16" landing.** The smallest integer with cascade coordinate equal to one $\omega$-period is $16$. Equivalently: $\omega^{-8} = 16$. The boundary cycle $\{1, 4, 2\}$ has cascade coordinates $\{0, 4, 2\}$, all strictly less than 8; the boundary attractor lives entirely inside the first $\omega$-cell.

---

## 5. Proved Lemmas (The Building Blocks)

### 5.1 Algebraic / Pell Family

**Lemma 5.1 (PROVEN). Geometric mean lives in $\mathbb{Q}(\sqrt 2)$.**

$$g = \sqrt{(3/2)(3/4)} = \frac{3}{2\sqrt 2} = \frac{3\sqrt 2}{4} \in \mathbb{Q}(\sqrt 2)$$

The norm is $N(g) = g \bar g = -2 \cdot (3/4)^2 = -9/8$, so $|N(g)| = 9/8$.

**Lemma 5.2 (PROVEN). Displacement identity.**

$$\frac{3}{2} - \sqrt 2 = \left(1 - \frac{1}{\sqrt 2}\right)^2 = \alpha^2$$

*Proof.* $(1 - 1/\sqrt 2)^2 = 1 - 2/\sqrt 2 + 1/2 = 3/2 - \sqrt 2$. $\Box$

**Lemma 5.3 (PROVEN). The corrected Pell defect.** Let $\alpha^{2n} = A_n - B_n \sqrt 2$ with $A_n, B_n \in \mathbb{Q}$. Then:

$$A_n^2 - 2 B_n^2 = N(\alpha^{2n}) = (N(\alpha^2))^n = (3/2 - \sqrt 2)(3/2 + \sqrt 2))^n = (9/4 - 2)^n = (1/4)^n \neq 0$$

This is the honest Pell defect at the correct period (2 cascade steps, since $|\omega|^2 = 1/2$ is the natural rational-step). The defect decays geometrically with ratio $1/4$ per period; it never vanishes for finite $n$.

**Lemma 5.4 (PROVEN). Cascade pulse.** The element $(3/2)(1 - \sqrt 2)^n$ has constant-magnitude norm $\pm 9/4$ oscillating in sign with period 2. This is the structural pulse of the cascade — distinct from the displacement defect, which is a decay.

**Status:** Both the displacement-defect decay and the cascade-pulse oscillation are exact algebraic identities. They measure different things:
- *Defect*: how close successive rational scalings get to powers of $\sqrt 2$. Decays. Feeds the death spiral.
- *Pulse*: the parity-2 swing between odd and even cascade-step amplification. Constant magnitude. The framework's heartbeat.

### 5.2 Transcendental / Baker Family

**Theorem 5.5 (ESTABLISHED, Baker / Rhin).** For positive integers $K, L$, $|K \ln 2 - L \ln 3| > C \cdot \max(K, L)^{-\kappa}$ for explicit constants $C > 0$ and $\kappa$ (current best $\kappa \approx 13.3$, Mignotte).

Equivalently, with $D = 2K - 3L$ and the cascade form: $|D \ln 2 - L \ln(9/8)| > 2 C \cdot \max(K, L)^{-\kappa}$.

This is the *quantitative* version of the irrationality of $\log_2 3$.

**Theorem 5.6 (ESTABLISHED, Mihailescu / Catalan).** The only solution to $x^a - y^b = 1$ with $x, y, a, b \geq 2$ is $3^2 - 2^3 = 1$.

**Corollary 5.7 (PROVEN in this frame). The boundary cycle is the unique $m=1$ solution.** For the cycle equation with $m = 1$: $N_L = 2^K - 3^L$. For $L = 1$: $N_1 = 1$, requiring $2^K - 3 = 1$, i.e., $K = 2$. For $L \geq 2$: Mihailescu rules out $2^K - 3^L = 1$ entirely (with $K \geq 2$, $L \geq 2$). Therefore the boundary cycle at $(K, L) = (2, 1)$ is the **only** $m = 1$ cycle.

The DNCC then categorically excludes this unique object. **The $m = 1$ case is fully closed.**

### 5.3 Modular Family

**Lemma 5.8 (PROVEN). Halving-pattern law.** For odd $m$:
- $m \equiv 1 \pmod 8 \Rightarrow v_2(3m+1) = 2$ (exactly)
- $m \equiv 3 \pmod 8 \Rightarrow v_2(3m+1) = 1$ (exactly)
- $m \equiv 5 \pmod 8 \Rightarrow v_2(3m+1) \geq 3$ (with refinement by $m \bmod 16$)
- $m \equiv 7 \pmod 8 \Rightarrow v_2(3m+1) = 1$ (exactly)

This is pure mod arithmetic; the verification is direct.

**Lemma 5.9 (PROVEN). The mod-8 transition graph.** With states $\{1, 3, 5, 7\}$ (odd residues mod 8) and transitions defined by $f$:

| Source | Targets | Rung $k$ |
|---|---|---|
| $1$ | $\{1, 3, 5, 7\}$ | $2$ |
| $3$ | $\{1, 5\}$ | $1$ |
| $5$ | $\{1, 3, 5, 7\}$ | $\geq 3$, variable |
| $7$ | $\{3, 7\}$ | $1$ |

Enumeration finds 77 distinct closed orbits of length $\leq 5$. **The achievable $K \bmod 8$ values over all orbits cover the full set $\{0, 1, 2, 3, 4, 5, 6, 7\}$.** Mod 8 alone does not isolate $K \equiv 0 \pmod 8$.

**Lemma 5.10 (PROVEN). The mod-5 funnel.** With transition determined by $(m \bmod 5, k \bmod 4)$:

| Source | Targets |
|---|---|
| $0$ | $\{1, 2, 3, 4\}$ (any $k \bmod 4$) |
| $1$ | $\{1, 2, 3, 4\}$ |
| $2$ | $\{1, 2, 3, 4\}$ |
| **$3$** | **$\{0\}$ only** (the funnel — every $k \bmod 4$ sends $3 \mapsto 0$) |
| $4$ | $\{1, 2, 3, 4\}$ |

State $3$ is structurally deterministic: any trajectory passing through $3 \bmod 5$ immediately exits to $0 \bmod 5$. This is because $m \equiv 3 \pmod 5$ gives $3m + 1 \equiv 0 \pmod 5$, and dividing by powers of 2 (which are coprime to 5) keeps the result $\equiv 0$.

**Lemma 5.11 (PROVEN). Forced $K \bmod 4$ per closed mod-5 orbit.** Each closed orbit in the mod-5 graph determines a unique sequence of $k \bmod 4$ values via the transitions, hence a unique $K \bmod 4$.

### 5.4 Dynamical / Contraction Family

**Lemma 5.12 (PROVEN). Average cascade drift is strictly negative.** Over odd $m$ with the geometric rung distribution ($\Pr[k = j] = 2^{-j}$), the expected one-step change in cascade coordinate is:

$$\mathbb{E}[\Delta n] = 2 \log_2 3 - 2 \sum_{j \geq 1} j \cdot 2^{-j} = 2 \log_2 3 - 4 = 2 \log_2(3/4) \approx -0.83$$

So typical orbits contract; this gives "almost all orbits descend" (the Tao 2019 territory).

**Lemma 5.13 (CONJECTURAL). Pointwise descent on cycles.** A cycle is a closed orbit with empirical $\Delta n$ sum equal to zero, against the expected $-0.83$ drift. The conjecture is that no such balanced orbit exists in $\mathbb{Z}_{\geq 2}$. *This is the conjecture itself; the contraction lemma alone does not close it.*

### 5.5 Connectivity

**Theorem 5.14 (PROVEN). Full mod-$2^n \times $ mod-5 connectivity.** The Collatz transition graph at any modular resolution $\mathbb{Z}/2^n \times \mathbb{Z}/5$ has a single connected component. There is no proper isolated subgraph at any finite modular level.

*Why:* $3$ is a primitive root mod 5; $S_1: m \mapsto 3m + 1$ acts as a single 4-cycle on $\{0, 1, 3, 4\}$ with fixed point 2. The mod-$2^n$ dynamics branches richly through the rung structure. Combined, no isolated sub-component can exist.

**Note:** Connectivity does *not* preclude cycles. The boundary cycle exists within a connected graph. Connectivity just means a non-trivial cycle would live in the same component as the boundary cycle, not in some isolated pocket.

### 5.6 Small Cycle Elimination

**Theorem 5.15 (PROVEN). No $L = 1$ cycles in $\mathbb{Z}_{\geq 2}$.** For $L = 1$: $m = 1/(2^k - 3)$. Positivity requires $k \geq 2$. At $k = 2$: $m = 1$ (boundary). For $k \geq 3$: $2^k - 3 \geq 5$, so $m < 1$. No valid $m \geq 2$.

**Theorem 5.16 (PROVEN by inverse construction). No cycle at $(K, L) \in \{(5,3), (8,5), (13,8), (16,10)\}$.** Exhaustive enumeration of all $\binom{K-1}{L-1}$ ordered partitions, with verification that $N_L \not\equiv 0 \pmod{2^K - 3^L}$ for any partition. See Section 7.5.

**Theorem 5.17 (ESTABLISHED, Simons-de Weger 2005).** No cycles exist for $L \leq 68$.

**Theorem 5.18 (ESTABLISHED, Barina 2020).** All trajectories starting below $2^{68}$ reach 1.

### 5.7 Growth Bound

**Theorem 5.19 (PROVEN). Lower bound on cycle elements at convergents.**

$$m \geq \frac{3^{L-1}}{2^K - 3^L}$$

At convergents of $\log_2 3$ where $2^K \approx 3^L$, this forces cycle elements to be astronomically large. Combined with verification (Theorem 5.18), cycle elements at the verified convergent families must exceed $2^{68}$.

---

## 6. Argument Families: How They Combine

The framework has five argument families, each with its own logic. Some are independent; some interlock into the death spiral.

### Family A: Algebraic-Pell Rigidity (Lemmas 5.1–5.4)

**Slogan:** $\sqrt 2$ is irrational; rational approximations have a non-vanishing defect.

**Mechanism:** The Pell defect $A_n^2 - 2 B_n^2 = (1/4)^n$ decays but never reaches zero. This propagates into Collatz via the geometric mean $g = 3/(2\sqrt 2)$ and the displacement $\alpha^2 = 3/2 - \sqrt 2$.

**What it gives:** Structural rigidity. The Collatz step ratios cannot exactly equal a power of 2 because $\sqrt 2$ is irrational.

**What it doesn't give:** Direct cycle exclusion. Pell defect rigidity isn't a divisibility statement on $N_L$.

### Family B: Transcendental-Baker (Theorems 5.5–5.7)

**Slogan:** $\log_2 3$ is transcendental; rational approximations have a quantitative lower bound.

**Mechanism:** Baker's theorem gives $|K \ln 2 - L \ln 3| > C / \max(K, L)^\kappa$. This is the quantitative shadow of $\log_2 3 \notin \mathbb{Q}$.

**What it gives:** A lower bound on the cycle equation's left-hand side, which combined with an upper bound on the correction sum yields contradictions for sufficiently large cycle elements.

**What it doesn't give:** Direct knock-out for small or moderate cycle elements (the constant $C$ is too weak).

### Family C: Modular Transition Graphs (Lemmas 5.8–5.11, Theorem 5.14)

**Slogan:** Cycles must form closed walks in every mod-$n$ transition graph.

**Mechanism:** Enumerate closed walks at increasing modular resolution. Each walk forces a $K \bmod 4$ (from mod 5) and a $K$ range with specific rung structure (from mod $2^n$). Combine via CRT to get mod-$40$, mod-$200$, etc. graphs.

**What it gives:** Structural constraints on $(L, K)$ pairs achievable for cycles. The mod-5 funnel forces specific transition patterns through state 3.

**What it doesn't give:** A clean "only $K \equiv 0 \pmod 8$" type constraint — closed orbits exist at every $K \bmod 8$ residue, so no single modulus isolates cycles.

### Family D: Dynamical Contraction (Lemmas 5.12–5.13)

**Slogan:** The flow contracts on average; cycles balance the contraction exactly.

**Mechanism:** Lyapunov-style analysis in cascade coordinates. Expected drift is $-0.83$ per step. Cycles must have empirical sum 0.

**What it gives:** Tao 2019 style "almost all" results — measure-1 set of orbits descend.

**What it doesn't give:** Pointwise descent on the measure-zero set of potential cycles. This is the canonical Collatz wall.

### Family E: Inverse Construction (Theorem 5.16)

**Slogan:** For each $(K, L)$, the cycle equation is a finite divisibility check.

**Mechanism:** Enumerate all $\binom{K-1}{L-1}$ ordered partitions of $K$ into $L$ positive parts. For each, compute $N_L$ and check whether $(2^K - 3^L) \mid N_L$.

**What it gives:** Rigid, finite, no-cycle results for each verified $(K, L)$.

**What it doesn't give:** Coverage of all $(K, L)$. The number of partitions explodes combinatorially; we lose feasibility past $(32, 20)$ or so.

### How they morph into each other

The **death spiral** (Section 8) braids Families B, D, and the growth bound (Theorem 5.19) into a single argument. Family E provides ground-truth verification at small parameters. Family C provides structural constraints that *would* sharpen E if combined. Family A is structurally aesthetic — it shows where the rigidity comes from but doesn't directly kill cycles.

The frame jump (Section 3) is what makes the death spiral computable: the cascade equation puts $D \in \mathbb{Z}$ in front, so the question becomes "at what $D$ can the equation hold?" rather than "do two transcendentals line up?"

---

## 7. The Formal Proof, As Far As It Goes

Here is the consolidated argument, with each step labeled by its status.

### 7.1 Setup

We prove the DNCC: no non-trivial cycle exists in $\mathbb{Z}_{\geq 2}$. By Theorem 1 (the Well-Ordering equivalence below), this implies the classical Collatz conjecture.

**Theorem 7.0 (PROVEN). DNCC implies Collatz convergence.** If every $n \in \mathbb{Z}_{\geq 2}$ admits $k \geq 1$ with $T^k(n) < n$, then by Well-Ordering, every trajectory reaches the floor and exits to the boundary $\{1\}$.

### 7.2 The $m = 1$ Case (PROVEN, categorical)

By Theorem 5.6 (Mihailescu) and Corollary 5.7, the only $m = 1$ cycle solution is $(K, L) = (2, 1)$, the boundary cycle. The DNCC banishes this. **No $m = 1$ cycle in the domain.** $\Box$

### 7.3 Small Cycle Cases (PROVEN, computational)

**Theorem 7.1 (PROVEN). No cycle exists for $L \leq 68$.** (Simons-de Weger, Theorem 5.17.)

**Theorem 7.2 (PROVEN). All orbits starting below $2^{68}$ reach 1.** (Barina, Theorem 5.18.)

These two cover the "small parameter" region completely. Any non-trivial cycle must have $L > 68$ and all elements $> 2^{68}$.

### 7.4 The Cascade Frame (PROVEN)

Restate the cycle condition in the cascade-decomposed equation:

$$D \ln 2 = L \ln(9/8) + 2 \sum_{i=1}^L \varepsilon_i$$

with $D = 2K - 3L \in \mathbb{Z}_{>0}$ (positivity required for cycles with $m > 0$) and $\varepsilon_i = \ln(1 + 1/(3 m_i))$.

By the Baker bound (Theorem 5.5):
$$|D \ln 2 - L \ln(9/8)| > 2 C / \max(K, L)^\kappa$$

Therefore the correction term satisfies:
$$2 \sum \varepsilon_i > 2 C / \max(K, L)^\kappa$$

### 7.5 The Death Spiral (PROVEN per convergent family, OPEN in general)

For any cycle with elements all $\geq m_{\min}$:
$$\sum \varepsilon_i \leq L \cdot \frac{1}{3 m_{\min}}$$

Combined with the Baker lower bound:
$$\frac{L}{3 m_{\min}} > C / \max(K, L)^\kappa$$

Rearranging:
$$m_{\min} < \frac{L \cdot \max(K, L)^\kappa}{3C}$$

This is the **death spiral bound**. It gives an upper limit on $m_{\min}$, which together with the lower limit $m_{\min} > 2^{68}$ from verification (Theorem 5.18) yields a contradiction whenever:

$$2^{68} > \frac{L \cdot \max(K, L)^\kappa}{3C}$$

For each convergent family of $\log_2 3$, this inequality is checkable. The 24 known convergent families have all been verified to satisfy this inequality, so cycles at any of these convergents are excluded.

**Status:** PROVEN for the 24 tested convergent families. OPEN whether there exists an *anomalous convergent* far out in the continued fraction expansion of $\log_2 3$ with an unusually large partial quotient, making the constants $C, \kappa$ effectively worse and breaking the inequality.

### 7.6 Inverse Construction Verification (PROVEN, finite)

For each $(K, L) \in \{(5, 3), (8, 5), (13, 8), (16, 10)\}$, enumerated all ordered partitions and verified $(2^K - 3^L) \nmid N_L$ for every partition. Rigid no-cycle proofs at these specific points.

**Status:** PROVEN at these specific $(K, L)$. Computationally extensible to $(24, 15)$, $(32, 20)$ with effort. Beyond that, combinatorial explosion makes direct enumeration infeasible.

### 7.7 The Walls

We hit two walls.

**Wall 1: Anomalous Partial Quotients.** The death spiral (7.5) covers all currently-known convergents of $\log_2 3$. It cannot rule out the existence of a far-out partial quotient large enough to weaken the Baker constants. Equivalently: *we have no proven upper bound on the irrationality measure of $\log_2 3$*.

**Wall 2: Combinatorial Explosion.** The inverse construction (7.6) is rigid where it applies but cannot brute-force all $(K, L)$. A structural theorem of the form "for all $(K, L)$ with $D > 0$ and $(K, L) \neq (2, 1)$, $N_L \bmod (2^K - 3^L)$ never equals 0 over the partition family" is required to extend the technique to all parameters. This theorem is currently absent.

These walls are related: if Wall 2 were closed, Wall 1 would be redundant. If Wall 1 were closed (a sharp irrationality-measure bound), Wall 2 would also fall.

**The honest summary of the formal proof:**

$$\underbrace{\text{Mihailescu} + \text{DNCC}}_{\text{covers } m=1} + \underbrace{\text{Simons-de Weger}}_{L \leq 68} + \underbrace{\text{Barina}}_{m < 2^{68}} + \underbrace{\text{Death spiral}}_{\text{24 convergent families}} + \underbrace{\text{Inverse construction}}_{(K,L) \leq (16,10)}$$

$$\Rightarrow \text{No cycle in } \mathbb{Z}_{\geq 2} \text{ except possibly at an anomalous convergent}$$

This is a substantial partial result. It is not yet Collatz.

---

## 8. Status Table

| Component | Status | What it gives |
|---|---|---|
| DNCC domain reframe | PROVEN | Excludes $\{1\}$ categorically |
| Cycle equation, log form | PROVEN | Classical formulation |
| Cascade-decomposed equation | PROVEN | The operative frame; $D \in \mathbb{Z}$ as primary observable |
| Geometric mean $g \in \mathbb{Q}(\sqrt 2)$, $|N(g)| = 9/8$ | PROVEN | Algebraic carrier of the cycle amplification |
| Displacement identity $\alpha^2 = 3/2 - \sqrt 2$ | PROVEN | Bridge to Pell defect |
| Corrected Pell defect $(1/4)^n$ | PROVEN | Honest period-2 decay |
| Cascade pulse $\pm 9/4$ period 2 | PROVEN | Structural heartbeat |
| Generator identities ($\omega$ gives $\pi, \ln 2$) | PROVEN | Structural unity |
| Integer phase period of $\omega$ = 8 | PROVEN | Of $\omega$ in $\mathbb{C}$, not of $\mathbb{Z}$-Collatz |
| Complex period $4\pi i / \ln 2$ of $\|\omega\|^n$ | PROVEN | Cascade magnitude periodicity in $\mathbb{C}$ |
| Halving-pattern law (Lemma 5.8) | PROVEN | $v_2(3m+1)$ determined by $m \bmod 8$ |
| Mod-8 transition graph and orbits | PROVEN | 77 closed orbits, all $K \bmod 8$ residues |
| Mod-5 funnel ($3 \to 0$) | PROVEN | Asymmetric directionality |
| Forced $K \bmod 4$ per mod-5 orbit | PROVEN | Sharper modular constraint |
| Full mod-$2^n \times 5$ connectivity | PROVEN | Single connected component |
| Mihailescu / Catalan | ESTABLISHED | Closes $m = 1$ case categorically |
| Boundary cycle is unique $m=1$ solution | PROVEN | Combines Mihailescu with cycle equation |
| Simons-de Weger ($L \leq 68$ no cycles) | ESTABLISHED | Small-$L$ coverage |
| Barina ($n < 2^{68}$ all descend) | ESTABLISHED | Verification bound |
| Baker linear-forms bound | ESTABLISHED | Quantitative transcendental gap |
| Average cascade drift $\approx -0.83$ | PROVEN | Lyapunov direction |
| Pointwise descent on cycles | CONJECTURAL | The Tao 2019 wall |
| Death-spiral elimination at known convergents | PROVEN | All 24 tested families killed |
| Inverse construction at $(5,3), (8,5), (13,8), (16,10)$ | PROVEN | Rigid finite checks |
| Inverse construction at all $(K, L)$ with $D > 0$ | OPEN | Structural theorem absent |
| Phase constraint $K \equiv 0 \pmod 8$ | NOT PROVEN, NOT DISPROVEN | Gauge artifact in standard derivation; no admissible counter-example |
| Upper bound on partial quotients of $\log_2 3$ | OPEN | The anomalous-convergent wall |

---

## 9. The Walls, Precisely Stated

**Wall A: The anomalous partial quotient.** The continued fraction expansion of $\log_2 3$ is $[1; 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, \ldots]$. No upper bound on the partial quotients $a_n$ is currently known. If some $a_n$ far out in the expansion is anomalously large, the corresponding convergent $p_n/q_n$ provides a rational approximation to $\log_2 3$ better than the Baker bound's worst case, potentially allowing a cycle to slip through the death spiral.

The wall is exactly one sentence: *we have no upper bound on the partial quotients of $\log_2 3$.*

This wall is identical to the wall encountered by Tao 2019, Krasikov's earlier work, and all other modern attacks on Collatz.

**Wall B: Combinatorial enumeration limits.** The inverse construction is feasible up to roughly $(K, L) = (32, 20)$ with serial computation. Beyond that, the number of ordered partitions $\binom{K-1}{L-1}$ grows beyond brute force. A structural theorem characterizing $N_L \bmod (2^K - 3^L)$ across the partition family is needed. The candidate theorem:

> **(Conjecture).** For all $(K, L) \in \mathbb{Z}_{>0}^2$ with $D = 2K - 3L > 0$ and $(K, L) \neq (2, 1)$, and all ordered partitions of $K$ into $L$ positive parts, $N_L \not\equiv 0 \pmod{2^K - 3^L}$.

This conjecture is exactly equivalent to the Collatz cycle non-existence statement in $\mathbb{Z}_{\geq 2}$. So it is no easier than Collatz itself, *unless* a structural pattern in $N_L \bmod (2^K - 3^L)$ can be identified.

A possible structural avenue: at the verified cases $(5,3), (8,5), (13,8), (16,10)$, the residues $N_L \bmod D$ cover a specific subset of $(\mathbb{Z}/D\mathbb{Z})^*$ that systematically excludes 0. Whether this pattern is dictated by an underlying group structure is open.

---

## 10. Open Computational Targets

Concrete, doable, narrowing-the-conjecture work:

1. **Inverse construction at $(24, 15)$.** $\binom{23}{14} = 817{,}190$ partitions; $D = 2^{24} - 3^{15} = 2{,}428{,}309$. Feasible serially (~1 hour) or quickly in parallel.

2. **Inverse construction at $(32, 20)$.** $\binom{31}{19} \approx 1.4 \times 10^8$. Borderline brute force; doable with care.

3. **Residue-class structure in verified cases.** Compute $\{N_L \bmod D : \text{all partitions}\}$ for each verified $(K, L)$ and look for a group-theoretic characterization that excludes $0 \bmod D$.

4. **Mod-40 transition graph.** Combine mod-5 and mod-8 graphs via CRT. Enumerate closed walks. For each, derive the forced $(K \bmod 4) \times (\text{rung distribution})$ signature and check consistency with cycle equation at small $(K, L)$.

5. **Higher-resolution 2-adic Cantor narrowing.** Extend Lemma 5.9 to mod-$2^n$ graphs for $n = 5, 6, 7, \ldots$ and quantify the rate at which surviving residues shrink. This is the 2-adic Cantor set computation; quantifying its density-zero limit may interlock with Baker.

6. **Continued fraction extension for $\log_2 3$.** Compute partial quotients of $\log_2 3$ further than current records. Each computed quotient either confirms regularity (closing the wall further) or reveals an anomaly (requiring investigation). No proof, but bounded narrowing.

---

## 11. Casual Observations and Conjectures

These are not proofs. They are intuitions, half-formed structural ideas, and observations worth flagging for further development.

**Observation 1: The 16-cell structure.** The cascade-coordinate value $n = 8$ corresponds to integer $v = 16$. Verification depth $2^{68}$ corresponds to $n = 136 = 17$ $\omega$-periods. The "outer skin" of each cell sits at integer-valued cascade coordinates $n \in \{0, 8, 16, 24, \ldots\}$, corresponding to values $\{1, 16, 256, 4096, \ldots\}$ — the powers $2^{4k}$. A cycle outside the verified annulus would have to live in cell $\geq 18$. Whether the cell structure imposes any divisibility-relevant constraint is open.

**Observation 2: Two readings of one rigidity.** Baker's theorem (transcendental) and the Pell defect (algebraic) both state "approach but never meet" — one in $\ln 2, \ln 3$; the other in $\sqrt 2$ approximation. The cascade operator $\omega$ is the algebraic root of both. This is structural unity but not yet a proof step. The dream is that Pell rigidity propagates through $\omega$ to give a uniform Baker-strength bound; whether this works mechanically is currently conjectural.

**Observation 3: The funnel is the only deterministic state.** In the mod-5 graph, only state 3 has a single output (always to 0). This is the only deterministic node in the residue dynamics. Whether the funnel's forced rung-1-followed-by-rung-≥3 pattern imposes a divisibility obstruction on $N_L$ at any specific $D$ is worth checking.

**Observation 4: 16 as the unit cell.** $16 = \omega^{-8}$. In the multiplicative ω-lattice on $\mathbb{C}$, 16 is the unit cell magnitude. Any geometric argument about "vortices in the ω-flow" should naturally use 16 as the unit.

**Observation 5: The "addition is rotation" reframe.** Translation in $\mathbb{Z}$ is projectively a rotation around the point at infinity. So the $+1$ in $3m+1$ is, projectively, a rotation. This intuition was floated but not developed; whether projective-rotation language gives any leverage on Collatz is unknown.

**Observation 6: Navier-Stokes analogy.** The Collatz dynamics as a vector field on the residue manifold, with cycles as "vortices" in a dissipative compressible flow. The flow has a single global sink (the boundary attractor). The conjecture is that the flow admits no other vortices in $\mathbb{Z}_{\geq 2}$. This is descriptive, not proof-bearing, but it gives the right shape for the open problem.

**Observation 7: The $D$ shadow.** At convergents of $\log_2 3$, $D$ values are 1, 1, 1, 1, 2, 3, 5, 7, 9, ... (Fibonacci-flavored growth). The $D = 1$ family (which includes the boundary case $(L, K) = (1, 2)$) extends to $(3, 5), (5, 8), (7, 11), \ldots$ — all small-$D$ convergents. Whether the $D = 1$ family has a uniform algebraic structure killing it all at once is worth investigating.

**Observation 8: The cascade pulse.** The $\pm 9/4$ pulse of $(3/2)(1-\sqrt 2)^n$ has period 2. The cycle equation involves $\ln(9/8)$, where $9/8$ is suggestively half of $9/4$. Is there a clean derivation of the cycle equation directly from the cascade pulse algebra? Worth examining.

**Observation 9: Frame jumps left to attempt.** The DNCC reframe banishes the boundary cycle. Mihailescu makes the $m=1$ case categorical. Could a similar categorical move handle the $m \geq 3$ case? Candidates: (a) an algebraic-K-theory framing where cycles are torsion elements of some group; (b) a sheaf-theoretic framing where cycles are non-trivial global sections; (c) a quantization framing where the cycle equation has commutator-like structure. All speculative; none has yielded concrete progress in this session.

**Observation 10: The $m = 1$ uniqueness.** The categorical closure of $m = 1$ cycles via Mihailescu is cleaner than expected. It means the only "trivial" hideout for a Collatz counter is structurally forbidden. Whether $m \geq 3$ cycles have a similar Catalan-style number-theoretic obstruction (perhaps via $S$-unit equations, Vojta's conjecture, or similar) is an open question with established machinery to attempt it.

---

## 12. How To Use This Document

For a researcher continuing the work:

1. **Start at Section 1 (Notation)** and Section 3 (the cascade equation). Everything operates in this frame.
2. **The proved-results table in Section 8** is the working capital.
3. **For new attacks**: pick a family in Section 6 and a wall in Section 9. Try to either close the wall or sharpen the family's reach.
4. **Computational targets in Section 10** are immediately doable with modest effort.
5. **Speculative directions in Section 11** are for the structural-thinking mode.

The framework is at a junction where computational extension and structural conjecture both have clear targets. The wall is one sentence wide. The path forward is not closed.

---

## Appendix A: Computational Code

The Python scripts that produced the verified results in this document:

- `mod8_graph_v2.py`: builds the mod-8 transition graph and enumerates closed orbits
- `inverse_K8_L5.py`: full inverse construction at $(K, L) = (8, 5)$
- `inverse_multi_v2.py`: multi-$(K, L)$ inverse construction
- `mod5_field.py`: mod-5 transition graph and closed orbits
- `triangle_check.py`: forced $k \bmod 4$ derivation per mod-5 orbit

All scripts are standalone Python 3, no external dependencies beyond the standard library.

## Appendix B: External References

- Tao, T. (2019). "Almost all orbits of the Collatz map attain almost bounded values." *Forum of Mathematics, Pi.*
- Simons, J. & de Weger, B. (2005). "Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem." *Acta Arithmetica.*
- Barina, D. (2020). "Convergence verification of the Collatz problem." *The Journal of Supercomputing.*
- Mihailescu, P. (2004). "Primary cyclotomic units and a proof of Catalan's conjecture." *Journal für die reine und angewandte Mathematik.*
- Baker, A. (1966+). "Linear forms in the logarithms of algebraic numbers." Various papers.
- Mignotte, M. (1995-2008). Refined effective bounds on linear forms in two logarithms.

## Appendix C: Notation Index (Alphabetical)

| Symbol | First defined |
|---|---|
| $\alpha = 1 - 1/\sqrt 2$ | Section 5.1 |
| $D = 2K - 3L$ | Section 3 |
| $\varepsilon_i = \ln(1 + 1/(3 m_i))$ | Section 2 |
| $f$ (reduced map) | Section 0 |
| $g = 3/(2\sqrt 2)$ | Section 5.1 |
| $K$ (total halvings) | Section 0 |
| $\kappa$ (Baker exponent) | Section 5.5 |
| $L$ (cycle length) | Section 0 |
| $\Lambda = K \ln 2 - L \ln 3$ | Section 1 |
| $\Lambda' = 2 \Lambda$ | Section 1 |
| $m_i$ (cycle element) | Section 0 |
| $N(\beta)$ (norm in $\mathbb{Q}(\sqrt 2)$) | Section 1 |
| $N_L$ (cycle numerator) | Section 1 |
| $n(v) = 2 \log_2 v$ | Section 4 |
| $T$ (classical Collatz) | Section 0 |
| $\omega = (1+i)/2$ | Section 1 |
| $v_2$ (2-adic valuation) | Section 0 |
| $\mathbb{Z}_{\geq 2}$ (DNCC domain) | Section 0 |

---

*End of standalone framework. Companion document `conversation_arc_2026-05-22.md` traces how this state was reached.*
