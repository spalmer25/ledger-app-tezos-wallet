# Not handled
## Consensus
Preattestation 
Attestation 
## Voting
## Anonymous
Seed nonce revelation
Vdf revelation
Double preattestation evidence
Double attestation evidence
Double baking evidence
Activate account
Drain delegate
## Manager
Dal publish commitment
Sc rollup cement
Sc rollup publish
Sc rollup refute
Sc rollup timeout
Sc rollup recover_bond
Zk rollup origination
Zk rollup publish
Zk rollup update

# Proposals
 - Source (PKH)
 - Period (Int32)
 - Proposals (Proto-hash list)

# Ballot
 - Source (PKH)
 - Period (Int32)
 - Proposal (Proto-hash)
 - Ballot (Ballot: Yay | Nay | Pass)

# Failing noop
 - Message (String)

# Reveal
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Public key (PK)

# Transation
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Amount (TZ)
 - Destination (PKH)
 - Entrypoint (String (1-31))
 - Parameter (Script)

# Origination
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Delegate (PKH option)
 - Script (Script)
 - Credit (TZ)

# Delegation
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Delegate (PKH option)

# Register global constant
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Value (Script)

# Set deposit limit
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Limit (TZ)

# Increase paid storage
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Amount (Z)
 - Destination (Contract-hash)

# Set consensus key
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Public key (PK)

# Transfer ticket
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Contents (Script)
 - Type (Script)
 - Ticketer (Contract-hash)
 - Amount (Z)
 - Destination (Contract-hash)
 - Entrypoint (String (1-31))

# Sc rollup originate
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Kind (Kind: Example_arith | Wasm_2_0_0 | Riscv)
 - Boot sector (String)
 - Parameters_ty (Script)
 - Whitelist (PKH list option)

# Sc rollup add message
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Messages (String list)

# Sc rollup execute outbox message
 - Source (PKH)
 - Fee (TZ)
 - Counter (Z)
 - Gas (Int)
 - Storage limit (Z)
 - Rollup (Rollup-hash)
 - Commitment (Commitment-hash)
 - Output proof (String)

