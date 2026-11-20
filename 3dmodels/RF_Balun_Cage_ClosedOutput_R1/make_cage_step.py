"""Generate the RF cage STEP model. Requires cadquery 2.7 or later.
Edit the dimensions below, then run: python make_cage_step.py
XY below follows KiCad; STEP Y is mirrored for KiCad 3D alignment.
The source footprint does not specify the vertical dimensions.
"""
from pathlib import Path
import math
import cadquery as cq

HEIGHT = 10.0          # PROVISIONAL overall height above PCB, mm
ROOF = 1.5             # PROVISIONAL roof thickness, mm
INPUT_RELIEF_HEIGHT = 1.5  # PROVISIONAL relief height above PCB, mm
TAP_DRILL_DEPTH = 4.5  # PROVISIONAL straight depth, plus drill point, mm
INNER_RADIUS = 1.0
TAP_DRILL_DIAMETER = 2.05  # nominal M2.5 x 0.45 tap-drill bore
OUTPUT = Path(__file__).with_name('RF_Balun_Cage_T1-T4_ClosedOutput_R1.step')

def box(x0, y0, x1, y1, height):
    return cq.Workplane('XY').center((x0+x1)/2, (y0+y1)/2).rect(x1-x0, y1-y0).extrude(height)

body = box(-12.576, -11.05, 58.294, 11.3, HEIGHT)
for x in [0, 15.24, 30.48, 45.72]:
    pocket = cq.Workplane('XY').center(x, 0).rect(12.4, 12.2).extrude(HEIGHT-ROOF).edges('|Z').fillet(INNER_RADIUS)
    body = body.cut(pocket)
    body = body.cut(box(x-1.45, -11.15, x+1.05, -5.9, INPUT_RELIEF_HEIGHT))
for x in [-9.826, 22.86, 55.546]:
    for y in [-8.5, 8.7]:
        bore = cq.Workplane('XY').center(x, y).circle(TAP_DRILL_DIAMETER/2).extrude(TAP_DRILL_DEPTH)
        h = (TAP_DRILL_DIAMETER/2) / math.tan(math.radians(59))
        tip = cq.Solid.makeCone(TAP_DRILL_DIAMETER/2, 0, h, cq.Vector(x, y, TAP_DRILL_DEPTH), cq.Vector(0, 0, 1))
        body = body.cut(bore.union(tip))
shape = body.val().mirror('XZ')
assert shape.isValid()
cq.exporters.export(shape, str(OUTPUT))
print(OUTPUT)
