import re
import sys

log_file=sys.argv[1]
usernames={}

with open(log_file) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result=re.search(pattern,line)
        if result is None:
            continue
        name=result[1]
        usernames[name] = usernames.get(name,0) + 1
print(usernames)