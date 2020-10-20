def bottle_of_beer(bob):
    """prints 99 bottles of beer on the wall lyrics.
    :param bob: Must be a positive int."""
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall.  {} bottles of beer. Take one down, pass it around, {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottle_of_beer(bob)

bottle_of_beer(99)