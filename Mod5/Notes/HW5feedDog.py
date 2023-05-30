def feedDog(hunger_level, biscuit_size):
     happyDogs = 0
     biscuit_size = sorted(biscuit_size)
     hunger_level = sorted(hunger_level)
     for hunger in hunger_level:
        if not biscuit_size:
            break
        for i, size in enumerate(biscuit_size):
            if size >= hunger:
                del biscuit_size[i]
                happyDogs += 1
                break
            return happyDogs
print(feedDog([1, 2, 3], [1, 1]))
print(feedDog([2, 1], [1, 3, 2]))
print(feedDog([1, 2, 3], [3, 2, 1]))