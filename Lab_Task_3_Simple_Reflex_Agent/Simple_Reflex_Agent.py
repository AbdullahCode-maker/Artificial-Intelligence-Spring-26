# Model-Based Reflex Agent class
class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.last_action = None
    def perceive(self, current_temperature):
        return current_temperature
    def act(self, current_temperature):
        if current_temperature < self.desired_temperature:
            if self.last_action != "ON":
                action = "Turn ON heater"
            else:
                action = "Do nothing (already ON)"
        else:
            if self.last_action != "OFF":
                action = "Turn OFF heater"  
            else:
                action = "Do nothing (already OFF)"
        self.last_action = "ON" if "ON" in action else "OFF"
        return action
agent = ModelBasedReflexAgent(22)
temps = [20, 21, 22, 21, 23]
for t in temps:
    print("Temp:", t, "→", agent.act(t))