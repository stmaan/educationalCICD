# 🚀 Educational CI/CD Pipeline
### Flask + Docker + Kubernetes (Kind) + GitHub Actions

Этот проект — полноценный автоматизированный конвейер (Pipeline), реализующий современные практики DevOps: тестирование, контейнеризацию и оркестрацию.

---

## 🏗 Архитектура проекта
*   **App:** Python Flask веб-сервер.
*   **CI/CD:** GitHub Actions с использованием **Self-hosted Runner** на локальном сервере.
*   **Registry:** Docker Hub.
*   **Orchestration:** Kubernetes (Kind) с разделением на среды **Staging** и **Production**.
*   **Notifications:** Интеграция с Bitrix24 через Email-уведомления.

---

## 📂 Структура файлов

| Файл | Описание |
| :--- | :--- |
| `app.py` | Веб-приложение с поддержкой динамических окружений (ConfigMap) |
| `Dockerfile` | Многослойная сборка образа с установкой зависимостей |
| `k8s-deployment.yml` | Универсальный манифест развертывания (Replicas: 2) |
| `k8s-service.yml` | Сетевой доступ внутри кластера (NodePort) |
| `sa.yaml` | Настройка RBAC (ServiceAccount, ClusterRoleBinding) |
| `kind-ci-config` | Kubeconfig для доступа Runner-а в кластер |
| `.github/workflows/ci.yml` | Логика пайплайна: Тесты -> Build -> Push -> Approval -> Deploy |

---

## 🛠 Реализованные возможности

1.  **Multi-Environment**: Разделение на namespaces `staging` и `production`.
2.  **Manual Approval**: Деплой в Production требует ручного подтверждения в GitHub Actions.
3.  **Dynamic Configs**: Использование ConfigMaps для изменения заголовков сайта без пересборки образа.
4.  **Notifications**: Уведомления в Bitrix24 со ссылками на конкретный запуск пайплайна.
5.  **Self-hosted Runner**: Использование собственного сервера в качестве вычислительного узла CI/CD.

---

## 🚦 Использование

### Доступ к окружениям (через SSH туннель):
*   **Staging:** `http://localhost:8586`
*   **Production:** `http://localhost:8585`

### Команды для проверки:
```bash
# Просмотр подов во всех окружениях
kubectl get pods -A -l app=educational-app

# Ручной откат версии (Rollback)
kubectl rollout undo deployment/educational-app -n production
```

---

## 👨‍💻 Автор
**stmaan** — DevOps Engineering Student
