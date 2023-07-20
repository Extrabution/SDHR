from datetime import datetime
from history_dto import History


async def concat_timestamp(signals_history) -> list[History]:
    combined_signals = []
    curr_status = None
    curr_timestamp = None
    start_timestamp = None
    for elem in signals_history:
        if curr_status is None:
            curr_status = elem["status"]
            curr_timestamp = elem["timestamp"] + 5
            start_timestamp = elem["timestamp"]
            continue
        if elem["status"] == curr_status:
            curr_timestamp += 5
        else:
            combined_signals.append(
                History(start_date=datetime.fromtimestamp(start_timestamp).strftime("%Y-%m-%dT%H:%M:%S"),
                        end_date=datetime.fromtimestamp(curr_timestamp).strftime("%Y-%m-%dT%H:%M:%S"),
                        status=curr_status.decode()))
            curr_status = elem["status"]
            curr_timestamp = elem["timestamp"] + 5
            start_timestamp = elem["timestamp"]
    combined_signals.append(History(start_date=datetime.fromtimestamp(start_timestamp).strftime("%Y-%m-%dT%H:%M:%S"),
                                    end_date=datetime.fromtimestamp(curr_timestamp).strftime("%Y-%m-%dT%H:%M:%S"),
                                    status=curr_status.decode()))
    return combined_signals
