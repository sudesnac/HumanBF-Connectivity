# Human Basal Forebrain (BF) Multimodal Connectivity 

This repository contains codes and data in support of the paper (tentative) "Multimodal gradients of human basal forebrain connectivity" 

## Publications

{Link to preprint DOI, publication DOI once it's ready...}

## Prerequisites

BF roi used is included in the data folder. This roi is created based on the [probabilistic atlas](https://pubmed.ncbi.nlm.nih.gov/18585468/).
All diffusion and functional data used for this study is downloded from [Human Connectome (HCP) project](http://www.humanconnectomeproject.org/).
The structural (diffusion) connectivity matrix is created using the [workflow](https://github.com/sudesnac/diffparc-smk). 
The functional connectivity matrix is created using the [workflow](https://github.com/khanlab/subcorticalparc-smk).
These workflow will create a .npz file containing all subject's connectivity matrices - the files should be placed in the data folder for running the analysis provided in the notebook. 

## Data

Contains the following data file necessary to run the analysis provided in the notebooks.\
BF roi: seed_1p6mm.nii.gz - used to construct the connectivity matrices and compute the gradients across BF.\
BF segmented roi: BF_masked_fullB_1p6mm.dseg.nii.gz - ch123 and ch4a/ch4p labeled roi used for statistical analysis.\
Yeo network: hcp_mmp10_yeo7_modes.txt - reference for Yeo 7 network mapped onto HCP-MMP1 parcellation from [here](https://pubmed.ncbi.nlm.nih.gov/30793087/). 

## Code

Python code for computing geodesic distance is provided here. 

## Notebooks and Results

The notebook folder contains the following jupyter notebooks for running the analysis and creating the figures used in this paper.\
The results folder has sub-folders each containing respective resultant data (such as .nii.gz and .gii files) and figures inside the figures folder. Reference surface for fsa-10k can be downloaded from [here](https://github.com/MICA-MNI/BrainSpace/tree/master/brainspace/datasets/surfaces) for visualizing gii results files using workbench.

### Diff_gradients

This notebook contains the code to compute diffusion gradients, diffusion gradient-weighted cortical maps, statistical analysis of the gradients against the histologically defined subregions and respective figures (Fig. 1B,C,D left and Fig. 2A top). 
{More detailed description of this notebook, what data is required to run through it, any changes users will need to make to paths and that kind of thing...}

### Func_gradients

{Same as Notebook 1}

### g-wCtx_networks

{Same as Notebook 1}

### gradient_correlation

{Same as Notebook 1}

### connectivity_distance

{Same as Notebook 1}
