class Ride():
    """
    In the input file:
    xStart
    yStart
    xEnd
    yEnd
    earlyStart
    latestFinish

    Calculated:
    time
    lastestStart
    """

    def __init__(self, L):
        self.xStart = L[0]
        self.yStart = L[1]
        self.xEnd = L[2]
        self.yEnd = L[3]
        self.earlyStart L[4]
        self.latestFinish = L[5]
        self.time = abs(xStart - xEnd) + abs(yStart - yEnd)
        self.latestStart = latestFinish - time
