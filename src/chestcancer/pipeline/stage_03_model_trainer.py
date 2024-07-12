

from chestcancer.config.configuration import ConfigurationManager
from chestcancer.components.model_trainer import Training





class ModelTrainingPipeline:
    
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.training_model()