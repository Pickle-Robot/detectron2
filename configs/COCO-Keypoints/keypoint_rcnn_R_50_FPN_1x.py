from ..common.models.keypoint_rcnn_fpn import model
from ..common.train import train

model.backbone.bottom_up.freeze_at = 2
train.init_checkpoint = "detectron2://ImageNetPretrained/MSRA/R-50.pkl"
