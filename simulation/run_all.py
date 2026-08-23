"""Orchestrator: reproduces every number and all three figures in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/*.png. Everything is exact
integer and rational arithmetic; a rerun reproduces every number bit for
bit. A failed invariant fails the run.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))

    from figures import plot_generation, plot_forms, plot_atomos
    plot_generation(results, str(OUT / "figures" / "generation.png"))
    plot_forms(results, str(OUT / "figures" / "forms.png"))
    plot_atomos(results, str(OUT / "figures" / "atomos.png"))

    g = results["generation"]
    print(f"generation: {g['total_weyl_states']} states, sums "
          f"{g['anomaly_sums']}, deletions breaking nothing: "
          f"{g['deletions_that_break_nothing']}")
    gl = results["global_forms"]
    print(f"global forms: screening order {gl['screening_subgroup_order']}, "
          f"{gl['n_distinct_lattices']} distinct lattices; "
          + str({k: (v['electric_one_form_order'],
                     v['magnetic_one_form_order'])
                 for k, v in gl['forms'].items()}))
    s = results["sl2z"]
    print(f"sl2z: box {s['box']}, primitive density {s['primitive_density']} "
          f"vs 6/pi^2 {s['six_over_pi_squared']} (gap {s['density_gap_pct']}%), "
          f"orbit iff coprime: {s['orbit_iff_coprime_verified']}")
    f = results["fusion"]
    print(f"fusion: 3x3x3 -> {f['su3_3x3x3']}, singlet {f['singlet_in_3x3x3']}; "
          f"SU(2) prime {f['su2_all_irreps_tensor_prime']}, "
          f"composite-as-summand {f['su2_all_composite_as_summand']}")
    print("checks:", f"{sum(results['checks'].values())}/{len(results['checks'])}")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
