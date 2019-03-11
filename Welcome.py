import os
import time
clear = lambda: os.system('cls')
color_greed= lambda : os.system('color 0a')
color_common=lambda : os.system('color 0f')
color_greed()
welcome1="""
      ____                    _        __  __           _             _   
     |  _ \                  | |      |  \/  |         | |           | |  
     | |_) |   ___     ___   | | __   | \  / |   __ _  | | __   ___  | |_ 
     |  _ <   / _ \   / _ \  | |/ /   | |\/| |  / _` | | |/ /  / _ \ | __|
     | |_) | | (_) | | (_) | |   <    | |  | | | (_| | |   <  |  __/ | |_ 
     |____/   \___/   \___/  |_|\_\   |_|  |_|  \__,_| |_|\_\  \___|  \__|
                                                                          
                                                                          """
welcome2="""
                              _______         
                             |__   __|        
                                | |      ___  
                                | |     / _ \ 
                                | |    | (_) |
                                |_|     \___/ 
                                              """
welcome3="""
             __          __         _                            
             \ \        / /        | |                           
              \ \  /\  / /    ___  | |   ___    ___    _ __ ___  
               \ \/  \/ /    / _ \ | |  / __|  / _ \  | '_ ` _ \ 
                \  /\  /    |  __/ | | | (__  | (_) | | | | | | |
                 \/  \/      \___| |_|  \___|  \___/  |_| |_| |_|
                                                                 
                                                     

"""
print(welcome3)
time.sleep(1)
print(welcome2)
time.sleep(1)
print(welcome1)
time.sleep(1)
clear()
color_common()
user=input("Plase login uesrname :")
