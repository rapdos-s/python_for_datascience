from time import time
from datetime import datetime

print(f"Seconds since January 1, 1970: {time():,.4f} or {time():.2e} in scientific notation")

print(f"{datetime.now():%b %d %Y}")
