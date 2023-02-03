import cadquery as cq


# Create a box
def main():
    result = cq.Workplane("XY").box(1, 2, 3)
    return result


if __name__ == "__main__":
    r = main()
    # Export the result of this script to an STL file
    cq.exporters.export(r, "out.stl")
