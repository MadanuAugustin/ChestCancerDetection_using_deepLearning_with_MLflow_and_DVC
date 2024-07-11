



import sys
from chestcancer.pipeline.stage_01_dataIngestion import DataIngestionTrainingPipeline
from chestcancer import (CustomException, logger)



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'-----------------{STAGE_NAME} started------------------------')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'-----------------{STAGE_NAME} completed successfully-----------------')
except Exception as e:
    raise(CustomException(e, sys))