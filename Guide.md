# Container-based Development with CUDA

GPU can be a scarce source most of the time. Therefore, we should be able to enable developers to work on GPU-servers in a clean and maintainable way.
- The CUDA enabled containers come to the rescue!
- Also, please see other possible cases when we might need to work on remote host containers [1].

Nvidia provides a CUDA Container Toolkit so that our containers can utilize GPU reosurces [2, 3].
- We do not share the installation steps to avoid getting outdated. Please refer to the offical documentation [2, 3].

We also should be aware of how to utilize GPU with docker and docker-compose. Here is a few resources to learn the concepts:
- Official Docs: [4, 5]
- Discussions: [6-10]

In this example project, we prefer to utilize offical tensorflow-gpu images, which builds up on cuda image.
- This image also provides many additional setup and provides setup of additional libraries (cudnn etc.). Please see [11] for details.
- Tensorflow images can be found at [12].
- Please follow the instructions at [13] which also guides for docker and nvidia-cuda-toolkit setup.


## Gotchas
- The main setup of the example project is the same as our [Remote Development Example](https://github.com/erelcan/vscode-hotreload-docker-env). Please first grasp the basics by following its guide.
- Critical observation for cuda enabled containers is that we must add runtime:nvidia in our docker-compose file.
  - For old versions of nvidia-docker, "--gpus all" was being passed as runtime argument but for nvida-docker2, this is not required.~
- We may define driver capabilities:
  - e.g. NVIDIA_DRIVER_CAPABILITIES: compute,utility
  - When "compute" capability is on we can utilize CUDA.
  - "utility" is for nvidia-smi like utilities.
  - Please see the full list at [14].
- We may define visible devices:
  - E.g. NVIDIA_VISIBLE_DEVICES=0,3
  - E.g. NVIDIA_VISIBLE_DEVICES=all
  - Please see the full list at [15].
- We may also set flags as environment variables (e.g. for TF image):
  - TF_XLA_FLAGS=--tf_xla_enable_xla_devices
    - which enables xla compiler to accelerate linear algebra operations [16].
- We may have NUMA warning (which is not fatal):
  - "...successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero..."
  - Please see discussion at [17] to understand the interaction between NUMA and TF.
  - Also, you may learn more on NUMA at [18].

## References

[1] [Why we need to develop on remote hosts?](https://github.com/erelcan/vscode-hotreload-docker-env/blob/master/Guide.md)

[2] [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker)

[3] [NVIDIA Container Toolkit - User Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/user-guide.html)

[4] [Runtime options with GPUs](https://docs.docker.com/config/containers/resource_constraints/#gpu)

[5] [Enabling GPU access with Compose](https://docs.docker.com/compose/gpu-support/)

[6] [GPU with rootless Docker](https://stackoverflow.com/questions/59373710/gpu-with-rootless-docker)

[7] [Support for NVIDIA GPUs under Docker Compose](https://github.com/docker/compose/issues/6691)

[8] [rootless nvidia runtime not working as expected](https://github.com/containers/podman/issues/3659#issuecomment-543912380)

[9] [nvidia-container-runtime doesn't work with rootless mode](https://github.com/moby/moby/issues/38729)

[10] [CUDA + Docker = ❤️ for Deep Learning](https://medium.com/@adityathiruvengadam/cuda-docker-%EF%B8%8F-for-deep-learning-cab7c2be67f9)

[11] [gpu.Dockerfile](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/dockerfiles/dockerfiles/gpu.Dockerfile)

[12] [TensorFlow Docker Images](https://hub.docker.com/r/tensorflow/tensorflow/)

[13] [Tensorflow-Docker](https://www.tensorflow.org/install/docker)

[14] [Container Toolkit - Driver Capabilities](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/user-guide.html#driver-capabilities)

[15] [Container Toolkit - GPU Enumeration](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/user-guide.html#gpu-enumeration)

[16] [XLA: Optimizing Compiler for Machine Learning](https://www.tensorflow.org/xla)

[17] [Stackoverflow - How to interpret TensorFlow output?](https://stackoverflow.com/questions/36838770/how-to-interpret-tensorflow-output)

[18] [Optimizing Applications for NUMA](https://software.intel.com/content/www/us/en/develop/articles/optimizing-applications-for-numa.html)