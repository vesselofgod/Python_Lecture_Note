import csv
import pygame

BLACK = (0,0,0)
RED = (0,255,150)

f=open('glider.csv')
data=csv.reader(f)

def initCell():
    i=0
    for row in data:
        subList=[]
        for j in range(len(row)):
            a=Cell(row[j],i,j)#cell을 cvs로 읽어서 죽었는지 살았는지 체크, 좌표도 넣어줌.
            subList.append(a)
        cells.append(subList)#cells맵에 넣어줌.
        i=i+1

def lifeGamePlay():
    pygame.init()
    width,height = 500, 500
    screen = pygame.display.set_mode((width,height))

    while True:
        #game loop
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:#종료 이벤트 설정
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:#클릭 시 다음 세대로 넘어감
                nextGeneration()

        screen.fill(BLACK)#화면을 검은 색으로 초기화

        for y in range(len(cells)):
            for x in range(len(cells[0])):
                if( cells[y][x].state == True ):
                    pygame.draw.rect(screen, RED, (x*(500/len(cells)),y*(500/len(cells)), (500/len(cells)), (500/len(cells))),1)

        pygame.display.flip()#화면 업데이트

class Cell:
    #세포 객체를 만들어주는 클래스
    def __init__(self,number, x,y):
        if number=='1':
            self.state=True
        else:
            self.state=False
        self.next=False
        self.nb=0
        self.x=x
        self.y=y

    def calcAdjCell(self):
        #이웃의 수를 구해주는 함수.
        #원래는 self.nb로 짜야하지만 마음에 안들어서 그냥 함수팜.
        adjCell=0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(0<= self.x+i < len(cells[0]) and 0<=self.y+j<len(cells)):
                    if(i != 0 or j != 0) and (cells[self.x+i][self.y+j].state==True):
                        adjCell+=1
        return adjCell

    def stateCheck(self):
        #다음 턴에 생존 및 사망 여부를 이웃 세포수로 판단함.
        #self.next는 매 턴마다 기본적으로 false이므로 다음턴에도 사는 조건만 체크하면 됨.
        num=self.calcAdjCell()
        if self.state == True and (num==2 or num==3):
            self.next = True
        elif self.state==False and num==3:
            self.next=True

    def changeGeneration(self):
        #세대를 교체해줌.
        self.state=self.next
        self.next=False

def nextGeneration():
    #모든 세포의 이웃들을 조사해서 다음 세대에 생존여부 조사.
    for row in cells:
        for i in row:
            i.stateCheck()
    #다음 세대로 넘어감.
    for row in cells:
        for i in row:
            i.changeGeneration()

cells=[]
initCell()
lifeGamePlay()