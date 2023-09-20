import re

import re

# Strip the text before taking input
test_case = input().strip()

r = re.compile(r"[A-Z]([A-Z]*|(-|.)[A-Z]+)@([A-Z]{3}.)+(LK){1}")

if r.match(test_case):
    print(True)
else:
    print(False)