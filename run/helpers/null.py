class NullType:
    """Type acting like None but not None.
    """

    # Public

    def __bool__(self):
        return False

    def __repr__(self):
        return 'Null'


Null = NullType()
