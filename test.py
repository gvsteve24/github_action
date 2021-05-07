import torchvision

model = torchvision.models.segmentation.fcn_resnet50(pretrained=True, progress=True)

for module in list(model.children()):
    print(module)