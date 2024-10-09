import argparse

from EmitterCollector import create_edges, EmitterCollector

create_edges(8, 8, thrust=0.003, angle_variation=360, speed=0, speed_variation=0)
factor = 8

parser = argparse.ArgumentParser(prog='emitter',
                                 description='Outputs images')
parser.add_argument('-d', '--debug', action='store_true')
parser.add_argument('-ds', '--draw', type=int, default=0)
parser.add_argument('-c', '--count', type=int, default=-1)
parser.add_argument('-s', '--skip', type=int, default=1)
args = parser.parse_args()

if args.count == -1:
    if args.debug:
        args.count = 30
    else:
        args.count = 300

if args.debug:
    factor = 1

for frame in range(1, args.count):
    EmitterCollector.run(frame)
    if frame >= args.draw and frame % args.skip == 0:
        fig = EmitterCollector.draw(frame, factor)
        fig.write_image('images/fig_%03d.png' % frame)
        if frame % 10 == 0:
            print("Wrote %d frame" % frame)
