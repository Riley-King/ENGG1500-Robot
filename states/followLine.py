import time
from libs.US import dist_mm
import libs.stateManager as sm

def state_followLine(env: dict, *args: any) -> str:

    # Do magic here...

    return "updateGraphics"

sm.registerState("followLine", state_followLine)
