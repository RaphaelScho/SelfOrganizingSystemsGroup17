if [ $1 == "train" ]
then 
	eval $"somtoolbox/somtoolbox.sh GrowingSOM som.prop"
elif [ $1 == "viz" ] 
then
	eval $"somtoolbox/somtoolbox.sh SOMViewer -u data/out/group17.unit.gz -w data/out/group17.wgt.gz --dw data/out/group17.dwm.gz -c data/classes_sampled1000.cls -v data/input_vector_file_sampled1000.in"
fi
