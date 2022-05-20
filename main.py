class Switch:
    def __init__(self, value):
        self.value = value

    def __call__(self, *works):
        for work in works:
            if work["value"] == self.value:
                exec(work["work"])
            if work["flag"] == "b":
                break


def switch(var):
    return Switch(value=var)


class Case:
    def __init__(self, value):
        self.value = value

    def __call__(self, work, f=None):
        return {"value": self.value, "work": work, "flag": f}


name = "Ivan"

switch(name)(
    Case("Ivan")("print(1)\n"),
    Case("Ivan")("print(2)\n", 'b')
)
