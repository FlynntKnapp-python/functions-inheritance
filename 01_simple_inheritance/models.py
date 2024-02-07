class Container(object):
    """
    A simple container class.
    """

    def __init__(self, desc, volume):
        self.desc = desc
        self.volume = volume

    def __str__(self):
        return f"{self.desc} with volume of {self.volume}."
