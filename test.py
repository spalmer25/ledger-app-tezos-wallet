from bip_utils import (
    Bip39SeedGenerator,
    Bip32Slip10Ed25519,
    Bip32Secp256k1,
    Bip32Nist256p1,
)
from bip_utils.bip.bip32.bip32_path import Bip32Path, Bip32PathParser
from pytezos.crypto.encoding import base58_decode, base58_encode

def print_sk(bip32, prefix, mnemonic, path, passphrase=""):
    seed = Bip39SeedGenerator(mnemonic).Generate(passphrase)
    node = bip32.FromSeedAndPath(seed_bytes=seed, path=path)
    private_key = node.PrivateKey()
    raw_private_key = private_key.Raw()
    sk = base58_encode(raw_private_key.ToBytes(), prefix)
    print(sk.decode())

# Keys from Ledger tests
mnemonic = "zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra"
path = "m/44'/1729'/0'/0'"

print_sk(Bip32Slip10Ed25519, b'edsk', mnemonic, path)
## edsk2tUyhVvGj9B1S956ZzmaU4bC9J7t8xVBH52fkAoZL25MHEwacd
print_sk(Bip32Secp256k1, b'spsk', mnemonic, path)
## spsk2Pfx9chqXVbz2tW7ze4gGU4RfaiK3nSva77bp69zHhFho2zTze
print_sk(Bip32Nist256p1, b'p2sk', mnemonic, path)
## p2sk2zPCmKo6zTSjPbDHnLiHtPAqVRFrExN3oTvKGbu3C99Jyeyura

# Keys from Kukai tests: /Tests/KukaiCryptoSwiftTests/KeyPairTests.swift: testHD
mnemonic = "gym exact clown can answer hope sample mirror knife twenty powder super imitate lion churn almost shed chalk dust civil gadget pyramid helmet trade"

print_sk(Bip32Slip10Ed25519, b'edsk', mnemonic, "m/44'/1729'/0'/0'")
## edsk3c6QgPqmzhgpqDN8qvb1dApHPSp3NqWTDYjTiJkHjkuvwzL2Fz
print_sk(Bip32Slip10Ed25519, b'edsk', mnemonic, "m/44'/1729'/1'/0'")
## edsk483gztCNnUPHFH12dtKfyyGbhTrVWwHWtTGqX1Zct7aEPeUcJt
print_sk(Bip32Slip10Ed25519, b'edsk', mnemonic, "m/44'/1729'/2147483647'/0'")
## edsk3EjmrWJFAhv2j53JaKadLMhjAtkkx3tn3VCE34A7Hi3AoTg3zs
print_sk(Bip32Slip10Ed25519, b'edsk', mnemonic, "m/44'/1729'/1'/1'/1'")
## edsk48ELW18zTz9rp2fsn6LUZJ9sBkqCK92fS81aZXN63Ng8UGg4an
print_sk(Bip32Slip10Ed25519, b'edsk', mnemonic, "m/44'/1729'/0'/0'", "superSecurePassphrase")
## edsk4ToSdMSN17uXcE4rzarApqJFsLudGo9UvQsbYkdEDRAucpTvLo

# Keys from Taquito tests: /packages/taquito-signer/test/taquito-signer.spec.ts and /integration-tests/__tests__/ledger/ledger-signer.spec.ts
mnemonic = "prefer wait flock brown volume recycle scrub elder rate pair twenty giant"

print_sk(Bip32Slip10Ed25519, b'edsk', mnemonic, "m/44'/1729'/0'/0'")
## edsk4H3kk3PYuQaNyb6U27HQLSfa5Yt4CFFPQKA74HveDMW4F2DrM4
print_sk(Bip32Secp256k1, b'spsk', mnemonic, "m/44'/1729'/0'/0'")
## spsk3EH3Dv34YUqKY1QjMzkBD38fVAVefynm91TDY5MmRx4hXUwChQ
print_sk(Bip32Secp256k1, b'spsk', mnemonic, "m/44'/1729'/0/0")
## spsk2iaDXdNDx1fJYdengwgmPmSYSgGpwsEZZgFvnGPAg5qVghyssC
print_sk(Bip32Nist256p1, b'p2sk', mnemonic, "m/44'/1729'/0'/0'")
## p2sk2hXJP6JVCk2Jsgobr1smKvZueMjyT1eKgwvxcW5tbftbovqJ9Q
print_sk(Bip32Nist256p1, b'p2sk', mnemonic, "m/44'/1729'/0/0")
## p2sk3rufMWYi85AMjhvyyDpGZBPRUHde5o7oBbguEy4i9ySDrFoLW3
print_sk(Bip32Nist256p1, b'p2sk', mnemonic, "m/44'/1729'/1'/0'")
## p2sk3Lma2c2dAgyVrgeLHgQWvx5qxAHQCg5td92uxweFt7gt9vYJBH
print_sk(Bip32Slip10Ed25519, b'edsk', mnemonic, "m/44'/1729'/1'/0'")
## edsk2pz7s86xGzFsQCRQ43RATWtpfZkxoehbM83Ep8ZaY8Ngn9M9KU



def print_sk_(bip32, mnemonic, path, passphrase=""):
    seed = Bip39SeedGenerator(mnemonic).Generate(passphrase)
    node = bip32.FromSeedAndPath(seed_bytes=seed, path=path)
    private_key = node.PrivateKey()
    raw_private_key = private_key.Raw()
    print(raw_private_key.ToBytes().hex())

def print_all_sk(bip32):
    print_sk_(
        bip32,
        "zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra",
        "m/44'/1729'/0'/0'"
    )
    print_sk_(
        bip32,
        "prefer wait flock brown volume recycle scrub elder rate pair twenty giant",
        "m/44'/1729'/0'/0'"
    )
    print_sk_(
        bip32,
        "zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra",
        "m/44'/1729'/0'/0'",
        passphrase="myPassPhrase"
    )
    print_sk_(
        bip32,
        "prefer wait flock brown volume recycle scrub elder rate pair twenty giant",
        "m/44'/1729'/0'/0'",
        passphrase="myPassPhrase"
    )
    print_sk_(
        bip32,
        "zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra",
        "m/44'/1729'/0/0"
    )
    print_sk_(
        bip32,
        "prefer wait flock brown volume recycle scrub elder rate pair twenty giant",
        "m/44'/1729'/0/0"
    )
    print_sk_(
        bip32,
        "zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra",
        "m/44'/1729'/0/0",
        passphrase="myPassPhrase"
    )
    print_sk_(
        bip32,
        "prefer wait flock brown volume recycle scrub elder rate pair twenty giant",
        "m/44'/1729'/0/0",
        passphrase="myPassPhrase"
    )
print_all_sk(Bip32Nist256p1)


def print_full_sk(bip32, mnemonic, path, passphrase=""):
    seed = Bip39SeedGenerator(mnemonic).Generate(passphrase)
    node = bip32.FromSeed(seed_bytes=seed)
    path = Bip32PathParser.Parse(path)
    print("Index", node.Index().ToBytes().hex())
    print("Depth", node.Depth().ToBytes().hex())
    print("ChainCode", node.ChainCode().ToBytes().hex())
    print("Sk", node.PrivateKey().Raw().ToBytes().hex())
    for i, index in enumerate(path):
        path = Bip32Path(elems=[index], is_absolute=(i==0))
        node = node.DerivePath(path=path)
        print("Index", node.Index().ToBytes().hex())
        print("Depth", node.Depth().ToBytes().hex())
        print("ChainCode", node.ChainCode().ToBytes().hex())
        print("Sk", node.PrivateKey().Raw().ToBytes().hex())


## TODO: print-step by step for secp256k1 & p256 for rust & python
# ::after FromSeed -> m_priv_key(priv_key ; key_data)
print_sk_(
    Bip32Secp256k1,
    "zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra",
    "m/44'/1729'/0'/0'"
)
print_full_sk(
    Bip32Nist256p1,
    "zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra zebra",
    "m/44'/1729'/51'/123'"
)

## Bip32Secp256k1,

# Index 00000000
# Depth 00
# ChainCode fa6f46e69ed23ecc9fb687da13a4a219405b15b14eb460b24fefe5cb77a07926
# Sk 438e7b5b56d4c4594efe92c8c99917b6e9d1d9d40d90da71abac50af98c5afa9

# Index 8000002c
# Depth 01
# ChainCode 31fbdafea4ca2bbfaf7d650638b08733942165f69c17d442dca87d0ac1f09270
# Sk 8972348ac5d9ac24edac6cc6354ecf14b452a70953a14396c2788c44f509e0ea

# Index 800006c1
# Depth 02
# ChainCode 9eefcd5659c19c0da9e8fdeda5669af4d332681630f33a7235ee44600305a415
# Sk 5b2263972b0444a6e8d0f4be325875c6868512fdbdb05618606a51ba9dfd6e30

# Index 80000000
# Depth 03
# ChainCode 0e7a8af20af0b28a60e2f36db5476a37e9a23280b938d0cad8fe78c5e85e37e6
# Sk 61c430f4717b5ab26e5dbfca6f695cdd99898e9b98bedf6e2c3610fe40370da5

# Index 80000000
# Depth 04
# ChainCode 732dd2247c526cbbc3cf8e6d3d6ecb073de4276673dd4ed0efea9d82eb15fa3e
# Sk 7f667b8863e8b72738077c4de2b57dc744ebb7b0f1182072eafd782ff8cd4c2b


# ChainCode fa6f46e69ed23ecc9fb687da13a4a219405b15b14eb460b24fefe5cb77a07926
# Sk 438e7b5b56d4c4594efe92c8c99917b6e9d1d9d40d90da71abac50af98c5afa9

# Index 8000002c
# Index 01
# ChainCode 31fbdafea4ca2bbfaf7d650638b08733942165f69c17d442dca87d0ac1f09270
# Sk 8972348ac5d9ac24edac6cc6354ecf14b452a70953a14396c2788c44f509e0ea
# Parent ChainCode fa6f46e69ed23ecc9fb687da13a4a219405b15b14eb460b24fefe5cb77a07926
# Parent Sk 438e7b5b56d4c4594efe92c8c99917b6e9d1d9d40d90da71abac50af98c5afa9

# Index 800006c1
# Index 02
# ChainCode 9eefcd5659c19c0da9e8fdeda5669af4d332681630f33a7235ee44600305a415
# Sk 5b2263972b0444a6e8d0f4be325875c6868512fdbdb05618606a51ba9dfd6e30
# Parent ChainCode 31fbdafea4ca2bbfaf7d650638b08733942165f69c17d442dca87d0ac1f09270
# Parent Sk 8972348ac5d9ac24edac6cc6354ecf14b452a70953a14396c2788c44f509e0ea

# Index 80000000
# Index 03
# ChainCode 0e7a8af20af0b28a60e2f36db5476a37e9a23280b938d0cad8fe78c5e85e37e6
# Sk 61c430f4717b5ab26e5dbfca6f695cdd99898e9b98bedf6e2c3610fe40370da5
# Parent ChainCode 9eefcd5659c19c0da9e8fdeda5669af4d332681630f33a7235ee44600305a415
# Parent Sk 5b2263972b0444a6e8d0f4be325875c6868512fdbdb05618606a51ba9dfd6e30

# Index 80000000
# Index 04
# ChainCode 732dd2247c526cbbc3cf8e6d3d6ecb073de4276673dd4ed0efea9d82eb15fa3e
# Sk 7f667b8863e8b72738077c4de2b57dc744ebb7b0f1182072eafd782ff8cd4c2b
# Parent ChainCode 0e7a8af20af0b28a60e2f36db5476a37e9a23280b938d0cad8fe78c5e85e37e6
# Parent Sk 61c430f4717b5ab26e5dbfca6f695cdd99898e9b98bedf6e2c3610fe40370da5

# 7f667b8863e8b72738077c4de2b57dc744ebb7b0f1182072eafd782ff8cd4c2b





## Bip32Nist256p1

# Index 00000000
# Depth 00
# ChainCode 3f6f3d86613872572e6fa5d447c48ddcb63815bba72d989011522d698d5f833a
# Sk 02bb547e37591107d36e0cfb2ec027d0b60019781dedd5cec41b6bee86e34b51

# Index 8000002c
# Depth 01
# ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
# Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa

# Index 800006c1
# Depth 02
# ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
# Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a

# Index 80000000
# Depth 03
# ChainCode b39b4e2cc2f6e3f7c8dc66b0a0c0a9f2fb428e881aff5cab72fe7c4cbc84b2ff
# Sk 4f2307a43982488a9ea4b669f2dbd097298833d1888264f9d56d3740a9bf52d5

# Index 80000000
# Depth 04
# ChainCode 2a2e8816bdfa89f5373267173f4d569ffb3c7b8a1b2994ebd79ca8a0dda18672
# Sk 555c11a02098f87b36373ca4754149d1c77ffd91e92c875e10730bda3b533b6b



# ChainCode 3f6f3d86613872572e6fa5d447c48ddcb63815bba72d989011522d698d5f833a
# Sk 02bb547e37591107d36e0cfb2ec027d0b60019781dedd5cec41b6bee86e34b51

# Index 8000002c
# Index 01
# ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
# Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa
# Parent ChainCode 3f6f3d86613872572e6fa5d447c48ddcb63815bba72d989011522d698d5f833a
# Parent Sk 02bb547e37591107d36e0cfb2ec027d0b60019781dedd5cec41b6bee86e34b51

# Index 800006c1
# Index 02
# ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
# Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a
# Parent ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
# Parent Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa

# Index 80000000
# Index 03
# ChainCode b39b4e2cc2f6e3f7c8dc66b0a0c0a9f2fb428e881aff5cab72fe7c4cbc84b2ff
# Sk 4f2307a33982488b9ea4b669f2dbd0982bc05198805163430954a376d5ec36e5
# Parent ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
# Parent Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a

# Index 80000000
# Index 04
# ChainCode f85fbc83809134b6fd291ecb1045eec021a2f02a1cbd44de5402843b8d6ed065
# Sk 5a5a24bef29b85519276eef2e3f755120225147070504083f230dae79ffb9413
# Parent ChainCode b39b4e2cc2f6e3f7c8dc66b0a0c0a9f2fb428e881aff5cab72fe7c4cbc84b2ff
# Parent Sk 4f2307a33982488b9ea4b669f2dbd0982bc05198805163430954a376d5ec36e















Index 00000000
Depth 00
ChainCode 3f6f3d86613872572e6fa5d447c48ddcb63815bba72d989011522d698d5f833a
Sk 02bb547e37591107d36e0cfb2ec027d0b60019781dedd5cec41b6bee86e34b51

Index 8000002c
Depth 01
ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa

Index 800006c1
Depth 02
ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a

Index 00000000
Depth 03
ChainCode 2f09a4faa7b14b3580e3c4bfb792eb210bd297fffdd14055008e031c754ae8d4
Sk bdbf06570136256e7bdb8a27599f1d986db7b0afe111d1c27dddf8cde4522c6b

Index 00000000
Depth 04
ChainCode 5e74b33a07b14790c45832eaf5de155e73c886204cbd7e09c1f23362534218e5
Sk f590cf065b653ebec80bf34a32f0b3ec5c7a1c6d78135a03600b095412bc6e2b



# ChainCode 3f6f3d86613872572e6fa5d447c48ddcb63815bba72d989011522d698d5f833a
# Sk 02bb547e37591107d36e0cfb2ec027d0b60019781dedd5cec41b6bee86e34b51

# Index 8000002c
# Index 01
# ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
# Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa

# Index 800006c1
# Index 02
# ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
# Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a

# Index 00000000
# Index 03
# ChainCode eefedbfff547d1957935ca184f6522f1315a71f1aa21835c74b143c5a1286980
# Sk ba6661e89f1b726c1698d531c06d020cf83d0f8bf81199985f6d7995cbe75a6f

# Index 00000000
# Index 04
# ChainCode 614b928c87aeeaf59539b7310b3ffd2e556c20903d23b12d585b0e7aef07ee13
# Sk edddc125f6ca73ac3c7fe26a5c0e4782622297da3e89f98620b53234140da782

# edddc125f6ca73ac3c7fe26a5c0e4782622297da3e89f98620b53234140da782

Index 8000002c
Depth 01
ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa

Index 800006c1
Depth 02
ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a

Index 00000000
Depth 03
ChainCode eefedbfff547d1957935ca184f6522f1315a71f1aa21835c74b143c5a1286980
Sk ba6661e89f1b726c1698d531c06d020cf83d0f8bf81199985f6d7995cbe75a6f

Index 00000000
Depth 04
ChainCode 614b928c87aeeaf59539b7310b3ffd2e556c20903d23b12d585b0e7aef07ee13
Sk edddc125f6ca73ac3c7fe26a5c0e4782622297da3e89f98620b53234140da782

edddc125f6ca73ac3c7fe26a5c0e4782622297da3e89f98620b53234140da782
















## m/44'/1729'/51'/123'

Index 00000000
Depth 00
ChainCode 3f6f3d86613872572e6fa5d447c48ddcb63815bba72d989011522d698d5f833a
Sk 02bb547e37591107d36e0cfb2ec027d0b60019781dedd5cec41b6bee86e34b51
Index 8000002c
Depth 01
ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa
Index 800006c1
Depth 02
ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a
Index 80000033
Depth 03
ChainCode e1f01d2b1695cdeb7629d48cef4e329776a0f9d7a50d8dbc0e1394f5e651b246
Sk 8317e565e16aa2a6c21ff17ca6585bde4f626eb021cb5a8314c8859e632d6cc6
Index 8000007b
Depth 04
ChainCode 0b98ef2c9395c18108aca4eaf0bd9b979431ec862d01c7e2da5bcf075d43eb8e
Sk 6c922a6e8d1ba23092bb5784a4d1c45822095f4bf455477db5b31a2445a20aa9

# ChainCode 3f6f3d86613872572e6fa5d447c48ddcb63815bba72d989011522d698d5f833a
# Sk 02bb547e37591107d36e0cfb2ec027d0b60019781dedd5cec41b6bee86e34b51

# Index 8000002c
# Depth 01
# ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
# Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa

# Index 800006c1
# Depth 02
# ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
# Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a

# Index 80000033
# Depth 03
# ChainCode e1f01d2b1695cdeb7629d48cef4e329776a0f9d7a50d8dbc0e1394f5e651b246
# Sk 8317e564e16aa2a7c21ff17ca6585bdf519a8c77199a58cc48aff1d48f5a50d6

# Index 8000007b
# Depth 04
# ChainCode 79dd2f06f3c4211a32310b6963f8fdc2846bbf3b07db47128af00bbe2fed0c28
# Sk 1e31eebf9db0da37aa70379b7f16f0fe14955c22fb6fcbc8227e4608771f885e

Index 8000002c
Depth 01
ChainCode ae1707d77bccf232cf3ceee72aa964bfc3732fb8b0f9c0d1fee83a8ef64d4347
Sk 5bcc4aa8d67ef86aa9f31f13f1e64b4032eed4e54dbc896b3cd962c27df8e9aa
Index 800006c1
Depth 02
ChainCode 497572756309467b619001489139d367b0956e4df6e601c12e733b3be631b11e
Sk cff43c75b7088845a17dde26f5904f2742adc003ebfaec64c6b55365c400e81a
Index 80000033
Depth 03
ChainCode e1f01d2b1695cdeb7629d48cef4e329776a0f9d7a50d8dbc0e1394f5e651b246
Sk 8317e564e16aa2a7c21ff17ca6585bdf519a8c77199a58cc48aff1d48f5a50d6
Index 8000007b
Depth 04
ChainCode 79dd2f06f3c4211a32310b6963f8fdc2846bbf3b07db47128af00bbe2fed0c28
Sk 1e31eebf9db0da37aa70379b7f16f0fe14955c22fb6fcbc8227e4608771f885e
