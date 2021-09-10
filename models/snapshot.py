from datetime import datetime

FIDELITY_DATE_FORMAT = "%Y/%m/%d-%H:%M:%S"


class Snapshot:
    date: datetime = None  # lt
    open: float = 0.0  # op
    close: float = 0.0  # cl
    high: float = 0.0  # hi
    low: float = 0.0  # lo
    volume: int = 0  # v

    def __init__(self, json_data: dict):
        self.date = datetime.strptime(json_data['lt'], FIDELITY_DATE_FORMAT)
        self.open = json_data['op']
        self.close = json_data['cl']
        self.high = json_data['hi']
        self.low = json_data['lo']
        self.volume = json_data['v']
