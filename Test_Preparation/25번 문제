class Annie:
    def __init__(self,hp,mp,ap,Time):
        self.hp=hp
        self.mp=mp
        self.ap=ap
        self.level=6
        self.DealingTime=Time
        #6레벨이라고 가정, 더 올리고 싶으면 levelup메소드 사용
        self.skillLevel=[3,2,1]
    def tibbers(self):
        print("티버: 피해량",400+0.65*self.ap)
    def levelUp(self):
        self.level+=1
        n=int(input("0: Q 강화, 1 : W강화, 2: R강화"))
        if 0<=n<=2:
            self.skillLevel[n]+=1
        else:
            print("스킬 강화에 실패했습니다.")
    def Q(self):
        return [80+(self.skillLevel[0]*35)+(0.8*self.ap), 5.5-(self.skillLevel[0]*0.5)]
    def W(self):
        return [70+(self.skillLevel[1]*45)+(0.85*self.ap), 8]
    def R(self):
        #스킬을 2번 이상 사용하는 경우는 테스트케이스에서 제외함.
        if self.DealingTime<=45:
            if self.skillLevel[2]==1:
                return [150 + (self.skillLevel[2]*125) + (0.65*self.ap) + (60+0.2*self.ap)*self.DealingTime ,140-self.skillLevel[2]*20]
            elif self.skillLevel[2]==2:
                return [150 + (self.skillLevel[2]*125) + (0.65*self.ap) + (85+0.2*self.ap)*self.DealingTime ,140-self.skillLevel[2]*20]
            elif self.skillLevel[2]==3:
                return [150 + (self.skillLevel[2]*125) + (0.65*self.ap) + (120+0.2*self.ap)*self.DealingTime ,140-self.skillLevel[2]*20]
        else:
            if self.skillLevel[2]==1:
                return [150 + (self.skillLevel[2]*125) + (0.65*self.ap) + (60+0.2*self.ap)*45 ,140-self.skillLevel[2]*20]
            elif self.skillLevel[2]==2:
                return [150 + (self.skillLevel[2]*125) + (0.65*self.ap) + (85+0.2*self.ap)*45 ,140-self.skillLevel[2]*20]
            elif self.skillLevel[2]==3:
                return [150 + (self.skillLevel[2]*125) + (0.65*self.ap) + (120+0.2*self.ap)*45 ,140-self.skillLevel[2]*20]
    def calcDamage(self):

        Qdamage=self.Q()
        Wdamage=self.W()
        Rdamage=self.R()

        Qtime = self.DealingTime//Qdamage[1]
        Wtime = self.DealingTime//Wdamage[1]

        total_damage = Qdamage[0]*Qtime+Wdamage[0]*Wtime+Rdamage[0]
        print(self.DealingTime, "동안의 데미지 :", total_damage)
        return total_damage

    def needAp(self,fighttime):
        self.ap=0
        #용하고 최대 몇초까지 싸울 수 있는지 계산한 값을 넣어줌.
        self.DealingTime=fighttime
        #솔루션 1 : while문을 이용해서 AP를 조금씩 늘였을 때 6000이상의 딜을 넣을 수 있을때까지 해서 값을 구함.
        #솔루션 2 : 코드가 조금 더러워지겠지만 직접 식으로 계산

        ##이후사항은 직접 구현.
        
    def fight(self,other):
        #용과 애니가 1초단위로 데미지를 주고받으면서 싸우는 메소드.
        #어느 한 쪽의 hp가 0이 되면 종료후 누가 이겼는지 출력..
        #for문을 통해서 구현하세요.
        
class dragon:
    def __init__(self):
        self.hp=6000
        self.ad=100
        self.dps=0.5
    def fighttime(self,other):
        #애니의 피를 전부 깍는데 걸리는 시간.
        return other.hp/(self.ad*self.dps)
        

health, mana, ability_power, Time = map(float, input().split())
 
player = Annie(hp=health, mp=mana, ap=ability_power, Time = Time )
Dragon= dragon()
#테스트케이스 : 여러분들이 더 테스트 해보시길 바랍니다.
player.tibbers()
print(player.Q())
player.calcDamage()
