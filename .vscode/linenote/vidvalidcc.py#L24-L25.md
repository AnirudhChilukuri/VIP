Detections(xyxy=array([[     58.921,           0,         640,         360]], dtype=float32), mask=None, confidence=array([    0.79958], dtype=float32), class_id=array([0]), tracker_id=None, data={'class_name': array(['manhole'], dtype='<U7')})

(array([     58.921,           0,         640,         360], dtype=float32), None, 0.7995751, 0, None, {'class_name': 'manhole'})

1 - xyxy
2 - mask
3 - confidence
4 - class_id
5 - tracker_id
6 - data

import supervision as sv

image = ...
detections = sv.Detections(...)

bounding_box_annotator = sv.BoundingBoxAnnotator()
annotated_frame = bounding_box_annotator.annotate(
    scene=image.copy(),
    detections=detections