from projectile.simulation import ProjectileSimulation
import numpy as np


def main():
    sim = ProjectileSimulation(v_init=100, theta=np.radians(45))
    sim.run()
    sim.plot()
    sim.print_range()


if __name__ == "__main__":
    main()
