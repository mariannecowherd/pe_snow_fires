library('raster')
library("sp","rgdal")
dir = 'c:/users/marianne/documents'
smallgrid <- raster(paste(dir, 'GOSIF_native_res_monthly_means_small.gri',sep='/'))
smallstack <- stack(paste(dir,'GOSIF_native_res_monthly_means_small.gri',sep='/'))


plot(smallstack, 
     zlim = c(0, 65000), 
     nc = 4)

sn <- readOGR('data/sn_watersheds.shp')

# Plot it
library(ggplot2)
ggplot() +
  geom_polygon(data = sn, aes( x = long, y = lat, group = group), fill="#69b3a2", color="black") +
  theme_void() 


writeRaster(smallstack, "smallstack.nc", overwrite=TRUE, format="CDF",     varname="GPP", varunit="C", 
        longname="GPP raster to nc", xname="Longitude",   yname="Latitude", zname="month")
