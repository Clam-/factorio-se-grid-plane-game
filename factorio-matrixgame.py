import sys
import math

class Component:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"

    # Subtracts another (c2) component from this component
    def sub(self, c2):
        return Component(self.x-c2.x, self.y-c2.y, self.z-c2.z)
    # Adds another (c2) component to this component
    def add(self, c2):
        return Component(self.x+c2.x, self.y+c2.y, self.z+c2.z)

    # Convert in to a scalar for normalization
    def scalar(self):
        x2 = self.x*self.x
        y2 = self.y*self.y
        z2 = self.z*self.z
        return math.sqrt(x2+y2+z2)

    # Divide this component using a scalar value
    def div_scalar(self, s):
        return Component(self.x/s, self.y/s, self.z/s)

    # Multiply this component using a scalar value
    def mult_scalar(self, s):
        return Component(self.x*s, self.y*s, self.z*s)

grid_size = float(input("Grid Size: "))
target_x = float(input("Target Cell X: "))
target_y = float(input("Target Cell Y: "))

tl_x = float(input("Top left X: "))
tl_y = float(input("Top left Y: "))
tl_z = float(input("Top left Z: "))
tl = Component(tl_x, tl_y, tl_z)

tr_x = float(input("Top right X: "))
tr_y = float(input("Top right Y: "))
tr_z = float(input("Top right Z: "))
tr = Component(tr_x, tr_y, tr_z)

bl_x = float(input("Bottom left X: "))
bl_y = float(input("Bottom left Y: "))
bl_z = float(input("Bottom left Z: "))
bl = Component(bl_x, bl_y, bl_z)

# Compute desired target position with the specified grid values
cell_size = 1/grid_size
middle_offset = cell_size/2
gx = (target_x*cell_size)-middle_offset
gy = (target_y*cell_size)-middle_offset
gz = 0
g = Component(gx, gy, gz)
print(f"Grid X pos: {gx}")
print(f"Grid Y pos: {gy}")

# Calculate the vector offset from a source to destination point
def calc_offset(source, destination, gridpos):
    v = destination.sub(source)
    vl = v.scalar() # scalar length
    #print(f"vl: {vl}")
    ndv = v.div_scalar(vl) # normalized direction vector
    #print(f"ndv: {ndv}")
    ts = gridpos*vl # scalar to target
    #print(f"st: {ts}")
    return ndv.mult_scalar(ts)

#print("calcing TL->BL")
offset1 = calc_offset(tl, bl, gy)
#print(f"w offset vector: {offset1}")
#print("calcing TL->TR")
offset2 = calc_offset(tl, tr, gx)
#print(f"w offset vector: {offset2}")
offset = offset1.add(offset2)
target = offset.add(tl)
print(f"Target X: {target.x}")
print(f"Target Y: {target.y}")
print(f"Target Z: {target.z}")
