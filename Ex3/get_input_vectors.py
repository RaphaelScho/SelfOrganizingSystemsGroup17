def create_input_vectors():
	out = ""
	counter = 0
	skip_first = True
	with open("data/mnist_784_sampled.csv", "r") as f_in:
		with open("data/input_vector_file_sampled.in", "a") as f_out:
			f_out.write("$TYPE inputvec\n" + \
						"$XDIM 70000\n" + \
						"$YDIM 1\n" + \
						"$VEC_DIM 784\n\n")
			for line in f_in:
				if skip_first:
					skip_first = False
					continue

				splited = line.split(",")[:-1]
				f_out.write(" ".join(splited) + " " + str(counter) + "\n")
				counter += 1

				if counter % 1000 == 0:
					print(counter)


def create_template_vectors():
	with open("data/template_vector_file.tv", "a") as f:
		f.write("$TYPE template\n" +
				"$XDIM 7\n" +
				"$YDIM 70000\n" +
				"$VECDIM 784\n\n")
		for i in range(784):
			f.write("{} pixel{} 1 1 1 1 1\n".format(i, i + 1))


if __name__ == '__main__':
	create_input_vectors()
	#create_template_vectors()