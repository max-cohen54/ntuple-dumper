

submit="grid" # local, grid
loglevel=info
parentsubmitdir="../data/trees" # better to use some location on eos that has a lot of space available
submitdir="EB_grid_07-09-2024"
nevents=-1 # -1: all
configFile="../configs/EB_config_main.py"
dataset="data24_13p6TeV.00473255.physics_EnhancedBias.merge.AOD.r15592_r15593_p6241"
outname="user.mmcohen.data24_473255_13p6TeV_EB_07-09-2024"

if [ "$submit" == "grid" ]; then
    # grid
    lsetup panda
    voms-proxy-init -voms atlas
    #infile="/eos/home-m/mmcohen/temp/xaodanahelpersminimalexample/data/DAODs/data22_13p6TeV.00437548.physics_Main.deriv.DAOD_JETM1.f1302_m2142_p5415/DAOD_JETM1.31025456._000028.pool.root.1"
    cmd="xAH_run.py --files $dataset --config $configFile --inputRucio --submitDir ${parentsubmitdir}/${submitdir}_$outname $extra -f prun --optGridOutputSampleName $outname --optTmpDir /tmp --optSubmitFlags=\"--addNthFieldOfInDSToLFN=2\""
    $cmd
    echo $cmd

else
    # local
    #infile="/eos/home-m/mmcohen/temp/xaodanahelpersminimalexample/data/AODs/data22_13p6TeV.00436169.physics_EnhancedBias.merge.AOD.r15498_r15499_p6193/AOD.38307777._000021.pool.root.1"
    #infile="/eos/home-m/mmcohen/temp/xaodanahelpersminimalexample/data/AODs/data22_13p6TeV.00440499.physics_EnhancedBias.merge.AOD.r15242_r15243_p6010_tid36850548_00/AOD.36850548._000050.pool.root.1"
    infile="/eos/home-m/mmcohen/temp/xaodanahelpersminimalexample/data/AODs/data24_13p6TeV.00473255.physics_EnhancedBias.merge.AOD.r15592_r15593_p6241/AOD.39475543._000149.pool.root.1"
    submitdir=${submitdir}_${nevents}
    mkdir -p $parentsubmitdir
    cmd="xAH_run.py --mode athena --files $infile --nevents $nevents --config $configFile --submitDir ${parentsubmitdir}/$submitdir --log-level $loglevel $extra --force direct"
    $cmd
    echo $cmd
fi

