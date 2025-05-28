class Counter(StateMachine):
    def __init__(self):
        self.value: int = 0

    def apply(self, command: str):
        if command == "INC":
            self.value += 1
        elif command == "RESET":
            self.value = 0
        else:
            raise ValueError(f"Invalid command: {command}")

    def get_value(self):
        return self.value