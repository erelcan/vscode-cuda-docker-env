# Enabling Cuda for VS Code Remote Development

In this project, we will present how to setup a **CUDA enabled** docker development environment by using VS Code Remote Development extension.

We present a guide and references to help us through installation and to grasp the basics. Please refer to [Guide.md](https://github.com/erelcan/vscode-cuda-docker-env/blob/master/Guide.md).

We demonstrate the usage by utilizing a tensorflow-gpu image (which builds up on nvidia-cuda image).
- We present a docker-compose example with 2 services (actually just scripts in this case).
- In these scripts, we can observe how to use tensorflow and Keras with GPU-support.
- We verify that GPU is in use.
- We also demonstrate how to use flags and different compilers (e.g. XLA).