#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Provide a path to the processed directory"
    exit
fi

ICONSPATH="$1"
mkdir ./"$ICONSPATH"/ttf
fantasticon ./"$ICONSPATH" -o ./"$ICONSPATH"/ttf --debug --font-types ttf

echo "Now use the web tool at https://android-iconics.mikepenz.com/ to upload the pack"
