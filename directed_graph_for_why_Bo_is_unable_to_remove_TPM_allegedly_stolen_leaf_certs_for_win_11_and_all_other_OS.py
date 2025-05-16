from graphviz import Digraph

g = Digraph('ImpossibleRemoval', filename='tpm_leaf_lock.gv', format='png')
g.attr(rankdir='LR', node_attr={'shape': 'box', 'style': 'filled', 'fillcolor': 'lightgray', 'fontname': 'Consolas'})

g.node('TPM_Root', 'TPM Root Key\n(EK ECC-P256)')
g.node('AIK', 'Attestation ID Key\n(ECDSA-P256)')
g.node('LeafCert', 'Leaf Cert\n(ECDSA-P384)\nNV Index')
g.node('PCR', 'Measured Boot PCR[7]\nSHA-256')
g.node('SecureBoot', 'UEFI Secure Boot Policy\nRSA-2048')
g.node('BootMgr', 'Windows Boot Manager\nSHA-256')
g.node('Kernel', 'Win11 Kernel Code\nSHA-256')
g.node('LSASS', 'LSASS & SAM\nAES-256')
g.node('BoMSA', 'Bo MSA Token\nRS256 JWT')
g.node('RemoveCmd', 'Remove-Item Cert:\\LocalMachine\\TrustedRoot')
g.node('Fail', 'Operation Fails\nAccess Denied')

g.edge('TPM_Root', 'AIK', 'derive')
g.edge('AIK', 'LeafCert', 'sign')
g.edge('LeafCert', 'SecureBoot', 'enforce')
g.edge('SecureBoot', 'BootMgr', 'verify')
g.edge('BootMgr', 'Kernel', 'verify')
g.edge('Kernel', 'LSASS', 'starts')
g.edge('BoMSA', 'RemoveCmd', 'invokes')
g.edge('RemoveCmd', 'LSASS', 'needs Admin')
g.edge('LSASS', 'Fail', 'blocks')
g.edge('LeafCert', 'Fail', 'TPM bound')

g.render()
