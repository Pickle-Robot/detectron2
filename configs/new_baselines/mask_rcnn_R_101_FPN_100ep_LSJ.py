from .mask_rcnn_R_50_FPN_100ep_LSJ import (
    model,
)

model.backbone.bottom_up.stages.depth = 101
