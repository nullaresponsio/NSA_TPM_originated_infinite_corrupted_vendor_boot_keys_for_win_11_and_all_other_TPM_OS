// Combined: store deployment + Ghidra analysis
digraph G {
    rankdir=LR;
    node [shape=box, style=filled, fillcolor="#FFFFCC"];

    /* Developer path */
    DevAcct [label="Bo Shang\nDeveloper Account\nECC P-256 dev cert"];
    VS      [label="Visual Studio\nBuild & Sign"];
    Appx    [label="Signed App (.appx)\nDev cert ECC P-256"];
    Store   [label="Microsoft Store\nIngestion"];
    NSA     [label="Admin PowerShell\nNSA RSA-2048"];

    DevAcct -> VS   [label="login", color=darkgreen];
    VS      -> Appx [label="sign",  color=darkgreen];
    Appx    -> Store[label="upload", color=darkgreen];
    NSA     -> VS   [label="not used", style=dashed, color=red];

    /* Ghidra analysis path */
    Ghidra  [label="Ghidra"];
    Drivers [label="Kernel Driver Set"];
    SigExt  [label="Extracted\nSignatures"];
    SavedECC[label="Saved non-corrupted\nECC P-256 cert"];
    TPMbad  [label="Corrupted TPM\nRSA-2048"];
    Compare [label="Compare\nsignatures"];

    DevAcct -> SavedECC    [label="attest & save", color=darkgreen];
    Ghidra  -> Drivers     [label="disassemble"];
    Drivers -> SigExt;
    SigExt  -> Compare;
    SavedECC-> Compare     [label="ECC input"];
    TPMbad  -> Compare     [label="RSA input", style=dashed, color=red];
}
