import aioconnect


class Test_get_values:

    json_metric_types = [
        {
            "_id": "5fb7bf2f8ce87f0012fcc8f3",
            "name": "Financial",
            "createdAt": "2020-11-20T13:05:51.280Z",
            "updatedAt": "2020-11-20T13:05:51.280Z",
            "__v": 0,
        },
        {
            "_id": "5fb7cc5c8ce87f0012fcc918",
            "name": "Percentage",
            "createdAt": "2020-11-20T14:02:04.671Z",
            "updatedAt": "2020-11-20T14:02:04.671Z",
            "__v": 0,
        },
        {
            "_id": "60018ae0f10fa9001326747c",
            "name": "Countable",
            "createdAt": "2021-01-15T12:30:24.325Z",
            "updatedAt": "2021-01-15T12:30:24.325Z",
            "__v": 0,
        },
        {
            "_id": "6019ed8072b96c00133df30d",
            "name": "Other",
            "createdAt": "2021-02-03T00:25:36.536Z",
            "updatedAt": "2021-02-03T00:25:36.536Z",
            "__v": 0,
        },
        {
            "_id": "6063127e01b2550013be8b63",
            "name": "My second DOT",
            "createdAt": "2021-03-30T11:58:54.230Z",
            "updatedAt": "2021-03-30T11:58:54.230Z",
            "__v": 0,
        },
    ]

    def test_metric_types_ids(self):
        assert aioconnect.get_values(json_data=self.json_metric_types, key="_id") == [
            "5fb7bf2f8ce87f0012fcc8f3",
            "5fb7cc5c8ce87f0012fcc918",
            "60018ae0f10fa9001326747c",
            "6019ed8072b96c00133df30d",
            "6063127e01b2550013be8b63",
        ]

    def test_metric_types_names(self):
        assert aioconnect.get_values(json_data=self.json_metric_types, key="name") == [
            "Financial",
            "Percentage",
            "Countable",
            "Other",
            "My second DOT",
        ]

    def test_metric_types_empty_feature(self):
        try:
            aioconnect.get_values(json_data=self.json_metric_types, key="")
        except ValueError:
            pass

    def test_metric_types_nofeature(self):
        assert aioconnect.get_values(json_data=self.json_metric_types) == [
            "5fb7bf2f8ce87f0012fcc8f3",
            "5fb7cc5c8ce87f0012fcc918",
            "60018ae0f10fa9001326747c",
            "6019ed8072b96c00133df30d",
            "6063127e01b2550013be8b63",
        ]

    # def test_list(self):
    #     json_data = [
    #         {
    #             "_id": "5fb7bf528ce87f0012fcc8f4",
    #             "name": "Material",
    #             "createdAt": "2020-11-20T13:06:26.598Z",
    #             "updatedAt": "2021-02-03T01:20:20.159Z",
    #             "__v": 0,
    #             "description": "This DOT type represents all goods that are most likely represented as material in ERP systems. E.g. finished goods, stock keeping units, raw materials, intermediate products, components or trading goods.",
    #         },
    #         {
    #             "_id": "5fb7bf598ce87f0012fcc8f5",
    #             "name": "Master Data Object",
    #             "createdAt": "2020-11-20T13:06:33.291Z",
    #             "updatedAt": "2020-11-20T13:06:33.291Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf628ce87f0012fcc8f6",
    #             "name": "Master Data Process",
    #             "createdAt": "2020-11-20T13:06:42.058Z",
    #             "updatedAt": "2020-11-20T13:06:42.058Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf678ce87f0012fcc8f7",
    #             "name": "Asset",
    #             "createdAt": "2020-11-20T13:06:47.530Z",
    #             "updatedAt": "2020-11-20T13:06:47.530Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf6a8ce87f0012fcc8f8",
    #             "name": "Line",
    #             "createdAt": "2020-11-20T13:06:50.621Z",
    #             "updatedAt": "2020-11-20T13:06:50.621Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf7b8ce87f0012fcc8f9",
    #             "name": "Production Department",
    #             "createdAt": "2020-11-20T13:07:07.155Z",
    #             "updatedAt": "2020-11-20T13:07:07.155Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf828ce87f0012fcc8fa",
    #             "name": "Customer Invoice",
    #             "createdAt": "2020-11-20T13:07:14.865Z",
    #             "updatedAt": "2020-11-20T13:07:14.865Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf888ce87f0012fcc8fb",
    #             "name": "Supplier Invoice",
    #             "createdAt": "2020-11-20T13:07:20.092Z",
    #             "updatedAt": "2020-11-20T13:07:20.092Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf8c8ce87f0012fcc8fc",
    #             "name": "Supplier",
    #             "createdAt": "2020-11-20T13:07:24.532Z",
    #             "updatedAt": "2020-11-20T13:07:24.532Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf8f8ce87f0012fcc8fd",
    #             "name": "Customer",
    #             "createdAt": "2020-11-20T13:07:27.963Z",
    #             "updatedAt": "2020-11-20T13:07:27.963Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf958ce87f0012fcc8fe",
    #             "name": "Process",
    #             "createdAt": "2020-11-20T13:07:33.602Z",
    #             "updatedAt": "2021-02-03T01:22:14.159Z",
    #             "__v": 0,
    #             "description": "This DOT type represents processes in an organization, typically identified by a Process ID and a process level. E.g. L0 - Plan Supply Chain, L1 -  Demand Planning,  L3  - Create statistical forecast, or L4 -  Download sales data",
    #         },
    #         {
    #             "_id": "5fb7bf9a8ce87f0012fcc8ff",
    #             "name": "Plant",
    #             "createdAt": "2020-11-20T13:07:38.167Z",
    #             "updatedAt": "2020-11-20T13:07:38.167Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "5fb7bf9e8ce87f0012fcc900",
    #             "name": "IT System",
    #             "createdAt": "2020-11-20T13:07:42.666Z",
    #             "updatedAt": "2020-11-20T13:07:42.666Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcaed52b0c500125fec82",
    #             "name": "Supplier Segment",
    #             "description": "Supplier segment ID",
    #             "createdAt": "2021-01-26T07:55:25.307Z",
    #             "updatedAt": "2021-01-26T07:55:25.307Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcaf952b0c500125fec87",
    #             "name": "Cost Center",
    #             "description": "Cost center ID",
    #             "createdAt": "2021-01-26T07:55:37.159Z",
    #             "updatedAt": "2021-01-26T07:55:37.159Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcafa52b0c500125fec88",
    #             "name": "Warehouse",
    #             "description": "Warehouse ID",
    #             "createdAt": "2021-01-26T07:55:38.670Z",
    #             "updatedAt": "2021-01-26T07:55:38.670Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcafc52b0c500125fec89",
    #             "name": "Lane",
    #             "description": "Lane ID",
    #             "createdAt": "2021-01-26T07:55:40.181Z",
    #             "updatedAt": "2021-01-26T07:55:40.181Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcafd52b0c500125fec8a",
    #             "name": "Destination",
    #             "description": "Destination ID",
    #             "createdAt": "2021-01-26T07:55:41.694Z",
    #             "updatedAt": "2021-01-26T07:55:41.694Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcaff52b0c500125fec8b",
    #             "name": "Project",
    #             "description": "Project ID",
    #             "createdAt": "2021-01-26T07:55:43.205Z",
    #             "updatedAt": "2021-01-26T07:55:43.205Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcb2452b0c500125fec8d",
    #             "name": "Product Group",
    #             "description": "Product group ID",
    #             "createdAt": "2021-01-26T07:56:20.733Z",
    #             "updatedAt": "2021-01-26T07:56:20.733Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcb2452b0c500125fec8e",
    #             "name": "Product Segment",
    #             "description": "Product segment ID",
    #             "createdAt": "2021-01-26T07:56:20.893Z",
    #             "updatedAt": "2021-01-26T07:56:20.893Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "600fcb2552b0c500125fec8f",
    #             "name": "Customer Segment",
    #             "description": "Customer segment ID",
    #             "createdAt": "2021-01-26T07:56:21.058Z",
    #             "updatedAt": "2021-01-26T07:56:21.058Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fa2072b96c00133df326",
    #             "name": "Standard",
    #             "description": "This DOT type represents any element being part of a measure. It can be used in a universal way.",
    #             "createdAt": "2021-02-03T01:19:28.547Z",
    #             "updatedAt": "2021-02-03T01:19:28.547Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fa7b72b96c00133df327",
    #             "name": "Data Object",
    #             "description": "This DOT type represents typically objects in IT systems described by several attributes. E.g. material master, customer master, mapping tables or parameter tables",
    #             "createdAt": "2021-02-03T01:20:59.620Z",
    #             "updatedAt": "2021-02-03T01:20:59.620Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fa9672b96c00133df328",
    #             "name": "Capacity Resource",
    #             "description": "This DOT type represents typically physical assets in transformation processes. E.g. machines, work places, production lanes or assembly lines in manufacturing",
    #             "createdAt": "2021-02-03T01:21:26.646Z",
    #             "updatedAt": "2021-02-03T01:21:26.646Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fb2672b96c00133df329",
    #             "name": "Business Partner",
    #             "description": "This DOT type represents all external relationships being part of a measure. E.g. customers, suppliers, contract manufacturers, banks or 3PLs",
    #             "createdAt": "2021-02-03T01:23:50.835Z",
    #             "updatedAt": "2021-02-03T01:23:50.835Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fb4572b96c00133df32a",
    #             "name": "Organizational Unit",
    #             "description": "This DOT type represents elements in an organizational structure on different levels. E.g. divisions, functions, legal entities, teams or people",
    #             "createdAt": "2021-02-03T01:24:21.817Z",
    #             "updatedAt": "2021-02-03T01:24:21.817Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fb7172b96c00133df32b",
    #             "name": "Account",
    #             "description": "This DOT type represents elements in a chart of account and could address account types. E.g account group like fixed assets or dedicated accounts like travel expenses.",
    #             "createdAt": "2021-02-03T01:25:05.859Z",
    #             "updatedAt": "2021-02-03T01:25:05.859Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fb8f72b96c00133df32c",
    #             "name": "Location",
    #             "description": "This DOT type represents a physical location that is part of a measure. E.g. site, plant, warehouse, store or country",
    #             "createdAt": "2021-02-03T01:25:35.141Z",
    #             "updatedAt": "2021-02-03T01:25:35.141Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fbaa72b96c00133df32d",
    #             "name": "Relation",
    #             "description": "This DOT type represents the relationship between two elements. E.g. transportation destination or partner relation",
    #             "createdAt": "2021-02-03T01:26:02.768Z",
    #             "updatedAt": "2021-02-03T01:26:02.768Z",
    #             "__v": 0,
    #         },
    #         {
    #             "_id": "6019fbbf72b96c00133df32e",
    #             "name": "Document Type",
    #             "description": "This DOT type represents specific documents in business interactions that are part of a measure. E.g. invoices, purchase orders or production orders",
    #             "createdAt": "2021-02-03T01:26:23.288Z",
    #             "updatedAt": "2021-02-03T01:26:23.288Z",
    #             "__v": 0,
    #         },
    #     ]


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
