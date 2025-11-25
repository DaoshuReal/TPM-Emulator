
TPM_RC_SUCCESS = 0x000
TPM_RC_COMMAND_CODE = 0x143
TPM_RC_FAILURE = 0x001
TPM_RC_INITIALIZE = 0x0B

TPM_SU_CLEAR = 0x0000
TPM_SU_STATE = 0x0001

TPM_CC = {
    "NV_UndefineSpaceSpecial":      0x0000011F,  # TPM_CC_NV_UndefineSpaceSpecial :contentReference[oaicite:0]{index=0}
    "EvictControl":                 0x00000120,  # :contentReference[oaicite:1]{index=1}
    "HierarchyControl":             0x00000121,  # :contentReference[oaicite:2]{index=2}
    "NV_UndefineSpace":             0x00000122,  # :contentReference[oaicite:3]{index=3}
    "ChangeEPS":                     0x00000124,  # :contentReference[oaicite:4]{index=4}
    "ChangePPS":                     0x00000125,  # :contentReference[oaicite:5]{index=5}
    "Clear":                          0x00000126,  # :contentReference[oaicite:6]{index=6}
    "ClearControl":                   0x00000127,  # :contentReference[oaicite:7]{index=7}
    "ClockSet":                       0x00000128,  # :contentReference[oaicite:8]{index=8}
    "HierarchyChangeAuth":            0x00000129,  # :contentReference[oaicite:9]{index=9}
    "NV_DefineSpace":                 0x0000012A,  # :contentReference[oaicite:10]{index=10}
    "PCR_Allocate":                   0x0000012B,  # :contentReference[oaicite:11]{index=11}
    "PCR_SetAuthPolicy":              0x0000012C,  # :contentReference[oaicite:12]{index=12}
    "PP_Commands":                    0x0000012D,  # :contentReference[oaicite:13]{index=13}
    "SetPrimaryPolicy":               0x0000012E,  # :contentReference[oaicite:14]{index=14}
    "FieldUpgradeStart":              0x0000012F,  # :contentReference[oaicite:15]{index=15}
    "ClockRateAdjust":                0x00000130,  # :contentReference[oaicite:16]{index=16}
    "CreatePrimary":                  0x00000131,  # :contentReference[oaicite:17]{index=17}
    "GetCapability":                   0x0000017A,  # :contentReference[oaicite:18]{index=18}
    "GetRandom":                        0x0000017B,  # :contentReference[oaicite:19]{index=19}
    "GetTestResult":                    0x0000017C,  # :contentReference[oaicite:20]{index=20}
    "Hash":                              0x0000017D,  # :contentReference[oaicite:21]{index=21}
    "PCR_Read":                         0x0000017E,  # :contentReference[oaicite:22]{index=22}
    "PolicyPCR":                        0x0000017F,  # :contentReference[oaicite:23]{index=23}
    "PolicyRestart":                   0x00000180,  # :contentReference[oaicite:24]{index=24}
    "ReadClock":                        0x00000181,  # :contentReference[oaicite:25]{index=25}
    "PCR_Extend":                        0x00000182,  # :contentReference[oaicite:26]{index=26}
    "PCR_SetAuthValue":                 0x00000183,  # :contentReference[oaicite:27]{index=27}
    "NV_Certify":                        0x00000184,  # :contentReference[oaicite:28]{index=28}
    "EventSequenceComplete":            0x00000185,  # :contentReference[oaicite:29]{index=29}
    "HashSequenceStart":                 0x00000186,  # :contentReference[oaicite:30]{index=30}
    "PolicyPhysicalPresence":              0x00000187,  # :contentReference[oaicite:31]{index=31}
    "PolicyDuplicationSelect":             0x00000188,  # :contentReference[oaicite:32]{index=32}
    "PolicyGetDigest":                     0x00000189,  # :contentReference[oaicite:33]{index=33}
    "TestParms":                             0x0000018A,  # :contentReference[oaicite:34]{index=34}
    "Commit":                                 0x0000018B,  # :contentReference[oaicite:35]{index=35}
    "PolicyPassword":                         0x0000018C,  # :contentReference[oaicite:36]{index=36}
    "ZGen_2Phase":                             0x0000018D,  # :contentReference[oaicite:37]{index=37}
    "EC_Ephemeral":                             0x0000018E,  # :contentReference[oaicite:38]{index=38}
    "PolicyNvWritten":                          0x0000018F,  # :contentReference[oaicite:39]{index=39}
    "PolicyTemplate":                             0x00000190,  # :contentReference[oaicite:40]{index=40}
    "CreateLoaded":                              0x00000191,  # :contentReference[oaicite:41]{index=41}
    "PolicyAuthorizeNV":                         0x00000192,  # :contentReference[oaicite:42]{index=42}
    "EncryptDecrypt2":                             0x00000193,  # :contentReference[oaicite:43]{index=43}
    "SelfTest":                                     0x00000143,  # note: in hex, this is 0x143 for SelfTest :contentReference[oaicite:44]{index=44}
    "Startup":                                      0x00000144,  # :contentReference[oaicite:45]{index=45}
    "Shutdown":                                     0x00000145,  # :contentReference[oaicite:46]{index=46}
    "StirRandom":                                   0x00000146,  # :contentReference[oaicite:47]{index=47}
    "ActivateCredential":                           0x00000147,  # :contentReference[oaicite:48]{index=48}
    "Certify":                                       0x00000148,  # :contentReference[oaicite:49]{index=49}
    "CertifyCreation":                               0x0000014A,  # :contentReference[oaicite:50]{index=50}
    "Duplicate":                                      0x0000014B,  # :contentReference[oaicite:51]{index=51}
    "GetTime":                                        0x0000014C,  # :contentReference[oaicite:52]{index=52}
    "GetSessionAuditDigest":                          0x0000014D,  # :contentReference[oaicite:53]{index=53}
    "PolicyNV":                                       0x00000149,  # :contentReference[oaicite:54]{index=54}
    "PolicyOR":                                       0x00000171,  # :contentReference[oaicite:55]{index=55}
    "PolicySigned":                                   0x00000160,  # :contentReference[oaicite:56]{index=56}
    "Quote":                                          0x00000158,  # :contentReference[oaicite:57]{index=57}
    "ReadPublic":                                     0x00000173,  # :contentReference[oaicite:58]{index=58}
    "Rewrap":                                          0x00000152,  # :contentReference[oaicite:59]{index=59}
    "Sign":                                           0x0000015D,  # :contentReference[oaicite:60]{index=60}
    "StartAuthSession":                              0x00000176,  # :contentReference[oaicite:61]{index=61}
    "Unseal":                                         0x0000015E,  # :contentReference[oaicite:62]{index=62},
    "VerifySignature":                                0x00000177,  # :contentReference[oaicite:63]{index=63},
}

class TPM:
    def __init__(self):
        # PCRs: 24 PCRs of 32 bytes each
        self.pcrs = [b'\x00' * 32 for _ in range(24)]
        
        # NV storage: persistent
        self.nv_storage = {}                              
        self.nv_counters = {}                              # NV write protection counters

        # Volatile objects
        self.keys = {}                                    # Transient keys
        self.persistent_handles = {}                      # Persistent keys
        self.sessions = {}                                # Auth sessions

        # Hierarchies
        self.hierarchies = {
            "owner": None,
            "endorsement": None,
            "platform": None
        }

        # Track if TPM has been started
        self.started = False

        # Command table
        self.commandTable = {}
        self.commandTable[TPM_CC["Startup"]] = self.handleStartup
        self.commandTable[TPM_CC["Shutdown"]] = self.handleShutdown

    def _parseHeader(self, headerBytes: bytes):
        tag = int.from_bytes(headerBytes[:2], 'big')
        size = int.from_bytes(headerBytes[2:6], 'big')
        code = int.from_bytes(headerBytes[6:10], 'big')
        return tag, size, code
    
    def _errorResponse(self, tag: int, errorCode):
        responseSize = 10
        return tag.to_bytes(2, 'big') + responseSize.to_bytes(4, 'big') + errorCode.to_bytes(4, 'big')

    def processCommand(self, commandBytes: bytes) -> bytes:
        tag, size, code = self._parseHeader(commandBytes)

        if code in self.commandTable:
            return self.commandTable[code](tag, commandBytes)
        else:
            return self._errorResponse(tag, TPM_RC_COMMAND_CODE)
        
    def handleStartup(self, tag, commandBytes: bytes) -> bytes:
        if len(commandBytes) < 12:
            return self._errorResponse(tag, TPM_RC_FAILURE)

        if self.started:
            return self._errorResponse(tag, TPM_RC_INITIALIZE)

        startupType = int.from_bytes(commandBytes[10:12], "big")

        if startupType == TPM_SU_CLEAR:
            # Clear PCRs
            self.pcrs = [b'\x00' * 32 for _ in range(24)]

            # Clear volatile sessions and transient keys
            self.sessions = {}
            self.keys = {}

            # Reset hierarchy auths
            self.hierarchies = {"owner": None, "endorsement": None, "platform": None}

            # Reset NV counters (volatile state), but keep NV storage intact
            self.nv_counters = {k:0 for k in self.nv_counters}
        elif startupType == TPM_SU_STATE:
            # TPM_SU_STATE preserves PCRs and volatile state
            pass
        else:
            return self._errorResponse(tag, TPM_RC_FAILURE)

        self.started = True
        responseSize = 10
        return tag.to_bytes(2, 'big') + responseSize.to_bytes(4, 'big') + TPM_RC_SUCCESS.to_bytes(4, 'big')

    def handleShutdown(self, tag, commandBytes: bytes) -> bytes:
        if len(commandBytes) < 12:
            return self._errorResponse(tag, TPM_RC_FAILURE)

        if not self.started:
            # Cannot shutdown if not started
            return self._errorResponse(tag, TPM_RC_INITIALIZE)

        shutdownType = int.from_bytes(commandBytes[10:12], "big")

        if shutdownType == TPM_SU_CLEAR:
            # Clear volatile state for next Startup
            self.sessions = {}
            self.keys = {}
            self.hierarchies = {"owner": None, "endorsement": None, "platform": None}
            self.pcrs = [b'\x00' * 32 for _ in range(24)]
            self.nv_counters = {k:0 for k in self.nv_counters}

        elif shutdownType == TPM_SU_STATE:
            # Preserve PCRs and volatile state
            pass
        else:
            return self._errorResponse(tag, TPM_RC_FAILURE)

        # Mark TPM as stopped
        self.started = False

        responseSize = 10
        return tag.to_bytes(2,'big') + responseSize.to_bytes(4,'big') + TPM_RC_SUCCESS.to_bytes(4,'big')
