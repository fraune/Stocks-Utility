from models.snapshot import Snapshot


class Series:
    # TODO: Read from JSON file as input
    # TODO: don't keep two data objects with the same data
    data: list = []
    data_by_date: dict = {}

    def __init__(self, json_list: list):
        for json_dict in json_list:
            snapshot = Snapshot(json_dict)
            self.data.append(snapshot)
            self.data_by_date[snapshot.date] = snapshot

    def get_oldest_snapshot(self):
        return self.data[0]

    def get_newest_snapshot(self):
        return self.data[len(self.data) - 1]
