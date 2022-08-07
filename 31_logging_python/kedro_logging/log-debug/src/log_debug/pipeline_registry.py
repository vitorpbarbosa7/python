"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from log_debug.pipelines import logging_tests as lt

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    logging_pipe = lt.create_pipeline()

    
    return {
            "__default__": logging_pipe
            }

    
