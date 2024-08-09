import datetime

import hdmf_zarr
import numpy as np
import pynwb

nwb = pynwb.NWBFile(
    session_id='test',
    session_description='test',
    identifier='12345',
    session_start_time=(
        datetime.datetime.now()
    ),
)
data = np.arange(100, 200, 10)
time_series = pynwb.TimeSeries(
    name="test_timeseries",
    description="an example time series",
    data=data,
    unit="m",
    starting_time=0.0,
    rate=1.0,
)
nwb.add_acquisition(time_series)

path = 'non-consolidated.nwb.zarr'
with hdmf_zarr.NWBZarrIO(path, 'w') as io:
    io.write(nwb)    