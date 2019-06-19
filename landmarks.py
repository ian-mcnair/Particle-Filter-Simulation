import random
def choose_landmark_loop(display_width,display_height):
    """ Loop which validates user choice in selection of landmark"""
    choice = True
    while choice:
        print("\n***************************************")
        print('Landmarks need to be created.\n Please input a numerical choice below:')
        print('1: Creates one landmark')
        print('2: Creates two landmarks')
        print('3: Creates three landmarks')
        print('4: Creates four landmarks')
        print('5: Creates random landmarks')
        print('6: Creates a grid of 12 landmarks')
        num = input('Input your choice:')
        try:
            num = int(num)
            if num < 7 and num > 0:
                landmarks = choose_landmark(num, display_width,display_height)
                choice = False
            else:
                print('Error: User input out of range of choices')
        except:
            print('Error: Count not convert user input to integer')
    return landmarks

def choose_landmark(choice, display_width, display_height):
    """ Takes input from user to select type of landmarks used in simulation"""
    if choice == 1:
        landmarks = [[int(display_width/2), int(display_height/2)]]
    elif choice == 2:
        landmarks = [[int(display_width/4), int(display_height/2)], 
                     [int(3*display_width/4), int(display_height/2)]]
    
    elif choice == 3:
        landmarks = [[int(display_width/2),int(display_height/3)],
                     [int(display_width/3), int(2*display_height/3)],
                     [int(2*display_width/3), int(2*display_height/3)]]

    elif choice == 4:
        landmarks = [[int(display_width/4),int(display_height/4)], 
                     [int(3*display_width/4),int(display_height/4)], 
                     [int(3*display_width/4),int(3*display_height/4)], 
                     [int(display_width/4),int(3*display_height/4)]]
        
    elif choice == 5:
        landmarks = [[int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)]]
        
    elif choice == 6:
        landmarks = []
        for i in range(4):
            landmarks.append([int(display_width/10 + i*275), int(display_height/6)])
            landmarks.append([int(display_width/10 + i*275), int(display_height*3/6)])
            landmarks.append([int(display_width/10 + i*275), int(display_height*5/6)])
            
    return landmarks
      