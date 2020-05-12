import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
if re.search(r"ticky: INFO: ([\w ]*) ", line):
    print("true") 