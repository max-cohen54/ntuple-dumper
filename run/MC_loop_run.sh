#!/bin/bash

# Initialization
submit="grid"
loglevel=info
parentsubmitdir="../data/trees"
submitdir="MC_grid_07-15-2024"
configFile="../configs/MC_config_main.py"
baseOutname="user.mmcohen." # Base name for output

# List of datasets
datasets=(
  # "data22_13p6TeV.00436169.physics_EnhancedBias.merge.AOD.r15498_r15499_p6193"
  # "data22_13p6TeV.00428855.physics_EnhancedBias.merge.AOD.r15498_r15499_p6193"
  # "data22_13p6TeV.00440499.physics_EnhancedBias.merge.AOD.r15498_r15499_p6193"
  # "data22_13p6TeV.00440199.physics_EnhancedBias.merge.AOD.r15498_r15499_p6193"
  "valid1.601499.PhPy8EG_PDF4LHC21_ggH125_MINLO_ZZ4lep_notau.recon.AOD.e8532_e8528_s4162_s4114_r15582_tid39407513_00"
  "valid1.512456.MGPy8EG_A14NNPDF23LO_HAHMggfZdZd2l2nu_125_28.recon.AOD.e8397_e8528_s4162_s4114_r15582_tid39407509_00"
  "valid1.801966.Py8EG_Zprime2EJs_Ld20_rho40_pi10_Zp1500_l50.recon.AOD.e8532_e8528_s4162_s4114_r15582_tid39407505_00"
  "valid1.515205.MGPy8EG_A14N23LO_HNL7p5_ctau1_eemu.recon.AOD.e8529_e8528_s4162_s4114_r15582_tid39407501_00"
  "valid1.523101.MGPy8EG_S1_qqa_Ph25_mRp15_gASp1_qContentUDSC.recon.AOD.e8514_e8528_s4162_s4114_r15582_tid39407498_00"
  "mc23_13p6TeV.601477.PhPy8EG_HHbbttHadHad_cHHH01d0.recon.AOD.e8514_e8528_s4162_s4114_r14668"
  "mc23_valid.801169.Py8EG_A14NNPDF23LO_jj_JZ4.merge.AOD.e8514_e8516_s4041_s4055_r14332_r14394"
  "mc23_valid.801167.Py8EG_A14NNPDF23LO_jj_JZ2.merge.AOD.e8514_e8516_s4041_s4055_r14332_r14394"
  "mc23_13p6TeV.601191.PhPy8EG_AZNLO_Ztautau.merge.AOD.e8514_e8528_s4111_s4114_r14622_r14663"
  "mc23_valid.801166.Py8EG_A14NNPDF23LO_jj_JZ1.merge.AOD.e8514_e8516_s4041_s4055_r14332_r14394"
  #"mc16_13TeV.524392.MGPy8EG_N2C1p_135_125_2L_MS_noG_uds_N1pT150.merge.AOD.e8435_e7400_s3126_r9364_r9315"
)

tags=(
  "ZZ4lep"
  "HAHMggfZdZd2l2nu"
  "Zprime2EJs"
  "A14N23LO_HNL7p5_ctau1_eemu"
  "qqa"
  "HHbbttHadHad"
  "jjJZ4"
  "jjJZ2"
  "Ztautau" 
  "jjJZ1"
  #"N2C1p"
)

# Setup for grid submission
if [ "$submit" == "grid" ]; then
    lsetup panda
    voms-proxy-init -voms atlas
    
    counter=0

    for dataset in "${datasets[@]}"; do
        # Generate a unique outname for each run
        outname="${baseOutname}${tags[counter]}_$(date +%m-%d-%Y)"
        
        # Submission command
        #cmd="xAH_run.py --files $dataset --config $configFile --inputRucio --submitDir ${parentsubmitdir}/${submitdir}_${outname} --optGridOutputSampleName $outname --optTmpDir /tmp --optSubmitFlags=\"--addNthFieldOfInDSToLFN=2\" -f prun"

        cmd="xAH_run.py --files $dataset --config $configFile --inputRucio --submitDir ${parentsubmitdir}/${submitdir}_$outname $extra -f prun --optGridOutputSampleName $outname --optTmpDir /tmp --optSubmitFlags=\"--addNthFieldOfInDSToLFN=2\""
        
        echo "Submitting job for dataset: $dataset with outname: $outname"
        $cmd
        ((counter++))
    done
fi
    
