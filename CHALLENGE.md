# Data Engineer Challenge

Uma das tarefas de um **Data Engineer** consiste em lidar com a quantidade massiva de informações de comportamento 
do usuário que geram em sites na internet. Felizmente, todos esses dados são coletados e armazenados para futuras 
análises, e o desafio é contruir um sistema que irá computar informações relevantes a partir desses dados _raw_.

## Data

Os dados para desenvolvimento da solução do desafio podem ser acessados em:

```
https://www.dropbox.com/s/mchpweqebj9ppm2/part-00000.json.gz
https://www.dropbox.com/s/wdpgftxdfglsir9/part-00001.json.gz
https://www.dropbox.com/s/vuoauc5s1gqjw28/part-00002.json.gz
https://www.dropbox.com/s/7c977bkn3opqpim/part-00003.json.gz
https://www.dropbox.com/s/1k8mqupr3fwozf3/part-00004.json.gz 
```

O conjunto total de dados está dividido em 5 arquivos, os quais estão particionados pelo campo `anonymous_id`, fazendo com que
 um mesmo `anonymous_id` **não** esteja em arquivos diferentes, e ordenados pelo `device_sent_timestamp` em ordem crescente.

Dentro desses arquivos, os dados estão no formato **JSON**, sendo delimitado cada registro por uma nova linha:

```JSON
{
   "anonymous_id":"84CC8775-0E38-4787-A4FF-DD66CCFCF956",
   "device_sent_timestamp":1554767994740,
   "name":"Property Full Screen Gallery",
   "browser_family":"Other",
   "os_family":"Other",
   "device_family":"Other"
}
```

Cada registro desse arquivo representa um evento que um usuário efetuou, sendo que alguns representam _clicks_ em links, 
outros uma busca, e outros a abertura de uma página, e assim por diante. O formato desses eventos é descrito da seguinte maneira:

|       Atributo	    |  Tipo  |	Descrição                                              |
|-----------------------|--------|---------------------------------------------------------|
| anonymous_id	        | String | ID que identifica o usuário                             |
| device_sent_timestamp |  Long  | Timestamp que representa o momento que o evento ocorreu |
| name	                | String | Ação feita pelo usuário no portal                       |
| browser_family	    | String | Família do Browser usado pelo usuário                   |
| os_family	            | String | Família do Sistema Operacional usado pelo usuário       |
| device_family	        | String | Família do Dispositivo usado pelo usuário               |

## Sessions

**Session** é uma técnica que busca associar todas as atividades do usuário que caracterizem uma jornada. Na prática, 
todos eventos de um usuário são agrupados por uma chave de afinidade durante um período de atividade, que é chamada **session**. 
Quando o usuário não está mais ativamente interagindo na plataforma, a **session** é expirada e os novos eventos desse usuário 
vão ser associados com uma nova **session**.

As regras de **sessions** podem ser variadas, porém para este desafio vamos assumir apenas as seguintes:

- Abertura da **session** para o primeiro evento de um usuário;;
- Todo evento do mesmo usuário que ocorrer até **30 minutos** após a última deve ser associado a **session** existente;
- Caso o evento ocorra após **30 minutos** do último evento do usuário, o evento deve ser associado a uma **nova session**.

## Purpose

Com conhecimento sobre os dados e regras de **sessions**, agora você precisa construir uma aplicação que calcule e apresente 
a quantidade de **sessions** únicas que ocorreram em cada `browser`, `os` ou `device` em formato **JSON**.
