# Session 12 - Tiny ImageNet and YOLO v2 Anchor Boxes

## Part 1 - ResNet18 on Tiny ImageNet Dataset


The model reaches a maximum accuracy of **55.42%** on Tiny-ImageNet using **ResNet 18** model.

### Parameters and Hyperparameters

- Loss Function: Cross Entropy Loss (combination of `nn.LogSoftmax` and `nn.NLLLoss`)
- Optimizer: SGD
  - Momentum: 0.9
  - Learning Rate: 0.01
- Reduce LR on Plateau
  - Patience: 2
  - Factor: 0.1
  - Min LR: 1e-6
- Epochs: 50
- Batch Size: 128

### Data Augmentation

The following data augmentation techniques were applied to the dataset during training:

- Horizontal Flip
- Vertical Flip
- Random Rotate
- CutOut

### Change in Training and Validation Accuracy

<img src="images/accuracy_change.png" width="450px">

## Part 2 - Finding YOLO v2 Anchor Boxes


### Plot of Number of clusters vs Mean IoU

![kmeans_iou](images/kmeans_iou.png)

After running the algorithm on the dataset, it was found that the best k can have the value of 3 or 4.

| Number of Clusters (k) | Mean IoU |                  Cluster Plot                  |                 Anchor Boxes                 |
| :--------------------: | :------: | :--------------------------------------------: | :------------------------------------------: |
|           3            |   0.75   | ![cluster_plot_k3](images/cluster_plot_k3.png) | ![anchor_bbox_k3](images/anchor_bbox_k3.png) |
|           4            |   0.79   | ![cluster_plot_k4](images/cluster_plot_k4.png) | ![anchor_bbox_k4](images/anchor_bbox_k4.png) |



