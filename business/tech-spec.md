```markdown
# Technical Specification for dev-vps

## Stack
- **Language**: Go (for backend services)
- **Framework**: Gin (for HTTP server)
- **Runtime**: Docker containers orchestrated by Kubernetes
- **Database**: PostgreSQL (for relational data)
- **Message Queue**: RabbitMQ (for asynchronous task processing)
- **Frontend**: React (for admin dashboard)

## Hosting
- **Free Tier**: AWS Free Tier (t2.micro instances, RDS, etc.)
- **Platforms**:
  - AWS (primary)
  - DigitalOcean (secondary for redundancy)
  - Fly.io (for edge locations)

## Data Model
### Tables/Collections
1. **Users**
   - `user_id` (UUID, primary key)
   - `email` (string, unique)
   - `password_hash` (string)
   - `created_at` (timestamp)
   - `updated_at` (timestamp)

2. **VPSInstances**
   - `instance_id` (UUID, primary key)
   - `user_id` (UUID, foreign key to Users)
   - `instance_name` (string)
   - `instance_type` (string, e.g., "t2.micro")
   - `status` (string, e.g., "running", "stopped")
   - `ip_address` (string)
   - `created_at` (timestamp)
   - `updated_at` (timestamp)

3. **Snapshots**
   - `snapshot_id` (UUID, primary key)
   - `instance_id` (UUID, foreign key to VPSInstances)
   - `snapshot_name` (string)
   - `created_at` (timestamp)

## API Surface
1. **POST /api/users** - Create a new user
2. **POST /api/sessions** - Authenticate a user
3. **GET /api/instances** - List all VPS instances for a user
4. **POST /api/instances** - Create a new VPS instance
5. **GET /api/instances/{instance_id}** - Get details of a specific VPS instance
6. **DELETE /api/instances/{instance_id}** - Delete a VPS instance
7. **POST /api/instances/{instance_id}/start** - Start a VPS instance
8. **POST /api/instances/{instance_id}/stop** - Stop a VPS instance
9. **POST /api/instances/{instance_id}/snapshots** - Create a snapshot of a VPS instance
10. **GET /api/instances/{instance_id}/snapshots** - List all snapshots for a VPS instance

## Security Model
- **Authentication**: JWT (JSON Web Tokens)
- **Secrets**: AWS Secrets Manager for storing sensitive information
- **IAM**: Role-based access control (RBAC) for user permissions
- **Encryption**: TLS for all API endpoints, encryption at rest for sensitive data

## Observability
- **Logs**: ELK Stack (Elasticsearch, Logstash, Kibana) for centralized logging
- **Metrics**: Prometheus for metrics collection and Grafana for visualization
- **Traces**: Jaeger for distributed tracing

## Build/CI
- **CI/CD Pipeline**: GitHub Actions for continuous integration and deployment
- **Testing**: Unit tests with Go's testing framework, integration tests with Postman
- **Deployment**: Kubernetes for orchestration, Helm for package management
- **Monitoring**: New Relic for application performance monitoring (APM)
```