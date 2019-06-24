from time import perf_counter
from time import sleep

#stolen from https://www.reddit.com/r/learnpython/comments/7836i0/is_there_a_more_accurate_thing_than_timesleep/doqsymo?utm_source=share&utm_medium=web2x
class Clock:

    def __init__(self, fps):
        self.start = perf_counter()
        self.frame_length = 1/fps

    @property
    def tick(self): #get number of ticks(ms) since frame start
        return (perf_counter() - self.start)

    def sleep(self): #sleep until next frame (approx 1ms resolution)
        while self.tick < self.frame_length:
            sleep(1/1000)
        self.start = perf_counter()