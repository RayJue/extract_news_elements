import numpy as np

def cosine_similarity(vec1, vec2):
        tx = np.array(vec1)
        ty = np.array(vec2)
        cos1 = np.sum(tx * ty)
        cos21 = np.sqrt(sum(tx ** 2))
        # print(ty)
        cos22 = np.sqrt(sum(ty ** 2))
        cosine_value = cos1 / float(cos21 * cos22)
        return cosine_value