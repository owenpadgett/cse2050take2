class SmartDevice():
    """Base class for smart devices with basic on/off functionality."""
    def __init__(self, name):
        """Initialize a smart device with a name and default status of OFF."""
        self.name = name
        self.status = False

    def turn_on(self):
        """Turn on the smart device."""
        self.status = True
    
    def turn_off(self):
        """Turn off the smart device."""
        self.status = False

    def __str__(self):
        """Return a string representation of the device's status."""
        return f"{self.name}: {'ON' if self.status else 'OFF'}"
    
class Light(SmartDevice):
    """A smart light with adjustable brightness."""
    def __init__(self, name):
        """Initialize a smart light with default brightness of 100."""
        super().__init__(name)
        self.brightness = 100

    def adjust_brightness(self, level):
        """Adjust the brightness level of the light."""
        self.brightness = level

    def __str__(self):
        """Return a string representation of the light's status and brightness."""
        return f"{self.name}: {'ON' if self.status else 'OFF'}, Brightness: {self.brightness}"
    
class Thermostat(SmartDevice):
    """A smart thermostat with adjustable temperature settings."""
    def __init__(self, name):
        """Initialize a smart thermostat with a default temperature of 65°F."""
        super().__init__(name)
        self.temperature = 65

    def adjust_temperature(self, temp):
        """Adjust the temperature within the allowable limits."""
        if self._check_temperature_limits(temp):
            self.temperature = temp

    def _check_temperature_limits(self, temp):
        """Check if the given temperature is within the allowable range (55°F - 80°F)."""
        ubound = 80
        lbound = 55
        if temp >= lbound and temp <= ubound:
            return True
        else:
            return False

    def __str__(self):
        """Return a string representation of the thermostat's status and temperature."""
        return f"{self.name}: {'ON' if self.status else 'OFF'}, Temperature: {self.temperature}"
    
class Speaker(SmartDevice):
    """A smart speaker with volume control."""
    def __init__(self, name):
        """Initialize a smart speaker with a default volume of 3."""
        super().__init__(name)
        self.volume = 3

    def increase_volume(self):
        """Increase the speaker volume by 1, up to a maximum of 10."""
        if self.volume < 10:
            self.volume += 1
    
    def decrease_volume(self):
        """Decrease the speaker volume by 1, down to a minimum of 1."""
        if self.volume > 1:
            self.volume -= 1

    def __str__(self):
        """Return a string representation of the speaker's status and volume."""
        return f"{self.name}: {'ON' if self.status else 'OFF'}, Volume: {self.volume}"
    
class SmartHome():
    """A smart home system that manages multiple smart devices."""
    def __init__(self):
        """Initialize a smart home with an empty list of devices."""
        self.devices = []

    def __add__(self, other):
        """Add a smart device to the home."""
        self.devices.append(other)
        return self.devices
    
    def turn_off_all(self):
        """Turn off all smart devices in the home."""
        for i in self.devices:
            i.status = False

    def __str__(self):
        """Return a string representation of all devices in the home."""
        finalString = ""
        for i in self.devices:
            finalString + f", {i.name}: {'ON' if i.status else 'OFF'}"
        return finalString