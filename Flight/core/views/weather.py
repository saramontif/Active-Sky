from datetime import datetime, timedelta
from pytz import timezone
import pytz
utc = pytz.utc
utc.zone
eastern = timezone('US/Eastern')
eastern.zone
amsterdam = timezone('Europe/Amsterdam')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
print(loc_dt.strftime(fmt))
ams_dt = loc_dt.astimezone(amsterdam)
ams_dt.strftime(fmt)
