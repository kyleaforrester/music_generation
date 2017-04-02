#!/usr/bin/env python3

import sys

HISTORY = 10

def shut_off_time(notes, pitch):
    for n in notes:
        if (int(n[4]) == pitch):
            return int(n[1])
    #Not found!
    return None

if (len(sys.argv) != 2):
    print('Usage: python3 my_script.py input_midi.csv')
    sys.exit(0)

notes = open(sys.argv[1], errors='ignore').readlines()
notes = [l.split(',') for l in notes if ('Note_on_c' in l)]
for i in range(len(notes)):
    for j in range(len(notes[i])):
        notes[i][j] = notes[i][j].strip()
notes = sorted(notes, key=lambda x: int(x[1]))

data_points = []
for i in range(len(notes)):
    time = int(notes[i][1])
    pitch = int(notes[i][4])
    intensity = int(notes[i][5])
    if (intensity > 0):
        duration = shut_off_time(notes[i+1:], pitch) - time
        data_points.append((time, pitch, intensity, duration))

ml_data = []
for i in range(HISTORY, len(data_points)):
    points = data_points[i-HISTORY:i]
    my_point = data_points[i]
    max_time = max(points, key=lambda x: x[0])[0]
    ml_data.append((list((max_time-p[0], p[1], p[2], p[3]) for p in points), (my_point[0]-max_time, my_point[1], my_point[2], my_point[3])))

for data in ml_data:
    printable_input = ','.join([str(field) for point in data[0] for field in point])
    printable_output = ','.join([str(field) for field in data[1]])
    print('{}={}'.format(printable_input, printable_output))

