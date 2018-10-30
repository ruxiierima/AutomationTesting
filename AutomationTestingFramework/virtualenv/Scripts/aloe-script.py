#!C:\Users\ierima\PycharmProjects\AutomationTestingFramework\virtualenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'aloe==0.1.18','console_scripts','aloe'
__requires__ = 'aloe==0.1.18'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('aloe==0.1.18', 'console_scripts', 'aloe')()
    )
