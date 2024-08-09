import datetime

import hdmf_zarr
import pynwb

nwb = pynwb.NWBFile(
    session_id='test',
    session_description='test',
    identifier='12345',
    session_start_time=(
        datetime.datetime.now()
    ),
)

path = 'test.nwb.zarr'
with hdmf_zarr.NWBZarrIO(path, 'w') as io:
    io.write(nwb)    