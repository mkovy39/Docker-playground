## 📝 Problem Statement

Delete the Docker container named **kke-container** on **App Server 3** in Stratos DC.  
This container was created for testing purposes by the Nautilus project developers and is no longer required.

---

## 🔧 Solution

### Step 1: List Running Containers

```bash
docker ps
````

### Step 2: Stop the Container

```bash
docker stop kke-container
```

### Step 3: List All Containers (Stopped and Running)

```bash
docker ps -a
```

### Step 4: Remove the Container

```bash
docker rm kke-container
```

(Optional) Clean up images if necessary:

```bash
docker images
docker rmi <image-name>
```

---

## ✅ Verification

Check that the container is deleted and no longer listed:

```bash
docker ps -a
```

Expected: **kke-container** should not appear in the output.

---

✅ **kke-container** has been successfully deleted from **App Server 3**.

```
