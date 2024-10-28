from pyflink.common import Types, WatermarkStrategy

from process_mining_flink.serialization.heuristics_discovery_flink import DirectlyFollowsGraphCreatorFlink
from process_mining_flink.serialization.heuristics_net_creator import HeuristicsNetCreatorFlink
from process_mining_flink.serialization.petri_net_creator_flink import PetriNetCreatorFlink


class HeuristicsMinerFlink:

    def __init__(self,
                 flink_pipeline,
                 sample_size,
                 batch_size,
                 and_threshold,
                 dependency_threshold):

        self.flink_pipeline = flink_pipeline
        self.sample_size = sample_size
        self.batch_size = batch_size
        self.and_threshold = and_threshold
        self.dependency_threshold = dependency_threshold

    def run(self):
        env = self.flink_pipeline.get_env()
        source = self.flink_pipeline.get_kafka_source()
        sink = self.flink_pipeline.get_kafka_sink()

        directly_follows_graph_creator = DirectlyFollowsGraphCreatorFlink(self.sample_size, self.batch_size)
        heuristics_net_creator = HeuristicsNetCreatorFlink(dependency_threshold=self.dependency_threshold, and_threshold=self.and_threshold)
        petri_net_creator = PetriNetCreatorFlink()

        (env.from_source(source, WatermarkStrategy.no_watermarks(), "kafka-source")
            .map(lambda event: directly_follows_graph_creator.process(event), Types.STRING())
            .filter(lambda directly_follows_graph: directly_follows_graph != "")
            .map(lambda directly_follows_graph: heuristics_net_creator.process(directly_follows_graph), Types.STRING())
            .map(lambda heuristics_net: petri_net_creator.process(heuristics_net), Types.STRING())
            .sink_to(sink))

        env.execute()
