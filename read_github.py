# python -m venv .venv-hdmf-test
# .venv-hdmf-test/scripts/activate (Windows)
# source .venv-hdmf-test/bin/activate (Linux)
# python -m pip install hdmf-zarr fsspec s3fs

import hdmf_zarr 
import zarr 

path = "https://github.com/bjhardcastle/test-hdmf-zarr/tree/main/consolidated.nwb.zarr"
   
# the zarr file is not empty:
z = zarr.open(path=path)
assert tuple(z.keys())

with hdmf_zarr.NWBZarrIO(path, mode='r') as read_io:
    read_io.open()
    assert isinstance(read_io.file.store, zarr.storage.ConsolidatedMetadataStore)
    try:
        # this fails:
        nwb = read_io.read()
    except Exception as exc:
        print(repr(exc))
        # ValueError: No data_type found for builder root
   
with hdmf_zarr.NWBZarrIO(path, mode='-r') as read_io:
    read_io.open()
    assert isinstance(read_io.file.store, zarr.storage.FSStore)
    try:    
        # this fails:
        nwb = read_io.read()
    except Exception as exc:
        print(repr(exc))
        # hdmf.backends.errors.UnsupportedOperation: Cannot build data. There are no values.
