import cadquery as cq


shaft_length = 60
shaft_girth = 15
tip_fillet = shaft_girth
ball_radius = 15


# Create a box
def main():
    result = (
        cq.Workplane("XY")
        .cylinder(shaft_length, shaft_girth)
        .faces("+Z")
        .fillet(tip_fillet)
        .transformed(offset=(0, -ball_radius, -shaft_length / 2))
        .sphere(ball_radius)
        .transformed(offset=(0, ball_radius * 2, 0))
        .sphere(ball_radius)
        .transformed(offset=(15, 0, 0))
        .transformed(offset=(0, -15, 0))
        .sphere(ball_radius)
    )
    return result


if __name__ == "__main__":
    r = main()
    # Export the result of this script to an STL file
    cq.exporters.export(r, "out.stl")
