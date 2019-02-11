from PIL import Image

import os

for f in os.listdir('.'):
    if f.endswith('.bmp'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fext)
        i.save('{}.png'.format(fn))

        #inicio laço para delete dos antigos
for f in os.listdir('.'):
    if f.endswith('.bmp'):
        os.remove(os.path.join(f))
