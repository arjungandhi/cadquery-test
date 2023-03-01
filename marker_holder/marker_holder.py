import cadquery as cq
import math


marker = {
    "cap": {
        "diameter": {
            "bottom": 15.5,
            "top": 18.0,
        },
        "length": 23.0,
        "tip": {"radius": 4.5, "length": 6},
    },
    "body": {
        "radius": {
            "bottom": 18.0 / 2,
            "top": 17.0 / 2,
        },
        "length": 95.5,
        "tip": {
            "radius": 8.6 / 2,
            "length": 15,
        },
        "marker_bit": {
            "length": 10,
            "radius": 6.8 / 2,
        },
        "bottom": {
            "radius": 4.5,
            "depth": 5,
        },
    },
}


def markerbody():
    marker_taper = math.tan(
        (marker["body"]["radius"]["top"] - marker["body"]["radius"]["bottom"])
        / marker["body"]["length"]
    )
    markerbody = (
        cq.Workplane("XY")
        .circle(marker["body"]["radius"]["bottom"])
        .extrude(marker["body"]["length"], taper=marker_taper)
        .faces(">Z")
        .fillet(marker["body"]["radius"]["top"] - marker["body"]["tip"]["radius"])
        .faces(">Z")
        .workplane()
        .circle(marker["body"]["tip"]["radius"])
        .extrude(marker["body"]["tip"]["length"])
        .faces(">Z")
        .workplane()
        .circle(marker["body"]["marker_bit"]["radius"])
        .extrude(marker["body"]["marker_bit"]["length"])
        .faces("<Z")
        .workplane()
        .hole(marker["body"]["bottom"]["radius"] * 2, marker["body"]["bottom"]["depth"])
    )

    return markerbody


# Create a box
def main():
    return markerbody()


if __name__ == "__main__":
    r = main()
    # Export the result of this script to an STL file
    cq.exporters.export(r, "out.stl")
