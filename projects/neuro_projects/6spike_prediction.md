## Project:
The topic is spike prediction for real neurons from the Allen Institute. You would fit a few classical single-neuron models to activity data, and try to see which ones are good fits, i.e. if they can predict held-out neural activity from input stimuli. See the .pdf file for more details.

## Data: 
The zipped folder contains an example data trace (.mat) for a layer-5 cell in visual cortex. That particular neuron can be checked out using their webpage [1], which hosts one of the best-documented and -presented datasets I know of. The data comes as voltage traces, but can spikes here can be obtained from just thresholding the voltages. The input stimulus is a time-dependent input current injected into the cell. The project can be done with that one provided layer-5 cell, but for testing the robustness of the algorithms you can download more data from other cells using the provided notebook as a template (just download the Allen package [2]). 

## Models: 
I would start out with the Generalized Linear Model (GLM) [3], since it is one of the more widely-used approaches. Recall we also had another (short) project on GLMs, which could serve as a start. Both for GLMs and other models, it is up to you to decide if you want to fully implement fitting algorithms yourselves, or if you want to find and use existing packages [say, 4]. Either way will be good exercise for work in computational neuroscience. We compiled a selection of papers that is meant to guide your choice on which neuron models to try. 

## Scope:
This topic is built on another project our lab designed for the CCCN summer school for computational neuroscience in Lisbon (which is awesome, consider applying!). That summer school is a three-week intensive course where students work in teams of two or three, so we do *not* expect you guys to go through all mentioned models and methods. The project is phrased open-ended - anything you can accomplish within the next two weeks is good. The final type of algorithms mentioned in the .pdf ('likelihood-free') is something we develop in our lab [5], so this might be worth a look if you're thinking about doing a rotation with us. 

## References
[1] http://celltypes.brain-map.org/mouse/experiment/morphology/464212183

[2] http://alleninstitute.github.io/AllenSDK/install.html

[3] www.marlenemueller.de/publications/HandbookCS.pdf

[4] https://github.com/madrury/py-glm

[5] http://www.mackelab.org/delfi/notebooks/quickstart.html

