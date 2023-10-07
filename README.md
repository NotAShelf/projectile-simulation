# Projectile Simulation

This project simulates the motion of a projectile with air resistance.

## Installation

1. Clone this repository.
2. Install the required packages using pip:

```shell
pip install -r requirements.txt
```

## Usage

Run the main.py script:

```shell
python main.py
```

Or alternatively, with your own parameters:

```shell
python main.py --g 9.8 --C_d 0.02 --v_init 150 --theta 45 --h_init 20 --dt 0.01 --t_end 10
```

### Arguments

- `--g`: The acceleration due to gravity in m/s^2. Default is 9.81.
- `--C_d`: The drag coefficient. Default is 0.01.
- `--v_init`: The initial velocity in m/s. Default is 100.
- `--theta`: The launch angle in degrees. Default is 180.
- `--h_init`: The launch height in meters. Default is 10.
- `--dt`: The time step in seconds. Default is 0.01.
- `--t_end`: The total time of the simulation in seconds. Default is 10.
