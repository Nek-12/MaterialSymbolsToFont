#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Provide a path to the font directory"
    exit
fi

ICONSPATH="$1"
mkdir ./"$ICONSPATH"/ttf
fantasticon ./"$ICONSPATH" -o ./"$ICONSPATH"/ttf --debug --font-types ttf
