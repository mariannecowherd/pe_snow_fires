#!/bin/bash

targetfile='c:/users/marianne/documents/pe_snow_fires/pedata/NCALDAS_NOAH0125_D.A19790103.002.nc4.SUB.tif'
for number in {1979..2016}
do
infile="swe_max_${number}.tif"
outfile="swe_rp_${number}.tif"
echo "Warping ${infile} using the SRS of ${targetfile} to ${outfile}"
projectionfile=$(mktemp /tmp/tif2targetsrs.XXXXXX)
gdalsrsinfo -o wkt "${targetfile}" > "${projectionfile}"
gdalwarp -tr .125 -.125 -t_srs "${projectionfile}" "${infile}" "${outfile}"
rm "${projectionfile}"
done
