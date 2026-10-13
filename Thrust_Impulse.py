"""
Estes C6-5 Rocket Practice Problem
Calculates:
A. Average thrust
B. Thrust-to-weight ratio
C. Net force and acceleration
D. Launch-guide exit velocity
E. Specific impulse
F. Effective exhaust velocity
G. Ideal delta-v
"""

import math


# ============================================================
# GIVEN VALUES
# ============================================================

total_impulse = 10.00       # N*s
burn_time = 1.60            # s
max_thrust = 15.30          # N

rocket_mass = 0.110         # kg
propellant_mass = 0.0122    # kg

gravity = 9.81              # m/s^2

# Values used during the launch-guide calculation
initial_thrust = 14.0       # N
guide_length = 0.90         # m


# ============================================================
# A. AVERAGE THRUST
# ============================================================

# Total impulse = Average Thrust * Burn Time
average_thrust = total_impulse / burn_time

print("A. Average Thrust")
print(f"Average thrust = {average_thrust:.2f} N")
print()


# ============================================================
# B. THRUST-TO-WEIGHT RATIO
# ============================================================

# Weight is mass multiplied by gravitational acceleration
weight = rocket_mass * gravity

# Compare maximum motor thrust to the rocket's weight
thrust_to_weight = max_thrust / weight

print("B. Thrust-to-Weight Ratio")
print(f"Rocket weight = {weight:.3f} N")
print(f"Thrust-to-weight ratio = {thrust_to_weight:.2f}:1")

# Check against the 5:1 guideline
if thrust_to_weight >= 5:
    print("The rocket exceeds the 5:1 guideline.")
else:
    print("The rocket does NOT meet the 5:1 guideline.")

print()


# ============================================================
# C. NET FORCE AND ACCELERATION
# ============================================================

# Thrust acts upward and weight acts downward
net_force = initial_thrust - weight

# Newton's Second Law: F = ma
acceleration = net_force / rocket_mass

# Convert acceleration to number of g's
acceleration_g = acceleration / gravity

print("C. Net Force and Acceleration")
print(f"Net force = {net_force:.2f} N")
print(f"Acceleration = {acceleration:.2f} m/s^2")
print(f"Acceleration = {acceleration_g:.2f} g")
print()


# ============================================================
# D. LAUNCH-GUIDE EXIT VELOCITY
# ============================================================

# v_f^2 = v_i^2 + 2*a*d
# The rocket starts from rest, so v_i = 0.
exit_velocity = math.sqrt(
    2 * acceleration * guide_length
)

print("D. Launch-Guide Exit Velocity")
print(f"Exit velocity = {exit_velocity:.2f} m/s")

# Compare against the illustrative 13-15 m/s range
if 13 <= exit_velocity <= 15:
    print("Exit velocity is within the 13-15 m/s range.")
elif exit_velocity < 13:
    print("Exit velocity is below the 13-15 m/s range.")
else:
    print("Exit velocity is above the 13-15 m/s range.")

print()


# ============================================================
# E. SPECIFIC IMPULSE
# ============================================================

# Isp = Total Impulse / (Propellant Mass * g0)
specific_impulse = total_impulse / (
    propellant_mass * gravity
)

print("E. Specific Impulse")
print(f"Specific impulse = {specific_impulse:.2f} s")
print()


# ============================================================
# F. EFFECTIVE EXHAUST VELOCITY
# ============================================================

# Effective exhaust velocity = Isp * g0
exhaust_velocity = specific_impulse * gravity

print("F. Effective Exhaust Velocity")
print(f"Effective exhaust velocity = {exhaust_velocity:.2f} m/s")
print()


# ============================================================
# G. IDEAL DELTA-V
# ============================================================

# Final mass is the rocket mass after its propellant is burned.
final_mass = rocket_mass - propellant_mass

# Tsiolkovsky Rocket Equation:
# delta_v = ve * ln(m0 / mf)
delta_v = exhaust_velocity * math.log(
    rocket_mass / final_mass
)

print("G. Ideal Delta-V")
print(f"Initial mass = {rocket_mass:.4f} kg")
print(f"Final mass = {final_mass:.4f} kg")
print(f"Mass ratio = {rocket_mass / final_mass:.4f}")
print(f"Ideal delta-v = {delta_v:.2f} m/s")