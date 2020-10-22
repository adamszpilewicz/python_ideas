import logging
import pandas as pd
from logger_tool import Logger


logger_instance = Logger()
decorator_logger = logger_instance.wrap(
    logger_instance.entering, logger_instance.exiting
)
logger = logging.getLogger(__name__)

# import exemplary dataset
@decorator_logger
def read_data():
    df_titanic = pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    logger.info(
        f"""
        \nColumns of df_titanic dataset:\n\n{df_titanic.columns}\n\nDescription of df_titanic dataset:\n\n{df_titanic.describe()}
    """
    )
    return df_titanic


if __name__ == "__main__":
    df = read_data()
    print(df.head())
    print(df.info())
