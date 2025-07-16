![NexusTop Architecture](docs/architecture/Security_Architecture.png)  

## 🚀 Instant Mobile Data & Airtime Platform  
**NexusTop** is a high-performance Django/React platform enabling instant purchases of mobile data and airtime through unified telecom API integrations.  

```mermaid  
graph LR  
    A[User] --> B[React Frontend]  
    B --> C[Django REST API]  
    C --> D[MTN/Airtel/9mobile APIs]  
    C --> E[Celery Async Tasks]  
    E --> F[Redis Queue]  
    C --> G[PostgreSQL]  
```  

## ✨ Key Features  
- ⚡ **0.5s Transaction Processing** with Celery workers  
- 🔒 **PCI-DSS Compliant Security** with JWT encryption  
- 🌐 **Unified API Gateway** for 10+ telecom providers  
- 📊 **Real-time Analytics Dashboard** for admins  
- 💳 **Wallet System** with Flutterwave/Paystack integration  

## 🛠 Technology Stack  
| **Layer**       | **Technology**                              |  
|-----------------|---------------------------------------------|  
| **Frontend**    | React 18, Vite, Tailwind CSS, Axios         |  
| **Backend**     | Django 4.2, Django REST Framework, Celery   |  
| **Database**    | PostgreSQL 15, Redis 7                      |  
| **Infra**       | AWS ECS, RDS, CloudFront, S3, CloudFormation|  
| **Monitoring**  | Sentry, Grafana, Prometheus                 |  
| **CI/CD**       | GitHub Actions, Docker                      |  

## 📂 Repository Structure  
```  
nexustop/  
├── backend/                  # Django project  
│   ├── config/               # Django settings  
│   ├── users/                # Auth app (JWT/OTP)  
│   ├── wallet/               # Transactions & balances  
│   ├── services/             # Provider adapters (MTN/Airtel)  
│   ├── manage.py  
│   └── requirements.txt  
├── frontend/                 # React SPA  
│   ├── public/  
│   ├── src/  
│   │   ├── components/       # UI components  
│   │   ├── pages/            # NextJS-style routing  
│   │   ├── services/         # API clients  
│   │   └── App.jsx  
│   └── vite.config.js  
├── infra/                    # AWS CloudFormation templates  
├── docs/                     # Architecture diagrams  
├── scripts/                  # Deployment utilities  
└── .github/workflows/        # CI/CD pipelines  
```  

## 🚀 Installation  

### Prerequisites  
- Python 3.10+  
- Node.js 18+  
- PostgreSQL 15  
- Redis 7  


## ⚙️ Configuration  
### Critical Environment Variables  
```ini  
# backend/.env  
DJANGO_SECRET_KEY=your_secret_key  
DB_URL=postgres://user:pass@localhost:5432/nexustop  
REDIS_URL=redis://localhost:6379/0  
MTN_API_KEY=your_mtn_key  
FLUTTERWAVE_SECRET_KEY=your_flw_key  

# frontend/.env  
VITE_API_BASE_URL=http://localhost:8000  
VITE_SENTRY_DSN=https://example@sentry.io/1  

## 🚦 Deployment  
### AWS ECS Deployment Workflow  
```mermaid  
graph LR  
    A[Git Push] --> B[GitHub Actions]  
    B --> C[Build Docker Images]  
    B --> D[Run Test Suite]  
    D --> E[Push to ECR]  
    E --> F[Update ECS Task]  
    F --> G[Blue-Green Deployment]  
```  


## 📚 API Documentation  

### Key Endpoints  
| **Endpoint**         | **Method** | **Description**                |  
|----------------------|------------|--------------------------------|  
| `POST /api/auth/otp` | POST       | Request login OTP              |  
| `GET /api/wallet`    | GET        | Get user wallet balance        |  
| `POST /api/purchase` | POST       | Initiate data/airtime purchase |  

[View Full API Spec](docs/API_REFERENCE.md)  



## 🛡️ Security  
```mermaid  
graph TB  
    A[User] -->|HTTPS| B[CloudFront]  
    B -->|WAF Rules| C[ALB]  
    C -->|JWT Auth| D[Django]  
    D -->|TLS| E[RDS]  
    D -->|Vault| F[Provider APIs]  
```  

### Security Practices:  
- 🔑 **Secrets Management**: AWS Secrets Manager  
- 🔐 **Encryption**: AES-256 for sensitive DB fields  
- 🛡️ **Web Application Firewall**: AWS WAF with OWASP rules  
- 📝 **Audit Logging**: CloudTrail + S3 access logs  

**© 2025 NexusTop | AWS Advanced Technology Partner**