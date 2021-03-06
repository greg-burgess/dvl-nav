BathyData = {


    ##################################################
    # Kolumbo Data Subset
    ##################################################
    'Kolumbo' : {
        # 'filepath'  : "/Users/zduguid/Dropbox (MIT)/MIT-WHOI/Kolumbo cruise 2019/Grids/kolumbo bathymetry.tif",
        'filepath'  : "C:/Users/grego/Dropbox/Kolumbo cruise 2019/zduguid/bathy/Kolumbo-10m.tif",
        'latlon_format' : True,
        'crop'  : [700, 1501, 700, 1300],
        # 'crop'  : [0, 2000, 0, 2000],
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'Kolumbo Volcano, Greece',
        'xlabel': 'Longitude [deg]',
        'ylabel': 'Latitude [deg]',
        'tick_format' : '%.2f',
        'num_ticks' : 3,
        'slope_max' : 50,
        'depth_max' : None,
        'depth_filter' : None,
    },


    ##################################################
    # Kolumbo Data Full
    ##################################################
    'Kolumbo_full' : {
        'filepath'  : "C:/Users/grego/Dropbox/Kolumbo cruise 2019/zduguid/bathy/Kolumbo-10m.tif",
        'latlon_format' : False,
        'crop'  : None,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'Kolumbo Volcano, Greece',
        'xlabel': 'Longitude [deg]',
        'ylabel': 'Latitude [deg]',
        'tick_format' : '%.3f',
        'num_ticks' : 3,
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : None,
    },


    ##################################################
    # Kolumbo Data Full
    ##################################################
    'Kolumbo_full_AR' : {
        'filepath'  : "C:/Users/grego/Dropbox/Kolumbo cruise 2019/zduguid/bathy/Kolumbo-10m.tif",
        'latlon_format'    : True,
        'crop'  : None,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'Kolumbo Volcano, Greece',
        'xlabel': 'Longitude [deg]',
        'ylabel': 'Latitude [deg]',
        'tick_format' : '%.3f',
        'num_ticks' : 3,
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : None,
    },


    ##################################################
    # Santorini Data Full
    ##################################################
    'Santorini_full' : {
        'filepath'  : "C:/Users/grego/Dropbox/Kolumbo cruise 2019/zduguid/bathy/Christiana-Santorini-Kolumbo.tif",
        'latlon_format'    : True,
        'crop'  : None,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'Kolumbo Volcano, Greece',
        'xlabel': 'Longitude [deg]',
        'ylabel': 'Latitude [deg]',
        'tick_format' : '%.3f',
        'num_ticks' : 3,
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : None,
    },


    ##################################################
    # Buzzards Bay Data
    ##################################################
    'BuzzardsBay' : {
        'filepath'  : "C:/Users/grego/Dropbox/NSF Arctic NNA/Environment-Data/BuzzardsBay-10m/BuzzBay_10m.tif",
        'latlon_format'    : False,
        'crop'  : [1500, 5740, 1500, 6200],
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'Buzzards Bay, MA',
        'xlabel': 'UTM Zone 19',
        'ylabel': '',
        'tick_format' : '%.2g',
        'slope_max' : 8,
        'depth_max' : 35,
        'depth_filter' : None,
        'num_ticks' : 3,
        'meta'  : {
            'utm_zone' : 19,
            'coordinate_system' : 'North American Datum of 1983 and the North American Vertical Datum of 1988',
            'link' : 'https://www.sciencebase.gov/catalog/item/5a4649b8e4b0d05ee8c05486'
        }
    },


    ##################################################
    # Costa Rica Data Area1
    ##################################################
    'CostaRica_area1' : {
        'filepath'  : "/Users/zduguid/Dropbox (MIT)/MIT-WHOI/18-Falkor Costa Rica/Bathy for Sentinel survey/Bathy_for_last_Sentinel_missions.tif",
        'latlon_format'    : False,
        'crop'  : None,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'Continental Margin, Costa Rica',
        'xlabel': 'UTM Zone 16',
        'ylabel': '',
        'tick_format' : '%.4g',
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : None,
        'num_ticks' : 3,
        'meta'  : {
            'utm_zone' : '16N',
        }
    },


    ##################################################
    # Costa Rica Data Area3 
    ##################################################
    'CostaRica_area3' : {
        'filepath'  : "/Users/zduguid/Documents/MIT-WHOI/MERS/Cook/cook/bathymetry/jaco-scar-depths.tif",
        'latlon_format'    : False,
        'crop'  : [75, 550, 600, 1200],
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'Jaco Scar, Costa Rica',
        'xlabel': 'UTM Zone 16',
        'ylabel': '',
        'tick_format' : '%.4g',
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : 1000,
        'num_ticks' : 3,
        'meta'  : {
            'utm_zone' : '16N',
        }
    },


    ##################################################
    # Costa Rica Data Full
    ##################################################
    'CostaRica_full' : {
        # 'filepath'  : "/Users/zduguid/Documents/MIT-WHOI/MERS/Cook/cook/bathymetry/jaco-scar-depths.tif",
        'filepath'  : "/Users/zduguid/Dropbox (MIT)/MIT-WHOI/18-Falkor Costa Rica/zduguid/three-factor-bathymetry/CostaRica Falkor.tif",
        'latlon_format'    : False,
        'crop'  : False,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'Falkor Dec 2018 Cruise, Costa Rica',
        'xlabel': 'UTM Zone 16',
        'ylabel': '',
        'tick_format' : '%.4g',
        'slope_max' : False,
        'depth_max' : False,
        'depth_filter' : None,
        'num_ticks' : 3,
        'nodata' : 0.0,
        'meta'  : {
            'utm_zone' : '16N',
        }
    },


    ##################################################
    # Hawaii Data Small
    ##################################################
    'Hawaii_small' : {
        'filepath'  : "/Users/zduguid/Documents/MIT-WHOI/MERS/Cook/cook/bathymetry/HI-small.tif",
        'latlon_format'    : True,
        'crop'  : None,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : "'Au'au Channel, Hawaii",
        'xlabel': 'Lon [deg]',
        'ylabel': 'Lat [deg]',
        'tick_format' : '%.4g',
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : None,
        'num_ticks' : 3,
        'nodata' : None,
        'meta'  : {
            'utm_zone' : '16N',
        }
    },


    ##################################################
    # Hawaii Data Small
    ##################################################
    'Hawaii_all' : {
        'filepath'  : "/Users/zduguid/Documents/MIT-WHOI/MERS/Cook/cook/bathymetry/HI-all.tif",
        'latlon_format'    : True,
        'crop'  : None,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : "'Au'au Channel, Hawaii",
        'xlabel': 'Lon [deg]',
        'ylabel': 'Lat [deg]',
        'tick_format' : '%.4g',
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : None,        
        'num_ticks' : 3,
        'nodata' : None,
        'meta'  : {
            'utm_zone' : '16N',
        }
    },


    ##################################################
    # Arctic 400m 
    ##################################################
    'Arctic' : {
        'filepath'  : "/Users/zduguid/Dropbox (MIT)/MIT-WHOI/NSF Arctic NNA/Environment-Data/Arctic-400m/IBCAO_v4_400m.tif",
        'latlon_format'    : False,
        'crop'  : None,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'TODO',
        'xlabel': 'TODO',
        'ylabel': 'TODO',
        'tick_format' : '%.2g',
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : None,
        'num_ticks' : 3,
        'meta'  : None,
    },


    ##################################################
    # Template Data 
    ##################################################
    'template' : {
        'filepath'  : "path/to/file.tif",
        'latlon_format'    : False,
        'crop'  : None,
            # crop  = [top, bot, left, right]
            # bathy = bathy_im[top:bot, left:right]
        'name' : 'TODO',
        'xlabel': 'TODO',
        'ylabel': 'TODO',
        'tick_format' : '%.2g',
        'slope_max' : None,
        'depth_max' : None,
        'depth_filter' : None,
        'num_ticks' : 3,
        'meta'  : None,
    },
    
}