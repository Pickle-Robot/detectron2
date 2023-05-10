from ..common.train import train
from ..common.models.mask_rcnn_c4 import model

model.backbone.freeze_at = 2
train.init_checkpoint = "detectron2://ImageNetPretrained/MSRA/R-50.pkl"
