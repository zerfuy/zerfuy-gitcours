#!C:\Users\gabba\OneDrive\Documents\cours\Python\videoDL\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tqdm==4.44.0','console_scripts','tqdm'
__requires__ = 'tqdm==4.44.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tqdm==4.44.0', 'console_scripts', 'tqdm')()
    )
