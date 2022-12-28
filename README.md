# Deepstream Resnet50

## Docker image
The first thing to do is to enter the docker container. The image to use is the nvidia image [nvcr.io/nvidia/deepstream:6.1.1-devel](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/deepstream). That image has deepstream 6.1.1 and tensorrt 8.4.1.5 installed, but it is missing packages to do the job. That's why I have made the image [maximofn/deepstream61](https://hub.docker.com/repository/docker/maximofn/deepstream61), you can download it from [docker hub](https://hub.docker.com/repository/docker/maximofn/deepstream61) or you can build it with the [docker/Dockerfile](https://github.com/maximofn/ds_resnet50/blob/master/docker/Dockerfile) file with this command

``` bash
cd docker
docker build -t maximofn/deepstream61:dev_1.0.7 .
```

Once you have the image downloaded or built you can enter it with the [docker/docker-compose.yml](https://github.com/maximofn/ds_resnet50/blob/master/docker/docker-compose.yml) file with this command

``` bash
docker compose up -d
```

## Inside docker

**From here on everything I will explain will be done assuming you are already inside the docker container.**

### Create pytorch model and export it to ONNX
A pre-trained resnet50 Pytorch model must be created and exported to ONNX. In the file [generate_onnx.py](https://github.com/maximofn/ds_resnet50/blob/master/generate_onnx.py) a pre-trained resnet50 pytorch model is created and exported to ONNX. The code works, it will generate you the file `resnet50_pytorch_BS1.onnx`, but the way it exports the model to ONNX I don't know if it is the right way.

### The job
Your job will be to change the way of exporting the model to ONNX (if necessary), then export it to engine and create the pipeline with deepstream on Python that:
 * Takes the video from the webcam
 * Makes the inference
 * Writes on the video the class of the object that is being viewed
 * Sends the video via UDP to 8554 port.
