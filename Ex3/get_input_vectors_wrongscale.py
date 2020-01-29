def create_input_vectors():
	out = ""
	counter = 0
	skip_first = True
	with open("data/mnist_784_sampled{}_wrongscale.csv".format(num_vectors), "r") as f_csv:
		with open("data/input_vector_file_sampled{}_wrongscale.in".format(num_vectors), "a") as f_vec:
			with open("data/classes_sampled{}.cls".format(num_vectors), "a") as f_cls:
				f_cls.write("$NUM_CLASSES 10\n" +
							"$CLASS_NAMES 0 1 2 3 4 5 6 7 8 9\n" +
							"$XDIM 2\n" +
							"$YDIM {}\n".format(num_vectors))

				f_vec.write("$TYPE inputvec\n" + \
							"$XDIM {}\n".format(num_vectors) + \
							"$YDIM 1\n" + \
							"$VEC_DIM 784\n")
				for line in f_csv:
					if skip_first:
						skip_first = False
						continue

					splited = line.split(",")
					label = int(splited[-1])
					splited = splited[:-1]
					f_vec.write(" ".join(splited) + " " + str(counter) + "\n")
					f_cls.write(str(counter) + " " + str(label) + "\n")
					counter += 1

					if counter % 1000 == 0:
						print(counter)


def create_template_vectors():
	with open("data/template_vector_file_sampled{}.tv".format(num_vectors), "a") as f:
		f.write("$TYPE template\n" +
				"$XDIM 7\n" +
				"$YDIM {}\n".format(num_vectors) +
				"$VECDIM 784\n")
		for i in range(784):
			f.write("{} pixel{} 1 1 1 1 1\n".format(i, i + 1))


if __name__ == '__main__':
	num_vectors = 1000
	create_input_vectors()
	create_template_vectors()