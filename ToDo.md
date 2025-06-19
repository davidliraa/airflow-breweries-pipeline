# TODO - Projeto Pipeline Airflow Breweries

## Melhorias e Funcionalidades Futuras

### Geral
- [ ] Versionar o projeto com Git (se ainda não estiver feito).
- [ ] Automatizar deploy da stack com Docker Compose em ambiente de produção.
- [ ] Configurar monitoramento e alertas para falhas nas DAGs.

### Pipeline
- [ ] Validar os dados recebidos na camada Bronze (schema e qualidade).
- [ ] Adicionar testes unitários e de integração para as funções Python das DAGs.
- [ ] Implementar retries e alertas personalizados para falhas nas tasks.
- [ ] Documentar variáveis e conexões usadas, criar `.env` seguro para produção.
- [ ] Ajustar DAGs para rodar com `schedule_interval` conforme frequência desejada.
- [ ] Melhorar tratamento de erros na ingestão e transformação dos dados.

### Armazenamento e Orquestração
- [ ] Implementar versionamento dos dados armazenados (ex: data lakes com particionamento).
- [ ] Avaliar migração para banco de dados (ex: BigQuery, Redshift) para camada Gold.
- [ ] Criar dashboards para visualização dos dados agregados (ex: com Superset, Metabase).

### Segurança
- [ ] Configurar autenticação e autorização no Airflow.
- [ ] Proteger secrets e credenciais via Airflow Secrets Backend.

### Outros
- [ ] Automatizar limpeza de arquivos antigos na camada Bronze/Silver/Gold.
- [ ] Melhorar documentação do projeto, incluindo diagramas de arquitetura.
