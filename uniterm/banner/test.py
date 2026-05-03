try: from recolor import BannerPainter
except: from .recolor import BannerPainter

def test():
    Banner_String = r"""
           _            _           _          _      
          /\ \         /\ \        / /\       /\ \    
          \_\ \       /  \ \      / /  \      \_\ \   
          /\__ \     / /\ \ \    / / /\ \__   /\__ \  
         / /_ \ \   / / /\ \_\  / / /\ \___\ / /_ \ \ 
        / / /\ \ \ / /_/_ \/_/  \ \ \ \/___// / /\ \ \
       / / /  \/_// /____/\      \ \ \     / / /  \/_/
      / / /      / /\____\/  _    \ \ \   / / /       
     / / /      / / /______ /_/\__/ / /  / / /        
    /_/ /      / / /_______\\ \/___/ /  /_/ /         
    \_\/       \/__________/ \_____\/   \_\/          
    """

    color_blue   = (60, 90, 200)
    color_cyan   = (120, 180, 255)
    color_green  = (255, 200, 120)
    color_purple = (180, 80, 200)
    color_pink   = (255, 120, 150)
    color_orange = (255, 140, 60)

    print(BannerPainter.two_color_horizontal(Banner_String, color_blue, color_purple) + BannerPainter.reset)
    print()
    print(BannerPainter.two_color_vertical(Banner_String, color_cyan, color_green) + BannerPainter.reset)
    print()
    print(BannerPainter.four_color_horizontal(Banner_String, color_blue, color_cyan, color_green, color_pink) + BannerPainter.reset)
    print()
    print(BannerPainter.four_color_vertical(Banner_String, color_purple, color_pink, color_orange, color_blue) + BannerPainter.reset)
    # print()
    # print(recolor_horizontal_4c(Banner_String, (87, 106, 143), (183, 189, 247), (255, 248, 222), (255, 116, 68)) + reset)

if __name__ == "__main__":
    import os
    os.system("")
    test()
    input()
