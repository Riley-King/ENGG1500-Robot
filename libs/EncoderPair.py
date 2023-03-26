import libs.encoderLib as encoderLib


# WARNING! Pin values are hard coded in constructor!
class EncoderPair:
    def __init__(self):
        self.l_ofst = 0
        self.r_ofst = 0
        self.enc = encoderLib.Encoder(13, 14)

    def get(self):
        return self.enc.get_left() - self.l_ofst, \
               self.enc.get_right() - self.r_ofst

    def getLeft(self):
        return self.enc.get_left() - self.l_ofst

    def getRight(self):
        return self.enc.get_right() - self.r_ofst


    def reset(self):
        self.enc.clear_count()
        self.l_ofst = 0
        self.r_ofst = 0

    def reset_left(self):
        self.l_ofst += self.getLeft()

    def reset_right(self):
        self.r_ofst += self.getRight()


    def getLRRatio(self):
        return self.getLeft() / self.getRight()

    def getRLRatio(self):
        return self.getRight() / self.getLeft()

    def getRatios(self):
        return self.getLRRatio(), self.getRLRatio()