import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import django
from datetime import datetime
import threading
import time

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parking_web.settings')
django.setup()

from parking.models import ParkingSpace

class ParkingSimulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking Simulator")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Time label
        self.time_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        self.time_label.pack(anchor="nw", padx=10, pady=10)
        self.update_time()

        # Title
        title = tk.Label(root, text="Parking Simulator", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=20)

        # Buttons frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # Buttons
        self.view_button = tk.Button(button_frame, text="View All Spaces", command=self.view_spaces, font=("Arial", 12), bg="#4CAF50", fg="white", width=15)
        self.view_button.grid(row=0, column=0, padx=10, pady=10)

        self.park_button = tk.Button(button_frame, text="Park Vehicle", command=self.park_vehicle, font=("Arial", 12), bg="#2196F3", fg="white", width=15)
        self.park_button.grid(row=0, column=1, padx=10, pady=10)

        self.remove_button = tk.Button(button_frame, text="Remove Vehicle", command=self.remove_vehicle, font=("Arial", 12), bg="#FF9800", fg="white", width=15)
        self.remove_button.grid(row=0, column=2, padx=10, pady=10)

        self.detail_button = tk.Button(button_frame, text="View Details", command=self.view_details, font=("Arial", 12), bg="#9C27B0", fg="white", width=15)
        self.detail_button.grid(row=1, column=0, padx=10, pady=10)

        self.edit_button = tk.Button(button_frame, text="Edit Space", command=self.edit_space, font=("Arial", 12), bg="#607D8B", fg="white", width=15)
        self.edit_button.grid(row=1, column=1, padx=10, pady=10)

        self.exit_button = tk.Button(button_frame, text="Exit", command=self.root.quit, font=("Arial", 12), bg="#F44336", fg="white", width=15)
        self.exit_button.grid(row=1, column=2, padx=10, pady=10)

        # Text area for output
        self.text_area = tk.Text(root, height=15, width=80, font=("Arial", 10), bg="#ffffff", fg="#333")
        self.text_area.pack(pady=20)

    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)

    def view_spaces(self):
        self.text_area.delete(1.0, tk.END)
        spaces = ParkingSpace.objects.all()
        if not spaces:
            self.text_area.insert(tk.END, "No parking spaces available.\n")
            return
        for space in spaces:
            status = "Occupied" if space.occupancy_status else "Free"
            self.text_area.insert(tk.END, f"Space {space.space_number}: {status}\n")
            if space.vehicle_type:
                self.text_area.insert(tk.END, f"  Vehicle: {space.vehicle_type}\n")
            if space.plate_number:
                self.text_area.insert(tk.END, f"  Plate: {space.plate_number}\n")
            if space.entry_time:
                self.text_area.insert(tk.END, f"  Entry: {space.entry_time}\n")
            if space.exit_time:
                self.text_area.insert(tk.END, f"  Exit: {space.exit_time}\n")
            if space.duration():
                self.text_area.insert(tk.END, f"  Duration: {space.duration()}\n")
            self.text_area.insert(tk.END, "\n")

    def park_vehicle(self):
        space_num = simpledialog.askinteger("Park Vehicle", "Enter space number:")
        if space_num is None:
            return
        try:
            space = ParkingSpace.objects.get(space_number=space_num)
            if space.occupancy_status:
                messagebox.showerror("Error", "Space is already occupied.")
                return
            vehicle_type = simpledialog.askstring("Park Vehicle", "Enter vehicle type:")
            plate_number = simpledialog.askstring("Park Vehicle", "Enter plate number (6 characters, letters and digits only, e.g., 603ZPC):")
            space.vehicle_type = vehicle_type
            space.plate_number = plate_number
            space.occupancy_status = True
            space.entry_time = datetime.now()
            space.save()
            messagebox.showinfo("Success", "Vehicle parked successfully.")
            self.view_spaces()
        except ParkingSpace.DoesNotExist:
            messagebox.showerror("Error", "Space does not exist.")

    def remove_vehicle(self):
        space_num = simpledialog.askinteger("Remove Vehicle", "Enter space number:")
        if space_num is None:
            return
        try:
            space = ParkingSpace.objects.get(space_number=space_num)
            if not space.occupancy_status:
                messagebox.showerror("Error", "Space is already free.")
                return
            space.occupancy_status = False
            space.exit_time = datetime.now()
            duration = space.duration()
            space.save()
            messagebox.showinfo("Success", f"Vehicle removed successfully.\nDuration: {duration}")
            self.view_spaces()
        except ParkingSpace.DoesNotExist:
            messagebox.showerror("Error", "Space does not exist.")

    def view_details(self):
        space_num = simpledialog.askinteger("View Details", "Enter space number:")
        if space_num is None:
            return
        try:
            space = ParkingSpace.objects.get(space_number=space_num)
            details = f"Space {space.space_number}\n"
            details += f"Status: {'Occupied' if space.occupancy_status else 'Free'}\n"
            details += f"Vehicle Type: {space.vehicle_type or 'N/A'}\n"
            details += f"Plate Number: {space.plate_number or 'N/A'}\n"
            details += f"Entry Time: {space.entry_time or 'N/A'}\n"
            details += f"Exit Time: {space.exit_time or 'N/A'}\n"
            if space.duration():
                details += f"Duration: {space.duration()}\n"
            messagebox.showinfo("Space Details", details)
        except ParkingSpace.DoesNotExist:
            messagebox.showerror("Error", "Space does not exist.")

    def edit_space(self):
        space_num = simpledialog.askinteger("Edit Space", "Enter space number:")
        if space_num is None:
            return
        try:
            space = ParkingSpace.objects.get(space_number=space_num)
            # Simple edit: change vehicle type and plate
            vehicle_type = simpledialog.askstring("Edit Space", "Enter new vehicle type:", initialvalue=space.vehicle_type or "")
            plate_number = simpledialog.askstring("Edit Space", "Enter new plate number (6 characters, letters and digits only, e.g., 603ZPC):", initialvalue=space.plate_number or "")
            space.vehicle_type = vehicle_type
            space.plate_number = plate_number
            space.save()
            messagebox.showinfo("Success", "Space updated successfully.")
            self.view_spaces()
        except ParkingSpace.DoesNotExist:
            messagebox.showerror("Error", "Space does not exist.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingSimulatorGUI(root)
    root.mainloop()