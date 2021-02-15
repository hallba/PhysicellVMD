# Physicell visualisation for VMD
Ben Hall
b.hall@ucl.ac.uk

VMD scripts derived from https://github.com/hallba/BioModelAnalyzer, under the same license.

Move the physicell files into a data directory. At present the specific values extracted are hardcoded. 
The radius has to be the last value in the extended xyz format.

## Patch 

In the VMD install directory, navigate to topotools1.7 plugin directory, and apply the patch

```bash
cd plugins/noarch/tcl/topotools1.7/
cp topovarxyz.tcl topovarxyz.tcl.orig
patch -R < topovarxyz.tcl.diff
```

## VMD console commands

These commands read the file, and set the agent radius to match the stored value (user)

```tcl
topo readvarxyz “organoid.xyz”
set molid 0
source VMD/AdvGraph.tcl
trace variable vmd_frame($molid) w  updateRadius 
```