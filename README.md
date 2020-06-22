# Local Versus Global Features in Convolutional Neural Networks

Interactive notebooks and python code for my Master's Thesis: "The Role of Local Versus Global Features in Convolutional Neural Networks" at the [University of Bamberg](https://www.uni-bamberg.de/en/).

See [this blog post](https://www.maltebuettner.com/post/master/) for a brief summary of the thesis.

## Abstract
The current state of the art Convolutional Neural Networks (CNNs) were shown to oper-
ate mostly by means of texture bias, whereas humans operate mostly on a shape bias. While
the ImageNet challenge led to several milestones in the advancement of the field, recent
publications question the suitability of ImageNet as a single criterion for evaluating a net-
work’s performance. Additionally, since local features are sufficient to solve ImageNet
comparatively well, ImageNet may be too "easy". In "ImageNet-trained CNNs are biased
towards texture; increasing shape bias improves accuracy and robustness" [Geierhos et
al.](https://arxiv.org/abs/1811.12231) [1] introduce stylized training – an augmentation
technique that aims to constrain a network to learn shapes –
in an effort to closer align CNNs with human vision.
Geierhos et al. report close to human shape bias in their experiments. Amongst others, however,
the small influence of stylized training on ImageNet-A, a dataset that should be solvable
with a distinctive shape bias, calls these claims into question.
This thesis aims to take a look inside the black box of a stylized trained ResNet-50, to test
whether prerequisites for a shape bias are satisfied and if the network relies on shape re-
gion in its classification process. Experiments show that a ResNet-50 trained on Stylized-
ImageNet is only in some cases superior to a ResNet-50 trained on standard ImageNet
regarding the prerequisites and that architectural refinements such as SE-ResNeXts might
be a more promising alternative.

### Usage
Due to the complex nature of the experiments, each step has its own notebbok. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mbuet2ner/local-global-features-cnn/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mbuet2ner/local-global-features-cnn/master)
1. In [1_imagenet_boundingboxes](1_imagenet_boundingboxes.ipynb) a one easy to work with file with ImageNet's bounding boxes is created.
2. [2_imagenette_boundingboxes](2_imagenette_boundingboxes.ipynb) adapts these bounding boxes to Imagenette and calculates the correct sizes of the boxes when resized to `256` and then center cropped to `224`.
3. [3_canny_edges.ipynb](3_canny_edges.ipynb) creates a file that contains Canny edge coordinates for Imagenette using a custom `auto-canny` function. A reduced file with coordinates that lie within the respective bounding box is also created. These Canny edges later serve as a proxy for shape.
4. In [4_create_datasets](4_create_datasets.ipynb) the "smoothed", "scrambled", and "patched" datasets are created from Imagenette input files.
5. The fifth step is concerned with the actual experiments and broken down in multiple sub-steps. First, [5_run_experiments](5_run_experiments.ipynb) runs the experiments on the created datasets. This does, however, not include the LRP and Canny edge experiments.
    * 5.1. For the aforementioned experiments to work, the PyTorch models need to be converted to Keras using [5.1_pytorch2keras](5.1_pytorch2keras.ipynb).
    * 5.2. In [5.2_lrp_regions](5.2_lrp_regions.ipynb) the LRP regions are calculated for both the Stylenet and the standard ResNet-50.
    * 5.3. [5.4_lrp_canny](5.4_lrp_canny.ipynb) combines the LRP coordinates with the Canny edge coordinates to check for overlaps.
6. [6_experiment_analysis](6_experiment_analysis.ipynb) contains the general analysis of the experiments and the accompanying plots.


### Requirements
under construction

## References
[1] Geirhos, Robert, et al. "ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness." arXiv preprint arXiv:1811.12231 (2018).
