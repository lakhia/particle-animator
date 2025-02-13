# Particle Animation Maker

## Introduction
This Python app uses Emitters to generate particles. The emitters and particles are animated via various physical forces such as acceleration, angular velocity, etc. This can be used to generate various animations.

## Methodology
The app uses numpy and plain arrays to manage emitters and particles. The drawing of lines, and various other shapes are done via pycairo and mathplotlib. The app does not generate the video directly. Instead, each frame is written out and an external tool such as `ffmpeg` can be used to make the final video. For example:

```shell
cd images; ffmpeg -y -pattern_type glob -i '*.png' -c:v libx264 -r 30 ../output.mp4; cd ..
```

## Command Line Options
When trying out patterns, you might want to consider using the `-d` option. This creates smaller output files that are useful for review but too small for 4K output. If you want to see animation develop quickly, you can also consider skipping frames using `-s 5` option. This will generate only the 5th frame.
