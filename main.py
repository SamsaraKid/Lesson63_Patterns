class Transformer:
    def run(self):
        if self.fuel <= 0:
            print('нет топлива')
            self.fill()
        else:
            self.dist += 10
            self.fuel -= 1

    def fill(self):
        self.fuel += 10
        print('заправился', self.fuel, 'литров', self.diesel)

    def __init__(self):
        self.dist = 0
        self.fuel = 10
        self.diesel = 'дизеля'
        self.status = 'robot'
        self.model = ''

    def transform(self):
        print('трансформируюсь')
        if self.status != 'robot':
            self.status = 'robot'
        else:
            self.status = self.model
        print('теперь я', self.status)


class Autobot(Transformer):
    def run(self):
        if self.fuel <= 0:
            print('нет топлива')
            self.fill()
        else:
            self.dist += 100
            self.fuel -= 1

    def __init__(self, model):
        Transformer.__init__(self)
        self.model = model


class Desepticon(Transformer):
    def run(self):
        if self.fuel <= 0:
            print('нет топлива')
            self.fill()
        else:
            self.dist += 200
            self.fuel -= 2
            
    def __init__(self, model):
        Transformer.__init__(self)
        self.model = model


fedor = Transformer()
print(fedor.dist, fedor.fuel)
fedor.run()
fedor.run()
print(fedor.dist, fedor.fuel)

# mark = Transformer()
# for i in range(20):
#     print('ход ', i + 1, ', топлива', mark.fuel, ', дистанция', mark.dist)
#     mark.run()


optim = Autobot('truck')
optim.run()
print(optim.dist, optim.fuel)

optim.transform()
optim.transform()
optim.transform()
