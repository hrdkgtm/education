#!/bin/bash
# 

# GLOBAL VAR DECLARE
DOCFILE="script_listing"


# START OF SCRIPT
echo "#!/bin/more" > "$DOCFILE"

ls *.sh > tmplisting.txt

while IFS= read -r FILENAME
do
    if [[ -f "$FILENAME" ]]; then
        echo "=======================================" >> "$DOCFILE"
        echo "SCRIPT NAME : $FILENAME " >> "$DOCFILE"
        echo "=======================================" >> "$DOCFILE"
        echo
        echo "`cat $FILENAME`" >> "$DOCFILE"
    fi
done < tmplisting.txt

chmod 755 "$DOCFILE"

rm tmplisting.txt
