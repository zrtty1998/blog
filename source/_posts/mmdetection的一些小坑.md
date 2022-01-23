---
title: mmdetection的一些小坑
reprint: false
cover:
date: 2022-01-23 12:46:21
updated: 2022-01-23 12:46:21
categories: 环境搭建
tags:
  - mmdetection
  - 目标检测
---


# 安装

pip install mmcv-full==1.3.9 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html

pip install mmcv-full==1.3.9 -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.7.0/index.html

修改完后，需要重新编译（python setup.py install)

pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/{torch_version}/index.html

pip install mmcv-full==1.3.3 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.8.0/index.html 

pip install -r requirements/build.txt
python setup.py develop



# 修改数据集为coco格式

目录格式：

```
mmdetection
├── mmdet
├── tools
├── configs
├── data
│   ├── coco
│   │   ├── annotations
│   │   ├── train2017
│   │   ├── val2017
│   │   ├── test2017
```

修改相关文件：

[(4条消息) mmdetection自定义数据集进行训练_xiangxianghehe的博客-CSDN博客_mmdetection 训练数据集](https://blog.csdn.net/xiangxianghehe/article/details/89812058#commentsedit)





# 常用命令

## 测试与训练

python tools/test.py configs/faster_rcnn/faster_rcnn_r50_fpn
_1x_coco.py checkpoints/epoch_2.pth --show

python tools/train.py configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py

python tools/test.py configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py checkpoints/{model}/latest.pth --out results/{model}/results.pkl --show-dir results/

```
python tools/test.py configs/fcos/fcos_r50_caffe_fpn_gn-head_1x_coco.py checkpoints/latest.pth --out results/fcos_r50_caffe_fpn_gn-head_1x_coco/results.pkl --show-dir results/
```

## train参数

This tool accepts several optional arguments, including:

- `--no-validate` (**not suggested**): Disable evaluation during training.
- `--work-dir ${WORK_DIR}`: Override the working directory.
- `--resume-from ${CHECKPOINT_FILE}`: Resume from a previous checkpoint file.
- `--options 'Key=value'`: Overrides other settings in the used config.

## 查看config

python tools/misc/print_config.py configs/zr/zr_fcos_r50_caffe_fpn_gn-head_1x_coco.py

## 学习率配置

X：我的一个batchsize输入图像数量
Y：mmdetction一个batchsize输入图像数量
Z：默认学习率

新的学习率= （X/Y）x Z
如：
X：1GPU+2img/GPU=2张
MMdet默认是8GPU*2img/GPU=16张
MMdet默认学习率=0.02
新的学习率=0.0025



为了克服数据量多的问题，我们会选择将数据分成几个部分，即batch，进行训练，从而使得每个批次的数据量是可以负载的。将这些batch的数据逐一送入计算训练，更新神经网络的权值，使得网络收敛。

一个epoch指代所有的数据送入网络中完成一次前向计算及反向传播的过程。由于一个epoch常常太大，计算机无法负荷，我们会将它分成几个较小的batches。

所谓Batch就是每次送入网络中训练的一部分数据，而Batch Size就是每个batch中训练样本的数量

所谓iterations就是完成一次epoch所需的batch个数。

简单一句话说就是，我们有2000个数据，分成4个batch，那么batch size就是500。运行所有的数据进行训练，完成1个epoch，需要进行4次iterations。

# TOOLS

## Log Analysis

`tools/analysis_tools/analyze_logs.py` plots loss/mAP curves given a training log file. Run `pip install seaborn` first to install the dependency.

```
python tools/analysis_tools/analyze_logs.py plot_curve [--keys ${KEYS}] [--title ${TITLE}] [--legend ${LEGEND}] [--backend ${BACKEND}] [--style ${STYLE}] [--out ${OUT_FILE}]
```

- ```
  python tools/analysis_tools/analyze_logs.py plot_curve work_dirs/faster_rcnn_r50_fpn_1x_coco/20210809_105106.log.json --keys loss_cls --legend loss_cls
  ```

- ```
  python tools/analysis_tools/analyze_logs.py plot_curve work_dirs/faster_rcnn_r50_fpn_1x_coco/20210809_105106.log.json --keys bbox_mAP --legend bbox_mAP
  ```

## Result Analysis

`tools/analysis_tools/analyze_results.py` calculates single image mAP and saves or shows the topk images with the highest and lowest scores based on prediction results.

Usage:

```
python tools/analysis_tools/analyze_results.py \
      ${CONFIG} \
      ${PREDICTION_PATH} \
      ${SHOW_DIR} \
      [--show] \
      [--wait-time ${WAIT_TIME}] \
      [--topk ${TOPK}] \
      [--show-score-thr ${SHOW_SCORE_THR}] \
      [--cfg-options ${CFG_OPTIONS}]
```

Description of all arguments:

- `config` : The path of a model config file.
- `prediction_path`: Output result file in pickle format from `tools/test.py`
- `show_dir`: Directory where painted GT and detection images will be saved
- `--show`：Determines whether to show painted images, If not specified, it will be set to `False`
- `--wait-time`: The interval of show (s), 0 is block
- `--topk`: The number of saved images that have the highest and lowest `topk` scores after sorting. If not specified, it will be set to `20`.
- `--show-score-thr`: Show score threshold. If not specified, it will be set to `0`.
- `--cfg-options`: If specified, the key-value pair optional cfg will be merged into config file

Examples:

Assume that you have got result file in pickle format from `tools/test.py` in the path ‘./result.pkl’.

Test Faster R-CNN and visualize the results, save images to the directory `results/`

```
python tools/analysis_tools/analyze_results.py configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py result.pkl results --show
```

Test Faster R-CNN and specified topk to 50, save images to the directory `results/`

```
python tools/analysis_tools/analyze_results.py \
       configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
       result.pkl \
       results \
       --topk 50
```

If you want to filter the low score prediction results, you can specify the `show-score-thr` parameter

```
python tools/analysis_tools/analyze_results.py \
       configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
       result.pkl \
       results \
       --show-score-thr 0.3
```

```
python tools/analysis_tools/eval_metric.py configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py result.pkl 
```

