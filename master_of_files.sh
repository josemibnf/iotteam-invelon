STR=$'[FILE]\nfolder = ./uploads\nid = '$2$'\nslots = 2'
echo "$STR" > $1
chmod o-r $1