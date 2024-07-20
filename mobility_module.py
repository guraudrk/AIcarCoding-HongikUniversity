from RobokitRS.RobokitRS import *
import time as t

rs = RobokitRS() #객체 담기


#포트 번호를 적어서 port_open 함수를 실행한다.

rs.port_open("COM6") #포트 번호는 개인마다 다르다.
print("연결 완료!")

#여기에 동작 함수들을 정의한다.
#모듈에 함수들을 정의하면 import만 하면 함수를 쉬이 불러올 수 있다.

#좌하향
def left_down(i=10): #기본값은 10
    rs.motor_write(1,1,i)
    rs.motor_write(3,1,i)
#우상향
def right_up(i=10):
    rs.motor_write(0,1,i)
    rs.motor_write(2,1,i)
#전진
def reverse(i=10):
    rs.motor_write(0,0,i)
    rs.motor_write(1,1,i)
    rs.motor_write(2,1,i)
    rs.motor_write(3,0,i)
#정지
def stop():
    rs.motor_write(0,1,0)
    rs.motor_write(1,1,0)
    rs.motor_write(2,1,0)
    rs.motor_write(3,1,0)
#후진
def forward(i=10):
    rs.motor_write(0,1,i)
    rs.motor_write(1,0,i)
    rs.motor_write(2,0,i)
    rs.motor_write(3,1,i)


#좌회전
def left(i):
    rs.motor_write(0,0,i)
    rs.motor_write(1,0,i)
    rs.motor_write(2,1,i)
    rs.motor_write(3,1,i)

#우회전
def right(i):
    rs.motor_write(0,1,i)
    rs.motor_write(1,1,i)
    rs.motor_write(2,0,i)
    rs.motor_write(3,0,i)
    