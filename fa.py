class FA:
    st = []
    alph = []
    trs = {}
    i = ''
    f = []

    def __init__(self,file):
        self.readFile(file)

    def readFile(self,file):
        with open(file,'r') as file:
            self.alph = file.readline().strip().split(' ')
            self.st = file.readline().strip().split(' ')
            self.i = file.readline().strip()
            self.f = file.readline().strip().split(' ')
            for l in file:
                transition = l.strip().split(' ')
                if (transition[0],transition[1]) not in self.trs.keys():
                    self.trs[(transition[0],transition[1])] = [transition[2]]
                else:
                    self.trs[(transition[0],transition[1])].append(transition[2])
        file.close()

    def statePrint(self):
        print(self.st)

    def alphabetPrint(self):
        print(self.alph)

    def trsPrint(self):
        for i in self.trs:
            print(i,":",self.trs[i])

    def finalsPrint(self):
        print(self.f)

    def isDFA(self):
        for path in self.trs.keys():
            if len(self.trs[path]) > 1:
                return False
        return True

    def checkSeq(self, seq):
        current_state = self.i
        while len(seq) > 0:
            transition = (current_state, seq.pop(0))
            current_state = self.trs[transition][0] if transition in self.trs.keys() else None
            if current_state is None:
                return False
        return current_state in self.f

    def checkIfSeq(self):
        seq = input("Give a sequence: ").strip().split(' ')
        if len(seq) == 0:
            print("Empty sequence not allowed")
            return

        if self.checkSeq(seq):
            print("Sequence is accepted")
        else:
            print("Sequence is not accepted")


    def menu(self):
        print("Menu:\n1. Print states\n2. Print alphabet\n3. Print transitions\n4. Print final states")
        if self.isDFA():
            print("5. Check sequence\n6. Exit\n")
        else:
            print("5. Exit\n")

    def run(self):
        commands = {1: self.statePrint, 2: self.alphabetPrint, 3: self.trsPrint, 4: self.finalsPrint}

        if self.isDFA():
            commands[5] = self.checkIfSeq()

        self.menu()
        while True:
            try:
                c = int(input("Type command: "))
                if c in commands.keys():
                    commands[c]()
                else:
                    break
            except ValueError:
                print("Invalid format!")

fa = FA("input.in")
fa.run()