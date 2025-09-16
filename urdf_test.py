
from urdf_pyvista import URDF

# Load the URDF robot model
robot = URDF.load('winder_robot/winder_robot.urdf')

# Print robot information
print(f"Robot name: {robot.robot.name}")
print(f"Number of actuated joints: {robot.num_actuated_joints}")
print(f"Actuated joint names: {robot.actuated_joint_names}")
print(f"Degrees of freedom: {robot.num_dofs}")

print("\nShowing robot model...")
robot.show(color_by_link=True, sliders=True)