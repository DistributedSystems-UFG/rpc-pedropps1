# RPC-Based List Manipulation Server with RPyC

Este projeto demonstra o uso da biblioteca RPyC (Remote Python Call) para construir um sistema cliente-servidor simples em Python. O servidor expõe um objeto que se comporta como uma lista, permitindo que clientes remotos manipulem seu estado através de chamadas de procedimento que se assemelham a chamadas de função locais.

O objetivo é ilustrar o poder e a simplicidade dos frameworks de RPC em comparação com a programação de rede de baixo nível com sockets, abstraindo toda a complexidade de serialização de dados, conexão e definição de protocolo.

## Arquitetura do Sistema

*   **`server.py`**: Inicia um servidor RPyC `ThreadedServer` que instancia a classe `DBList`. Cada método na classe prefixado com `exposed_` fica automaticamente disponível para ser chamado por clientes remotos. O servidor mantém o estado da lista em memória.
*   **`client.py`**: Um script de cliente que se conecta ao servidor RPyC e executa uma série de operações de teste para demonstrar todas as funcionalidades implementadas, imprimindo os resultados de cada passo.
*   **`constRPYC.py`**: Um arquivo de configuração simples para definir o endereço `SERVER` e a `PORT` para a comunicação.

## Funcionalidades Implementadas (Procedimentos Remotos)

O servidor foi aprimorado para expor um conjunto completo de operações de manipulação de lista:

| Procedimento Remoto           | Descrição                                                    |
| ----------------------------- | -------------------------------------------------------------- |
| `exposed_value()`             | Retorna o estado atual da lista (todos os seus elementos).      |
| `exposed_append(data)`        | Adiciona um novo elemento ao final da lista.                   |
| `exposed_insert(index, data)` | Insere um elemento em um índice específico na lista.            |
| `exposed_remove(data)`        | Remove a primeira ocorrência do elemento especificado.         |
| `exposed_search(data)`        | Verifica se um elemento existe na lista, retornando `True` ou `False`. |
| `exposed_get_by_index(index)` | Retorna o elemento localizado em um determinado índice.           |
| `exposed_sort()`              | Ordena os elementos da lista em ordem crescente.               |
| `exposed_clear()`             | Remove todos os elementos da lista, deixando-a vazia.          |

## Pré-requisitos

Antes de executar, certifique-se de que você tem o Python 3 e a biblioteca RPyC instalada.


## Como Executar o Sistema

Siga estes passos para testar a aplicação.

**1. Configurar a Conexão**

Edite o arquivo `constRPYC.py`. Para testar em sua máquina local, a configuração deve ser:

```python
SERVER = "localhost"
PORT   = 5002
```
*Observação: Se estiver executando em máquinas diferentes (ex: instâncias AWS), substitua `"localhost"` pelo endereço IP privado da máquina servidora e certifique-se de que a `PORT` está liberada no firewall (Security Group).*

**2. Iniciar o Servidor**

Abra um terminal, navegue até a pasta do projeto e execute:

```bash
python3 server.py
```
O servidor será iniciado e ficará aguardando por conexões de clientes.

**3. Executar o Cliente**

Abra um **segundo terminal** e, na mesma pasta, execute o script do cliente:

```bash
python3 client.py
```

O cliente se conectará ao servidor e executará uma sequência de testes, demonstrando cada uma das funções remotas implementadas. Você verá a saída detalhada das operações no terminal do cliente e os logs de atividade no terminal do servidor.

## Conceito Chave: Sockets vs. RPyC

Este projeto destaca a principal vantagem do RPC sobre a programação direta com sockets: a **transparência**.

*   **Com Sockets**: Você é responsável por serializar dados (ex: com `pickle`), definir um protocolo de mensagens (ex: dicionários com chaves "OP" e "V1"), e escrever um bloco `if/elif` no servidor para rotear os comandos.
*   **Com RPyC**: A chamada `conn.root.exposed_sort()` no cliente invoca diretamente o método `exposed_sort` no servidor. A serialização de argumentos, a invocação da função e o retorno do resultado são tratados de forma automática e transparente pela biblioteca, resultando em um código muito mais limpo e focado na lógica da aplicação.````