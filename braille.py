from PIL import Image

bletters=['A','B','C','D','E','F','H','G','I','J','K','L','M','N','O','P','Q','R','S','T','U',
'V','W','X','Y','Z']
blettersl=[0]*26


class bletter() :
   def __init__(self, i) :
       self.name=bletters[i]
       self.im1=Image.open(self.name+".jpg")
       self.locked=False

for i in range(len(bletters)) :
    blettersl[i]=bletter(i) 

def collect_image(letter) :
    let_val= ord(letter)- ord("A")
    (blettersl[let_val].im1).show()


    