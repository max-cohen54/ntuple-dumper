#adapted from: https://xaodanahelpers.readthedocs.io/en/latest/UsingUs.html

from xAODAnaHelpers import Config
c = Config()

c.algorithm("BasicEventSelection", {"m_truthLevelOnly": False,
#                                    "m_applyGRLCut": True,
#                                    "m_GRLxml": "$ROOTCOREBIN/data/xAODAnaHelpers/data12_8TeV.periodAllYear_DetStatus-v61-pro14-02_DQDefects-00-01-00_PHYS_StandardGRL_All_Good.xml",
                                    "m_doPUreweighting": False,
                                    "m_vertexContainerName": "PrimaryVertices",
                                    "m_PVNTrack": 2,
                                    "m_useMetaData": False,
                                    "m_triggerSelection": "L1_.*|HLT_.*",
                                    "m_storeTrigDecisions": True,
                                    "m_storePassL1": True,
                                    "m_storePassHLT": True,
                                    "m_name": "myBaseEventSel"})


# Calibrate the offline jets
#c.algorithm("JetCalibrator",     {
#    "m_name"                    :   "calib",
#    #"m_msgLevel"                :   "debug",
#
#    # Container Flow
#    "m_inContainerName"         :   "AntiKt4EMPFlowJets",
#    "m_jetAlgo"                 :   "AntiKt4EMPFlowJets",
#    "m_outContainerName"        :   "AntiKt4EMPFlowJets_calib",
#    "m_outputAlgo"              :   "HLT_jets_calib_algo",
#    "m_sort"                    :   False,
#
#    # Systematics
#    "m_systName"                :   "Nominal",            ## For data
#    "m_systVal"                 :   0,                    ## For data
#
#    # Calibration
#    "m_calibConfigFullSim"      :   "PreRec_R22_PFlow_ResPU_EtaJES_GSC_February23_230215.config",
#    "m_calibConfigData"         :   "PreRec_R22_PFlow_ResPU_EtaJES_GSC_February23_230215.config",
#    "m_jetAlgo"                 :   "AntiKt4EMPFlow",
#    "m_calibSequence"           :   "JetArea_Residual_EtaJES_GSC_Insitu",
#
#    # Skip Cleaning
#    "m_doCleaning"              :   False,
#    "m_jetCleanCutLevel"        :   "LooseBad",
#    "m_jetCleanUgly"            :   False,
#    "m_saveAllCleanDecisions"   :   True,
#    "m_cleanParent"             :   False
#        
#} )

c.algorithm("TreeAlgo", {
                         "m_debug": True,
                         "m_name": "EB_Tree",
                         "m_jetContainerName": "HLT_AntiKt4EMPFlowJets_subresjesgscIS_ftf",
                         "m_jetBranchName": "HLT_jet",
                         "m_jetDetailStr": "kinematic clean timing energy",
			             "m_TrigMETContainerName": "HLT_MET_pfopufit",
                         "m_TrigMETDetailStr": "kinematic",
                         "m_trigDetailStr": "basic passTriggers",
                         "m_clusterContainerName": "HLT_TopoCaloClustersFS",#HLT_TopoCaloClustersLC",
                         "m_clusterBranchName": "HLT_TopoCaloClustersFS",
                         "m_clusterDetailStr": "kinematic",
                         #"m_jetDetailStr"                :  "kinematic", #trackPV trackAll allTrack
                         "m_trackParticlesContainerName" :  "HLT_IDTrack_FS_FTF",
                         "m_trackParticlesDetailStr"     :  "kinematic vertex numbers fitpars", #numbers fitpars
			             "m_evtDetailStr": "pileup eventCleaning"# caloClusters"
                         })


