import network
import mnist_loader
import matplotlib.pyplot as plt


training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network.Network([784, 30, 10])

net.SGD(training_data, 2, 5, 3.0, test_data=test_data)

net.write_parameters("pysource1.txt")

net_2 = network.Network([784, 30, 10], "pysource1.txt")

# # print(net_2.weights)
# # print(net_2.biases)

# training_data = list(training_data)
# # It's supposed to be a 4. 
# a = training_data[1][0]


# result = net_2.feedforward(a)
# bar_stuff = list()
# for output in result:
#     bar_stuff.append(output[0])


# fig = plt.figure(figsize=(10, 5))
# plt.bar([0, 1, 2, 3, 4, 5, 6, 
#          7, 8, 9], bar_stuff)
# plt.show()
