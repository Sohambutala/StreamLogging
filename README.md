# Dockerized ELK Stack with Kafka Integration
This repository contains a Docker Compose setup to run an integrated Elastic (Elasticsearch, Logstash, Kibana, Beats) stack with Apache Kafka, including Zookeeper, Schema Registry, and Confluent Control Center, enhanced with Metricbeat for monitoring. This setup is ideal for development, testing, and small-scale production environments for real-time log analysis and visualization.

## Features
1. `Elasticsearch` for powerful search and data analytics
2. `Logstash` for log processing and ingestion into Elasticsearch
3. `Kibana` for data visualization with dashboards and analytics
4. `Apache Kafka` with `Zookeeper` for reliable log streaming
5. `Schema Registry` for managing Kafka data schemas
6. `Confluent Control Center` for Kafka cluster management and monitoring
7. `Metricbeat` for monitoring system metrics and Docker containers

## Prerequisites
Docker and Docker Compose installed on your machine
Basic understanding of Docker, ELK Stack, and Apache Kafka

## Quick Start
1. Clone the Repository
```bash
Copy code
git clone https://github.com/Sohambutala/StreamLogging.git
cd StreamLogging
```
2. Start the Services
```bash
Copy code
docker-compose up -d
This command starts all the services defined in the docker-compose.yml file in detached mode.
```

3. Access the Services
- Kibana: Open `http://localhost:5601` to access Kibana's web interface.
- Confluent Control Center: Visit `http://localhost:9021` to manage and monitor your Kafka cluster.
- Elasticsearch: Accessible at `http://localhost:9200`.

4. Monitor with Metricbeat
Metricbeat is configured to collect metrics from Docker containers and the host system. Check the Metricbeat dashboards in Kibana for insights.

## Configuration
You can customize the configurations for each service by modifying their respective configuration files in the repository:

Elasticsearch: `./elasticsearch/elasticsearch.yml`
Logstash: `./logstash/config/logstash.yml` and the pipeline files in `./logstash/pipeline/`
Kibana: `./kibana/kibana.yml`
Metricbeat: `./metricbeat/metricbeat.yml`

## Stopping the Services
To stop all services and remove containers, networks, and volumes created by docker-compose up, run:
```bash
Copy code
docker-compose down -v
```
## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to improve the project.

## License
This project is licensed under the `MIT License` - see the file for details.
