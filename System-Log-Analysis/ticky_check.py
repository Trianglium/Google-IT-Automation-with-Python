import re
import operator
import csv

errors = {}
per_user = {}
formula = r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"
lfile = "syslog.log"

with open(lfile, 'r') as syslogfile:
  for log in syslogfile:
      logs = re.search(formula, log)
      if logs is not None:
          name = str(logs.groups()[2])[1:-1]
          if logs.groups()[0] == "INFO":
              ntype = logs.groups()[0]
              msg = logs.groups()[1]
              if name in per_user:
                  user = per_user[name]
                  user[ntype] += 1
              else:
                  per_user[name] = {"INFO":1, "ERROR":0}

          elif logs.groups()[0] == "ERROR":
              ntype = logs.groups()[0]
              msg = logs.groups()[1]
              errors[msg] = errors.get(msg, 0) + 1
              if name in per_user:
                  user = per_user[name]
                  user[ntype] += 1
              else:
                  per_user[name] = {"INFO":0, "ERROR":1}


all_errors = [("Error", "Count")] + sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
user_stats = [("Username", "INFO", "ERROR")] + sorted(per_user.items())

with open("error_message.csv", 'w') as em:
    for row in all_errors:
        em.write("{}, {}\n".format(row[0], row[1]))

with open("user_statistics.csv", 'w') as us:
    for row in user_stats:
        if isinstance(row[1], dict):
            us.write("{}, {}, {}\n".format(row[0], row[1].get("INFO"), row[1].get("ERROR")))
        else:
            us.write("{}, {}, {}\n".format(row[0], row[1], row[2]))
