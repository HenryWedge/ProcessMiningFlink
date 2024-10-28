import os
import sys

from dotenv import load_dotenv
from process_mining_flink.flink_util.flink_pipeline_base import FlinkPipelineBase
from process_mining_flink.pipeline.heuristics_miner.heuristics_miner_pipeline import HeuristicsMinerFlink

if __name__ == '__main__':
    if "local" in sys.argv:
        load_dotenv()

    heuristics_miner = HeuristicsMinerFlink(
        flink_pipeline=FlinkPipelineBase(
            bootstrap_server=os.environ["BOOTSTRAP_SERVER"],
            input_topic=os.environ["INPUT_TOPIC"],
            output_topic=os.environ["MODEL_TOPIC"],
            group=os.environ["GROUP"],
            parallelism=int(os.environ["PARALLELISM"]),
            connect_jar_location=f"file://{os.environ['PATH_TO_CONNECT_JAR']}/resources/flink-sql-connector-kafka-1.17.2.jar"
        ),
        sample_size=int(os.environ["SAMPLE_SIZE"]),
        batch_size=int(os.environ["BATCH_SIZE"]),
        and_threshold=float(os.environ["AND_THRESHOLD"]),
        dependency_threshold=float(os.environ["DEPENDENCY_THRESHOLD"])
    )

    heuristics_miner.run()