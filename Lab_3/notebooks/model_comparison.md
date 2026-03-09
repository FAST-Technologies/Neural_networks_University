# Segmentation Models Comparison

|              | Category        |   mIoU (%) |   pixel_acc |   Time (ms) |   unique_classes |
|:-------------|:----------------|-----------:|------------:|------------:|-----------------:|
| maskformer   | Other           |        0.3 | 0.0121334   |        93.1 |                8 |
| segformer_b2 | Transformer     |        0.3 | 0.0100001   |        53.5 |                7 |
| dpt          | Hybrid          |        0.2 | 0.00798694  |       277.3 |               10 |
| mask2former  | Universal       |        0.2 | 0.00714049  |        85.7 |                8 |
| sam2         | Promptable      |        0.1 | 0.00496145  |      3610.6 |                8 |
| segformer    | Transformer     |        0.1 | 0.00562775  |       112.5 |                9 |
| deeplab_tv   | Other           |        0.1 | 0.0103318   |        76.2 |                1 |
| oneformer    | Multi-task      |        0.1 | 0.00513017  |       345.3 |                8 |
| sam          | Promptable      |        0.1 | 0.0015585   |      3284   |               22 |
| maskrcnn_tv  | Other           |        0.1 | 0.0103318   |        64.1 |                2 |
| upernet      | CNN+FPN         |        0.1 | 0.00308268  |       206.4 |                8 |
| segnet       | Encoder-Decoder |        0   | 3.14559e-05 |       247.7 |               23 |
| fcn_tv       | Other           |        0   | 0.000423225 |       271.9 |               36 |
| unet_smp     | Other           |        0   | 5.71925e-06 |       306.2 |               82 |
| fpn_mit      | Other           |        0   | 0           |       127.3 |               18 |