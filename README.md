# json_log

Lib para criar logs em formato JSON, com suporte a FluentD. 

Esta lib utiliza o [logging](https://docs.python.org/3/library/logging.html) nativo do Python, sobrescrevendo seu output para formato JSON, para uso com FluentD e/ou outras ferramentas de consumo de log em JSON.

Através dela, também é possivel incluir tags personalizadas ao JSON de forma fácil e intuitiva.

## Instalação
Adicionar ao `requirements.txt` do projeto:

```
git+https://github.com/douglasmoraisdev/json_log#egg=json_log
```

OU manualmente com PIP:
```bash
$ pip install git+https://github.com/douglasmoraisdev/json_log#egg=json_log
```



## Configuração
A Lib utiliza `variaveis de ambiente` para sua configuração. As mesmas podem ser encontradas no arquivo '.env.sample', e consumidas via arquivo .env, se for o padrão do projeto.

```ini
LOG_FLUENTD=true #true=utiliza as configuracoes de FluentD a seguir #false=utiliza log em arquivo
LOG_FLUENTD_HOST=localhost #host do FluentD, se utilizado
LOG_FLUENTD_PORT=24224 #porta do FluentD, se utilizado
LOG_LEVEL=INFO #Nivel de log
LOG_NAME=teste_log #Nome do arquivo de log, caso não use FluentD
LOG_LOCAL_PATH=log/ #Path do log, caso não use FluentD
```


## Importação e uso
Para utilizar o log basta importar o objeto `applog` da package e utilizar os metodos de logging (info, debug, error, etc).

#### params
* message(required, positional): Texto da mensagem do log
* **campos personalizados(optional): Parametros nomeados que serão incluidos no log. Ver a sessão `Tags e campos personalizadas` para mais informações.

Exemplo:
```py
from json_log import applog

if __name__ == '__main__':
    applog.info('Alguma mensagem de log nivel INFO')
    applog.debug('Alguma mensagem de log nivel DEBUG')    

```

Irá resultar em:
```json
{
    "@timestamp": "2020-05-12 14:08:40,657",
    "appname": "teste_log",
    "loglevel": "INFO",
    "run_id": "470e25bc-7e5d-4af8-b71a-2e22d582cc5a",
    "message": "Alguma mensagem de log nivel INFO"
}
{
    "@timestamp": "2020-05-12 14:08:40,657",
    "appname": "teste_log",
    "loglevel": "DEBUG",
    "run_id": "470e25bc-7e5d-4af8-b71a-2e22d582cc5a",
    "message": "Alguma mensagem de log nivel DEBUG"
}
```
* Obs.: O exemplo desse output em JSON está identado para melhor visualização nesta documentação. O output normal, não é identado, e sim um registro por linha.



## Tags e campos personalizadas
É possivel o envio de tags e campos personalizadas para o log. Basta passar como argumento nomeado(kwargs) na chamada do log.

Tags e campos personalizados são úteis para a ferramenta de log que irá consumir o JSON. Com estes campos é possivel facilitar o parse e consulta destes logs de forma flexivel, como por exemplo, filtrando todos os logs que contem a `tag` 'x' ou 'y'.

Exemplo:

```py
    applog.error('Alguma mensagem de log nivel ERRO', algum_campo_personalizado='algum_valor_util', tags=['erro', 'processamento_x', 'outra_tag'])
```

Output:
```json
{
    "@timestamp": "2020-05-12 14:24:35,667",
    "appname": "teste_log",
    "loglevel": "ERROR",
    "run_id": "2f15f1b0-c9d4-48fb-8cbd-7abcda7380dc",
    "algum_campo_personalizado": "algum_valor_util",
    "tags": [
        "erro",
        "processamento_x",
        "outra_tag"
    ],
    "message": "Alguma mensagem de log nivel ERRO"
}
```
* Note o nó algum_campo_personalizado e tags.



## Logs especiais
Alguns metodos da classe de log foram criados para situações especiais, para facilitar seu uso e tem outputs com campos extras de informação.


### `time_metric`
Loga o tempo total de uma execução. Adiciona a tag `metrics` no log.

#### params
    message(required): Texto da mensagem do log
    func_name(required): Nome da função cronometrada
    total_time(required): Tempo total de execução
    **kwargs(optional): campos personalizados

Exemplo:

```py
    applog.time_metric('Executada funcao_x', 'funcao_x', 4)    
```

Output:
```json
{
    "@timestamp": "2020-05-12 14:42:48,258",
    "appname": "teste_log",
    "loglevel": "INFO",
    "run_id": "b0d19656-0dbe-4c35-aa4f-d3b1c11b3b44",
    "message": "Executada funcao_x",
    "total_time": 4,
    "function_name": "funcao_x",
    "tags": [
        "metrics"
    ]
}
```
* Obs.: Os `campos personalizados` continuam tendo o mesmo funcionamento.