import pickle

parameters_files = ["pyramidal_cells.pickle", "interneurons.pickle", "ca3_generators.pickle", "mec_generators.pickle", "lec_generators.pickle"]
neurons = []

for pfile in parameters_files:
    with open(pfile, mode="br") as file:
        neuron = pickle.load(file)
    neurons.extend(neuron)

print(len(neurons))
with open("neurons.pickle", mode="bw") as file:
    pickle.dump(neurons, file)