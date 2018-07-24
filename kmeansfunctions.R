getwd()

rast_image = "M:\\GS\\Projects\\09001_ISM_P3\\RemoteSensing\\WORKSPACE\\Xenia\\BS567608.tif"

ndvifun <- function(file){
  imported_raster = brick(file)
  minmax_image = setMinMax(imported_raster)
  
  band4 = raster(minmax_image, layer=3)
  band5 = raster(minmax_image, layer=4)
  
  NDVI = (band5 - band4)/(band5 + band4)
  NDVI = na.omit(NDVI)
}

kmeansfun <- function(file){
  nr <- getValues(file)
  set.seed(25)
  kmncluster =  kmeans(na.omit(nr), centers = 5, iter.max = 100, nstart = 5, algorithm="Lloyd")
  
  knr <- NDVI
  knr[] <- kmncluster$cluster
}
