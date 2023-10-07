import unittest
from projectile.simulation import ProjectileSimulation
import numpy as np


class TestProjectileSimulation(unittest.TestCase):
    def setUp(self):
        self.sim = ProjectileSimulation()

    def test_reset(self):
        self.sim.reset()
        self.assertEqual(self.sim.x, [0])
        self.assertEqual(self.sim.y, [self.sim.h_init])
        self.assertEqual(self.sim.vx, [self.sim.v_init * np.cos(self.sim.theta)])
        self.assertEqual(self.sim.vy, [self.sim.v_init * np.sin(self.sim.theta)])
        self.assertEqual(self.sim.t, [0])

    def test_calculate_acceleration(self):
        state = [
            0,
            self.sim.h_init,
            self.sim.v_init * np.cos(self.sim.theta),
            self.sim.v_init * np.sin(self.sim.theta),
        ]
        acceleration = self.sim.calculate_acceleration(0, state)
        self.assertEqual(len(acceleration), 4)

    def test_update_state(self):
        state = [
            0,
            self.sim.h_init,
            self.sim.v_init * np.cos(self.sim.theta),
            self.sim.v_init * np.sin(self.sim.theta),
        ]
        new_state = self.sim.update_state(0, state)
        self.assertEqual(len(new_state), 4)

    def test_run(self):
        self.sim.run()
        self.assertTrue(self.sim.t[-1] >= self.sim.t_end)

    def test_print_range(self):
        self.sim.run()
        range_projectile = self.sim.x[-1]
        self.assertEqual(
            self.sim.print_range(), f"Range of projectile: {range_projectile:.2f} m"
        )


if __name__ == "__main__":
    unittest.main()
