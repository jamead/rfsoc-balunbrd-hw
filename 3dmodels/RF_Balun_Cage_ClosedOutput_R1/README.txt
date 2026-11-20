RF BALUN CAGE - CLOSED OUTPUT SIDE, R1 INNER CORNERS

Files:
- RF_Balun_Cage_T1-T4_ClosedOutput_R1.kicad_mod
- RF_Balun_Cage_T1-T4_ClosedOutput_R1.step
- cage_preview.png
- dimensions.json
- make_cage_step.py (editable CadQuery model generator)

Footprint changes:
- Closed all four openings on the +Y side (lower edge in Footprint Editor).
  This is the output side; the -Y input openings remain.
- One continuous F.Cu/F.Mask custom GND land now joins all four sections.
  All copper and plated pads retain pad number 1. Assign it to GND.
- R1.0 mm cavity corners on both mechanical and copper profiles.
  F.Fab arcs are true circles; copper arcs are polygonized at <0.001 mm error.
- Original six 2.8 mm mounting drills / 4.8 mm plated lands and both
  0.35 mm stitching drills / 0.9 mm lands remain at their original locations.
- Original courtyard retained; overall mechanical envelope remains
  70.87 x 22.35 mm. Cavities are 12.4 x 12.2 mm on a 15.24 mm pitch.
- Four 2.5 mm input-side wall reliefs remain in the mechanical model.
  Copper clearance gaps are 3.1 mm wide, as in the original footprint.
- No solder paste apertures added.

STEP dimensions needing confirmation:
The supplied footprint has no cage height, roof thickness, relief height,
or blind-hole depth, and the previously referenced STEP was not supplied.
The new STEP therefore uses these explicit provisional design dimensions:
  Overall height above PCB:     10.0 mm
  Roof thickness:               1.5 mm
  Cavity depth from underside:  8.5 mm
  Input relief height:          1.5 mm above PCB
  Blind tap-drill depth:        4.5 mm straight plus 118-degree drill point
  Nominal tapping callout:      6 x M2.5 x 0.45, 2.05 mm tap-drill bore
Threads are represented by tap-drill bores; no helical threads are modelled.
The height/depth assumptions should be confirmed before machining. They can
be edited at the top of make_cage_step.py and the STEP regenerated.
Changing INNER_RADIUS also requires updating the footprint cavity geometry.

KiCad use:
1. Import the .kicad_mod into your footprint library.
2. Put the .step file in the same directory as your .kicad_pro project file.
   The footprint model path is ${KIPRJMOD}/RF_Balun_Cage_T1-T4_ClosedOutput_R1.step.
3. Update the board footprint from the library and verify orientation.
   The closed wall is +Y in footprint coordinates. Existing rotations on
   the board may place it on a different screen edge.

Validation:
- Footprint loads in KiCad 9; there are nine pads total: one custom
  continuous GND pad and eight original plated through-hole pads.
- STEP contains one valid solid and was exported/reimported successfully.
- STEP XY coordinates are mirrored in Y relative to footprint coordinates
  for alignment with KiCad's 3D coordinate convention; Z=0 is the seating face.
