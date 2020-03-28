"""Tools for working with data from the Ocean Observatories Initiative data portal """

import requests
import re
import os
import time

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

def make_data_request(data_request_url,params,API_USERNAME,API_TOKEN):
    """Function for making data request"""

    # Makes data request to OOI server
    r = requests.get(data_request_url, params=params, auth=(API_USERNAME, API_TOKEN))
    data = r.json()

    # Checks each second to see if complete,
    try:
        check_complete = data['allURLs'][1] + '/status.json'
    except KeyError:
        print('No data found in specified date range')
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

def list_thredds_datasets(catalog_url,pattern_str='',append_str='',tds_url=None):
    """Return a list of NetCDF datasets from an OOI THREDDS catalog.

    catalog_url - string containing full url for the catalog, ending with /catalog.html
    pattern_str - string containing a pattern that must be in the dataset name (default '')
    append_str - string that will be appended to the end of each filename (default '')
    tds_url - the base OpenDAP url for the datasets
              (default: https://opendap.oceanobservatories.org/thredds/dodsC)
    """

    # set default tds_url if none provided
    if tds_url is None:
        tds_url = 'https://opendap.oceanobservatories.org/thredds/dodsC'

    # parse datasets in catalog
    datasets = requests.get(catalog_url).text
    urls = re.findall(r'href=[\'"]?([^\'" >]+)', datasets)
    x = re.findall(r'(ooi/.*?'+pattern_str+'.*?.nc)', datasets)
    for i in x:
        if i.endswith('.nc') == False:
            x.remove(i)
    for i in x:
        try:
            float(i[-4])
        except:
            x.remove(i)

    # create list of datasets
    dataset_list = [os.path.join(tds_url, i)+append_str for i in x]
    return dataset_list
