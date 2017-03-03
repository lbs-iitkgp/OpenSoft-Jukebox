import numpy as np
import cv2
from Queue import *
class MPoint:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sprint(self):
        print(self.x)
        print(self.y)
img=cv2.imread('last.jpg',1)
x=img.shape
q=Queue()
start=MPoint(0,0)
end=MPoint(x[0]-1,x[1]-1)
r=x[0]
c=x[1]
visited = [[False for x1 in range(c)] for y1 in range(r)]
t=len(visited)==x[0]
l=len(visited[0])==x[1]
print(t)
print(l)
parent = [[MPoint(-1,-1) for x1 in range(c)] for y1 in range(r)]
q.put(start)
visited[start.x][start.y]=True
parent[start.x][start.y].x=0
parent[start.x][start.y].y=0
while not(q.empty()):
    p=q.get()
    for i in range(-1,2):
        if p.x+i<x[0] and p.x+i>=0:
            for j in range(-1,2):
                if p.y+j<x[1] and p.y+j>=0 and img[p.x+i,p.y+j,1]>100:
                    if abs(i)+abs(j)!=2 and visited[p.x+i][p.y+j]==False:
                        parent[p.x+i][p.y+j].x=p.x
                        parent[p.x+i][p.y+j].y=p.y
                        visited[p.x+i][p.y+j]=True
                        """if p.x > 350 and p.y > 400:
                            print(p.x+i)
                            print(p.y+j)"""
                        q.put(MPoint(p.x+i,p.y+j))
#visited = [[False for x1 in range(c)] for y1 in range(r)]
print(end.x)
print(end.y)
print img.shape
xx=parent[end.x][end.y]
xx.sprint()
cp=end
while cp.x!=start.x or cp.y!=start.y:
    img[cp.x,cp.y,0]=0
    img[cp.x,cp.y,1]=0
    img[cp.x,cp.y,2]=255
    cp=parent[cp.x][cp.y]
cv2.namedWindow('MazeSolver',cv2.WINDOW_NORMAL)
cv2.imshow('MazeSolver',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
