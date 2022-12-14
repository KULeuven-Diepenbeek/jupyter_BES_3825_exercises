GITDIR=.
EXDIR=../mijn_oefeningen
echo "Copying new files from gitdir to exercises dir..."
mkdir $EXDIR 2>/dev/null
yes n | cp -i -R $GITDIR/* $EXDIR 2>/dev/null
chmod +w -R $EXDIR 
rm $EXDIR/update_workspace.sh

rm $EXDIR/modeleerFuncties.py
cp $GITDIR/modeleerFuncties.py $EXDIR/modeleerFuncties.py
rm $EXDIR/knipFuncties.py
cp $GITDIR/knipFuncties.py $EXDIR/knipFuncties.py
rm $EXDIR/plotFuncties.py
cp $GITDIR/plotFuncties.py $EXDIR/plotFuncties.py

rm $EXDIR/hulpfunctiesBroeikasgassen.py
cp $GITDIR/hulpfunctiesBroeikasgassen.py $EXDIR/hulpfunctiesBroeikasgassen.py
rm $EXDIR/hulpfunctiesKlimaatopwarming.py
cp $GITDIR/hulpfunctiesKlimaatopwarming.py $EXDIR/hulpfunctiesKlimaatopwarming.py

chmod -w $EXDIR/hulpfunctiesBroeikasgassen.py 
chmod -w $EXDIR/hulpfunctiesKlimaatopwarming.py 
chmod -w $EXDIR/knipFuncties.py 
chmod -w $EXDIR/modeleerFuncties.py 
chmod -w $EXDIR/plotFuncties.py 

rm $EXDIR/handleiding.ipynb
rm -R $EXDIR/assets_handleiding
cp $GITDIR/handleiding.ipynb $EXDIR/handleiding.ipynb
cp -r $GITDIR/assets_handleiding $EXDIR/assets_handleiding
rm $EXDIR/Jupyterlab_tips_and_tricks.ipynb
cp $GITDIR/Jupyterlab_tips_and_tricks.ipynb $EXDIR/Jupyterlab_tips_and_tricks.ipynb

rm -R $EXDIR/assets
cp -r $GITDIR/assets $EXDIR/assets
echo "DONE"