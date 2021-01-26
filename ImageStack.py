# %% 
import glob
import os
import numpy as np
from pathlib import Path
from PIL import Image
# %% 
imagefilePath = glob.glob('*/*/*.tif')
for imagePath in imagefilePath:
    dataset = Image.open(imagePath)
    h, w = np.shape(dataset)
    numFrames = dataset.n_frames
    stepSize = 25
    framesKeep = np.arange(0, numFrames, stepSize)
    numKeep = len(framesKeep)
    tifKeep = np.zeros((h,w,numKeep))
    index = 0
    for frame in framesKeep:
        dataset.seek(frame)
        tifKeep[:,:,index] = np.array(dataset) 
        index += 1
    tifMin = np.min(tifKeep, axis = 2)  
    img = Image.fromarray(tifMin)

    saveName = imagePath.split('.')[0]
    saveName = saveName.split('\\')[-1]
    img.save(saveName + '.tif')
# %%
