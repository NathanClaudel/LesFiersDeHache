class Ride():
    """
    In the input file:
    xStart
    yStart
    xEnd
    yEnd
    earlyStart
    latestFinish
    id

    Calculated:
    time
    lastestStart
    done
    """

    def __init__(self, L, id_number):
        self.posStart = (L[0], L[1])
        self.posEnd = (L[2], L[3])
        self.earlyStart = L[4]
        self.latestFinish = L[5]
        self.time = abs(self.posStart[0] - self.posEnd[0]) + abs(self.posStart[1] - self.posEnd[1])
        self.latestStart = self.latestFinish - self.time
        self.id = id_number
        self.done = False
