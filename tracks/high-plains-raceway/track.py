"""High Plains Full Course, curated from OSM and the official course map."""
from lib.dsl import Track, osm

t = Track(
    "high-plains-raceway",
    "High Plains Raceway",
    aka=["High Plains", "HPR"],
    country="US",
    location=dict(
        lat=39.736,
        lon=-103.897,
        locality="Deer Trail",
        region="Colorado",
        timezone="America/Denver",
    ),
    osm=osm([39.72, -103.92, 39.75, -103.88]),
)

lap = t.layout(
    "full",
    "Full Course",
    length_m=4103.8272,
    direction="clockwise",
    start_finish=dict(
        location=[-103.8952, 39.7350],
        note="Approximate position on the paddock straight from the official diagram; "
             "not a surveyed timing line. Confirm before lap timing use.",
    ),
    # Includes the full-course main straight tagged "Short North" and the
    # corner "High Plains Drifter"; excludes pit lane and the west shortcut.
    osm_way_ids=[
        132189631, 132189632, 132189633, 289314482, 289314483,
        289314484, 289314485, 289314486, 289314488, 289314489,
    ],
)

t.surface()

# Official diagram numbering; the two bends of Turn 9 retain 9a/9b codes.
# Markers are provisional geometric apexes on the OSM centerline, not braking
# points or apexes extracted from the owner's driving line.
corners = [
    dict(number=1, marker=0.070244, direction="left"),
    dict(number=2, marker=0.1200, direction="right"),
    dict(number=3, marker=0.166829, direction="right"),
    dict(number=4, marker=0.387317, direction="right", official="Bikers Berm"),
    dict(number=5, marker=0.427317, direction="left", official="Niagara"),
    dict(number=6, marker=0.504390, direction="right", official="Danny's Lesson"),
    dict(number=7, marker=0.586341, direction="right", official="High Plains Drifter"),
    dict(number=8, marker=0.661463, direction="left"),
    dict(number=9, code="9a", marker=0.699512, direction="right",
         official="To Hell on a Bobsled", complex="To Hell on a Bobsled"),
    dict(number=10, code="9b", marker=0.725854, direction="left",
         official="To Hell on a Bobsled", complex="To Hell on a Bobsled"),
    dict(number=11, code="10", marker=0.757073, direction="right"),
    dict(number=12, code="11", marker=0.824390, direction="right"),
    dict(number=13, code="12", marker=0.864390, direction="left",
         official="Ladder to Heaven"),
    dict(number=14, code="13", marker=0.922927, direction="left",
         official="Prairie Corkscrew", complex="Prairie Corkscrew"),
    dict(number=15, code="14", marker=0.937561, direction="right",
         official="Prairie Corkscrew", complex="Prairie Corkscrew"),
    dict(number=16, code="15", marker=0.953171, direction="left",
         official="Prairie Corkscrew", complex="Prairie Corkscrew"),
]
# Named OSM ways describe whole sections, not precise apexes. Using their
# centroids as alignment anchors would move the curated lap origin.
lap.corners([{**corner, "match_osm": False} for corner in corners])

t.note(
    "Official layout reference: https://www.highplainsraceway.com/track-info/ . "
    "Start/finish is approximate; corners were curated against the official map. "
    "Private telemetry is used only for local comparison, never as surface input."
)
