#!/usr/bin/env python
# coding: utf-8

import gtfstk as gt
import pandas as pd

path = 'gtfs.zip'
feed = gt.read_gtfs(path, dist_units='km')

for agency in feed.agency.agency_id:
    route_ids_for_agency = list(feed.routes[feed.routes['agency_id']==agency]['route_id'])
    little_feed = feed.restrict_to_routes(route_ids=route_ids_for_agency)

    #don't know why, but the transfers have invalid stops :(  so it seems better to remove them
    col_names =  ['from_stop_id', 'to_stop_id', 'transfer_type', 'min_transfer_time']
    little_feed.transfers  = pd.DataFrame(columns = col_names)

    gt.write_gtfs(little_feed, 'output/{}.zip'.format(agency))
