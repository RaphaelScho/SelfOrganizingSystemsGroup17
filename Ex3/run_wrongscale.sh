if [ $1 == "train" ]
then 
	eval $"somtoolbox/somtoolbox.sh GrowingSOM som_wrongscale.prop"
elif [ $1 == "viz" ] 
then
	eval $"somtoolbox/somtoolbox.sh SOMViewer -u data/$2/group17.unit.gz -w data/$2/group17.wgt.gz --dw data/$2/group17.dwm.gz -c data/classes_sampled1000.cls -v data/input_vector_file_sampled1000_wrongscale.in -t data/template_vector_file_sampled1000.tv --vis MetroMap"
fi