_base_ = './base_config.py'

# model settings
model = dict(
    name_path='./configs/cls_context60.txt',
    prob_thd=0.15
)

# dataset settings
dataset_type = 'PascalContext60Dataset'
data_root = './datasets/VOCdevkit/VOC2010'

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(2048, 336), keep_ratio=True),
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_prefix=dict(
            img_path='/data/dss/dataset/OVSS/VOCdevkit/VOC2010/JPEGImages',
            seg_map_path='/data/dss/dataset/OVSS/VOCdevkit/VOC2010/SegmentationClassContext'),
        ann_file='/data/dss/dataset/OVSS/VOCdevkit/VOC2010/ImageSets/SegmentationContext/val.txt',
        pipeline=test_pipeline))

#test_dataloader = dict(
#    batch_size=1,
#    num_workers=4,
#    persistent_workers=True,
#    sampler=dict(type='DefaultSampler', shuffle=False),
#    dataset=dict(
#        type=dataset_type,
#        data_root=data_root,
#        data_prefix=dict(
#            img_path='JPEGImages', seg_map_path='SegmentationClassContext'),
#        ann_file='ImageSets/SegmentationContext/val.txt',
#        pipeline=test_pipeline))