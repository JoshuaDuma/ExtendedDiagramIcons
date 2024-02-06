#!/bin/bash

app_root_dir="ExtendedDiagramIcons"

# NOTE: azure icon set is not latest version
providers=(
  "onprem",
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
  python -m scripts.generate "$pvd"
done

# Generate doc for custom module
echo "generating the docs for custom"
python -m scripts.generate "custom"

# copy icons across to website
echo "copying icons to website static folder"
cp -r resources website/static/img/

# run black
echo "linting the all the diagram modules"
black "$app_root_dir"/**/*.py