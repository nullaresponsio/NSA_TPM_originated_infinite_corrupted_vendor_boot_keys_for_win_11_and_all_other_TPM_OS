digraph G {
    rankdir=LR;
    node [shape=box, style=filled, fillcolor="#FFFFCC"];

    Bo       [label="Bo Shang"];
    Cloud    [label="Microsoft Cloud\nAttest ECC P-256"];
    SavedECC [label="Saved Non-Corrupted\nECC P-256 cert"];
    Ghidra   [label="Ghidra"];
    Drivers  [label="Kernel Driver Set"];
    SigExt   [label="Extracted\nSignatures"];
    TPMbad   [label="Corrupted TPM\nRSA-2048"];
    Compare  [label="Compare\nSignatures"];

    /* attest & save */
    Bo    -> Cloud    [label="Login / attest",  color=darkgreen];
    Cloud -> SavedECC [label="Save cert",       color=darkgreen];

    /* analysis path */
    Bo     -> Ghidra  [label="Launch",          color=darkgreen];
    Ghidra -> Drivers [label="Disassemble",     color=darkgreen];
    Drivers-> SigExt  [label="Extract",         color=darkgreen];
    SigExt -> Compare [label="Input sigs",      color=gray];

    /* comparison inputs */
    SavedECC -> Compare [label="ECC input",   color=darkgreen];
    TPMbad   -> Compare [label="RSA input",  style=dashed, color=red];
}
