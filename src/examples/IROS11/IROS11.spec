# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)
T_stationary, 1
T_fast, 1
T_low, 1
T_nonholonomic_turning, 1

CompileOptions:
convexify: True
fastslow: False

CurrentConfigName:
Test1

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
IROS11.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
predator, 1
prey, 1
poison, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
Mountain2 = p9
Mountain = p10
Field = p13
Bridge = p15
Tunnel = p7
Island = p12
Water3 = p3
Water2 = p4, p5
between$Island$and$Dock$ = p5, p15
Water = p6
Dock = p14
others = p2, p16, p17
Springs = p8
Meadows = p11

Spec: # Specification in structured English
# The robot avoids to enter the water areas (Water, Water2, Water3)
# If it senses poison it goes to Springs
# If it senses nothing it patrols between Meadows and Dock
# It activates T_low and T_nonholonomic_turning if and only if it is in Tunnel
# It activates T_fast between Island and Dock and deactivates it on Dock
# If it senses predator then it stops moving
# If it senses prey while in Dock or Field or Meadows or Springs then do T_stationary


Env starts with false
Robot starts in Island
Always not Water and not Water2 and not Water3

If you were in Tunnel then always not prey
If you were in between Island and Dock then always not prey

If you are not sensing predator and you are not sensing prey and you are not sensing poison then visit Meadows
If you are not sensing predator and you are not sensing prey and you are not sensing poison then visit Dock
If you are not sensing predator and you are not sensing prey and you are sensing poison then visit Springs

Do T_low and T_nonholonomic_turning if and only if you are in Tunnel

T_fast is set on between Island and Dock and reset on Dock
If you are sensing predator then stay there
If you are sensing prey and you are in Dock or Field or Meadows or Springs then do T_stationary

