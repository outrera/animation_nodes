import bpy
from ... base_types import AnimationNode

class VectorAngleNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_VectorAngleNode"
    bl_label = "Vector Angle"

    def create(self):
        self.newInput("Vector", "A", "a", value = [1, 0, 0])
        self.newInput("Vector", "B", "b", value = [0, 0, 1])
        self.newOutput("Float", "Angle", "angle")
        self.newOutput("Quaternion", "Rotation Difference", "rotationDifference")

    def getExecutionCode(self, required):
        if "angle" in required:
            yield "angle = a.angle(b, 0.0)"
        if "rotationDifference" in required:
            yield "rotationDifference = a.rotation_difference(b)"