import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
mylist = [int(input('First Number: ')), int(input('Second Number: ' )), int(input('Third Number: ')), int(input('Fourth Number: ')) ]
for i in range(4):
  print(mylist[i])
mylist[0], mylist[3] = mylist[3], mylist[0]
print(mylist)
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':


  
    main()
