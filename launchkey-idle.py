# this script animates launchkey mini lights

from launchkey import Launchkey
from utils import load_programs
import time

if __name__ == "__main__":
    try:
        # init launchkey connection
        lk = Launchkey()

        # load light programs
        programs = load_programs("programs")

        # time used for switching programs automatically
        start_time = time.time()
        time_per_program = 120

        # steps used for program animation
        steps = 0

        while True:
            # calculate current program index based on elapsed time
            elapsed_time = time.time() - start_time
            current_program = round(
                elapsed_time / time_per_program) % len(programs)

            steps = (steps + 1) % 3000

            # run program
            programs[current_program](lk, steps)

    except KeyboardInterrupt:
        pass

    lk.disconnect()
