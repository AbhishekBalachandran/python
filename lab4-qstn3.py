import datetime
import time
print("\nThe unix timestamp is ",time.time())
print("\nWhen converted to readable date :  ",
    datetime.datetime.fromtimestamp(
        int(time.time())
    ).strftime('%Y-%m-%d %H:%M:%S'))