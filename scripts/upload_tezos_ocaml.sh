#!/usr/bin/env bash

TEZOS_LEDGER_BUILD=europe-west2-docker.pkg.dev/ledger-401708/ledger-build

gcloud auth login
docker image tag ledger-app-tezos-ocaml $TEZOS_LEDGER_BUILD/tezos_ocaml:latest
docker push $TEZOS_LEDGER_BUILD/tezos_ocaml:latest
