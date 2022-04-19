---
layout: post
title: Vision-Anomaly Detection
subtitle: Machine vision systems in industrial applications
subsubtitle: Machine vision systems in industrial applications.
date: 2021-12-01
description: This post introduce energy-based model 
author: Anthony Faustine 
image: ebm.jpg
---

Machine learning and, specifically, computer vision have demonstrated performance near human-level in many real-world applications. As a result, computer vision algorithms are replacing human supervision in different applications domains such as medical diagnosis, controlling the manufacturing process, and traffic surveillance. Anomaly detection is a fundamental computer vision problem that identifies instances in visual data such as images that deviate from the norm samples. Consequently, vision anomaly detection is vital for most computer vision applications interacting with the physical world, such as visual inspection, robotic guidance and control [1]–[3] in industries and manufacturing processes. Other use-cases include detecting and quantifying diseases from medical imaging data[8] and deciding when to delegate high-risk predictions for human intervention.  

Most of the existing machine learning methods for anomaly detection have focused on low-dimension space, such as time-series signals. Such techniques face difficulties when applied to high-dimensional data such as images [4]. On the other hand, computer vision methods based on deep-learning excel in many computer vision tasks such as image classification and object detection. As a result, deep learning-based anomaly detection algorithms for vision applications have become increasingly popular [2], [3], [5]–[7].

Vision anomaly detection approaches based on deep learning can be categorized into three methods: reconstruction-based, deep hybrid, and confidence-based. 

**Reconstruction-based**: Learn AD from scratch,  utilising the representation-learning ability of deep generative models such as autoencoders and GANS, with an assumpition that  the difference between normal and anomaly instances is embedded in a lower-dimensional subspace. 







   


