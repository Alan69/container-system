import os
import subprocess
import shutil

class Container:
    def __init__(self, name, image=None):
        self.name = name
        self.image = image
        self.rootfs = f"/tmp/{self.name}-rootfs"
        self.network = None
        self.volumes = {}

    def create(self):
        if self.image:
            self._create_from_image()
        else:
            self._create_from_scratch()

    def _create_from_image(self):
        # Copy image root filesystem
        shutil.copytree(self.image, self.rootfs)

        # Set up namespaces and networking
        self._set_up_namespaces()

        # Mount volumes
        for source, target in self.volumes.items():
            target_path = os.path.join(self.rootfs, target)
            os.makedirs(target_path, exist_ok=True)
            subprocess.call(["mount", "-o", "bind", source, target_path])

        # Run a shell inside the container
        subprocess.call(["chroot", self.rootfs, "bash"])

    def _create_from_scratch(self):
        # Create a new root filesystem
        os.makedirs(self.rootfs)

        # Set up namespaces and networking
        self._set_up_namespaces()

        # Run a shell inside the container
        subprocess.call(["chroot", self.rootfs, "bash"])

    def _set_up_namespaces(self):
        # Unshare namespaces for the child process
        os.unshare(os.CLONE_NEWUTS)  # Create a new UTS namespace
        os.unshare(os.CLONE_NEWPID)  # Create a new PID namespace
        os.unshare(os.CLONE_NEWNS)   # Create a new mount namespace
        os.unshare(os.CLONE_NEWNET)  # Create a new network namespace

    def execute_command(self, command):
        # Execute a command inside the container
        subprocess.call(command)

    def stop(self):
        # Unmount volumes
        for target in self.volumes.values():
            target_path = os.path.join(self.rootfs, target)
            subprocess.call(["umount", target_path])

        # Remove root filesystem
        shutil.rmtree(self.rootfs)


# Example usage
if __name__ == "__main__":
    # Create a container from an image
    container = Container("my_container", image="/path/to/image/rootfs")
    container.volumes = {"/host/path": "/container/path"}
    container.create()

    # Create a container from scratch
    container = Container("scratch_container")
    container.create()

    # Execute a command inside the container
    container.execute_command(["ls", "-l"])

    # Stop the container
    container.stop()
