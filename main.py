import argparse
from projectile.simulation import ProjectileSimulation
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Run a projectile simulation.")
    parser.add_argument(
        "--g", type=float, default=9.81, help="Acceleration due to gravity (m/s^2)"
    )
    parser.add_argument("--C_d", type=float, default=0.01, help="Drag coefficient")
    parser.add_argument(
        "--v_init", type=float, default=100, help="Initial velocity (m/s)"
    )
    parser.add_argument(
        "--theta",
        type=float,
        default=np.radians(180),
        help="Launch angle (degrees to radians)",
    )
    parser.add_argument("--h_init", type=float, default=10, help="Launch height (m)")
    parser.add_argument("--dt", type=float, default=0.01, help="Time step (s)")
    parser.add_argument(
        "--t_end", type=float, default=10, help="Total time of simulation (s)"
    )

    args = parser.parse_args()

    sim = ProjectileSimulation(
        g=args.g,
        C_d=args.C_d,
        v_init=args.v_init,
        theta=args.theta,
        h_init=args.h_init,
        dt=args.dt,
        t_end=args.t_end,
    )
    sim.run()
    sim.plot()
    sim.print_range()


if __name__ == "__main__":
    main()
