
## Problem Statement

Install Docker-CE and Docker Compose on **App Server 3**, which runs **CentOS**.

---

## Solution

### Step 1: Check Linux Version

```bash
cat /etc/os-release
````

Expected Output:

```
CentOS Linux
```

---

### Step 2: Install Docker-CE on CentOS

Followed the [official Docker documentation for CentOS](https://docs.docker.com/engine/install/centos/#installation-methods).

**Commands:**

```bash
# Remove old versions (if any)
sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine

# Set up the repository
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Install Docker Engine
sudo yum install docker-ce docker-ce-cli containerd.io

# Start Docker
sudo systemctl start docker

# Enable Docker at boot
sudo systemctl enable docker
```

---

### Step 3: Install Docker Compose

```bash
# Download Docker Compose binary (replace version if necessary)
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions
sudo chmod +x /usr/local/bin/docker-compose

# Check Docker Compose version
docker-compose --version
```

---

## Verification

### 1️⃣ Check Docker Version

```bash
docker --version
```

### 2️⃣ Run Docker Test

```bash
sudo docker run hello-world
```

Expected Output:

```
Hello from Docker! This message shows that your installation appears to be working correctly.
```

### 3️⃣ Check Docker Compose Version

```bash
docker-compose --version
```

---

Docker-CE and Docker Compose installation on App Server 3 is complete and verified.
