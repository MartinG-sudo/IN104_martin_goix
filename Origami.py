
class Origami:
    def __init__(self, author, steps, paper_used):
        self.author=author
        self.steps=steps
        self.paper_used=paper_used

    def getSteps(self):
        print(self.steps)


class Single_paper(Origami):
    def __init__(self, author, steps, paper_used, flat, wet):
        Origami.__init__(self, author, steps, paper_used)
        self.flat=flat
        self.wet=wet

    def flat_folded(self):
        if self.flat==True:
            print("This Origami is flatfolded")
        else: print("This Origamis is not flatfolded")

    def __privateWetfolded(self):
        print(self.wet)

class Modular_Origami(Origami):
    def __init__(self, author, steps, paper_used, number_of_paper, glued):
        Origami.__init__(self, author, steps, paper_used)
        self.number_of_paper=number_of_paper
        self.glued=glued

    def __str__(self):
        print("This Origami uses %d sheets of paper." %self.number_of_paper)

    def __cheat(self):
        if self.glued:
            return True
        else: return False



Crane=Single_paper("Somebody",19,"Washi",True,False)
print(Crane)
Crane.flat_folded()
Crane.getSteps()
'''Crane.__privateWetfolded()'''

Star=Modular_Origami("Me",8,"Kraft",32,False)
Star.__str__()

