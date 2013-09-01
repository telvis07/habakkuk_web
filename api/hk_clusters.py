import jsonlib2 as json
import traceback
import logging

from api.models import KmeansCluster

def clusters(dt):
    clusters = KmeansCluster.objects.filter(date=dt)
    if len(clusters):
        return parse_cluster(clusters[0])
    else:
        return {}

def parse_cluster(cluster):
    try:
        return json.loads(cluster.data)
        # TODO: read from real mahout data
    except Exception, ex:
        print ex
        return {}
