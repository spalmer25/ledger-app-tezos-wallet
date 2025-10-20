#!/usr/bin/env bash

set -x

CURR_DIR=$PWD

cd $(dirname "$0")/tezos/

if [ ! -z $FORCE ];
then
    rm -rf _opam
fi

make build-deps
eval $(opam env)
make install
dune install tezos-protocol-018-Proxford
dune install tezos-benchmarks-proto-018-Proxford

opam remote add opam https://opam.ocaml.org
opam update

opam install -y terminal_size

cd $CURR_DIR

exit 0


# RUSTUP_TOOLCHAIN=1.77.2
OCTEZ_VERSION=19.1
OCTEZ_REPO=https://gitlab.com/tezos/tezos.git
OCTEZ_COMMIT=`git ls-remote $OCTEZ_REPO octez-v$OCTEZ_VERSION | cut -f 1`
OCTEZ_URL=$OCTEZ_REPO#$OCTEZ_COMMIT
# wget https://sh.rustup.rs/rustup-init.sh
# chmod +x rustup-init.sh
# ./rustup-init.sh --profile minimal --default-toolchain $RUSTUP_TOOLCHAIN -y
# source "$HOME/.cargo/env"

if [ ! -z $FORCE ];
then
    rm -rf _opam
    opam switch -y create . 4.14.1
fi
opam install -y octez-rust-deps.$OCTEZ_VERSION
eval $(opam env)
opam update

opam install -y terminal_size octez-protocol-018-Proxford-libs.$OCTEZ_VERSION merlin ocamlformat
opam pin -y tezos-micheline-rewriting.$OCTEZ_VERSION                    $OCTEZ_URL
opam pin -y tezos-benchmark-type-inference-018-Proxford.$OCTEZ_VERSION  $OCTEZ_URL
opam pin -y tezos-benchmark-018-Proxford.$OCTEZ_VERSION                 $OCTEZ_URL
opam pin -y tezos-benchmarks-proto-018-Proxford.$OCTEZ_VERSION          $OCTEZ_URL

exit 0

if [ ! -z $FORCE ];
then
    rm -rf _opam
    opam switch -y create . 5.2.1 # tezos/scripts/version.sh
    opam remote add octez-22.1 https://github.com/tezos/opam-repository.git#octez-22.1
    opam update octez-22.1
fi

eval $(opam env)

OCTEZ_VERSION=22.1
OCTEZ_REPO=https://gitlab.com/tezos/tezos.git
OCTEZ_COMMIT=`git ls-remote $OCTEZ_REPO octez-v$OCTEZ_VERSION | cut -f 1`
OCTEZ_URL=$OCTEZ_REPO#$OCTEZ_COMMIT

# downgrade opentelemetry from 0.11.2 to 0.10
opam install -y opentelemetry.0.10 octez-protocol-022-PsRiotum-libs.$OCTEZ_VERSION terminal_size
opam pin -y tezos-micheline-rewriting.$OCTEZ_VERSION                    $OCTEZ_URL
opam pin -y tezos-benchmark-type-inference-022-PsRiotum.$OCTEZ_VERSION  $OCTEZ_URL
opam pin -y tezos-benchmark-022-PsRiotum.$OCTEZ_VERSION                 $OCTEZ_URL
opam pin -y tezos-benchmarks-proto-022-PsRiotum.$OCTEZ_VERSION          $OCTEZ_URL

exit 0

# RUSTUP_TOOLCHAIN=1.77.2
OCTEZ_VERSION=22.0
OCTEZ_REPO=https://gitlab.com/tezos/tezos.git
OCTEZ_COMMIT=`git ls-remote $OCTEZ_REPO octez-v$OCTEZ_VERSION | cut -f 1`
OCTEZ_URL=$OCTEZ_REPO#$OCTEZ_COMMIT
# wget https://sh.rustup.rs/rustup-init.sh
# chmod +x rustup-init.sh
# ./rustup-init.sh --profile minimal --default-toolchain $RUSTUP_TOOLCHAIN -y
# source "$HOME/.cargo/env"

if [ ! -z $FORCE ];
then
    rm -rf _opam
    opam switch -y create . 5.2.1
fi

eval $(opam env)
opam update
opam pin -y tezos-micheline-rewriting.$OCTEZ_VERSION                    $OCTEZ_URL
opam pin -y tezos-benchmark-type-inference-022-PsRiotum.$OCTEZ_VERSION  $OCTEZ_URL

opam install -y terminal_size opentelemetry.0.10 merlin ocamlformat
opam pin -y bls12-381.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-alcotezt.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-distributed-internal.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-distributed-lwt-internal.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-internal-libs.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-libs.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-proto-libs.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-protocol-compiler-compat.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-version.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-protocol-compiler.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezos-benchmark.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-shell-libs.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-rustzcash-deps.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezos-protocol-022-PsRiotum.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezt-tezos.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-node-config.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezos-dal-node-services.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y dal_node_migrations.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-riscv-api.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-riscv-pvm.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-performance-metrics.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-rust-deps.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-l2-libs.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezos-dal-node-lib.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-crawler.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-injector.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y octez-protocol-022-PsRiotum-libs.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezos-micheline-rewriting.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezos-benchmark-type-inference-022-PsRiotum.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezos-benchmark-022-PsRiotum.$OCTEZ_VERSION $OCTEZ_URL
opam pin -y tezos-benchmarks-proto-022-PsRiotum.$OCTEZ_VERSION $OCTEZ_URL

exit 0


sudo cp /usr/bin/opam-2.1 /usr/bin/opam
opam remote add opam https://opam.ocaml.org
opam remote add octez-22.0 https://github.com/tezos/opam-repository.git#octez-22.0
opam update
RUSTUP_TOOLCHAIN=1.77.2
OCTEZ_VERSION=22.0
OCTEZ_REPO=https://gitlab.com/tezos/tezos.git
OCTEZ_COMMIT=`git ls-remote $OCTEZ_REPO octez-v$OCTEZ_VERSION | cut -f 1`
OCTEZ_URL=$OCTEZ_REPO#$OCTEZ_COMMIT
wget https://sh.rustup.rs/rustup-init.sh
chmod +x rustup-init.sh
./rustup-init.sh --profile minimal --default-toolchain $RUSTUP_TOOLCHAIN -y
source "$HOME/.cargo/env"
opam install -y opentelemetry.0.10

opam install -y octez-protocol-022-PsRiotum-libs.$OCTEZ_VERSION

opam install -y terminal_size
opam pin -y tezos-micheline-rewriting.$OCTEZ_VERSION                    $OCTEZ_URL
opam pin -y tezos-benchmark-type-inference-022-PsRiotum.$OCTEZ_VERSION  $OCTEZ_URL
opam pin -y tezos-benchmark-022-PsRiotum.$OCTEZ_VERSION                 $OCTEZ_URL
opam pin -y tezos-benchmarks-proto-022-PsRiotum.$OCTEZ_VERSION          $OCTEZ_URL



sudo cp /usr/bin/opam-2.1 /usr/bin/opam
opam remote add opam https://opam.ocaml.org
RUSTUP_TOOLCHAIN=1.77.2
OCTEZ_VERSION=22.0
OCTEZ_REPO=https://gitlab.com/tezos/tezos.git
OCTEZ_COMMIT=`git ls-remote $OCTEZ_REPO octez-v$OCTEZ_VERSION | cut -f 1`
OCTEZ_URL=$OCTEZ_REPO#$OCTEZ_COMMIT
wget https://sh.rustup.rs/rustup-init.sh
chmod +x rustup-init.sh
./rustup-init.sh --profile minimal --default-toolchain $RUSTUP_TOOLCHAIN -y
source "$HOME/.cargo/env"
opam remote add octez-22.0 https://github.com/tezos/opam-repository.git#octez-22.0
opam update
opam install -y opentelemetry.0.10 
opam install -y octez-protocol-022-PsRiotum-libs.$OCTEZ_VERSION 
opam install -y terminal_size
opam pin -y tezos-micheline-rewriting.$OCTEZ_VERSION                    $OCTEZ_URL
opam pin -y tezos-benchmark-type-inference-022-PsRiotum.$OCTEZ_VERSION  $OCTEZ_URL
opam pin -y tezos-benchmark-022-PsRiotum.$OCTEZ_VERSION                 $OCTEZ_URL
opam pin -y tezos-benchmarks-proto-022-PsRiotum.$OCTEZ_VERSION          $OCTEZ_URL

### HERE



[ERROR] The compilation of octez-rustzcash-deps.22.1 failed at "dune build -p octez-rustzcash-deps -j 255".
-> installed optint.0.3.0
-> installed ordering.3.19.1
[ERROR] The compilation of octez-rust-deps.22.1 failed at "dune build -p octez-rust-deps -j 255".




sudo apk add --no-cache musl-dev musl-utils

sudo cp /usr/bin/opam-2.1 /usr/bin/opam
opam remote add opam https://opam.ocaml.org
RUSTUP_TOOLCHAIN=1.77.2
OCTEZ_OPAM_REPO_VERSION=octez-22.1
OCTEZ_VERSION=22.1
OCTEZ_REPO=https://gitlab.com/tezos/tezos.git
OCTEZ_COMMIT=`git ls-remote $OCTEZ_REPO octez-v$OCTEZ_VERSION | cut -f 1`
OCTEZ_URL=$OCTEZ_REPO#$OCTEZ_COMMIT
wget https://sh.rustup.rs/rustup-init.sh
chmod +x rustup-init.sh
./rustup-init.sh --profile minimal --default-toolchain $RUSTUP_TOOLCHAIN -y
source "$HOME/.cargo/env"
opam remote add $OCTEZ_OPAM_REPO_VERSION https://github.com/tezos/opam-repository.git#$OCTEZ_OPAM_REPO_VERSION
opam update $OCTEZ_OPAM_REPO_VERSION

opam install -y octez-rust-deps.$OCTEZ_VERSION

    opam install -y octez-rust-deps.$OCTEZ_VERSION bls12-381.$OCTEZ_VERSION octez-protocol-022-PsRiotum-libs.$OCTEZ_VERSION qcheck-core terminal_size



    opam install -y octez-rust-deps.$OCTEZ_VERSION




    sudo apt update && apt-get install -y build-essential cmake pkg-config libssl-dev   m4 unzip wget curl git libgmp-dev libev-dev libhidapi-dev
apt-get update && apt-get install -y build-essential cmake pkg-config libssl-dev   m4 unzip wget curl git libgmp-dev libev-dev libhidapi-dev
apk
rustup default stable
opam install -y octez-rust-deps.$OCTEZ_VERSION
history | less



















sudo cp /usr/bin/opam-2.1 /usr/bin/opam
opam remote add opam https://opam.ocaml.org

RUSTUP_TOOLCHAIN=1.77.2
OCTEZ_VERSION=22.1
OCTEZ_OPAM_REPO_VERSION=octez-$OCTEZ_VERSION
OCTEZ_REPO=https://gitlab.com/tezos/tezos.git
OCTEZ_COMMIT=$(git ls-remote $OCTEZ_REPO octez-v$OCTEZ_VERSION | cut -f 1)
OCTEZ_URL=$OCTEZ_REPO#$OCTEZ_COMMIT

sudo apk add --no-cache musl-dev musl-utils

wget https://sh.rustup.rs/rustup-init.sh
chmod +x rustup-init.sh
./rustup-init.sh --profile minimal --default-toolchain $RUSTUP_TOOLCHAIN -y
source "$HOME/.cargo/env"

opam remote add octez-$OCTEZ_VERSION https://github.com/tezos/opam-repository.git#octez-$OCTEZ_VERSION
opam update
opam install -y octez-rust-deps.$OCTEZ_VERSION
