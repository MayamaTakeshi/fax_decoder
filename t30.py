t30 = {
  "CED": {
    "meaning": "Called station identification",
    "details": "to indicate a called non-speech terminal. At 1.8 to 2.5 seconds after the called station is connected to the line, it send a continuous 2100 Hz tone for a duration of not less than 2.6 seconds and not more than 4.0 seconds."
  },
  "CFR": {
    "meaning": "Confirmation to receive",
    "details": "response confirming that the entire pre-message procedure has been completed and the message transmission may commence."
  },
  "CRP": {
    "meaning": "Command repeat",
    "details": "response indicating that the previous command was received in error and should be repeated."
  },
  "CIG": {
    "meaning": "Calling subscriber identification",
    "details": "signal indicating that the following FIF information is an identification of that calling station."
  },
  "CNG": {
    "meaning": "Calling tone",
    "details": "to indicate a calling non-speech terminal. A cyclic 1100 Hz tone, ON for 0.5 second, OFF for 3 seconds, to indicate to multifunction answering devices, or humans, that a fax sender is calling."
  },
  "CSI": {
    "meaning": "Called subscriber identification",
    "details": "signal providing the specific identity of the called subscriber by its international telephone number."
  },
  "DCN": {
    "meaning": "Disconnect",
    "details": "indicates the initiation of phase E (call release). This command requires no response."
  },
  "DCS": {
    "meaning": "Digital command signal",
    "details": "set-up command responding to the standard capabilities identified by the DIS signal."
  },
  "DIS": {
    "meaning": "Digital identification signal",
    "details": "characterizes the standard capabilities of the called apparatus."
  },
  "DTC": {
    "meaning": "Digital transmit command",
    "details": "response to the standard capabilities identified by the DIS signal."
  },
  "ECM": {
    "meaning": "Error correction mode"
  },
  "EOM": {
    "meaning": "End-of-message",
    "details": "indicates the end of a page of facsimile information and returns to the beginning of phase B."
  },
  "EOP": {
    "meaning": "End-of-procedures",
    "details": "indicates the end of a page of facsimile information and further indicates that no further documents are forthcoming."
  },
  "FCF": {
    "meaning": "Facsimile control field"
  },
  "FIF": {
    "meaning": "Facsimile information field"
  },
  "FTT": {
    "meaning": "Failure to train",
    "details": "response rejecting the Group 3 training signal and requesting a retraining."
  },
  "GC": {
    "meaning": "Group command",
    "details": "indicates to receiver what group transmitter will use."
  },
  "GI": {
    "meaning": "Group identification",
    "details": "indicates to sender what group receiver is capable of"
  },
  "HDLC": {
    "meaning": "High",
    "details": "level data link control"
  },
  "LCS": {
    "meaning": "Line conditioning signals"
  },
  "MCF": {
    "meaning": "Message confirmation",
    "details": "indicates that a complete message has been received and that additional messages may follow. (This is a positive response to MPS or EOM.)"
  },
  "MPS": {
    "meaning": "Multipage signal",
    "details": "indicates the end of a page of facsimile information and returns to the beginning of phase C upon receipt of a confirmation."
  },
  "NSC": {
    "meaning": "Non-standard facilites command",
    "details": "response to the information contained in the NSF signal."
  },
  "NSF": {
    "meaning": "Non-standard facilities",
    "details": "optional signal used to identify specific user requirements which are not covered by the standards."
  },
  "NSS": {
    "meaning": "Non-standard facilities set-up",
    "details": "optional signal is the response to the information contained in the NSC or NSF signal."
  },
  "PIN": {
    "meaning": "Procedure interrupt negative",
    "details": "indicates that the previous message has not been satisfactorily received and that further transmissions are not possible without operator intervention."
  },
  "PIP": {
    "meaning": "Procedure interrupt positive",
    "details": "indicates that a message has been received but that further transmissions are not possible without operator intervention."
  },
  "PIS": {
    "meaning": "Procedure interrupt signal",
    "details": "optional signal used to stop the distant machine. 462 Hz for minimum of 3 seconds."
  },
  "PPR": {
    "meaning": "Partial page request",
    "details": ""
  },
  "PPS": {
    "meaning": "Partial page signal",
    "details": "is used in ECM to indicate the end of a partial block"
  },
  "PRI-EOM": {
    "meaning": "Procedure interrupt",
    "details": "End-of-message - indicates the same as an EOM command with the additional optional capability of requesting operator intervention."
  },
  "PRI-EOP": {
    "meaning": "Procedure interrupt",
    "details": "End-of-procedure - indicates the same as an EOP command with the additional optional capablity of requesting operator intervention."
  },
  "PRI-MPS": {
    "meaning": "Procedure interrupt - Multipage signal",
    "details": "indicates the same as an MPS command with the additional optional capability of requesting operator intervention."
  },
  "RR": {
    "meaning": "Receiver ready",
    "details": "request to recipient in ECM for updated status after receiving an initial RNR."
  },
  "RNR": {
    "meaning": "Receiver not ready",
    "details": "response to sender in ECM if receiver is momentarily busy."
  },
  "RTN": {
    "meaning": "Retrian negative",
    "details": "indicates that the previous message has not been satisfactorily received. However, further receptions may be possible, provided training and/or phasing are retransmitted."
  },
  "RTP": {
    "meaning": "Retrain positive",
    "details": "indicates that a complete message has been received and that additional messages may follow after retransmission of training and/or phasing and CFR."
  },
  "TCF": {
    "meaning": "Training check",
    "details": "command sent through the T.4 modulation system to verify training and to give a first indication of the acceptability of the channel for this data rate."
  },
  "TSI": {
    "meaning": "Transmitting subscriber identification",
    "details": "signal indicating that the following FIF information is the identification of the transmitting station."
  },
  "CTC": {
    "meaning": "Continue to correct",
    "details": "Only used with ECM. A response message sent after the fourth PPR message indicating that the transmitter will continue to correct the previous message."
  },
  "CTR": {
    "meaning": "Response for continue to correct",
    "details": "An ECM message that is the response to a CTC that indicates that the receiving device accepts the contents included in the CTC message."
  },
}

