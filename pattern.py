def get_features(event):
    features = []
    for key, val in event.iteritems():
        features.append(str(key) + "$" + str(val))
    return features

