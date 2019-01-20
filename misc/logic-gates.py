class LogicGate():
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performGateLogic()
        print(self.output)
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate " + self.get_label() +
                   "----->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate " + self.get_label() +
                   "----->"))


class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate " + self.get_label() +
                   "----->"))


class AndGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPin()

        return 0 if a == 1 else 1


# g1 = AndGate('G1')
# g1.get_output()
# g2 = OrGate('O1')
# g2.get_output()
g3 = NotGate('N1')
g3.get_output()