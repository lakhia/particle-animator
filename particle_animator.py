import argparse

from EmitterCollector import create_emitter_star, EmitterCollector

create_emitter_star(8, px=0.50, py=0.50, speed=0, speed_variation=0)
create_emitter_star(8, px=0.25, py=0.75, speed=0, speed_variation=0)
create_emitter_star(8, px=0.75, py=0.75, speed=0, speed_variation=0)
create_emitter_star(8, px=0.25, py=0.25, speed=0, speed_variation=0)
create_emitter_star(8, px=0.75, py=0.25, speed=0, speed_variation=0)
factor = 4

parser = argparse.ArgumentParser(prog='emitter',
                                 description='Outputs images')
parser.add_argument('-d', '--debug', action='store_true')
parser.add_argument('-c', '--count', default=-1)
args = parser.parse_args()

if args.count == -1:
    if args.debug:
        args.count = 30
        factor = 1
    else:
        args.count = 300

for frame in range(1, args.count):
    EmitterCollector.run(frame)
    fig = EmitterCollector.draw(frame, factor)
    fig.write_image('images/fig_%03d.png' % frame)
    if frame % 10 == 0:
        print("Wrote %d frame" % frame)
