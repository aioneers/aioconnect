import aioconnect
import aiox


def test_json_extract():
    test_json = {
        "destination_addresses": [
            "Washington, DC, USA",
            "Philadelphia, PA, USA",
            "Santa Barbara, CA, USA",
            "Miami, FL, USA",
            "Austin, TX, USA",
            "Napa County, CA, USA",
        ],
        "origin_addresses": ["New York, NY, USA"],
        "rows": [
            {
                "elements": [
                    {
                        "distance": {"text": "227 mi", "value": 365468},
                        "duration": {"text": "3 hours 54 mins", "value": 14064},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "94.6 mi", "value": 152193},
                        "duration": {"text": "1 hour 44 mins", "value": 6227},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "2,878 mi", "value": 4632197},
                        "duration": {"text": "1 day 18 hours", "value": 151772},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1,286 mi", "value": 2069031},
                        "duration": {"text": "18 hours 43 mins", "value": 67405},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1,742 mi", "value": 2802972},
                        "duration": {"text": "1 day 2 hours", "value": 93070},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "2,871 mi", "value": 4620514},
                        "duration": {"text": "1 day 18 hours", "value": 152913},
                        "status": "OK",
                    },
                ]
            }
        ],
        "status": "OK",
    }

    my_values = aioconnect.json_extract(test_json, "value")

    durations = my_values[1::2]  # Get every even-index value from a list
    distances = my_values[2::1]  # Get every odd-index value from a list

    print("Durations = ", durations)
    print("Distances = ", distances)

    assert durations == [14064, 6227, 151772, 67405, 93070, 152913]
    assert distances == [
        152193,
        6227,
        4632197,
        151772,
        2069031,
        67405,
        2802972,
        93070,
        4620514,
        152913,
    ]