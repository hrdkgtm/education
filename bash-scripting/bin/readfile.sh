#!/bin/bash
# simple file reading

read -p "Enter a filename to read :" FILENAME
echo

while read -r SUPERHERO; do
    echo " Superhero Name : $SUPERHERO"
done < "$FILENAME"
