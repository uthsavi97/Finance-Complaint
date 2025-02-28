from FinanceComplaint.pipeline.training import TrainingPipeline
from FinanceComplaint.entity.config_entity import TrainingPipelineConfig
import sys
import os

sys.path.append(os.path.abspath("."))  # Adds current directory to path


if __name__=="__main__":
    training_pipeline_config = TrainingPipelineConfig()
    training_pipeline = TrainingPipeline(training_pipeline_config=training_pipeline_config)
    training_pipeline.start()
