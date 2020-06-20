# Local Versus Global Features in Convolutional Neural Networks

Interactive notebooks and python code for my Master's Thesis: "The Role of Local Versus Global Features in Convolutional Neural Networks".

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
under constuction

### Requirements
under construction

## References
[1] Geirhos, Robert, et al. "ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness." arXiv preprint arXiv:1811.12231 (2018).
