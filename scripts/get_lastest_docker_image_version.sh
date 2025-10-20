#!/usr/bin/env bash

GITHUB_TOKEN="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"

REPO=${REPO:-"ledgerhq/ledger-app-builder/ledger-app-dev-tools"}

DOCKER_TOKEN=$(curl -s "https://ghcr.io/token?scope=repository:$REPO:pull" | jq -r '.token')

LATEST=$(curl -s -H "Authorization: Bearer $DOCKER_TOKEN" "https://ghcr.io/v2/$REPO/tags/list" | jq -r '.tags[-1]')
CURRENT=$(docker inspect "ghcr.io/$REPO" | jq -r '.[].Config.Labels.["org.opencontainers.image.version"]')

RED="\e[31m"
GREEN="\e[32m"
BLUE="\e[34m"
RESET="\e[0m"

if [ "$LATEST" == "$CURRENT" ]; then
    echo -e "${BLUE}$REPO${RESET} is up to date: ${GREEN}$LATEST${RESET}"
    exit 0
else
    echo -e "${BLUE}$REPO${RESET} is out of date"
    echo -e "Latest version: ${GREEN}$LATEST${RESET}"
    echo -e "Current version: ${RED}$CURRENT${RESET}"
    exit 1
fi
