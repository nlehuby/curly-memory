#!/usr/bin/env python
# coding: utf-8

import gtfstk as gt

path = 'gtfs.zip'
feed = gt.read_gtfs(path, dist_units='km')
route_ids_for_agency = list(feed.routes[feed.routes['agency_id']=="372"]['route_id'])
little_feed = feed.restrict_to_routes(route_ids=route_ids_for_agency)
gt.write_gtfs(little_feed, '372.zip')
