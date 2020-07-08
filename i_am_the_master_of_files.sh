#!/bin/bash
echo $'[FILE]\nfolder = ./uploads\nid = '$2$'\nslots = 2' > $1
chmod o-r $1