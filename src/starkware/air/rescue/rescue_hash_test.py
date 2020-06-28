from .rescue_hash import rescue_hash


def test_rescue_hash():
    # The list of constants being compared to the result of rescue_hash was generated by performing
    # the hash on [1, 2, 3, 4, 5, 6, 7, 8] with the marvellous_hash function given in
    # https://starkware.co/hash-challenge-implementation-reference-code/#marvellous.
    assert rescue_hash([1, 2, 3, 4, 5, 6, 7, 8]) == \
        [1701009513277077950, 394821372906024995,
         428352609193758013, 1822402221604548281]
