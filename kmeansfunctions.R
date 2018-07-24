#function performs ndvi on raster image, then performs kmeans clustering on image, then exports the kmeans as a geotiff.

getwd()

rast_image = "M:\\GS\\Projects\\09001_ISM_P3\\RemoteSensing\\WORKSPACE\\Xenia\\BS567608.tif"

set.seed(25)

ndvikmean <- function(file){
  ###create the ndvi 
  imported_raster = brick(file)
  minmax_image = setMinMax(imported_raster)
  
  band4 = raster(minmax_image, layer=3)
  band5 = raster(minmax_image, layer=4)
  
  NDVI = (band5 - band4)/(band5 + band4)
  NDVI = na.omit(NDVI)
  
  ###perform the kmeans

  nr <- getValues(NDVI)
  str(nr)
  kmncluster =  kmeans(na.omit(nr), centers = 7, iter.max = 100, nstart = 5, algorithm="Lloyd")
  
  knr <- NDVI
  knr[] <- kmncluster$cluster
  
  #export the results
  writeRaster(knr, "knrtest", format = "GTiff")
}


ndvikmean(rast_image)
