import json
import string

from process_mining_core.algorithms.stream_heuristics.heuristics_net_creator import HeuristicsNetCreator
from process_mining_flink.serialization.directly_follows_graph_serializer import DirectlyFollowsGraphSerDes


class HeuristicsNetCreatorFlink:

    def __init__(self, dependency_threshold, and_threshold):
        self.heuristics_net_creator = HeuristicsNetCreator(dependency_threshold, and_threshold)

    def process(self, directly_follows_graph_string: string) -> string:
        directly_follows_graph = DirectlyFollowsGraphSerDes().deserialize(directly_follows_graph_string)

        heuristics_result = self.heuristics_net_creator.create_heuristics_net(directly_follows_graph)

        return json.dumps(heuristics_result.__dict__)
