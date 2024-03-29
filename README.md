# ez_img_diff

*A tool for doing quick percieved image difference analysis*


## What does ez_img_diff do?

ez_img_diff is a CLI and api for doing a simple form of percieved image difference analysis with SSIM. This allows for tons of features, but the main one is being able to compare some sort of "baseline" image of an application to a "current" itteration in visual regression testing. 

Down the road I will write a selenium integration to tie this whole process together!

## Why should I use ez_img_diff?

There are a ton of great and more robust tools out there for this analysis, or for visual regression testing, but I found each of them had their own problems, here's a list:

|Package|Issue|
|-------|-----|
|[needle](https://github.com/python-needle/needle)| Requires a Nose test runner, and had out of date dependencies|
|[pytest-needle](https://github.com/jlane9/pytest-needle) | Works well, but cannot use [webdiver_manager](https://pypi.org/project/webdriver-manager/) with it | 
|[dpxdt](https://github.com/bslatkin/dpxdt) | Didn't test, but was 7 years old and mostly focused on CI/CD usage|
|[Visual Regression Tracker](https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker) | Works great, but for some of my use cases I need an API not a full application|
|[hermione](https://github.com/gemini-testing/hermione)|Could not use javascript/nodeJS for my use case|
|[specter](https://github.com/letsgetrandy/specter)|Could not use javascript/nodeJS for my use case|
|[Cypress-image-screenshot](https://github.com/jaredpalmer/cypress-image-snapshot)|Could not use javascript/nodeJS for my use case|


## Quick-start

### Installation

#### From source

1. Clone this repo: [https://github.com/Descent098/ez-img-diff](https://github.com/Descent098/ez-img-diff)
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory

#### From PyPi

1. Run ```pip install ez_img_diff```

## Examples

### API Examples

#### Compare 2 images without saving difference files
```python
from ez_img_diff.api import compare_images

img1 = "baseline.png"
img2 = "current.png"

compare_images(im1, img2) # 14.03
```

#### Compare 2 images with saving difference and threshold files
```python
from ez_img_diff.api import compare_images

img1 = "baseline.png"
img2 = "current.png"

compare_images(im1, img2, "difference.png", "threshold.png") # 14.03
```

### CLI Usage

```bash
ez img diff

A tool for doing quick perceptual image difference analysis

Usage: 
    img_diff [-h] [-v]
    img_diff (<img1> <img2>) [-o OUTPUT_FOLDER] 

Options:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -o OUTPUT_FOLDER, --output OUTPUT_FOLDER 
                        the folder to output difference files to
```

so for example to get the diff of two images use:

```bash
$> img_diff baseline.png current.png
14.03
```

You can then store the diff and threshold of the two images with:

```bash
$> img_diff baseline.png current.png -o results
14.03

$> cd results && ls
diff.png
thresh.png
```

#### Notes

Some things to keep in mind:

- Output folder will have 2 files in it `diff.png` and `thresh.png`
  - `diff.png` is the regular difference png, which shows where things differ
  - `thresh.png` is the threshold png, which is much higher contrast and shows you where the biggest changes happened more clearly

## How the system works

In the interest of promoting learning here is some detail on how the system works. It is largely adapted from [this post](https://pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/), I would highly recommend reading and downloading their resource guide for even more details!

Primarily it works on computer vision, and a library called [opencv-python](https://pypi.org/project/opencv-python/), which is a python port of a computer vision toolkit called [opencv](https://opencv.org/). Without getting into the math too much it uses computer vision combined with [SSIM](https://www.imatest.com/support/docs/23-1/ssim/#:~:text=Introduction%20%E2%80%94%20The%20Structural%20Similarity%20Index,by%20losses%20in%20data%20transmission.). SSIM is a percieved quality analysis metric that tends to be used to benchmark how well compression systems retain the original image quality. We can use the same principle to help with regression testing by using it to compare the "quality differences" between two images (a baseline, and a current itteration), to be able to tell the percieved differences between them. This comparison is provided by [scikit-image](https://scikit-image.org/).

With opencv we also end up mostly dealing with arrays of numbers representing each pixel in an image. Working with these types is hard so we use [imutils](https://pypi.org/project/imutils/) to work with these values more effectively!

