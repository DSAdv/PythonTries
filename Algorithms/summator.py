class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def get_name(self):
        return self.name

    def get_output(self):
        self.output = self.perform_logic()
        return self.output

    def perform_logic(self):
        pass


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.get_name() + "-->"))
        else:
            return self.pinA.get_from().get_output()

    def get_pinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.get_name() + "-->"))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def perform_logic(self):

        a = self.get_pinA()
        b = self.get_pinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def perform_logic(self):

        a = self.get_pinA()
        b = self.get_pinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.get_name() + "-->"))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def perform_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g4.get_output())


main()
