import argparse

from EmitterCollector import create_grid, EmitterCollector

create_grid(num_x=8, num_y=3, rate=0.08, thrust=0.02, angle_variation=360, speed=0, speed_variation=0.015)
factor = 8

parser = argparse.ArgumentParser(prog='emitter',
                                 description='Outputs images')
parser.add_argument('-d', '--debug', action='store_true')
parser.add_argument('-st', '--start', type=int, default=1)
parser.add_argument('-e', '--end', type=int, default=240)
parser.add_argument('-s', '--skip', type=int, default=1)
args = parser.parse_args()

if args.end == -1:
    if args.debug:
        args.end = 30
    else:
        args.end = 300

if args.debug:
    factor = 1

for frame in range(1, args.end):
    EmitterCollector.run(frame)
    if frame >= args.start and frame % args.skip == 0:
        fig = EmitterCollector.draw(frame, factor)
        fig.write_to_png('images/fig_%03d.png' % frame)
        if frame % 10 == 0:
            print("Wrote %d frame" % frame)
