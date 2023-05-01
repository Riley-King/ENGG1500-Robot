class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

from typing import Callable, Any

states = {}
state = "None"
env = dotdict({})

def isState(label: str) -> bool:
    return states[label] is None

def registerState(label: str, fn: Callable[[dict, Any], str]) -> (bool, str):
    if isState(label):
        states[label] = fn
        return (True, "")
    else:
        return (False, f"The state \"{label}\" has already been registered")

def clearState(label: str) -> (bool, str):
    if isState(label):
        states[label] = None
        return (True, "")
    else:
        return (False, f"The state \"{label}\" does not exist")
def updateState(*args) -> str:
    global state
    if not isState(state):
        raiseError("No such state exists")
    env.state = state
    state = states[state](args)
    env.state = state

    env.motors.applyDuty()
    return state
def raiseError(msg):
    print(f"Error in <{state}>: ".join(msg))
    return "Error"

def state_Error(env: dict, *args: Any) -> str:
    print("An error has occurred.")
    exit(-2)
def state_None(env: dict, *args: Any) -> str:
    print("Default None state is not valid. Set an initial state before running")
    exit(-1)

registerState("Error", state_Error)
registerState("None", state_None)
