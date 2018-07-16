library(raster)
library(rgdal)
library(ggplot2)
library(tiff)
library(maptools)

getwd()

rast_image = "E:\\Image\\trainingfolder\\ls_d2_fil_flr1.tif"
vector_layer = "E:\\final_merge.shp"

imported_raster = brick(rast_image)
imported_vector = readShapePoly(vector_layer)
  
print(imported_raster)
print(imported_vector)

crs(imported_vector) <- "+proj=lcc +lat_1=34.93333333333333 +lat_2=36.23333333333333 +lat_0=34.33333333333334 +lon_0=-92 +x_0=399999.9999999999 +y_0=0 +ellps=GRS80 +units=us-ft +no_defs "

clipped_raster = mask(imported_raster, imported_vector)

plot(clipped_raster)

final_raster <- writeRaster(clipped_raster, 'R_is_the_best_language.tif', overwrite=TRUE)

print(final_raster)
