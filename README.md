# ntuple-dumper
Intructions for how to set up xAODAnaHelpers and TLA algos for making ntuples

## Preface
In this repo, we'll learn how to set up the TLA-atlas-run3 suite, which will allow us to make ntuples from AOD and DAOD files. The most important framework we'll set up is xAODAnaHelpers, which is the base framework for making the ntuples. There are also custom TLA algorithms that can be used with xAODAnaHelpers.

xAODAnaHelpers has is mostly written in c++, but as a user, one just has to create simple config files that will call the c++ in the background. This config file is then called with a run.sh script, which controlls the infile (input AOD/DAOD file), output directory, number of events to process, and whether to run locally or on the grid. In practice then, one just has to know what keywords to put in the config file (which is sometimes nontrivial to figure out unfortunately).

There are example config files and run scripts in this repo.

The output of xAODAnaHelpers will be a TTree containing all the relevant data. One can then use one of the notebooks in `./read_tree` to read in this TTree and output an h5 file with the ntuples. It's important to note that the trigger menu was changed relatively recently, so I have different `read_tree` examples for MC vs data.

## Setting up the TLA suite
Fortunately there is good documentation for how to set up the TLA projects: https://gitlab.cern.ch:8443/tla-atlas-run3/tla-steering-run-3

## Configuring xAODAnaHelpers
Next, we'll merge in a few additions to xAODAnaHelpers that give us a few important peices of functionality: accessing L1 objects, accessing L1/HLT MET to name a few. Let's start by adding this forked version as an upstream.

```
cd src/xAODAnaHelpers
git remote add xAOD-fork https://github.com/max-cohen54/xAODAnaHelpers.git
git fetch xAOD-fork
```

Now, we'll make local branches and merge the edits. Because there are slight differences between running over data vs MC, we'll make a branch for each.

```
git checkout -b TLA-MC
git merge xAOD-fork/cohen-TLA-MC

git checkout -b TLA-data
git merge xAOD-fork/cohen-TLA-data
```

## Setup
Every time you log in to the project, you'll have to set up the AnalysisBase environment.

```
setupATLAS
lsetup cmake
lsetup git
cd src
lsetup "asetup AnalysisBase,25.2.9,here"
source ../build/*/setup.sh
cd ..
```
I recommend making a script `my_setup.sh` in the base directory with those lines that you can source whenever you log in. You can source it like `source my_setup.sh` or `. my_setup.sh`.

## Build
Finally, we can build everything.

```
cd build
cmake ../src
make
```

# Tutorial
For a short tutorial regarding how to use xAODAnaHelpers, you can refer to https://gitlab.cern.ch/tofitsch/xaodanahelpersminimalexample. It's outdated and therefore won't work with this version of AnalysisBase, but reading it should give you some idea of how to actually use xAODAnaHelpers.

The output after using xAODAnaHelpers is a TTree containing all the relevant data. One can then use one of the notebooks in the `read_tree` directory to read in the TTree, and output an h5 file with the ntuples. In practice you may need to make small edits to these notebooks depending on the branch names you use in your config file, and the data you're interested in saving (as well as the input/output paths).

# Information about the Enhanced Bias data (slightly out of date, to be updated soon)
Recent EB data gets repossessed weekly

Weights are calculated for each (good) event

Simulated L1 and HLT are applied and trigger decisions are saved (all with PS=1)

Here’s a recent reprocessing: `https://its.cern.ch/jira/browse/ATR-28661`
you can look at the HLT Reprocessings label to see them all
By clicking on the Panda [task], then scroll down to the bottom Slice outputs: AOD and click the green ‘finished’ we can see the output collection was `data22_13p6TeV.00440499.physics_EnhancedBias.merge.AOD.r15247_r15248_p6016_tid36850978_00`

EB weights are kept in XML files, which can be read in with a short script. 

List of datasets and location of weight XMLs: `https://twiki.cern.ch/twiki/bin/viewauth/Atlas/EnhancedBiasData`

Existing c++ tool to read the weights: `https://acode-browser1.usatlas.bnl.gov/lxr/source/athena/Trigger/TrigCost/EnhancedBiasWeighter/EnhancedBiasWeighter/EnhancedBiasWeighter.h`

It ended up being easier to write our own python script to read in the weights from the XML: `/data_pipeline/EB_weighter.py`

Simulated L1 and HLT trigger decisions can be accessed normally through the TrigDecisionTool (or normally through xAODAnaHelpers).


EB data (with the weights) should be representative of the “as seen by L1” data, and can therefore be used for L1 studies.


In order to obtain “as seen by HLT” data from the EB, we compiled a large list of PS=1 L1 physics triggers with the largest rates: `https://atlas-runquery.cern.ch/query.py?q=find+r+data22_13p6TeV.periodF+%2F+show+trigkeys`
Click ‘rates’ to see rates of the triggers
Then we made a dataset only with events that passed one of these triggers.

Later this year, some folks are planning to collect a separate dataset which is streamed only based on HLT_noalg_L1All, which would directly be the “as seen by HLT” data.
