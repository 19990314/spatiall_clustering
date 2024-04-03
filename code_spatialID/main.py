import stereo as st
import warnings
warnings.filterwarnings('ignore')

# read the GEF file
gef_path = ""
data_path = './SS200000135TL_D1.tissue.gef'
data = st.io.read_gef(file_path=data_path, bin_size=50)
data.tl.raw_checkpoint()

# remember to set flavor as scanpy
adata = st.io.stereo_to_anndata(data,flavor='scanpy',output='scanpy_out.h5ad')