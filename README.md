# URDF PyVista Viewer

A Python library for loading, visualizing, and interacting with URDF (Unified Robot Description Format) files using PyVista for 3D visualization.

## Features

- **URDF Loading**: Parse and load URDF files with full support for links, joints, materials, and geometries
- **Interactive 3D Visualization**: View URDF models using PyVista with real-time joint manipulation
- **Joint Control**: Interactive sliders for all actuated joints with proper limit handling
- **Link Coloring**: Color-code different links for better visualization
- **Forward Kinematics**: Real-time updates of robot configuration
- **Scene Graph Support**: Build visual and collision scene graphs
- **Mesh Loading**: Support for various 3D mesh formats (STL, OBJ, DAE, etc.)

## Installation

```bash
pip install -e .
```

## Dependencies

- numpy
- trimesh
- pyvista
- lxml
- six

## Quick Start

```python
from urdf_pyvista import URDF

# Load a URDF file
robot = URDF.load('path/to/your/robot.urdf')

# Display the robot with interactive joint sliders
robot.show(color_by_link=True)

# Access robot properties
print(f"Robot name: {robot.robot.name}")
print(f"Number of links: {len(robot.robot.links)}")
print(f"Number of joints: {len(robot.robot.joints)}")
print(f"Actuated joints: {robot.actuated_joint_names}")
```

## Advanced Usage

### Loading Options

```python
# Load with custom options
robot = URDF.load(
    'robot.urdf',
    build_scene_graph=True,          # Enable forward kinematics
    load_meshes=True,                # Load 3D meshes
    color_by_link=True,              # Color each link differently
    mesh_dir='path/to/meshes'        # Custom mesh directory
)
```

### Joint Configuration

```python
# Set joint configuration
config = [0.0, 1.57, -1.57, 0.0, 1.57, 0.0]  # radians for revolute joints
robot.update_cfg(config)

# Get current configuration
current_config = robot.cfg

# Get joint limits
for joint in robot.actuated_joints:
    if joint.limit:
        print(f"{joint.name}: [{joint.limit.lower}, {joint.limit.upper}]")
```

### Visualization Options

```python
# Show visual geometry (default)
robot.show(collision_geometry=False, color_by_link=True)

# Show collision geometry
robot.show(collision_geometry=True)

# Custom callback for plotter customization
def custom_callback(plotter):
    plotter.add_text("Custom Robot Viewer", position='upper_left')
    plotter.camera_position = 'isometric'

robot.show(callback=custom_callback)
```

## Interactive Controls

When using `robot.show()`, the viewer provides:

- **Mouse Controls**: 
  - Left-click + drag: Rotate view
  - Right-click + drag: Pan view  
  - Scroll wheel: Zoom in/out

- **Joint Sliders**: 
  - Interactive sliders for each actuated joint
  - Real-time updates of robot pose
  - Automatic unit conversion (degrees for revolute joints)
  - Reset button to return to zero configuration

- **Keyboard Shortcuts**:
  - 'r': Reset all joints to zero position

## Supported Joint Types

- **revolute**: Single-axis rotation with limits
- **continuous**: Single-axis rotation without limits  
- **prismatic**: Single-axis translation with limits
- **fixed**: No movement (excluded from controls)
- **floating**: 6-DOF free movement
- **planar**: 2-DOF planar movement

## File Structure

```
urdf_pyvista.py     # Main URDF parser and viewer
README.md           # This file
pyproject.toml      # Package configuration
```

## Examples

### Basic Robot Loading
```python
import urdf_pyvista as up

# Load and display a simple robot
robot = up.URDF.load('simple_robot.urdf')
robot.show()
```

### Advanced Visualization
```python
# Load with collision geometry and custom coloring
robot = up.URDF.load(
    'complex_robot.urdf',
    build_collision_scene_graph=True,
    load_collision_meshes=True
)

# Show collision geometry with link coloring
robot.show(collision_geometry=True, color_by_link=True)
```

## Troubleshooting

### Common Issues

1. **Meshes not loading**: Check mesh file paths in URDF and ensure files exist
2. **PyVista display issues**: Try different backends or update graphics drivers
3. **Joint limits**: Verify joint limits are properly defined in URDF

### Debug Mode

Enable debug logging to troubleshoot issues:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

robot = up.URDF.load('robot.urdf')
```

## License

This project is provided as-is for educational and research purposes.