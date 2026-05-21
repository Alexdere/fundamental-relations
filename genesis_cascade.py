"""
Genesis Cascade visualization.

Implements the framework's minimal generative computation:
- Start at κ-hinge (origin).
- Tick 1: 𝓔 (emit) — create 4 corners of a square at unit radius.
- Tick n+1: 𝓓 (descend) — inscribed square at +45° rotation, scaled by 1/√2.
- Iterate. Cascade converges back to κ in the limit.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('/mnt/user-data/outputs', exist_ok=True)

# Parameters
N_TICKS = 20
INITIAL_RADIUS = 1.0
SCALE = 1 / np.sqrt(2)
ROT_PER_TICK_DEG = 45

def square_corners(radius, rotation_deg):
    """Return the 4 corners of a square at center distance `radius`, rotated by `rotation_deg`."""
    angles_rad = np.radians(np.array([45, 135, 225, 315]) + rotation_deg)
    return np.column_stack([radius * np.cos(angles_rad), radius * np.sin(angles_rad)])

# Build the cascade
cascade = []
for tick in range(N_TICKS):
    radius = INITIAL_RADIUS * SCALE**tick
    rotation = ROT_PER_TICK_DEG * tick
    corners = square_corners(radius, rotation)
    cascade.append({'tick': tick, 'radius': radius,
                    'rotation': rotation, 'corners': corners})

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.patch.set_facecolor('#0a0a0a')

# --- Panel 1: Nested squares ---
ax = axes[0]
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect('equal')
ax.set_facecolor('#0a0a0a')

cmap_squares = plt.cm.plasma(np.linspace(0.85, 0.15, N_TICKS))

for i, level in enumerate(cascade):
    corners = level['corners']
    closed = np.vstack([corners, corners[0]])
    ax.plot(closed[:, 0], closed[:, 1], color=cmap_squares[i],
            linewidth=max(0.6, 2.5 - 0.1 * i), alpha=0.95)
    ax.scatter(corners[:, 0], corners[:, 1], color=cmap_squares[i],
               s=max(6, 60 - 2.5 * i), alpha=0.95, zorder=5,
               edgecolors='none')

ax.scatter([0], [0], color='#ff3366', s=320, marker='*',
           edgecolors='white', linewidths=1.8, zorder=10)
ax.annotate('κ', (0.04, 0.04), color='white', fontsize=14, fontweight='bold')

ax.set_title(f'Genesis cascade — {N_TICKS} ticks\nEach tick: rotate +45°, scale by 1/$\\sqrt{{2}}$',
             color='white', fontsize=12, pad=14)
ax.tick_params(colors='#888888')
for spine in ax.spines.values():
    spine.set_color('#444444')
ax.grid(True, alpha=0.08, color='white')

# --- Panel 2: Corner trajectories (4 logarithmic spirals) ---
ax = axes[1]
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect('equal')
ax.set_facecolor('#0a0a0a')

corner_colors = ['#00d4ff', '#ff66cc', '#aaff33', '#ffaa33']
for corner_idx in range(4):
    trajectory = np.array([level['corners'][corner_idx] for level in cascade])
    ax.plot(trajectory[:, 0], trajectory[:, 1],
            color=corner_colors[corner_idx], linewidth=2, alpha=0.85,
            marker='o', markersize=3.5,
            label=f'Corner {corner_idx + 1}')

ax.scatter([0], [0], color='#ff3366', s=320, marker='*',
           edgecolors='white', linewidths=1.8, zorder=10)
ax.annotate('κ', (0.04, 0.04), color='white', fontsize=14, fontweight='bold')

ax.set_title('Per-corner trajectories\n4 logarithmic spirals converging to κ',
             color='white', fontsize=12, pad=14)
ax.tick_params(colors='#888888')
for spine in ax.spines.values():
    spine.set_color('#444444')
ax.grid(True, alpha=0.08, color='white')
ax.legend(loc='upper right', facecolor='#161616', edgecolor='#444444',
          labelcolor='white', fontsize=9)

plt.suptitle('The Genesis Computation: Emit (E) then iterated Descend (D) — cascade returns to κ',
             color='white', fontsize=14, y=1.01)
plt.tight_layout()

output_path = '/mnt/user-data/outputs/genesis_cascade.png'
plt.savefig(output_path, dpi=150, facecolor='#0a0a0a',
            edgecolor='none', bbox_inches='tight')
plt.close()

# Print summary
print(f"Saved: {output_path}\n")
print(f"  Ticks computed:     {N_TICKS}")
print(f"  Initial radius:     {INITIAL_RADIUS}")
print(f"  Final radius:       {cascade[-1]['radius']:.6e}")
print(f"  Total rotation:     {(N_TICKS - 1) * ROT_PER_TICK_DEG}°")
print(f"  Scale per tick:     1/√2 ≈ {SCALE:.6f}")
print(f"  After 20 ticks:     radius shrunk by factor {(1/SCALE)**(N_TICKS-1):.2f}")
