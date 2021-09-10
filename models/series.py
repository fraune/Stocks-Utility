from dateutil.relativedelta import relativedelta

from models.snapshot import Snapshot


class Series:
    data: list = []
    data_by_date: dict = {}

    def __init__(self, json_list: list):
        for json_dict in json_list:
            snapshot = Snapshot(json_dict)
            self.data.append(snapshot)
            self.data_by_date[snapshot.date] = snapshot
        # self.force_order_old_to_new()

    def get_oldest_snapshot(self):
        return self.data[0]

    def get_newest_snapshot(self):
        return self.data[len(self.data) - 1]
