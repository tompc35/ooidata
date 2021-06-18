"""Tools for working with data from the Ocean Observatories Initiative data portal """

import requests
import re
import os
import time
import fnmatch

def make_url(site,node,instrument,method,stream,API_USERNAME,API_TOKEN):
    """Function for generating meta and data request urls"""

    SENSOR_BASE_URL = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/'
    VOCAB_BASE_URL = 'https://ooinet.oceanobservatories.org/api/m2m/12586/vocab/inv'
    meta_request_url ='/'.join((VOCAB_BASE_URL,site,node,instrument)) # Python wizard best
    data_request_url ='/'.join((SENSOR_BASE_URL,site,node,instrument,method,stream))

    # Retrieve vocabulary information for a given instrument
    r = requests.get(meta_request_url, auth=(API_USERNAME, API_TOKEN))
    meta_data = r.json()

    return (data_request_url,meta_data)

def make_data_request(data_request_url,params,API_USERNAME,API_TOKEN,check_status=True):
    """Function for making data request"""

    # Makes data request to OOI server
    r = requests.get(data_request_url, params=params, auth=(API_USERNAME, API_TOKEN))
    data = r.json()

    try:
        check_complete = data['allURLs'][1] + '/status.json'
    except KeyError:
        raise Exception('No data found in specified date range')

    # Checks each second to see if complete
    if check_status==True:
        for i in range(1000):
            r = requests.get(check_complete)
            if r.status_code == requests.codes.ok:
                print('request completed')
                break
            else:
                time.sleep(1)

    # Grab urls
    url_thredds = data['allURLs'][0]
    url_netcdf = data['allURLs'][1]

    return (url_thredds, url_netcdf, data)

def list_opendap_urls(catalog_url,pattern_str='',append_str=''):
    """Return a list of OpenDAP urls from an OOI THREDDS catalog.

    catalog_url - string containing full url for the catalog, ending with catalog.html or catalog.xml
    pattern_str - string containing a pattern that must be in the dataset name (default '*.nc')
                  (uses Unix shell-style wildcards)
    append_str - string that will be appended to the end of each filename
                (example: '#fillmismatch', which is usually needed for OOI data)

    Similar inputs and functionality as older obsolete function list_thredds_datasets
    Requires siphon package: https://unidata.github.io/siphon/latest/
    """

    from siphon.catalog import TDSCatalog

    catalog = TDSCatalog(catalog_url)
    dataset_subset = fnmatch.filter(catalog.datasets,pattern_str)

    opendap_url_list = []
    for dataset_name in sorted(dataset_subset):
        opendap_url = catalog.datasets[dataset_name].access_urls['OPENDAP']
        opendap_url_list.append(opendap_url+append_str)

    return opendap_url_list

if __name__ == '__main__':
    print('testing list_opendap_urls')
    catalog_url = 'http://thredds.dataexplorer.oceanobservatories.org/thredds/catalog/ooigoldcopy/public/CE02SHSM-RID26-01-ADCPTA000-recovered_inst-adcp_velocity_earth/catalog.html'
    pattern_str = 'deployment0009*ADCP*20190904*.nc'
    append_str = '#fillmismatch'

    opendap_url_list = list_opendap_urls(catalog_url,pattern_str,append_str)
    print(opendap_url_list)
