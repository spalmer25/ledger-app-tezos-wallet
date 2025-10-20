#!/usr/bin/env bash

TEZOS_LEDGER_BUILD=europe-west2-docker.pkg.dev/ledger-401708/ledger-build

gcloud auth login
docker pull $TEZOS_LEDGER_BUILD/tezos_ocaml:latest
docker image tag $TEZOS_LEDGER_BUILD/tezos_ocaml ledger-app-tezos-ocaml:latest
