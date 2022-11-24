GITDIR=.
EXDIR=../mijn_oefeningen
echo "Copying new files from gitdir to exercises dir..."
mkdir $EXDIR 2>/dev/null
yes n | cp -i -R $GITDIR/* $EXDIR 2>/dev/null
chmod +w -R $EXDIR 
rm $EXDIR/update_workspace.sh
chmod -w $EXDIR/hulpfunctiesBroeikasgassen.py 
chmod -w $EXDIR/hulpfunctiesKlimaatopwarming.py 
chmod -w $EXDIR/knipFuncties.py 
chmod -w $EXDIR/modeleerFuncties.py 
chmod -w $EXDIR/plotFuncties.py 
echo "DONE"