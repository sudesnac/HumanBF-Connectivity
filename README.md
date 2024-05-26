[![DOI](https://zenodo.org/badge/599280727.svg)](https://zenodo.org/badge/latestdoi/599280727)

# Human Basal Forebrain (BF) Multimodal Connectivity 

This repository contains codes and data in support of the paper (tentative) "Multimodal gradients of human basal forebrain connectivity" 

## Publications

Preprint: [Multimodal gradients of human basal forebrain connectivity](https://www.biorxiv.org/content/10.1101/2023.05.26.541324v3)

## Prerequisites

BF roi used is included in the data folder. This roi is created based on the [probabilistic atlas](https://pubmed.ncbi.nlm.nih.gov/18585468/).
All diffusion and functional data used for this study is downloded from [Human Connectome (HCP) project](http://www.humanconnectomeproject.org/).
The structural (diffusion) connectivity matrix is created using this [workflow](https://github.com/sudesnac/diffparc-smk). 
The functional connectivity matrix is created using this [workflow](https://github.com/khanlab/subcorticalparc-smk).
These workflow will create a .npz file containing all subject's connectivity matrices - the files should be placed in the data folder for running the analyses provided in the notebooks. 

## Data

Contains the following data file necessary to run the analysis provided in the notebooks.
| **Data**                         | **File**                                                                            | **Description**                                                                                                                                                                                                                                         |
|----------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BF ROI                           | `seed_1p6mm.nii.gz`                                                                   | Used to construct the connectivity matrices and compute the gradients across the BF                                                                                                                                                                     |
| BF segmented ROI                 | `BF_masked_fullB_1p6mm.dseg.nii.gz`                                                   | Ch123 and Ch4a/Ch4p labeled ROI used for the statistical analysis                                                                                                                                                                                       |
| HCP-MMP1 annotation files        | `{lh,rh}_HCP-MMP1_fsa10.annot`                                                        | HCP-MMP1 parcellation annotation files in fsa10k space for [BrainSpace](https://brainspace.readthedocs.io) visualization                                                                                                                                                                     |
| Yeo network                      | `hcp_mmp10_yeo7_modes.txt`                                                            | Reference for Yeo 7 network mapped onto HCP-MMP1 parcellation from [here](https://doi.org/10.1162/netn_a_00068)                                                                                                                                                                                 |
| HCP-MMP1 fsa5 label files        | `glasser_360_fsaverage5_{lh,rh}label.gii`                                              | HCP-MMP1 parcellation labels in fsa10k for parcellating whole brain data (such as the geodesic, myelin and FEOBV data)                                                                                                                                  |
| BF surface label                 | `seed-BASF.{L,R}.bin.fsa5.shape.gii`                                                  | BF seed label in surface space (see Methods section of the publication for the details of creating this file)                                                                                                                                           |
| Geodesic distance map            | `seed-BASF_geodesic-distance-no-zeros.pial.{lh,rh}.shape.gii`                         | BF-cortical geodesic distance (see Methods section of the publication for the details)                                                                                                                                                                  |
| Myelin map                       | `source-hcps1200_desc-myelinmap_space-fsaverage5_den-10k_hemi-{L,R}_feature.func.gii` | T1w/T2w ratio as a proxy measure myelin maps used in this study                                                                                                                                                                                         |
| Streamline counts                | `Diff_streamline-counts_summed_seed-BASF_voxels.xlsx`                                 | Excel file detailing the streamlines recieved by the cortical parcels from the BF                                                                                                                                                                       |
| Human and Mouse cross-validation | `Figure7G_Mouse_Human_PET_rawData.xlsx`                                               | Excel file containing the raw data values for the cross-validation analysis done in Fig. 7G|

The mouse and human atlases are available at the [Allen Brain Atlas](https://atlas.brain-map.org/) and [Yeo et al. (2011)](https://surfer.nmr.mgh.harvard.edu/fswiki/CorticalParcellation_Yeo2011), respectively. Branch counts for the mouse data shown in Fig. 7B was done using the [SI Appendix, Fig. S7](https://www.pnas.org/doi/full/10.1073/pnas.1703601115#supplementary-materials) of [Li et al. (2017)](https://www.pnas.org/doi/full/10.1073/pnas.1703601115). 

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

This notebook contains visualization of streamline counts, fiber length, wiring cost, geodesic distance and FEOBV data; parcellation and rescaling of these data as well as correlation (scatter plots and spin tests using null model) of these maps with other connectivity and residual data. (Fig. 4,5,6,8, and Supplemental Fig.S5,S6)

### extra_analysis

This notebook contains validation analyses to examine the stability of <br> 
1. gradients, by split-half and leave-one-out across the 173 individuals used in this study (Supplemental Fig.S3) and <br>
2. structure- function tethering (Residual BF) across different gradient component pairs (Supplemental Fig.S4).
