Instead of "Review request to sign operation" use "Review transaction to propose protocols" ?

# Proposals
 - Source (2-3)
 - Period
 - Proposals (3-4) (---)
 "Review transaction to propose protocols"
 Remove source if equals to signer

# Ballot
 - Source (2-3)
 - Period
 - Proposal (3-4)
 - Ballot
 "Review transaction to vote a protocol"
 Remove source if equals to signer
 Rename "Ballot" ?

# Failing noop
 - Message (---)
 "Review a failing noop message"

# Reveal
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 - Public key (3-4)
 "Review transaction to vote a protocol"
 Remove source if equals to signer
 Don't display if (pk == signer) && (1 other operation) ?
 Remove fee if equals 0
 Remove storage limit if equals 0

# Transation
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 - Amount
 - Destination (2-3)
 ? Entrypoint (---1-2(1-31))
?! Parameter (---)
 "Review transaction to transfert tz"
 Remove source if equals to signer
 Remove fee if equals 0
 Remove storage limit if equals 0
 "Review transaction to stake tz" ... (what should we do for other known entrypoint ?)
 "Review transaction to call a smart contract"
 Remove amount if equals 0 ?

# Origination
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 - Balance
 - Delegate? (1-2-3)
 ! Code (---)
 ! Storage (---)
 "Review transaction to originate a smart contract"
 Remove source if equals to signer
 Remove fee if equals 0
 Remove storage limit if equals 0

# Delegation
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 ? Delegate (2-3)
 "Review transaction to choose a delegate"
 Remove source if equals to signer
 Remove fee if equals 0
 Remove storage limit if equals 0
 "Review transaction to self-delegate"

# Register global constant
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 ! Value (---)
 "Review transaction to register a global constant"
 Remove source if equals to signer
 Remove fee if equals 0
 Remove storage limit if equals 0
 if just the hash (as it should be) no complex

# Set deposit limit
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 ? Staking limit
 "Review transaction to set a deposit limit"
 Remove source if equals to signer
 Remove fee if equals 0
 Remove storage limit if equals 0
 "Review transaction to remove the deposit limit"

# Increase paid storage
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 - Amount
 - Destination (2-3)

# Set consensus key
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 - Public key (3-4)

# Transfer ticket
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 ! Contents (---)
 ! Type (---)
 - Ticketer (2-3)
 - Amount
 - Destination (2-3)
 - Entrypoint (---1-2(1-31))

# Sc rollup originate
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 - Kind
 ! Kernel (---)
 ! Parameters (---)
 ? Whitelist (2-3) (---)

# Sc rollup add message
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 - Messages (---) (---)

# Sc rollup execute outbox message
 - Source (2-3)
 - Fee
 / Counter
 / Gas
 - Storage limit
 - Rollup (2-3)
 - Commitment (3-4)
 ! Output proof (---)























Proposals                        (---)
Ballot                           (4-7)
Failing noop                     (---)
Reveal                           (4-7)
Transation                       (---)
Origination                      (---)
Delegation                       (4-6)
Register global constant         (---)
Set deposit limit                (4-5)
Increase paid storage            (5-7)
Set consensus key                (4-7)
Transfer ticket                  (---)
Sc rollup originate              (---)
Sc rollup add message            (---)
Sc rollup execute outbox message (---)



Reveal                           (4-7) multiple
Transation                       (---)
Delegation                       (4-6)
Sc rollup add message            (---)

Proposals                        (---) without_fee_n_amount 

Sc rollup add message            (---) one_operation

Transation                       (---) x6 many_transaction

Sc rollup add message            (---) too_large
Transation                       (---)
