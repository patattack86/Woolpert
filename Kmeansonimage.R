library(raster)
library(rgdal)
library(ggplot2)
library(tiff)
library(maptools)
library(tidyverse)  # data manipulation
library(cluster)    # clustering algorithms
library(factoextra) # clustering algorithms & visualization

getwd()

rast_image = "M:\\GS\\Projects\\09001_ISM_P3\\RemoteSensing\\WORKSPACE\\Xenia\\BS567608.tif"


imported_raster = brick(rast_image)
minmax_image = setMinMax(imported_raster)

colorimage = plotRGB(minmax_image,axes = TRUE, r = 3, g = 2, b = 1, stretch = "lin", main = "Bands321")

colorimage = setMinMax(colorimage)

band4 = raster(minmax_image, layer=3)
band5 = raster(minmax_image, layer=4)

NDVI = (band5 - band4)/(band5 + band4)
NDVI = na.omit(NDVI)

set.seed(25)

nr <- getValues(NDVI)
str(nr)

kmnclusterL =  kmeans(na.omit(nr), centers = 5, iter.max = 500, nstart = 5, algorithm="Lloyd")
kmnclusterH =  kmeans(na.omit(nr), centers = 5, iter.max = 500, nstart = 5, algorithm="Hartigan-Wong")
kmnclusterF =  kmeans(na.omit(nr), centers = 5, iter.max = 500, nstart = 5, algorithm="Forgy")
kmnclusterM =  kmeans(na.omit(nr), centers = 5, iter.max = 500, nstart = 5, algorithm="MacQueen")

knrL <- NDVI
knrH <- NDVI
knrF <- NDVI
knrM <- NDVI

# Now replace raster cell values with kmncluster$cluster array
knrL[] <- kmnclusterL$cluster
knrH[] <- kmnclusterH$cluster
knrF[] <- kmnclusterF$cluster
knrM[] <- kmnclusterM$cluster

mycolor <- c("#fef65b","#ff0000", "#daa520","#0000ff","#0000ff","#00ff00","#cbbeb5",
             "#c3ff5b", "#ff7373", "#00ff00", "#808080")

par(mfrow = c(2,3))
plot(colorimage, main = 'RGB')
plot(NDVI, main = 'Landsat-NDVI')
plot(knrL, main = 'Unsupervised Lloyd')
plot(knrH, main = 'Unsupervised Hartigan-Wong')
plot(knrF, main = 'Unsupervised Forgy')
plot(knrM, main = 'Unsupervised MacQueen')
