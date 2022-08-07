from kedro.pipeline import Pipeline, node

from .nodes import print_logs

def create_pipeline(**kwargs):
    return Pipeline(
        [
        node(func=print_logs,
            inputs='params:mensagem_logging',
            outputs='dummy_string',
            name='logging_debug_node'
        )
    ]
)