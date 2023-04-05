class Example(str):
    def __init__(self, par):
        super().__init__()

    def __len__(self) -> int:
        return 25


a = Example(30)

print(len(a))
