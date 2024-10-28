import json
import string

from process_mining_core.datastructure.core.event import Event


class EventSerDes:

    def deserialize(self, event_string: string) -> Event:
        event_as_dict = json.loads(event_string)
        return Event(
            timestamp=event_as_dict["timestamp"],
            activity=event_as_dict["activity"],
            case_id=event_as_dict["caseid"],
            node=event_as_dict["node"],
            group_id=event_as_dict["group"]
        )
