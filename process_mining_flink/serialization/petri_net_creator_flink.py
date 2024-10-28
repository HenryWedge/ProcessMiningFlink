import json

from process_mining_core.datastructure.converter.heuristics_net_petri_net_converter import \
    HeuristicsNetPetriNetConverter
from process_mining_core.datastructure.core.model.heuristics_net import HeuristicsNet
from process_mining_flink.serialization.petri_net_serializer import PetriNetSerDes


class PetriNetCreatorFlink:

    def __init__(self):
        self.petri_net_converter = HeuristicsNetPetriNetConverter()

    def process(self, heuristics_result_str: str) -> str:
        heuristics_result_dict = json.loads(heuristics_result_str)
        heuristics_result = HeuristicsNet(
            all_activities=heuristics_result_dict["all_activities"],
            start_activities=heuristics_result_dict["start_activities"],
            end_activities=heuristics_result_dict["end_activities"],
            relations=heuristics_result_dict["relations"],
            concurrent_activities=heuristics_result_dict["concurrent_activities"],
        )
        petri_net = self.petri_net_converter.create_petri_net(heuristics_result)
        return PetriNetSerDes().serialize(petri_net)
