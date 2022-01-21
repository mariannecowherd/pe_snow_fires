## file to define values and folders
import geopandas as gpd
import matplotlib
import numpy as np
import os

def normalize(data):
    avg = np.nanmean(data)
    out = (data-avg)/avg
    return out
    
path = os.path.expanduser('~')


home_dir=path + '/documents/pe_snow_fires/'

pe_data_dir = path + '/documents/pe_snow_fires/data/'
sn_watersheds= gpd.read_file(pe_data_dir + 'sn_watersheds.shp')
data_dir = path + '/documents/data/'
mtbs= gpd.read_file(data_dir + 'mtbs_perimeter_data/mtbs_perims_DD.shp')
fire_sn = gpd.read_file(pe_data_dir + 'firebounds_sn.gdf')

blues = matplotlib.cm.get_cmap('Blues', 256)
newcolors = blues(np.linspace(0, 1.5, 256))
pink = np.array([248/256, 24/256, 148/256, 1])
white = np.array([1,1,1,0])
newcolors[:10, :] = white
newcmp = matplotlib.colors.ListedColormap(newcolors)
 
kwargs = {"cmap": newcmp, "vmax": 1}


names = ['Sacramento',
            'Feather',
            'Yuba',
            'American',
            'Cosumnes',
            'Mokelumne',
            'Stanislaus',
            'Tuolumne',
            'Merced',
            'San Joaquin',
            'King',
            'Kaweah',
            'Tule',
            'Kern',
            'Owens',
            'Mono',
            'Walker',
            'Carson',
            'Tahoe',
            'Truckee']

northwest = ['upper_sacramento','feather','yuba','american','cosumnes','mokelumne','stanislaus']
southwest = ['tuolumne','merced','san_joaquin','kings','kaweah','tule','kern']
southeast = ['owens','mono','walker']
northeast = ['truckee','tahoe','carson']
all_watersheds = sorted(northwest+northeast+southeast+southwest)

mean_april_gpp= [951.4664443518133,
 704.1253620190319,
 768.3370554177005,
 630.0247933884298,
 909.1195202646816,
 548.3355426677713,
 612.8457402812242,
 845.3971074380165,
 650.9219008264463,
 713.7125154894671,
 532.1344642118329,
 533.9119470855726,
 759.480380008261,
 946.9206939281289,
 864.4333470903838,
 916.4643004539827]
mean_july_gpp = [1315.0396203054065,
 1123.918283120099,
 900.3528683450269,
 793.3012794056954,
 1151.3318200577796,
 993.3351217498969,
 913.4036318613289,
 968.1386710689228,
 879.1820057779612,
 839.4601733388362,
 1081.4255055716055,
 1302.7263722657863,
 1088.8832026413536,
 814.151465125877,
 783.3702022286421,
 1071.7919933966157]
mean_august_gpp = [972.8349153941394,
 924.1403219149814,
 850.6512587701197,
 1064.243912505159,
 1022.331407346265,
 948.098225340487,
 1058.8918695831615,
 871.2711514651259,
 767.4015683037557,
 916.7560874948412,
 990.9186958316137,
 1090.6776723070573,
 737.9711101939744,
 954.0416838629798,
 934.5476681799422,
 844.9083780437475]
years_gpp = range(2000,2016)
