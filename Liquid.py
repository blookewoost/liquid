import _ClassDefs
import tkinter as tk

class EntryField:


    def __init__(self, _name, _entry):
        self.name = _name
        self.entry = _entry

ThroatRadius = EntryField('Throat Radius', 0)
TargetAltitude = EntryField('Target Altitude', 0)
ContractionRatio = EntryField('Contraction Ratio', 0)
Alpha = EntryField('Alpha', 0)
Beta = EntryField('Beta', 0)
ChamberRatio = EntryField('Chamber Ratio', 0)
ThroatCountour = EntryField('Throat Contour', 0)

## OPTIONS FOR USER TO SELECT AND GIVE INPUT

fuel_opts = ['Ethanol']
oxidizer_opts = ['NO2']

fields = [ThroatRadius, TargetAltitude, ContractionRatio, Alpha, Beta, ChamberRatio, ThroatCountour]
################################################################

## CREATING SELECTION WINDOW ###################################

root = tk.Tk()
i = 0
for field in fields:
    field.entry = tk.DoubleVar()
    tk.Label(root, text=field.name).grid(row=i, column=0)
    tk.Entry(root, textvariable=field.entry).grid(row=i, column=1)
    i = i + 1

def generate():
    for field in fields:
        field.entry = float(field.entry.get())
    root.destroy()

button = tk.Button(root, text="Done", command=generate)
button.grid(row=7, column=1)
root.mainloop()

for field in fields:
    print(field.entry)

# _fuel, _oxidizer, _throatradius, _targetalt, _contractionratio, _alpha, _beta, _chamberratio, _throatcontour):
# newThrustChamber = _ClassDefs.ThrustChamber('Ethanol', 'NO2', '0.5', '10000', '4', '15', '40', '4', '1')


