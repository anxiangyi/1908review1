import os
import re
import shutil
import sys

# os.chdir('aa')
# with open('aaa.txt','wb') as ws:
#     pass
print(re.search('Asuper.*?B.*?','AsuperBdsajdAsuper111BAsuperAsuperB').group())
print(re.findall('Asuper.*?B.*?','AsuperBdsajdAsuper111BAsuperAsuperB'))