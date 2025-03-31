import numpy as np
from tkinter import *
import customtkinter as ct
from stl import mesh

def set_up():
    ct.set_appearance_mode("dark") # Modes: system, light, dark
    root = ct.CTk()
    root.title('ACME Solutions | Bid Generation') # Title card
    root.geometry('1200x1200')

def calculate_volume(stl_file):
    # Load the STL file
    your_mesh = mesh.Mesh.from_file(stl_file)

    # Calculate the volume
    volume = 0.0
    for i in range(len(your_mesh.vectors)):
        v0, v1, v2 = your_mesh.vectors[i]
        volume += np.abs(np.dot(v0, np.cross(v1, v2))) / 6.0

    return volume  # Volume in cubic mm


def calculate_cost(stl_file, cost_per_cm3):
    volume_mm3 = calculate_volume(stl_file)

    # Convert volume from cubic mm to cubic cm
    volume_cm3 = volume_mm3 / 1000.0

    # Calculate cost
    total_cost = volume_cm3 * cost_per_cm3
    return total_cost, volume_cm3


if __name__ == "__main__":
    set_up()
    stl_file = input("Enter the path to the STL file: ")
    cost_per_cm3 = float(input("Enter the material cost per cubic cm: "))
    total_cost, volume = calculate_cost(stl_file, cost_per_cm3)

    print(f"Estimated Material Volume: {volume:.2f} cm³")
    print(f"Total Material Cost: ${total_cost:.2f}")
