# ntuple-dumper
Intructions for how to set up xAODAnaHelpers and TLA algos for making ntuples

## Preface
In this repo, we'll learn how to set up the TLA-atlas-run3 suite, which will allow us to make ntuples from AOD and DAOD files. The most important framework we'll set up is xAODAnaHelpers, which is the base framework for making the ntuples. There are also custom TLA algorithms that can be used with xAODAnaHelpers.

xAODAnaHelpers has is mostly written in c++, but as a user, one just has to create simple config files that will call the c++ in the background. This config file is then called with a run.sh script, which controlls the infile (input AOD/DAOD file), output directory, number of events to process, and whether to run locally or on the grid. In practice then, one just has to know what keywords to put in the config file (which is sometimes nontrivial to figure out unfortunately).

There are example config files and run scripts in this repo.

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
