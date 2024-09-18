from dotenv import load_dotenv
import os
import sys


def get_args(arg):
    """
        Recupera o valor de um argumento enviado na linha de comando ou, caso esteja executando em modo debug, recupera
        o valor do arquivo '.env'.
        \n
        Parameters
        ----------
        arg: argumento a ser consultado.\n
        \n
        Returns
        -------
        Retorna o valor do respectivo argumento.
    """
    if sys.monitoring.get_tool(sys.monitoring.DEBUGGER_ID) is not None:
        load_dotenv()
        return os.getenv('ENV')
    else:
        for env in sys.argv:
            if f"{arg}:" in env:
                return env.replace(f"{arg}:", "")


def force_known_error_message(task):
    """
        Indica que o teste possui um erro que já é conhecido e que o mesmo já possui uma task aberta para tratar o problema.
        \n
        Parameters
        ----------
        task: número da task aberta para tratar o erro.
        \n
        Returns
        -------
        Mensagem padrão para indicar que o teste possui um erro conhecido.
    """
    raise Exception(f'Esse teste falha e é um bug conhecido! ({task}).')
