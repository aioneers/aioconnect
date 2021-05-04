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
