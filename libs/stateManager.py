class StateManager:
    def __init__(self, state: str ="None"):
        self.states: dict = {}
        self.env = {}
        self.state: str = state
        self.env["state"] = self.state

        def state_None(env: dict, *args):
            print("State became none")
            exit(-1)
        def state_Error(env: dict, *args):
            print(f"A state error occurred")
            if env.err is not None: print(env.err)
            exit(-2)

        self.registerState("None", state_None)
        self.registerState("Error", state_Error)

    def isState(self, label: str) -> bool:
        return label in self.states

    def registerState(self, label: str, fn) -> None:
        if not self.isState(label):
            self.states[label] = fn
        else:
            raise RuntimeError(f"State \"{self.state}\" already registered")

    def removeState(self, label: str) -> None:
        if self.isState(label):
            self.states[label] = None
        else:
            raise RuntimeError(f"State \"{self.state}\" does not exist")

    def updateState(self, *args):
        if self.isState(self.state):
            self.env["state"] = self.state
            self.state = self.states[self.state](self.env, args)
            self.env["state"] = self.state
            self.env["motors"].applyDuty()
        else:
            raise RuntimeError(f"State \"{self.state}\" does not exist")
