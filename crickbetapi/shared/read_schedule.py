import logging


logger = logging.getLogger(__name__)

date = None

with open("ipl.txt", 'r') as f:
    content = f.readlines()
    lines = [line.strip() for line in content]

    i = 0
    while i < len(lines):
        if lines[i].endswith('2018:'):
            date = lines[i]
            i += 1
            print('Date is :' + date)
        else:
            # get 2 lines
            description = lines[i]
            i += 1
            match_no, time, statium, venue = lines[i].split(',')
            i += 1
            print(description, match_no, time, statium, venue)
            

