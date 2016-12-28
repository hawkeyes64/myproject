import json

with open("geojson_ballarat_publiclighting.json") as f:
    data = json.load(f)
    with open("geojson_ballarat_publiclighting.txt", 'w') as wr:
        wr.write("from big_geo_ballarat.models import feature_geometry, data_geo, data_crs\n")
        for test in data:
            print(test)

        # print data['features']

        for features_data in data['features']:
            # print(str(features_data) + "\n")

            # print ("id: " + features_data['id'])  # Needed
            # print ("\ttype: " + features_data['type'])

            # print("\tcoordinate_type: " + features_data['geometry']['type'])
            # print("\tcoordinate_0: " +
            #      str(features_data['geometry']['coordinates'][0]))
            # print("\tcoordinate_1: " +
            #      str(features_data['geometry']['coordinates'][1]))
            # print("\tcoordinate_02: " +
            #      str(features_data['geometry']['coordinates'][2]))

            # print("\tgeometry_name: " + features_data['geometry_name'])
            # print("\tcentral_as: " + features_data['properties']['central_as'])
            # print("\tsite_name: " + features_data['properties']['site_name'])
            # print("\tfeature_lo: " + str(features_data['properties']['feature_lo']))
            # print("\tfeature_ty: " + features_data['properties']['feature_ty'])
            # print("\tcentroid_e: " + str(features_data['properties']['centroid_e']))
            # print("\tcentroid_n: " + str(features_data['properties']['centroid_n']))

            # print("\n")
            geometry_id = features_data['id']

            geometry_type = features_data['type']
            coordinate_x = str(features_data['geometry']['coordinates'][0])
            coordinate_y = str(features_data['geometry']['coordinates'][1])
            coordinate_z = str(features_data['geometry']['coordinates'][2])

            geometry_name = features_data['geometry_name']
            central_as = features_data['properties']['central_as']
            site_name = str(features_data['properties']['site_name'])
            feature_lo = str(features_data['properties']['feature_lo'])
            feature_ty = features_data['properties']['feature_ty']
            centroid_e = str(features_data['properties']['centroid_e'])
            centroid_n = str(features_data['properties']['centroid_e'])

            wr.write("data = feature_geometry(" +
                     "geometry_id=\"" + geometry_id + "\", " +
                     "coordinate_x=\"" + coordinate_x + "\", " +
                     "coordinate_y=\"" + coordinate_y + "\", " +
                     "coordinate_z=\"" + coordinate_z + "\", " +
                     "geometry_name=\"" + geometry_name + "\", " +
                     "central_as=\"" + central_as + "\", " +
                     "site_name=\"" + site_name + "\", " +
                     "feature_lo=\"" + feature_lo + "\", " +
                     "feature_ty=\"" + feature_ty + "\", " +
                     "centroid_e=\"" + centroid_e + "\", " +
                     "centroid_n=\"" + centroid_n + "\", " +
                     "feature_data_geo=data_geo.objects.get(geo_data_label=\"Ballarat Car Parking Areas\")" + ", " +
                     "feature_data_crs=data_crs.objects.get(crs_properties_name=\"urn:ogc:def:crs:EPSG::28354\")" +
                     ")\n")
            wr.write("data.save()\n")
        wr.close()
    f.close()
