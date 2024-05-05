# Simple Container System in Python

This project implements a simple container system in Python, inspired by Docker. The container system provides basic functionalities for creating lightweight containers using Linux namespaces and control groups.

## Features

- **Container Creation**: Create containers from scratch or based on existing container images.
- **Volume Management**: Mount volumes inside containers for persistent storage.
- **Execution**: Execute commands inside containers.
- **Cleanup**: Stop and clean up containers.

## Getting Started

To use the container system, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Alan69/container-system.git
    ```

2. Navigate to the project directory:

    ```
    cd container-system
    ```

3. Run the container system using Python:

    ```
    python container.py
    ```

4. Follow the on-screen instructions to create, manage, and execute commands inside containers.

## Usage

- **Creating Containers**: Use the `Container` class to create containers from scratch or based on existing container images. Specify volumes to mount inside containers if needed.
- **Executing Commands**: Use the `execute_command` method to execute commands inside containers.
- **Cleaning Up**: Use the `stop` method to stop and clean up containers.

## Examples

```python
# Create a container from an image
container = Container("my_container", image="/path/to/image/rootfs")
container.volumes = {"/host/path": "/container/path"}
container.create()

# Execute a command inside the container
container.execute_command(["ls", "-l"])

# Stop the container
container.stop()
```

## Requirements

- Python 3.x

## Contributing

Contributions to this project are welcome! If you have any ideas, suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.
