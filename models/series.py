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

    # return a snapshot with the time difference
    # def get_snapshot_with_time_diff(self, beginning_snapshot: Snapshot, difference_years: int):
    #     if beginning_snapshot is self.get_oldest_snapshot() and difference_years > 0:
    #         return None
    #     if beginning_snapshot is self.get_newest_snapshot() and difference_years < 0:
    #         return None
    #
    #     new_date = beginning_snapshot.date + relativedelta(years=difference_years)
    #     # beginning_snapshot.date.
    #     print(new_date)
    #     print(new_date)