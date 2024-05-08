[![DOI](https://zenodo.org/badge/599280727.svg)](https://zenodo.org/badge/latestdoi/599280727)

# Human Basal Forebrain (BF) Multimodal Connectivity 

This repository contains codes and data in support of the paper (tentative) "Multimodal gradients of human basal forebrain connectivity" 

## Publications

Preprint: [Multimodal gradients of human basal forebrain connectivity](https://www.biorxiv.org/content/10.1101/2023.05.26.541324v1)

## Prerequisites

BF roi used is included in the data folder. This roi is created based on the [probabilistic atlas](https://pubmed.ncbi.nlm.nih.gov/18585468/).
All diffusion and functional data used for this study is downloded from [Human Connectome (HCP) project](http://www.humanconnectomeproject.org/).
The structural (diffusion) connectivity matrix is created using this [workflow](https://github.com/sudesnac/diffparc-smk). 
The functional connectivity matrix is created using this [workflow](https://github.com/khanlab/subcorticalparc-smk).
These workflow will create a .npz file containing all subject's connectivity matrices - the files should be placed in the data folder for running the analyses provided in the notebook. 

## Data

Contains the following data file necessary to run the analysis provided in the notebooks.\
**BF roi**: _seed_1p6mm.nii.gz_ - used to construct the connectivity matrices and compute the gradients across BF.\
**BF segmented roi**: _BF_masked_fullB_1p6mm.dseg.nii.gz_ - ch123 and ch4a/ch4p labeled roi used for statistical analysis.\
**HCP-MMP1 annot files**: *{lh,rh}_HCP-MMP1_fsa10.annot* - HCP-MMP1 parcellation annotation files in fsa-10k space for [brainspace](https://brainspace.readthedocs.io/en/stable/index.html) visualization.\
**Yeo network**: *hcp_mmp10_yeo7_modes.txt* - reference for Yeo 7 network mapped onto HCP-MMP1 parcellation from [here](https://pubmed.ncbi.nlm.nih.gov/30793087/).\
**Glasser 360 fsa5 label files**:_glasser_360_fsaverage5_{lh,rh}label.gii_ - Glasser parcellation labels in fsa10k for parcellating whole brain data (such as the geodesic, myelin and FEOBV data).\
**BF surface label**:_seed-BASF.{L,R}.bin.fsa5.shape.gii_ - BF seed label in surface space (see Methods section of the publication for the details of creating this file).\
**Geodesic distance files**:_seed-BASF_geodesic-distance-no-zeros.pial.{lh,rh}.shape.gii_ - BF-cortical geodesic distance (see Methods section of the publication for the details).\
**Myelin map**:_source-hcps1200_desc-myelinmap_space-fsaverage5_den-10k_hemi-{L,R}_feature.func.gii_ - T1w/T2w ratio as a proxy measure myelin maps used in this study.

## Code

Python code for computing geodesic distance is provided here. 

## Notebooks and Results

The notebook folder contains the following jupyter notebooks for running the analysis and creating the figures used in this paper.\
The results folder has sub-folders each containing respective resultant data (such as .nii.gz and .gii files) and figures inside the figures folder. Reference surface for fsa-10k can be downloaded from [here](https://github.com/MICA-MNI/BrainSpace/tree/master/brainspace/datasets/surfaces) for visualizing gii results files using workbench.

### Diff_gradients

This notebook contains the code to compute diffusion gradients, diffusion gradient-weighted cortical maps, statistical analysis of the gradients against the histologically defined subregions and respective figures (Fig. 2A,C,D left). 

### Func_gradients

This notebook contains the code to compute functional gradients, functional gradient-weighted cortical maps, statistical analysis of the gradients against the histologically defined subregions and respective figures (Fig. 2A,C,D right).

### g-wCtx_networks

This notebook is used to compute the distribution of cortical gradient-weighted values (diffusion and functional) decomposed into seven functional networks as defined by [Yeo 2011](https://journals.physiology.org/doi/full/10.1152/jn.00338.2011). 

### gradient_correlation

This notebook is for calculating gradient correlations betweeen the diffusion and functional gradients and computing the weighted residuls in BF as well as cortical space. (see Methods section of the publication for the details of this calculation.) (Fig.2E,F, and Fig.3)

### connectivity_distance

This notebook contains visualization of fiber length, geodesic distance and FEOBV data; parcellation and rescaling of these data as well as correlation (scatter plots and spin tests using null model) of these maps with other connectivity and residual data. (Fig. 4,5,6 and 8)

### extra_analysis

This notebook contains cross-validation analyses  (split-half or leave-one-out) across the 173 individuals used (Supplemental Fig. 3 and 4)
