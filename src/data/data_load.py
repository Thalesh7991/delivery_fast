import os
import sys

import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))


import structlog

logger = structlog.getLogger()

from utils.utils import load_config_file


class DataLoad:
    def __init__(self) -> None:
        pass

    def load_data(self, dataset_name: str) -> pd.DataFrame:
        """Essa função retorna um dataframe"""

        print(os.path.join(os.path.dirname(__file__)))
        logger.info("Iniciando o carregamento")
        try:
            dataset = load_config_file().get(dataset_name)
            if dataset is None:
                raise ValueError(
                    "Error: O nome do dataset informado está errado: {dataset}"
                )
            
            print( os.path.abspath(os.path.join(os.path.dirname(__file__))) ) 
  
            print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/raw/', dataset)))

            loaded_data = pd.read_csv(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/raw/', dataset)))



            return loaded_data
        
        #[load_config_file().get("columns_to_use")]
        except ValueError as ve:
            logger.error(str(ve))
        except Exception as e:
            logger.error(f"Erro Inesperado: {str(e)}")