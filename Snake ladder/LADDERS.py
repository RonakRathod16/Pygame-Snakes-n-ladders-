


def ladders(x1,y1,pos):
    if x1==811 and y1==600:
        x1=811
        y1=250
        pos+=59
    elif x1==188 and y1==600:
        x1=99
        y1=460
        pos+=21
    elif x1==366 and y1==530:
        x1=544
        y1= 320
        pos+=29
    elif x1==633 and y1==460:
        x1=811 
        y1=40
        pos+=58
    elif x1==10 and y1==390:
        x1=99
        y1==250
        pos+=21
    elif x1==366 and y1==390:
        x1=277
        y1=110
        pos+=39
    elif x1==633 and y1==250:
        x1=722
        y1=110
        pos+=21
    elif x1==455 and y1==180:
        x1=544
        y1=40
        pos+=26
    elif x1==366 and y1==670:
        x1=455
        y1=600
        pos+=10
    return x1,y1,pos



def ladders2(x2,y2,pos):
    if x2==376 and y2==670:
        x2=465
        y2=600
        pos+=10
    if x2==821 and y2==600:
        x2=821
        y2=250
        pos+=59
    elif x2==198 and y2==600:
        x2=109
        y2=460
        pos+=21
    elif x2==376 and y2==530:
        x2=554
        y2= 320
        pos+=29
    elif x2==643 and 2==460:
        x2=821 
        y2=40
        pos+=58
    elif x2==20 and y2==390:
        x2=109
        y2==250
        pos+=21
    elif x2==376 and y2==390:
        x2=287
        y2=110
        pos+=39
    elif x2==643 and y2==250:
        x2=732
        y2=110
        pos+=21
    elif x2==465 and y2==180:
        x2=554
        y2=40
        pos+=26
    return x2,y2,pos
    
def snakes_1(x1,y1,pos):
    if x1==633 and y1==530:
        x1=544
        y1==670
        pos-=21
    elif x1==188 and y1==390:
        x1=544
        y1=530
        pos-=16
    elif x1==633 and y1==110:
        x1=366
        y1=250
        pos-=23
    elif x1==366 and y1==40:
        x1=10
        y1=460
        pos-=56
    elif x1==99 and y1==40:
        x1=10
        y1=180
        pos-=19
        
    return x1,y1,pos


def snakes_2(x2,y2,pos):
    if x2==643 and y2==530:
        x2=554
        y2==670
        pos-=21
    elif x2==198 and y2==390:
        x2=554
        y2=530
        pos-=16
    elif x2==643 and y2==110:
        x2=376
        y2=250
        pos-=23
    elif x2==376 and y2==40:
        x2=20
        y2=460
        pos-=56
    elif x2==109 and y2==40:
        x2=20
        y2=180
        pos-=19
        
    return x2,y2,pos