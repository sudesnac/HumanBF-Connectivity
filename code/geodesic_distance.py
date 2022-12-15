import gdist
import numpy as np
import nibabel as nib
import pyvista as pv

hemi = ['rh','R']

# Load vtk surface
surf = pv.read(f'/project/6050199/rhaast/03_Ongoing/basal_forebrain/resources/fsa5.{hemi[0]}.pial.vtk')

# Remove medial wall
ctx_path = f'/project/6050199/rhaast/03_Ongoing/basal_forebrain/resources/fsa5.{hemi[0]}.cortex.label'
ctx = nib.freesurfer.io.read_label(ctx_path)

# Load basal forebrain label
bf_path = f'/project/6050199/rhaast/03_Ongoing/basal_forebrain/results/funcparc_icafix/group/atlas/seed-BASF.{hemi[1]}.bin.fsa5.shape.gii'
bf = nib.load(bf_path).darrays[0].data
bf_coords = surf.points[np.argwhere(bf)[:,0]]

# Extract surface without medial wall
ctx      = np.hstack((ctx, np.argwhere(bf)[:,0]))
surf_ctx = surf.extract_points(ctx, adjacent_cells=True)

v_ctx = surf_ctx.points
f_ctx = surf_ctx.cells.reshape(surf_ctx.n_cells,4)[:,1:]

# Save to gifti surface
new_gii = nib.gifti.GiftiImage()
new_gii.add_gifti_data_array(
    nib.gifti.GiftiDataArray(
        data=v_ctx.astype(np.float32),
        intent='NIFTI_INTENT_POINTSET'
    )
)

new_gii.add_gifti_data_array(
    nib.gifti.GiftiDataArray(
            data = f_ctx.astype(np.int32),
            intent = 'NIFTI_INTENT_TRIANGLE'
        )
)

new_gii.to_filename(f'/project/6050199/rhaast/03_Ongoing/basal_forebrain/resources/fsa5_wo_medialwall.pial.{hemi[0]}.surf.gii')

# Update indices of label for new surface
src_new = [ np.where(np.sum(np.sign(v_ctx-coords), axis=1)==0)[0][0] for coords in bf_coords ]

# Compute distance
dist = gdist.compute_gdist(v_ctx.astype(np.float64), f_ctx.astype(np.int32), source_indices=np.array(src_new, dtype=np.int32))

# Back to original surface
orig_idx = [ np.where(np.sum(np.sign(surf.points-coords), axis=1)==0)[0][0] for coords in v_ctx ]
data = np.zeros(len(surf.points))
data[orig_idx] = dist

# Set medial wall back to zero
data[~np.isin(np.arange(0,surf.points.shape[0]),ctx)] = 0

# Save distance to gifti file
gii = nib.gifti.GiftiImage()
gii.add_gifti_data_array(
    nib.gifti.GiftiDataArray(
        data=data.astype(np.float32)
        )
) 

nib.save(gii, f'/project/6050199/rhaast/03_Ongoing/basal_forebrain/resources/seed-BASF_geodesic-distance.pial.{hemi[0]}.shape.gii')

# Fix possible zeroes along cortex
zero_mask = np.isin(np.argwhere(data==0), ctx)[:,0]
zero_ind  = np.argwhere(data==0)[zero_mask][~np.isin(np.argwhere(data==0)[zero_mask], np.argwhere(bf))]

# Get faces
surf = nib.load(f'/project/6050199/rhaast/03_Ongoing/basal_forebrain/resources/fsa5.pial.{hemi[0]}.surf.gii')
faces = surf.darrays[1].data

# Fill zero vertices with average across neighbors
data_filled = data.copy()
for i in enumerate(zero_ind):    
    f_mask = [ True if np.sum(np.isin(face, i[1])) != 0 else False for face in faces ]

    nbrs_values = data[np.unique(faces[f_mask])]
    data_filled[i[1]] = nbrs_values[np.nonzero(nbrs_values)].mean()

# Save distance to gifti file
gii = nib.gifti.GiftiImage()
gii.add_gifti_data_array(
    nib.gifti.GiftiDataArray(
        data=data_filled.astype(np.float32)
        )
) 

nib.save(gii, f'/project/6050199/rhaast/03_Ongoing/basal_forebrain/resources/seed-BASF_geodesic-distance-no-zeros.pial.{hemi[0]}.shape.gii')    