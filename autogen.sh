#!/bin/bash

app_root_dir="ExtendedDiagramIcons"

# NOTE: azure icon set is not latest version
providers=(
  "octopusdeploy"
  "dnsproviders"
  "generic"
  "digitalocean"
)

# generate the module classes and docs
for pvd in "${providers[@]}"; do
  echo "generating the modules & docs for provider '$pvd'"
  python3 -m scripts.generate "$pvd"
done