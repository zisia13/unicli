#from uniterm import BannerPainter
#BannerPainter.DisableAutoUpdate()
#
#
#
#import sys
#sys.exit()


from uniterm import Selector as s
s.DisableAutoUpdate()
texts = s.Texts(question = "Hello?", choices = ("choice1", "choice2"))
selection = s.select(texts = texts)
print(selection)
