import numpy as np

#load first file to get shape
data = np.load(snakemake.input.connmap_npz[0])
affine = data['affine']
mask = data['mask']
conn_shape = data['conn'].shape
nsubjects = len(snakemake.input.connmap_npz)
conn_group = np.zeros([nsubjects,conn_shape[0],conn_shape[1]])

for i,npz in enumerate(snakemake.input.connmap_npz):
    data = np.load(npz)
    conn_group[i,:,:] = data['conn']
    
#save conn_group, mask and affine
np.savez(snakemake.output.connmap_group_npz, conn_group=conn_group,mask=mask,affine=affine)

