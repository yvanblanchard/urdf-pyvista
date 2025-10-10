
import numpy as np
from urdf_pyvista import URDF

# Load the URDF robot model
robot = URDF.load('winder_robot/winder_robot.urdf')

# Print robot information
print(f"Robot name: {robot.robot.name}")
print(f"Number of actuated joints: {robot.num_actuated_joints}")
print(f"Actuated joint names: {robot.actuated_joint_names}")
print(f"Degrees of freedom: {robot.num_dofs}")

# =============================================================================
# EXAMPLE: Setting Joint Values
# =============================================================================

print("\n" + "="*60)
print("JOINT VALUE SETTING EXAMPLES")
print("="*60)

# Method 1: Set joint values using a list/array (positional, same order as actuated_joint_names)
print("\n1. Setting joint values using list/array (positional):")
print(f"   Joint order: {robot.actuated_joint_names}")

# Set specific values for each actuated joint
joint_values_list = [100.0, 50.0, 1.57, -0.5]  # [carriage, cross_carriage, eye, spindle]
robot.update_cfg(joint_values_list)
print(f"   Set values: {joint_values_list}")
print(f"   Current cfg: {robot.cfg}")

# Method 2: Set joint values using a dictionary (by joint name)
print("\n2. Setting joint values using dictionary (by name):")
joint_values_dict = {
    'carriage': -200.0,      # prismatic joint (mm)
    'cross_carriage': 75.0,  # prismatic joint (mm) 
    'eye': -1.57,            # revolute joint (radians)
    'spindle': 3.14          # revolute joint (radians)
}
robot.update_cfg(joint_values_dict)
print(f"   Set values: {joint_values_dict}")
print(f"   Current cfg: {robot.cfg}")

print("\n" + "="*60)
print("END OF JOINT VALUE EXAMPLES")
print("="*60)

print("\nShowing robot model with interactive sliders...")
robot.show(color_by_link=True, sliders=True)