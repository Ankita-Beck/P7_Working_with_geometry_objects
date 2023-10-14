import arcpy
import os

gdb_path = r"D:\Programming_for_GIS_3\P7_Working_with_geometry_objects\Practical_7_ProProject\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
output_fc_name = "Mumbai_to_Lonavala_to_Karjat"
output_fc_path = os.path.join(gdb_path, output_fc_name)


x_mum = 72.83468645728531
y_mum = 18.92219716661799


x_lona = 73.40654304595003
y_lona = 18.75730127064558

x_karjat = 73.32784365774987
y_karjat = 18.910076869254212

pnt_mumbai_obj = arcpy.Point(x_mum, y_mum)
pnt_lonavala_obj = arcpy.Point(x_lona, y_lona)
pnt_karjat_obj = arcpy.Point(x_karjat, y_karjat)

# Spatial Reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

# Array Object
polygon_array = arcpy.Array()

polygon_array.add(pnt_mumbai_obj)
polygon_array.add(pnt_lonavala_obj)
polygon_array.add(pnt_karjat_obj)

polygon_geom =arcpy.Polygon(polygon_array, spatial_ref)

arcpy.CopyFeatures_management(polygon_geom, output_fc_path)
print("Process Completed")