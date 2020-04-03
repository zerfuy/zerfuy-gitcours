# -*- coding: utf-8 -*-

import re

regex = r'\w+'

with open("YEET.html", 'rb') as file:

    wlist = re.findall(regex, str(file.read()))
    print("{} mots trouvés".format(len(wlist)))
    print(wlist)
