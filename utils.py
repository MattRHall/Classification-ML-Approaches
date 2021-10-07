import random
def sample_shuffler(large, small, sample_type = "split", shuffle = "True", random_seed = True):
    if random_seed:
        random.seed(10)
    if sample_type == "down":
        large_shrunk = random.sample(large, len(small))
        large, small = large_shrunk, small
    elif sample_type == "up":
        small_expand = small + random.choices(small, k=len(large)-len(small))
        large, small = large, small_expand
    elif sample_type == "split":
        small_expand = small + random.choices(small, k=round(0.5*(len(large)-len(small))))
        large_shrunk = random.sample(large, len(small_expand))
        large, small = large_shrunk, small_expand
    else:
        return ValueError
    return large, small