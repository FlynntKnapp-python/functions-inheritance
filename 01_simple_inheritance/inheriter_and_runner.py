from models import Container


simple_bottle = Container("Bottle", 20)
print(simple_bottle)

simple_can = Container("Can", 12)
print(simple_can)


class ContainerWithLabel(Container):
    """
    A simple container with a label.
    """

    def __init__(self, desc, volume, label):
        super().__init__(desc, volume)
        self.label = label

    def __str__(self):
        return f"{self.desc} with volume of {self.volume} and a label of {self.label}."


container_with_label = ContainerWithLabel("Can", 12, "Kaja Kola!")
print(container_with_label)


class PaintedContainerWithLabel(ContainerWithLabel):
    """
    A simple container with a label and paint.
    """

    def __init__(self, desc, volume, label, paint_color):
        super().__init__(desc, volume, label)
        self.paint_color = paint_color

    def __str__(self):
        return f"{self.desc} with volume of {self.volume}, a label of {self.label}, and painted {self.paint_color}."


painted_container_with_label = PaintedContainerWithLabel(
    "Can", 12, "Kaja Kola!", "Chartreuse"
)
print(painted_container_with_label)
