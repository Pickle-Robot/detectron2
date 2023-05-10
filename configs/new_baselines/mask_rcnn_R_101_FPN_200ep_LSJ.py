from .mask_rcnn_R_101_FPN_100ep_LSJ import (
    lr_multiplier,
    train,
)

train.max_iter *= 2  # 100ep -> 200ep

lr_multiplier.scheduler.milestones = [
    milestone * 2 for milestone in lr_multiplier.scheduler.milestones
]
lr_multiplier.scheduler.num_updates = train.max_iter
