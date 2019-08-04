#!/usr/bin/env python
# coding: utf-8

import gtfstk as gt

path = 'gtfs.zip'
feed = gt.read_gtfs(path, dist_units='km')

for agency in feed.agency.agency_id:
    route_ids_for_agency = list(feed.routes[feed.routes['agency_id']==agency]['route_id'])
    little_feed = feed.restrict_to_routes(route_ids=route_ids_for_agency)
    gt.write_gtfs(little_feed, 'output/{}.zip'.format(agency))
