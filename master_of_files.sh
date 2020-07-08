> $1
chmod o-r $1
echo "[FILE]" >> $1
echo "folder = ./uploads" >> $1
echo "id = "$2 >> $1
echo "slots = 2" >> $1