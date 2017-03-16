from cs1graphics import *
import random


class ExitButtonHandler(EventHandler):
    ''' Handler for the Exit Button '''

    def __init__(self,paper):
        self._paper = paper
        EventHandler.__init__(self)

    def handle(self,event):
        if event.getDescription() == 'mouse click':
            self._paper.close()
            exit(0)

class TallyHandler(EventHandler):
    
    def __init__(self,textObj):
        EventHandler.__init__(self)
        self._count=0
        self._text=textObj
        self._text.setMessage(str(self._count))

    def handle(self,event):
        if event.getDescription() == 'mouse click':
            self._count += 1
            self._text.setMessage(str(self._count))
            shape = event.getTrigger()
            shape.setFillColor(generate_Color())
    
def generate_Color():
    for i in range(75):
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        color = (r, g, b)
    return color


def main():

    
    paper=Canvas(700,600,'linen')
    score =Text('',20,Point(200,500))
    score2 =Text('',20,Point(500,500))
    tittle = Text('Change the color of each shape with one click',20,Point(350,50))
    paper.add(tittle)

    clicksNumber = Text('Number of clicks ↓',20,Point(120,450))
    clicksNumber2 = Text('Number of Clicks ↓',20,Point(420,450))
    paper.add(clicksNumber)
    paper.add(clicksNumber2)
    
    
    paper.add(score)
    paper.add(score2)

    # exit button
    button=Button("EXIT",Point(600,555))
    button.setFillColor("light green")
    button.setBorderColor("green")
    button.setFontSize(18)

    
  
    cir = Circle( 70, Point(500,300))
    cir.setBorderColor('black')
    cir.setFillColor('white')
    paper.add(cir)
  
    rect = Rectangle(180, 100, Point(200,300))
    rect.setBorderColor('black')
    rect.setFillColor('white')
    paper.add(rect)

    referee = TallyHandler(score)
    rect.addHandler(referee)

    referee2 = TallyHandler(score2)
    cir.addHandler(referee2)

    e = ExitButtonHandler(paper)
    button.addHandler(e)   
                               
    paper.add(button)

main()
