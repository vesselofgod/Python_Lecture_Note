import pygame
import random

pygame.init()#게임 초기화

height, width = 480, 640

screen = pygame.display.set_mode((width,height))#화면 넓이 설정.

FPS = 30
fpsClock=pygame.time.Clock()#파이게임 모듈에 사용될 FPS 설정


asteroidtimer=100
asteroids = [[20, 0, 0]]
score = 0


#file load, 
try:
    #게임에 쓸 이미지들을 불러옴.
    spaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    
    #튜플에 각각의 이미지객체들을 넣어줌.
    asteroidimgs = (asteroid0, asteroid1, asteroid2)

    gameover = pygame.image.load("./img/gameover.jpg")

    #배경음악을 불러옴
    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")
    takeoffsound.play()
except Exception as err:
    print('그림 또는 효과음 삽입에 문제가 있습니다.: ', err)
    #에러가 발생하면 프로그램을 종료함.
    pygame.quit()
    exit(0)

def text(arg, x, y):
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("Score: " + str(arg).zfill(6), True, (0, 0, 0))#zfill : 앞자리를 0으로 채움
    textRect = text.get_rect()#텍스트 객체를 출력위치에 가져옴
    textRect.centerx = x#출력할 때의 x좌표를 설정한다
    textRect.centery = y
    screen.blit(text, textRect)#화면에 텍스트객체를 그린다.


running=True #boolean flag

while running:
    screen.fill((255, 255, 255))#화면을 색칠함.

        #게임 종료조건, 우측 상단에 X 버튼 누르면 pygame모듈과 프로그램이 종료되는 코드
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    score += 1#점수 더해줌.
    
    text(score, 400, 10)#폰트 오브젝트를 윈도우에 띄우는 코드 좌표 (400,10)
    if score % 100 == 0:
        FPS += 2#스코어가 조금씩 오를수록 게임 진행속도가 빨라짐.(난이도 조절)
        
    position = pygame.mouse.get_pos()#아우스 위치를 받아옴
    
    #spaceshippos = (position[0], 600)
    spaceshippos = (position[0], position[1])#마우스의 위치를 우주선의 위치로 설정
    
    screen.blit(spaceshipimg, spaceshippos)#우주선을 그려줌.
    spaceshiprect = pygame.Rect(spaceshipimg.get_rect())#이미지의 표면의 좌표를 가져와서 객체의 위치 지정
    spaceshiprect.left = spaceshippos[0]
    spaceshiprect.top = spaceshippos[1]
    
    asteroidtimer -= 10
    if asteroidtimer <= 0:
        #운석을 소환함, first,second parameter는 소환위치
        asteroids.append([random.randint(5, 475), 0, random.randint(0, 2)])
        asteroidtimer = random.randint(20, 50)#다시 소환되는 시간 지정, 운석이 많이 소환되게끔 난이도 조정을 할 수 있음
    index = 0
    for stone in asteroids:
        stone[1] += 10#운석이 y축으로 내려옴
        if stone[1] > 640:#운석이 맵 밖으로 벗어났을 때
            asteroids.pop(index)#운석을 지워줌.
        stonerect = pygame.Rect(asteroidimgs[stone[2]].get_rect())
        stonerect.left = stone[0]
        stonerect.top = stone[1]
        if stonerect.colliderect(spaceshiprect):#객체의 충돌여보 감지함.
            landingsound.play()#충돌시에 뜨는 bgm
            asteroids.pop(index)
            running = False
        screen.blit(asteroidimgs[stone[2]], (stone[0], stone[1]))#운석을 그려줌
        index += 1
    fpsClock.tick(FPS)#다음 와일문으로 넘어감. loop
    pygame.display.flip()
    
screen.blit(gameover, (0, 0))#게임오버 이미지를 띄움
text(score, screen.get_rect().centerx, screen.get_rect().centery)#최종 점수를 맵 중앙에 띄움
pygame.display.flip()

while True:
    for event in pygame.event.get():#마찬가지로 게임 종료 설정
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
