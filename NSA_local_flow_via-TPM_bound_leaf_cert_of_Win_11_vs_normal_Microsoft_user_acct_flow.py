# Directed cryptographic flow: MSA user vs NSA local admin via TPM-bound leaf certificate
from graphviz import Digraph

g = Digraph('CryptoFlow', filename='crypto_flow.gv', format='png')
g.attr(rankdir='LR', node_attr={'shape': 'box', 'style': 'filled', 'fillcolor': 'lightgray'})

g.node('MSAKey',          'MSA Account Key\nRSA-2048')
g.node('AADJWT',          'Azure AD JWT Token\nRS256')
g.node('KerbTGT',         'Kerberos TGT\nAES256-SHA1')
g.node('UserSessionKey',  'User Session Key\nDPAPI\nAES256-CBC')
g.node('TPMRootKey',      'TPM Root Storage Key\nECC-P-256')
g.node('NSAStolenLeaf',   'NSA Leaf Cert\nECC-P-384')
g.node('NSAAdminToken',   'NSA Admin Token\nECDSA-P-384')
g.node('AdminSAMHash',    'Local Admin SAM Hash\nNTLMv2')
g.node('PowerShellNonAdmin', 'PowerShell (Non-Admin Session)\nRestricted')
g.node('PowerShellAdmin',    'PowerShell (Admin Session)\nFull Control')

g.edge('MSAKey',        'AADJWT',         label='sign RS256')
g.edge('AADJWT',        'KerbTGT',        label='issue AS-REP')
g.edge('KerbTGT',       'UserSessionKey', label='decrypt DPAPI')
g.edge('UserSessionKey','PowerShellNonAdmin', label='invoke • denied')

g.edge('TPMRootKey',    'NSAStolenLeaf',  label='bind')
g.edge('NSAStolenLeaf', 'NSAAdminToken',  label='sign ECDSA-P-384')
g.edge('NSAAdminToken', 'AdminSAMHash',   label='unlock SAM')
g.edge('NSAAdminToken', 'PowerShellAdmin',label='invoke • allowed')

g.render()
