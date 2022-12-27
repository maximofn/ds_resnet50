# Deepstream Resnet50

## Docker image
The first thing to do is to enter the docker container. The image to use is the nvidia image [nvcr.io/nvidia/deepstream:6.1.1-devel](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/deepstream). That image has deepstream 6.1.1 and tensorrt 8.4.1.5 installed, but it is missing packages to do the job. That's why I have made the image [maximofn/deepstream61:dev_1.0.3](https://hub.docker.com/layers/maximofn/deepstream61/dev_1.0.3/images/sha256-26b639c916465ac31de986079e901f303d55a293f9bbd8322731ff3dc1243f4f?context=repo), you can download it from [docker hub](https://hub.docker.com/layers/maximofn/deepstream61/dev_1.0.3/images/sha256-26b639c916465ac31de986079e901f303d55a293f9bbd8322731ff3dc1243f4f?context=repo) or you can build it with the [docker/Dockerfile](https://github.com/maximofn/ds_resnet50/blob/master/docker/Dockerfile) file.

Once you have the image downloaded or built you can enter it with the [docker/docker-compose.yml](https://github.com/maximofn/ds_resnet50/blob/master/docker/docker-compose.yml) file.

## Inside docker

**From here on everything I will explain will be done assuming you are already inside the docker container.**

### Create pytorch model and export it to ONNX
A pre-trained resnet50 Pytorch model must be created and exported to ONNX. In the file [generate_onnx.py](https://github.com/maximofn/ds_resnet50/blob/master/generate_onnx.py) a pre-trained resnet50 pytorch model is created and exported to ONNX. The code works, it will generate you the file "resnet50_pytorch_BS1.onnx", but the way it exports the model to ONNX I don't know if it is the right way.

### The job
Your job will be to change the way of exporting the model to ONNX (if necessary), then export it to engine and create the pipeline that takes the video from the webcam, makes the inference, writes on the video the class of the object that is being viewed and sends the video via UDP.
