import torchvision
import torch
from torch.onnx import OperatorExportTypes

model = torchvision.models.resnet50(weights=torchvision.models.ResNet50_Weights.DEFAULT)

# Export to ONNX.
# The code below works, it generates an ONNX model, but I don't know if 
# this is the right way to do it and then export it to engine and make it work in a 
# deepstream pipeline.
BATCH_SIZE=1
onnx_file = f"resnet50_pytorch_BS{BATCH_SIZE}.onnx"
dummy_input=torch.randn(BATCH_SIZE, 3, 224, 224)
torch.onnx.export(model, dummy_input, onnx_file, verbose=False, input_names=["input"], output_names=["output"], operator_export_type=OperatorExportTypes.ONNX_ATEN_FALLBACK)
print("Done exporting to ONNX")