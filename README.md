# FocalForge
Redefine Your Focus with FocalForge


![logo-png](https://github.com/Ashwinr-07/FocalForge/assets/105007681/f3955dae-7018-41d2-a7f6-85ab447e8ff1)


Depth based Image Refocussing

<img width="475" alt="image" src="https://github.com/Ashwinr-07/FocalForge/assets/105007681/470533c8-b897-41d9-b132-316686e4b866">




This project explores the task of image refocusing, allowing users to adjust the focus and depth of field in a single image after it has been captured. It utilizes Depth Prediction Transformers (DPTs) to estimate depth maps from input images and applies various image processing techniques to simulate focus adjustments.

## Dataset
The dataset comprises 200 unique records, each containing the following images:
- Ultra-wide-angle image
- Shallow-focused image
- Deep-focused image
- Normal image
- Depth map generated using a DPT model

  A Record in our Dataset
  <img width="462" alt="image" src="https://github.com/Ashwinr-07/FocalForge/assets/105007681/eb3e7b56-c921-4ccb-b6f0-e93edc315ef4">


The images were captured using a Samsung Galaxy S22 smartphone with a stereo camera setup.

## Implementation
The implementation follows these steps:

1. **Depth Map Generation**: Utilizes a Depth Prediction Transformer (DPT) model to generate depth maps from input images.
2. **Depth Map Enhancement**: Enhances the quality of generated depth maps through contrast stretching and sharpening.
3. **Mask Creation**: Creates a mask based on the enhanced depth map, identifying regions to be blurred or focused.
4. **Focus Adjustment**: Applies the mask to the original image and selectively applies Gaussian blur to either the masked or unmasked regions, depending on desired focus.

DPT Architecture

<img width="535" alt="image" src="https://github.com/Ashwinr-07/FocalForge/assets/105007681/27030550-0be5-475a-84da-eed6fe564d56">



The processing pipeline is implemented in Python using libraries such as PIL, OpenCV, and scikit-image.

## Evaluation Metrics
The project explores several evaluation metrics to assess the quality of refocused images, including:
- Structural Similarity Index (SSIM)
- Peak Signal-to-Noise Ratio (PSNR)
- Learned Perceptual Image Patch Similarity (LPIPS)

These metrics provide quantitative measures of image similarity and quality, facilitating comparison between original and refocused images.

![Animated GIF](https://github.com/Ashwinr-07/FocalForge/raw/main/static/ezgif.com-animated-gif-maker.gif)





## Usage
To use this implementation, follow these steps:

1. Clone the repository:
    ```bash
    https://github.com/Ashwinr-07/FocalForge.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Prepare your input images and place them in the appropriate directory.



Ensure to replace `/path/to/input/images` with the directory containing your input images and `/path/to/output/dir` with the desired output directory.
