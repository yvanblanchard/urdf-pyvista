from urdf_pyvista import URDF
import numpy as np

# Load the URDF robot model
robot = URDF.load('winder_machine/winder_machine.urdf')

# Print robot information
print(f"Robot name: {robot.robot.name}")
print(f"Number of actuated joints: {robot.num_actuated_joints}")
print(f"Actuated joint names: {robot.actuated_joint_names}")
print(f"Degrees of freedom: {robot.num_dofs}")

# Set joint values using a dictionary (joint name -> value mapping)
print("\n1. Setting joint values using dictionary (joint name -> value):")
print(f"   Joint order: {robot.actuated_joint_names}")

# Set specific values for each actuated joint
# Note: Prismatic joints use linear units (mm), revolute joints use RADIANS
joint_values_dict = {
    robot.actuated_joint_names[0]: 100.0,              # carriage
    robot.actuated_joint_names[1]: 50.0,               # cross_carriage
    robot.actuated_joint_names[2]: np.radians(90.0),   # eye
    robot.actuated_joint_names[3]: np.radians(20.0)    # spindle
}
robot.update_cfg(joint_values_dict)

print("\nShowing robot model with interactive sliders...")
robot.show(color_by_link=True, sliders=True, grid=True, viewup_vector=[0, 1, 0])