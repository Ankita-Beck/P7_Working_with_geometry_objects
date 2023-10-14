import arcpy
import os

x_charkop = 72.82190281349168
y_charkop = 19.213723099498782

# Point object
pnt_obj = arcpy.Point(x_charkop, y_charkop)

# spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

#  Point geometry
pnt_geom = arcpy.PointGeometry(pnt_obj, spatial_ref)

gdb_path = r"D:\Programming_for_GIS_3\P7_Working_with_geometry_objects\Practical_7_ProProject\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
fc_name = "Mumbai_Charkop"
fc_path = os.path.join(gdb_path, fc_name)

arcpy.CopyFeatures_management(pnt_geom, fc_path)

print("Process Completed")