#!/usr/bin/env python
import requests
import json
import sys, os
import pandas as pd
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))

YEARS = [ 2013, 2014, 2015 ]
H_2A_VISA_ID = 8

URL = "https://icert.doleta.gov/index.cfm"
BASE_PARAMS = {
    "event": "ehLCJRExternal.doAdvCertSearchCounter",
    "create_date": "undefined",
    "post_end_date": "undefined",
    "visa_class_id": H_2A_VISA_ID
}

def get_count(**kwargs):
    params = dict(BASE_PARAMS)
    params.update(**kwargs)
    res = requests.get(URL, params=params)
    return int(res.content.decode("utf-8").strip())

def get_fy_count(fy, **kwargs):
    params = {
        "start_date_from": "10/01/{0}".format(fy-1),
        "start_date_to": "9/30/{0}".format(fy),
    }
    params.update(kwargs)
    return get_count(**params)

def get_annual_stats(state_id=None):
    counts = pd.DataFrame([{
        "year": year,
        "total": get_fy_count(year, location_state_id=state_id),
        "req_experience": get_fy_count(year, location_state_id=state_id, experience=1),
    } for year in YEARS ])
    counts["prop_req_experience"] = (counts["req_experience"] / counts["total"]).round(3)
    if state_id != None:
        counts["state"] = state_id
    return counts

def get_state_stats():
    state_ids = pd.read_csv(os.path.join(HERE, "../data/oflc-state-ids.csv"))
    df = pd.concat([ get_annual_stats(s_id) for s_id in state_ids["state_id"] ])
    joined = df.set_index("state").join(state_ids.set_index("state_id"))
    return joined

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("aggregation", choices=["overall", "by_state"])
    args = parser.parse_args()
    if args.aggregation == "overall":
        get_annual_stats().set_index("year").to_csv(sys.stdout)
    elif args.aggregation == "by_state":
        get_state_stats().set_index([ "year", "state_name" ]).to_csv(sys.stdout)
        
