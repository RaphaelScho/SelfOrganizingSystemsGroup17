PATH_TO_PROP="C:/Users/Raphael/Dropbox/UNI/S13_WS_2019/Self_Organizing_Systems/Exercises/SelfOrganizingSystemsGroup17/Ex3"
PATH_TO_DATA="C:/Users/Raphael/Dropbox/UNI/S13_WS_2019/Self_Organizing_Systems/Exercises/SelfOrganizingSystemsGroup17/Ex3/data"

if [ $1 == "train" ] 
then 
	eval $"./somtoolbox.sh GrowingSOM ${PATH_TO_PROP}/som.prop"
elif [ $1 == "viz" ] 
then
	eval $"./somtoolbox.sh SOMViewer -u ${PATH_TO_DATA}/out/group17.unit.gz -w ${PATH_TO_DATA}/out/group17.wgt.gz --dw ${PATH_TO_DATA}/out/group17.dwm.gz -c ${PATH_TO_DATA}/classes_sampled1000.cls -v ${PATH_TO_DATA}/input_vector_file_sampled1000.in"
fi
