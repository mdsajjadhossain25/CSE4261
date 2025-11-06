# CSE 4261: Neural Network and Deep Learning

This repository contains all lab assignments and implementations for the course **CSE 4261: Neural Network and Deep Learning**.

## 📚 Course Overview

This repository showcases practical implementations of various deep learning architectures and techniques, covering fundamental to advanced topics in neural networks, computer vision, and natural language processing.

## 📂 Repository Structure

```
CSE4261/
├── Assignment-1/          # CNN Model Comparison on CIFAR100
├── Assignment-2/          # Activation Functions & Kernel Types Analysis
├── Assignment-3/          # Transfer Learning & Feature Extraction
├── Assignment-4/          # Manual Neural Network & Backpropagation
├── Assignment-5/          # Adversarial Attacks (FGSM)
├── Assignment-6/          # Explainable AI (Grad-CAM & Integrated Gradients)
├── Assignment-7/          # Object Detection with YOLO
├── Assignment-8/          # Semantic Segmentation & Crowd Counting
├── Assignment-9/          # Autoencoders & Data Augmentation
├── Assignment-10/         # Image Generation with Autoencoders
├── Assignment-11/         # Face Verification & VAE Loss Functions
├── Assignment-12/         # Knowledge Distillation
├── Assignment-13/         # Generative Adversarial Networks (GANs)
├── Assignment-14/         # Vision Transformers (ViT)
├── Assignment-15/         # BERT from Scratch
└── question.txt           # All assignment questions and requirements
```

## 🎯 Assignment Topics

### Assignment 1: CNN Architecture Comparison
- Performance comparison of 10 pre-trained CNNs on ImageNet
- Evaluation using 20 classes from CIFAR100 dataset
- Analysis of accuracy, model size, inference time, and hardware requirements

### Assignment 2: Activation Functions & Convolution Kernels
- Effect of different activation functions on CNN performance
- Analysis of regular, deformable, dilated, and depthwise separable kernels
- Feature map visualization across different layers

### Assignment 3: Transfer Learning & Dimensionality Reduction
- Feature extraction analysis using pre-trained CNNs
- Transfer learning from ImageNet to MNIST dataset
- 2D visualization using PCA, t-SNE, and UMAP

### Assignment 4: Manual Neural Network Implementation
- Hand-drawn neural network architecture design
- Forward and backward propagation computation graphs
- Manual derivation of weight update equations
- Implementation using `tf.GradientTape()` vs `model.fit()`

### Assignment 5: Adversarial Attacks
- Fast Gradient Sign Method (FGSM) implementation
- Adversarial examples generation on pre-trained CNNs
- Comparison with Gaussian noise-based attacks

### Assignment 6: Explainable AI
- Grad-CAM and Integrated Gradients implementation
- Analysis of adversarial examples
- Visualization of important image regions

### Assignment 7: Object Detection with YOLO
- Object detection comparison: YOLOv8, YOLOv11, YOLOv12
- Face detection fine-tuning on WIDER FACE dataset
- YOLOv1 implementation from scratch

### Assignment 8: Segmentation & Crowd Counting
- U-Net implementation for semantic segmentation
- U-Net for crowd counting
- MCNN (Multi-Column CNN) for crowd counting
- Comparative analysis of crowd counting approaches

### Assignment 9: Autoencoders & Data Augmentation
- Autoencoder as 2D feature generator for CIFAR10
- Comparison with CNN-extracted features (PCA, t-SNE)
- Denoising autoencoder implementation
- Impact of data augmentation on CNN classifiers

### Assignment 10: Image Generation with Autoencoders
- Image generation using normal Autoencoder decoder
- Image generation using Denoising Autoencoder decoder
- Variational Autoencoder (VAE) training and evaluation
- Synthetic image generation from latent space

### Assignment 11: Face Verification & VAE Loss Analysis
- Face verifiers with BCE, Contrastive, and Triplet loss
- VAE reconstruction loss comparison: BCE vs MSE
- Performance analysis across different loss functions

### Assignment 12: Knowledge Distillation
- Small CNN classifier training from scratch
- Fine-tuning pre-trained CNNs for 10-class classification
- Knowledge transfer from large to small models
- Multi-teacher knowledge distillation

### Assignment 13: Generative Adversarial Networks
- Deep Convolutional GAN (DCGAN) for face generation
- Conditional GAN (cGAN) for controlled image synthesis
- CycleGAN for image-to-image translation
- Mathematical derivation of GAN loss functions

### Assignment 14: Vision Transformers
- ViT classifier training on ImageNet subset (20 classes)
- Comparison: ViT vs FCFNN vs CNN
- Effect of attention heads on performance
- Impact of patch embedding strategies
- Positional embedding analysis

### Assignment 15: BERT from Scratch
- BERT model implementation and training
- Masked Language Modeling (MLM) task
- Fine-tuning for sentiment classification
- Question-answering on SQuAD dataset
- Semantic similarity on SNLI dataset

## 🛠️ Technologies & Frameworks

- **Deep Learning Frameworks:** TensorFlow, PyTorch
- **Computer Vision:** OpenCV, Ultralytics (YOLO)
- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **ML Tools:** scikit-learn, TensorBoard

## 📊 Datasets Used

- ImageNet
- CIFAR10 / CIFAR100
- MNIST
- WIDER FACE
- SQuAD (Stanford Question-Answering Dataset)
- SNLI (Stanford Natural Language Inference)
- Custom video datasets for object detection
- Various segmentation and crowd counting datasets

## 🚀 Key Concepts Covered

- **Neural Network Fundamentals:** Forward/backward propagation, gradient descent
- **Convolutional Neural Networks:** Various architectures and kernel types
- **Transfer Learning:** Feature extraction and fine-tuning
- **Adversarial Machine Learning:** Attack and defense mechanisms
- **Explainable AI:** Model interpretation techniques
- **Object Detection:** YOLO family of models
- **Semantic Segmentation:** U-Net architecture
- **Autoencoders:** VAE, denoising autoencoders
- **Generative Models:** GANs (DCGAN, cGAN, CycleGAN)
- **Attention Mechanisms:** Vision Transformers (ViT)
- **Natural Language Processing:** BERT, transformers
- **Model Compression:** Knowledge distillation
- **Loss Functions:** Custom loss design and analysis

## 📝 Assignment Deliverables

Each assignment folder typically contains:
- Jupyter notebooks with complete implementation
- Trained model weights (where applicable)
- Generated visualizations and plots
- Performance metrics and comparisons
- Detailed analysis and observations

## 📖 Documentation

- `question.txt` - Complete assignment questions and requirements
- Individual assignment folders contain implementation notebooks
- PDF reports with detailed discussions (in assignment PDF folder)

## 👨‍🎓 Course Information

- **Course Code:** CSE 4261
- **Course Title:** Neural Network and Deep Learning
- **Academic Year:** 2025

## 📧 Contact

For questions or discussions about the implementations, please refer to the course materials or contact through the appropriate academic channels.

---

**Note:** This repository is for educational purposes as part of the CSE 4261 course curriculum.
