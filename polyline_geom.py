import arcpy
import os

gdb_path = r"D:\Programming_for_GIS_3\P7_Working_with_geometry_objects\Practical_7_ProProject\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
output_fc_name = "Mumbai_to_Lonavala"
output_fc_path = os.path.join(gdb_path, output_fc_name)


x_mum = 72.83468645728531
y_mum = 18.92219716661799


x_lona = 73.40654304595003
y_lona = 18.75730127064558

pnt_mumbai_obj = arcpy.Point(x_mum, y_mum)
pnt_lonavala_obj = arcpy.Point(x_lona, y_lona)

# Spatial Reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

# Array Object
polyline_array = arcpy.Array()

polyline_array.add(pnt_mumbai_obj)
polyline_array.add(pnt_lonavala_obj)

polyline_geom =arcpy.Polyline(polyline_array, spatial_ref)

arcpy.CopyFeatures_management(polyline_geom, output_fc_path)
print("Process Completed")