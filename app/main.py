import time
import sys

import make87
from datetime import datetime, timezone

import logging
logging.basicConfig(level=logging.DEBUG)

def get_current_datetime():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def main():
    make87.initialize()

    while True:
        logging.debug(f"Debug @ {get_current_datetime()}")
        time.sleep(0.1)
        logging.info(f"Info @ {get_current_datetime()}")
        time.sleep(0.1)
        logging.warning(f"Warning @ {get_current_datetime()}")
        time.sleep(0.1)
        logging.error(f"Error @ {get_current_datetime()}")
        time.sleep(0.1)
        logging.critical(f"Critical @ {get_current_datetime()}")
        time.sleep(0.1)
        print(f"Stdout Print @ {get_current_datetime()}", file=sys.stdout)
        time.sleep(0.1)
        print(f"Stderr Print @ {get_current_datetime()}", file=sys.stderr)
        time.sleep(5.0)


if __name__ == "__main__":
    main()
