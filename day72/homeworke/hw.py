
def warn_the_sheep(queue):
    wolf_index = queue.index("wolf")

    if queue[-1] == "wolf":
        return 'Pls go away and stope eating my sheep'
    else:
        return "Oi! Sheep number" + str(len(queue) - (wolf_index+1)) + " ! You are about to be eaten"


                                                                                                                        










