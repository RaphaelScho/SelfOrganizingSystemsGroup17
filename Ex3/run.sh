if [ $1 == "train" ]
then 
	eval $"somtoolbox/somtoolbox.sh GrowingSOM som.prop"
elif [ $1 == "viz" ] 
then
	eval $"somtoolbox/somtoolbox.sh SOMViewer -u data/$2/group17.unit.gz -w data/$2/group17.wgt.gz --dw data/$2/group17.dwm.gz -c data/classes_sampled1000.cls -v data/input_vector_file_sampled1000.in -t data/template_vector_file_sampled1000.tv --vis MetroMap"
elif [ $1 == "qe" ]
then
  eval $"somtoolbox/somtoolbox.sh QualityMeasureComputer -w data/$2/group17.wgt.gz -m data/$2/group17.map -u data/$2/group17.unit.gz -v data/input_vector_file_sampled1000.in -t data/template_vector_file_sampled1000.tv --dw data/$2/group17.dwm.gz --qualityClass q_qe --qualityVariant MQE_Map ./out.txt"
fi