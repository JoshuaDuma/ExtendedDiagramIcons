#!/bin/bash

app_root_dir="ExtendedDiagramIcons"

# NOTE: azure icon set is not latest version
providers=(
  "octopusDeploy",
  "dndProviders",
  "generic"
)

if ! [ -x "$(command -v black)" ]; then
  echo 'black is not installed'
  exit 1
fi

# generate the module classes and docs
for pvd in "${providers[@]}"; do
  echo "generating the modules & docs for provider '$pvd'"
  python3 -m scripts.generate "$pvd"
done

# Generate doc for custom module
echo "generating the docs for custom"
python3 -m scripts.generate "custom"