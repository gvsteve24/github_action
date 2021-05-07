import torchvision

model = torchvision.models.segmentation.fcn_resnet50(pretrained=True, progress=True)

for key, value in dict(model.children()):
    print(key)