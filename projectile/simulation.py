import numpy as np
import matplotlib.pyplot as plt


class ProjectileSimulation:
    """
    A class used to simulate the motion of a projectile with air resistance.

    ...

    Attributes
    ----------
    g : float
        acceleration due to gravity (m/s^2)
    C_d : float
        drag coefficient
    v_init : float
        initial velocity (m/s)
    theta : float
        launch angle (degrees to radians)
    h_init : float
        launch height (m)
    dt : float
        time step (s)
    t_end : float
        total time of simulation (s)

    Methods
    -------
    reset():
        Resets the simulation to its initial state.
    calculate_acceleration(t, state):
        Calculates the acceleration at a given time and state.
    update_state(t, state):
        Updates the state using the Runge-Kutta method.
    run():
        Runs the simulation.
    plot():
        Plots the trajectory of the projectile.
    print_range():
        Prints the range of the projectile.
    """

    def __init__(
        self,
        g=9.81,
        C_d=0.01,
        v_init=100,
        theta=np.radians(180),
        h_init=10,
        dt=0.01,
        t_end=10,
    ):
        self.g = g
        self.C_d = C_d
        self.v_init = v_init
        self.theta = theta
        self.h_init = h_init
        self.dt = dt
        self.t_end = t_end
        self.reset()

    def reset(self):
        """Resets the simulation to its initial state."""
        self.x = [0]
        self.y = [self.h_init]
        self.vx = [self.v_init * np.cos(self.theta)]
        self.vy = [self.v_init * np.sin(self.theta)]
        self.t = [0]

    def calculate_acceleration(self, t, state):
        """Calculates the acceleration at a given time and state."""
        x, y, vx, vy = state
        v = np.sqrt(vx**2 + vy**2)
        F_air_x = -self.C_d * v * vx
        F_air_y = -self.C_d * v * vy
        ax = F_air_x
        ay = F_air_y - self.g
        return [vx, vy, ax, ay]

    def update_state(self, t, state):
        """Updates the state using the Runge-Kutta method."""
        k1 = self.calculate_acceleration(t, state)
        k2 = self.calculate_acceleration(
            t + 0.5 * self.dt, [s + 0.5 * self.dt * k for s, k in zip(state, k1)]
        )
        k3 = self.calculate_acceleration(
            t + 0.5 * self.dt, [s + 0.5 * self.dt * k for s, k in zip(state, k2)]
        )
        k4 = self.calculate_acceleration(
            t + self.dt, [s + self.dt * k for s, k in zip(state, k3)]
        )
        return [
            s + self.dt / 6 * (k1_i + 2 * k2_i + 2 * k3_i + k4_i)
            for s, k1_i, k2_i, k3_i, k4_i in zip(state, k1, k2, k3, k4)
        ]

    def run(self):
        """Runs the simulation."""
        while self.t[-1] < self.t_end:
            state = [self.x[-1], self.y[-1], self.vx[-1], self.vy[-1]]
            state = self.update_state(self.t[-1], state)
            self.x.append(state[0])
            self.y.append(state[1])
            self.vx.append(state[2])
            self.vy.append(state[3])
            self.t.append(self.t[-1] + self.dt)

    def plot(self):
        """Plots the trajectory of the projectile."""
        plt.plot(self.x, self.y)
        plt.xlabel("Horizontal distance (m)")
        plt.ylabel("Vertical distance (m)")
        plt.title("Projectile Motion with Air Resistance")
        plt.show()

    def print_range(self):
        """Prints and returns the range of the projectile."""
        range_projectile = self.x[-1]
        range_string = f"Range of projectile: {range_projectile:.2f} m"
        print(range_string)
        return range_string
