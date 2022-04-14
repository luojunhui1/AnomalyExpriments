from BaseSVDD import *
from numpy import *
from sklearn.ensemble import IsolationForest

def svdd_ad(data):
    svdd = BaseSVDD(C=0.8, gamma=0.3, kernel='rbf', display='off')
    svdd.fit(data)
    anomaly_score = svdd.get_distance(data) - svdd.radius
    anomaly_score = (anomaly_score-min(anomaly_score))/(max(anomaly_score)-min(anomaly_score))
    return anomaly_score

def iforest_ad(data):
    clf = IsolationForest(contamination=0.02, max_features=2)
    clf.fit(data)
    anomaly_score = clf.score_samples(data)
    anomaly_score = (anomaly_score-min(anomaly_score))/(max(anomaly_score)-min(anomaly_score))
    anomaly_score = 1 - anomaly_score
    return anomaly_score

def chisquare_ad(data):
    means = mean(data,axis=1)
    chi = [sum(((data[i] - means)**2)/means) for i in range(0, len(data))]
    cur = chi - mean(chi)
    anomaly_score = [0 if cur[i] < 0 else cur[i] for i in range(0, len(cur))]
    return anomaly_score

