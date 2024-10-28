from process_mining_core.algorithms.directly_follows_graph_creator import DirectlyFollowsGraphCreator
from process_mining_flink.serialization.directly_follows_graph_serializer import DirectlyFollowsGraphSerDes
from process_mining_flink.serialization.event_serializer import EventSerDes

class DirectlyFollowsGraphCreatorFlink:

    def __init__(self, sample_size, batch_size):
        self.directly_follows_graph_creator = DirectlyFollowsGraphCreator(sample_size, batch_size)

    def process(self, event_string: str) -> str:
        print(event_string)
        event = EventSerDes().deserialize(event_string)
        directly_follows_graph = self.directly_follows_graph_creator.process(event)
        if not directly_follows_graph:
            return ""
        directly_follows_graph_as_string = DirectlyFollowsGraphSerDes().serialize(directly_follows_graph)
        return directly_follows_graph_as_string
