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
rm $EXDIR/handleiding.ipynb
rm -R $EXDIR/assets_handleiding
cp $GITDIR/handleiding.ipynb $EXDIR/handleiding.ipynb
cp -r $GITDIR/assets_handleiding $EXDIR/assets_handleiding
echo "DONE"