import tkinter as tk
from tkinter import messagebox

# Device Classes 

class Device:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

    def get_status(self):
        return f"{self.name}: {self.status}"


class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 22

    def set_temperature(self, temp):
        self.temperature = temp

    def get_status(self):
        return f"{self.name}: {self.status}, Temp: {self.temperature}°C"


class SmartLock:
    def __init__(self):
        self.locked = True

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def get_status(self):
        return f"Door Lock: {'LOCKED' if self.locked else 'UNLOCKED'}"


#GUI Application 

class SmartHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Control Devices")
        self.root.geometry("420x520")

        # Devices
        self.light = Device("Light")
        self.fan = Device("Fan")
        self.ac = SmartAC("AC")
        self.lock = SmartLock()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Control Devices", font=("Arial", 16, "bold")).pack(pady=10)

        # Light
        self.light_label = tk.Label(self.root, text="Light: OFF")
        self.light_label.pack()
        tk.Button(self.root, text="Turn ON", command=self.light_on).pack()
        tk.Button(self.root, text="Turn OFF", command=self.light_off).pack()

        # Fan
        self.fan_label = tk.Label(self.root, text="Fan: OFF")
        self.fan_label.pack(pady=(10, 0))
        tk.Button(self.root, text="Turn ON", command=self.fan_on).pack()
        tk.Button(self.root, text="Turn OFF", command=self.fan_off).pack()

        # AC
        self.ac_label = tk.Label(self.root, text="AC: OFF, Temp: 22°C")
        self.ac_label.pack(pady=(10, 0))
        tk.Button(self.root, text="Turn AC ON", command=self.ac_on).pack()
        tk.Button(self.root, text="Turn AC OFF", command=self.ac_off).pack()

        tk.Label(self.root, text="Set AC Temperature").pack()
        self.temp_entry = tk.Entry(self.root, width=5)
        self.temp_entry.insert(0, "22")
        self.temp_entry.pack()
        tk.Button(self.root, text="Set Temperature", command=self.set_temp).pack()

        # Door Lock
        self.lock_label = tk.Label(self.root, text="Door Lock: LOCKED")
        self.lock_label.pack(pady=(10, 0))
        tk.Button(self.root, text="Lock Door", command=self.lock_door).pack()
        tk.Button(self.root, text="Unlock Door", command=self.unlock_door).pack()

        # Status
        tk.Button(self.root, text="Check Status", command=self.check_status).pack(pady=10)

        self.status_box = tk.Text(self.root, height=6, width=40)
        self.status_box.pack()

    # Button Functions

    def light_on(self):
        self.light.turn_on()
        self.light_label.config(text="Light: ON")

    def light_off(self):
        self.light.turn_off()
        self.light_label.config(text="Light: OFF")

    def fan_on(self):
        self.fan.turn_on()
        self.fan_label.config(text="Fan: ON")

    def fan_off(self):
        self.fan.turn_off()
        self.fan_label.config(text="Fan: OFF")

    def ac_on(self):
        self.ac.turn_on()
        self.ac_label.config(text=f"AC: ON, Temp: {self.ac.temperature}°C")

    def ac_off(self):
        self.ac.turn_off()
        self.ac_label.config(text="AC: OFF")

    def set_temp(self):
        try:
            temp = int(self.temp_entry.get())
            self.ac.set_temperature(temp)
            self.ac_label.config(text=f"AC: {self.ac.status}, Temp: {temp}°C")
        except ValueError:
            messagebox.showerror("Error", "Enter valid temperature")

    def lock_door(self):
        self.lock.lock()
        self.lock_label.config(text="Door Lock: LOCKED")

    def unlock_door(self):
        self.lock.unlock()
        self.lock_label.config(text="Door Lock: UNLOCKED")

    def check_status(self):
        self.status_box.delete(1.0, tk.END)
        self.status_box.insert(tk.END, self.light.get_status() + "\n")
        self.status_box.insert(tk.END, self.fan.get_status() + "\n")
        self.status_box.insert(tk.END, self.ac.get_status() + "\n")
        self.status_box.insert(tk.END, self.lock.get_status())


#Run App 

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()

