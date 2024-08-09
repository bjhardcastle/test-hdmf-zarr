# python -m venv .venv-hdmf-test
# .venv-hdmf-test/scripts/activate (Windows)
# source .venv-hdmf-test/bin/activate (Linux)
# python -m pip install hdmf-zarr fsspec s3fs

import hdmf_zarr 
import zarr 

s3_path = "https://dandiarchive.s3.amazonaws.com/zarr/ccefbc9f-30e7-4a4c-b044-5b59d300040b/"

with hdmf_zarr.NWBZarrIO(s3_path, mode='r') as read_io:
    read_io.open()
    assert isinstance(read_io.file.store, zarr.storage.ConsolidatedMetadataStore)
    try:
        # this fails:
        nwb = read_io.read()
    except Exception as exc:
        print(repr(exc))
        # ValueError: No data_type found for builder root
   
with hdmf_zarr.NWBZarrIO(s3_path, mode='-r') as read_io:
    read_io.open()
    assert isinstance(read_io.file.store, zarr.storage.FSStore)
    try:    
        # this fails:
        nwb = read_io.read()
    except Exception as exc:
        print(repr(exc))
        # hdmf.backends.errors.UnsupportedOperation: Cannot build data. There are no values.
   
# the zarr file is empty:
z = zarr.open(s3_path, mode='r')
assert not tuple(z.keys())
