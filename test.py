import torchvision

model = torchvision.models.segmentation.fcn_resnet50(pretrained=True, progress=True)

for key in model.children().keys():
    print(key)