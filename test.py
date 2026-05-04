#from uniterm import BannerPainter
#BannerPainter.DisableAutoUpdate()
#
#
#
#import sys
#sys.exit()




from uniterm import Selector
Selector.DisableAutoUpdate()
texts = Selector.Texts(question = "Hello?", choices = ("choice1", "choice2"))
selection = Selector.select(texts = texts)
print(selection)
