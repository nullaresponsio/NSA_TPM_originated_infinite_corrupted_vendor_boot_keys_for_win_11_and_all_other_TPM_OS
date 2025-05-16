digraph G {
    rankdir=LR;
    node [shape=box, style=filled];

    /* Palette */
    BoStyle      = "#FFF6C0";    // light yellow
    ToolStyle    = "#FFD28A";    // light orange
    TrustedStyle = "#E0F6D5";    // light green
    TPMStyle     = "#F4B0AD";    // light red
    DecideStyle  = "#B0C8E8";    // light blue

    Bo       [label="Bo Shang",                 fillcolor=BoStyle];
    Cloud    [label="Microsoft Cloud\n(attest ECC P-256)", fillcolor=TrustedStyle];
    SavedECC [label="Saved Non-Corrupted\nECC P-256 Cert", fillcolor=BoStyle];
    Ghidra   [label="Ghidra",                   fillcolor=ToolStyle];
    Drivers  [label="Kernel Driver Set",        fillcolor=ToolStyle];
    SigExt   [label="Extracted\nSignatures",    fillcolor=ToolStyle];
    TPMbad   [label="Corrupted TPM\nRSA-2048",  fillcolor=TPMStyle];
    Decide   [label="Mismatch?", shape=diamond, fillcolor=DecideStyle];
    Clean    [label="Driver Clean",             fillcolor=DecideStyle];
    Reinst   [label="Integrity\nCompromised →\nReinstall", fillcolor=DecideStyle];

    /* trusted steps (green) */
    Bo    -> Cloud    [label="attest & fetch", color=darkgreen, penwidth=2];
    Cloud -> SavedECC [label="save",           color=darkgreen, penwidth=2];

    Bo    -> Ghidra   [label="launch",         color=darkgreen];
    SavedECC -> Drivers [label="extract",      color=darkgreen];

    /* analysis (gray) */
    Ghidra -> Drivers [label="load",           color=gray];
    Drivers -> SigExt [label="extract",        color=gray];
    SigExt  -> Decide [color=gray];

    /* corrupted input (red dashed) */
    TPMbad  -> Decide [label="RSA input", style=dashed, color=red];

    /* ECC input (green) */
    SavedECC -> Decide [label="ECC input", color=darkgreen];

    /* decision */
    Decide -> Reinst [label="Yes", color=red];
    Decide -> Clean  [label="No",  color=darkgreen];
}
