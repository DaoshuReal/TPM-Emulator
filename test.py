from TPM import TPM, TPM_CC, TPM_SU_CLEAR, TPM_SU_STATE, TPM_RC_SUCCESS, TPM_RC_INITIALIZE

def build_command(cc, startup_type=None):
    """
    - Tag: TPM_ST_NO_SESSIONS = 0x8001 (standard for no-session commands)
    - Size: 10 or 12 bytes
    - CommandCode: TPM_CC
    - Optional: Startup type (2 bytes)
    """
    tag = (0x8001).to_bytes(2, 'big')
    if startup_type is not None:
        size = (12).to_bytes(4, 'big')
        code = cc.to_bytes(4, 'big')
        type_bytes = startup_type.to_bytes(2, 'big')
        return tag + size + code + type_bytes
    else:
        size = (10).to_bytes(4, 'big')
        code = cc.to_bytes(4, 'big')
        return tag + size + code

def main():
    tpm = TPM()

    print("Testing command before Startup...")
    cmd = build_command(TPM_CC["Shutdown"], TPM_SU_CLEAR)
    resp = tpm.processCommand(cmd)
    print("Shutdown response before Startup:", resp.hex())
    assert resp[-4:] == TPM_RC_INITIALIZE.to_bytes(4, 'big')

    print("Starting TPM...")
    cmd = build_command(TPM_CC["Startup"], TPM_SU_CLEAR)
    resp = tpm.processCommand(cmd)
    print("Startup response:", resp.hex())
    assert resp[-4:] == TPM_RC_SUCCESS.to_bytes(4, 'big')

    print("Attempting second Startup...")
    cmd = build_command(TPM_CC["Startup"], TPM_SU_CLEAR)
    resp = tpm.processCommand(cmd)
    print("Second Startup response:", resp.hex())
    assert resp[-4:] == TPM_RC_INITIALIZE.to_bytes(4, 'big')

    print("Shutting down TPM (SU_STATE)...")
    cmd = build_command(TPM_CC["Shutdown"], TPM_SU_STATE)
    resp = tpm.processCommand(cmd)
    print("Shutdown response:", resp.hex())
    assert resp[-4:] == TPM_RC_SUCCESS.to_bytes(4, 'big')

    print("Restarting TPM with SU_STATE...")
    cmd = build_command(TPM_CC["Startup"], TPM_SU_STATE)
    resp = tpm.processCommand(cmd)
    print("Startup response:", resp.hex())
    assert resp[-4:] == TPM_RC_SUCCESS.to_bytes(4, 'big')

    print("All tests passed!")

if __name__ == "__main__":
    main()
