



import sys
from chestcancer.pipeline.stage_01_dataIngestion import DataIngestionTrainingPipeline
from chestcancer.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chestcancer import (CustomException, logger)



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'-----------------{STAGE_NAME} started------------------------')
    dataIngestion = DataIngestionTrainingPipeline()
    dataIngestion.main()
    logger.info(f'-----------------{STAGE_NAME} completed successfully-----------------')
except Exception as e:
    raise(CustomException(e, sys))





STAGE_NAME = 'Prepare Base Model Stage'

try:
    logger.info(f'-----------------{STAGE_NAME} started------------------------')
    preparebasemodel = PrepareBaseModelTrainingPipeline()
    preparebasemodel.main()
    logger.info(f'-----------------{STAGE_NAME} completed successfully-----------------')
except Exception as e:
    raise CustomException(e, sys)