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
c.algorithm("JetCalibrator",     {
    "m_name"                    :   "calib",
    #"m_msgLevel"                :   "debug",

    # Container Flow
    "m_inContainerName"         :   "AntiKt4EMPFlowJets",
    "m_jetAlgo"                 :   "AntiKt4EMPFlowJets",
    "m_outContainerName"        :   "AntiKt4EMPFlowJets_calib",
    "m_outputAlgo"              :   "HLT_jets_calib_algo",
    "m_sort"                    :   False,

    # Systematics
    "m_systName"                :   "Nominal",            ## For data
    "m_systVal"                 :   0,                    ## For data

    # Calibration
    "m_calibConfigFullSim"      :   "PreRec_R22_PFlow_ResPU_EtaJES_GSC_February23_230215.config",
    "m_calibConfigData"         :   "PreRec_R22_PFlow_ResPU_EtaJES_GSC_February23_230215.config",
    "m_jetAlgo"                 :   "AntiKt4EMPFlow",
    "m_calibSequence"           :   "JetArea_Residual_EtaJES_GSC_Insitu",

    # Skip Cleaning
    "m_doCleaning"              :   False,
    "m_jetCleanCutLevel"        :   "LooseBad",
    "m_jetCleanUgly"            :   False,
    "m_saveAllCleanDecisions"   :   True,
    "m_cleanParent"             :   False
        
} )

c.algorithm("TreeAlgo", {
                         "m_debug": True,
                         "m_name": "EB_Tree",
                         "m_jetContainerName": "HLT_AntiKt4EMPFlowJets_subresjesgscIS_ftf AntiKt4EMPFlowJets_calib",
                         "m_jetBranchName": "HLT_jet ofl_jet",
                         "m_jetDetailStr": "kinematic clean timing energy",
                         "m_photonContainerName": "HLT_egamma_Photons Photons",
                         "m_photonBranchName": "HLT_ph ofl_ph",
                         "m_photonDetailStr": "kinematic PID PID_Medium",
                         "m_elContainerName": "HLT_egamma_Electrons_GSF HLT_egamma_Electrons_LRT Electrons",
                         "m_elBranchName": "HLT_el HLT_el_LRT, ofl_el",
                         "m_elDetailStr": "kinematic PID PID_Medium",
                         "m_muContainerName": "HLT_Muons_FS HLT_MuonsCB_LRT Muons",
                         "m_muBranchName": "HLT_muon HLT_muon_LRT ofl_muon",
                         "m_muDetailStr": "kinematic quality RECO_Medium",
			             "m_l1JetContainerName": "L1_jFexSRJetRoI L1_jFexLRJetRoI",
                         "m_l1JetBranchName": "L1_jFexSRJet L1_jFexLRJet",
			             "m_TrigMETContainerName": "HLT_MET_pfopufit",
                         "m_TrigMETDetailStr": "kinematic",
                         "m_trigDetailStr": "basic passTriggers",
                         "m_l1MuonContainerName": "LVL1MuonRoIs",
                         "m_l1MuonBranchName": "L1Muon",
                         "m_l1TauContainerName": "L1_jFexTauRoI L1_eTauRoI",
                         "m_l1TauBranchName": "L1Tau_jFex L1Tau_eFex",
                         "m_l1EMContainerName": "L1_eEMRoI",
                         "m_l1EMBranchName": "L1Egamma",
                         "m_l1MetContainerName": "L1_jFexMETRoI",
                         "m_l1MetDetailStr": "kinematic",
                         "m_l1MetBranchName": "L1MET",
			             "m_evtDetailStr": "pileup"
                         })


