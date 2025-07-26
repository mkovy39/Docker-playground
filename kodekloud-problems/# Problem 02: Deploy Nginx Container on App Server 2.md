## Problem Statement

The Nautilus DevOps team requires a Docker container deployment for testing purposes on **Application Server 2**.  
Create a container named **nginx_2** using the **nginx** image with the **alpine** tag. Ensure the container is in a **running** state.

---

## Solution

Run the following command to create and start the container:

```bash
docker run -d --name=nginx_2 nginx:alpine
````

* `-d` runs the container in detached mode.
* `--name=nginx_2` names the container `nginx_2`.
* `nginx:alpine` uses the `nginx` image with the `alpine` tag.

---

## Verification

Verify the container is running:

```bash
docker ps
```

Expected Output:

```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
abcd1234efgh   nginx:alpine   "/docker-entrypoint.…"   X seconds ago    Up X seconds              nginx_2
```

---

**nginx\_2** container using the **nginx\:alpine** image is successfully running on **Application Server 2**.
