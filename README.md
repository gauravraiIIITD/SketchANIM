# SketchAnim: Real-time sketch animation transfer from videos
*Animation of hand-drawn sketches is an adorable art. It allows the animator to generate animations with expressive freedom and requires significant expertise. In this work, we introduce a novel sketch animation framework designed to address inherent challenges, such as motion extraction, motion transfer, and occlusion. The framework operates on a video input featuring a moving object, utilizing a robust motion transfer technique to animate the corresponding sketch. Comparative evaluations demonstrate the superior performance of our method over existing sketch animation techniques. Notably, our approach exhibits a higher level of user accessibility in contrast to conventional sketch-based animation systems, positioning it as a promising contributor to the field of sketch animation.*

### Workflow:

<img src="/assets/pipeline.png" style="zoom:10%;" />

### Setup:

```
git clone https://github.com/graphics-research-group/SketchAnimation-vid2sketch.git
cd SketchAnimation-vid2sketch
```

### Installation:

```
conda env create -f environment.yml
```

Next, need to install [co-tracker](https://github.com/facebookresearch/co-tracker.git) and [DeformationPyramid](https://github.com/rabbityl/DeformationPyramid.git).

```
git clone https://github.com/facebookresearch/co-tracker.git
git clone https://github.com/rabbityl/DeformationPyramid.git
```

Download the shared library for bbw wrapper from [here](https://drive.google.com/drive/folders/1KvePZ8urGLwaywVXROZquLJT4y9ayp-n?usp=drive_link).


### Draw a skeleton:

Draw the skeleton on the first frame (rest pose) of the video. 

```
python gui.py
```



| <img src="/assets/skeleton.gif"  /> |
| -------------------------------------------------- |

### Animate a sketch:

Run the following notebook to generate the final animation with their intermediate results. Users can use custom hand-drawn sketches or find our sketch dataset [here](https://drive.google.com/drive/folders/1Lm03H5WdVp_T5zErNa_XraWeYvSu4xUp?usp=drive_link).

```
python main.ipynb
```

### Results:

| ![](/assets/biped1.gif) | ![](/assets/biped2.gif) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](/assets/quadruped2.gif) | ![](/assets/quadruped1.gif) |
| ![](/assets/inanimate1.gif) | ![](/assets/inanimate2.gif) |




### Acknowlegement:

This project is supported by TiH anubhuti IIIT Delhi.
