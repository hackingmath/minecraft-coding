from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

x,y,z = -108,0,56
length,width,height = 6,8,6

blockTypes = [17,#oak wood
              5,#oak planks
              4,#cobblestone
              57,#diamond ore
              114,#nether brick
              155,#quartz
              49,#obsidian
              22]#lapus lazuli block

def house(x,y,z,length,width,height,blockType,carpet):
    '''builds a house at the given location with
    the given dimensions, blockType and carpet color'''
   

    mc.setBlocks(x-2,y-2,z-2,x+10,y+10,z+10,0) #clear the area

    #stone foundation
    #mc.setBlocks(x-2,y-2,z-2,x+3,y,z+3,2)

    mc.setBlocks(x-2,y-2,z-2,x+length+2,y,z+width+2,4)
    

    #wood outside
    mc.setBlocks(x,y,z,x+length,y+height,z+width,blockType)#35,10)

    #air inside
    mc.setBlocks(x+1,y+1,z+1,x+length-1,y+height-1,z+width-1,0)

    #glass roof
    mc.setBlocks(x+1,y+height,z+1,x+length-1,y+height,z+width-1,20)
    mc.setBlocks(x,y+1,z+2,x, y+height-1,z+4,20)
    mc.setBlocks(x+1,y+2,z,x+3,y+4,z,20)
    mc.setBlocks(x+2,y+2,z+width,x+5,y+5,z+width,20)

    #torches
    for i in range(length):
        mc.setBlock(x+i,y+2,z-1,50)
        mc.setBlock(x+i,y+2,z+width+1,50)

    #wooden door
    mc.setBlock(x+length,y+1,z+3,64,0,4)
    mc.setBlock(x+length,y+2,z+3,64,8,4)

    #quartz stairs
    mc.setBlock(x+length+1,y,z+3,156,1)

    #chest
    mc.setBlock(x+1,y+1,z+width-1,54)

    #pink floor
    mc.setBlocks(x+1,y,z+1,x+length-1,y,z+width-1,35,carpet)

    #BED
    mc.setBlock(x+1,y+1,z+1,26)
    mc.setBlock(x+1,y+1,z+2,26,8)

    #bookshelves
    mc.setBlocks(x+3,y+1,z+1,x+5,y+4,z+1,47)

for i in range(10):
    house(20*i,1,0,
          random.randint(6,8),
          random.randint(5,10),
          random.randint(6,10),
          random.choice(blockTypes),
          random.choice(list(range(10))))
