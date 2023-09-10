# 文件的作用
main.py 主函数
metric 训练的指标函数，主要是hausdorff_score，3d分割效果的指标，这个指标越高表示分割越精确
mytest.py test.py  和训练没啥关系，自己的测试代码
utils.py 包括了optimizer， scheduler优化器，以及数据导入相关的dataloader 和 dataset，以及自定义的loss
default_config.py 是基础配置
cfg_unet_multilabel.py 是更详细的配置，包括了数据增强的部分




