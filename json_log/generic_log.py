from dotenv import load_dotenv
import textwrap
import yaml

config = yaml.safe_load(open('config.yml'))


class GenericLog:

    log_level = config['LOG_LEVEL']
    log_path = config['LOG_LOCAL_PATH']

    # Override esse método caso necessario nas classes filhas
    def _format_message(self, **kwargs):
        
        return kwargs

    # Mensagens de log padrao
    def info(self, message, **kwargs):
        msg = {'message' : message}
        kwargs.update(msg)
        message = self._format_message(**kwargs)
        self.log.info(message, extra={'run_id': self.run_id})

    def error(self, message, **kwargs):
        msg = {'message' : message}
        kwargs.update(msg)        
        message = self._format_message(**kwargs)
        self.log.error(message, extra={'run_id': self.run_id})

    def debug(self, message, **kwargs):
        msg = {'message' : message}
        kwargs.update(msg)        
        message = self._format_message(**kwargs)
        self.log.debug(message, extra={'run_id': self.run_id})

    # Mensagens de log especiais
    def time_metric(self, message, func_name, total_time, **kwargs):

        # Tags default = 'metrics'
        # concatena tags extras caso informadas
        tags = ['metrics']
        if 'tags'in kwargs:
            tags.extend(kwargs['tags'])

        default_nodes = {"message": message,
                         "total_time": total_time,
                         "function_name": func_name,
                         "tags": ['metrics']
                        }
        kwargs.update(default_nodes)
        message = self._format_message(**kwargs)
        self.log.info(message, extra={'run_id': self.run_id})

    def _sanitize_json(self, text: str) -> str:
        sanitezed = text.replace("\"", "\'") \
            .replace("{", "") \
            .replace("}", "") \
            .replace("[", "") \
            .replace("]", "") \
            .replace("]", "")

        sanitezed = "".join(textwrap.wrap(sanitezed))

        return sanitezed
