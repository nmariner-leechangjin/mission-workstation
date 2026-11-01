\# Mission Workstation



Docker 기반 Python 실행 환경을 구축하고, GitHub에 프로젝트를 업로드하는 실습 프로젝트입니다.



\## 프로젝트 목표



\- Windows PowerShell 환경에서 개발 워크스테이션 구성

\- Python 및 Git 설치 확인

\- Linux CLI 기본 명령어 실습

\- Docker Desktop 설치 및 실행 확인

\- Dockerfile 작성

\- Python 애플리케이션 Docker 이미지 빌드

\- Docker 컨테이너 실행

\- GitHub 저장소 생성 및 push

\- .gitignore 작성



\## 프로젝트 구조



```text

mission-workstation/

├── app/

│   └── main.py

├── docs/

│   └── screenshots/

├── Dockerfile

├── .gitignore

└── README.md

```



\## 실행 환경



\- OS: Windows

\- Shell: PowerShell

\- Editor: Visual Studio Code

\- Language: Python

\- Container: Docker Desktop

\- Version Control: Git / GitHub



\## Python 실행 파일



`app/main.py`



```python

print("Hello from Docker")

```



\## Dockerfile



```dockerfile

FROM python:3.11-slim



WORKDIR /app



COPY app/ .



CMD \["python", "main.py"]

```



\## Docker 이미지 빌드



```powershell

docker build -t mission-python-app .

```



\## Docker 컨테이너 실행



```powershell

docker run mission-python-app

```



실행 결과:



```text

Hello from Docker

```



\## Git 명령어 기록



```powershell

git init

git add .

git commit -m "Initial commit"

git remote add origin https://github.com/nmariner-leechangjin/mission-workstation.git

git push -u origin main

```



`.gitignore` 추가 후:



```powershell

git add .gitignore

git commit -m "Add gitignore"

git push

```



\## 스크린샷



실습 과정의 주요 화면은 `docs/screenshots/` 폴더에 저장했습니다.



주요 스크린샷:



\- VSCode PowerShell 터미널 실행

\- 프로젝트 폴더 생성

\- Python / Git 버전 확인

\- Linux CLI 명령어 실습

\- Docker 설치 및 버전 확인

\- Dockerfile 작성

\- Docker 이미지 빌드 성공

\- Docker 컨테이너 실행 성공

\- Git 초기화 및 GitHub push 성공



\## GitHub Repository



https://github.com/nmariner-leechangjin/mission-workstation

---

## 실행 환경

| 항목 | 내용 |
|---|---|
| OS | Windows |
| 터미널 | PowerShell / VSCode Terminal |
| Docker | `docker --version` 결과 작성 |
| Git | `git --version` 결과 작성 |
| Python | `python --version` 결과 작성 |

---

## 수행 항목 체크리스트

| 항목 | 완료 여부 | 확인 방법 |
|---|---|---|
| 터미널 작업 환경 구성 | 완료 | VSCode 터미널 실행 |
| 권한/경로 확인 | 완료 | `pwd`, `ls` |
| Docker 설치 확인 | 완료 | `docker --version`, `docker info` |
| Dockerfile 작성 | 완료 | `Dockerfile` 파일 확인 |
| 이미지 빌드 | 완료 | `docker build` |
| 컨테이너 실행 | 완료 | `docker run` |
| Git 저장소 초기화 | 완료 | `git init`, GitHub push |
| GitHub 연동 | 완료 | 원격 저장소 확인 |

---

## 검증 방법 및 결과

### 1. Python 등 확인

```powershell
python --version
Python 3.13.15
git --version
git version 2.55.0.windows.4
PS C:\Codyssey\mission-workstation> docker --version
Docker version 29.9.2, build a82e528
PS C:\Codyssey\mission-workstation> docker info     
Client:
 Version:    29.9.2
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  agent: Docker AI Agent Runner (Docker Inc.)
    Version:  v1.152.0
    Path:     C:\Users\somed\.docker\cli-plugins\docker-agent.exe
  ai: Docker AI Agent - Ask Gordon (Docker Inc.)
    Version:  v1.33.0
    Path:     C:\Users\somed\.docker\cli-plugins\docker-ai.exe
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.38.1
    Path:     C:\Users\somed\.docker\cli-plugins\docker-buildx.exe
  compose: Docker Compose (Docker Inc.)
    Version:  v5.6.1
    Path:     C:\Users\somed\.docker\cli-plugins\docker-compose.exe
  debug: Get a shell into any image or container (Docker Inc.)
    Version:  0.49.0
    Path:     C:\Users\somed\.docker\cli-plugins\docker-debug.exe
  desktop: Docker Desktop commands (Docker Inc.)
    Version:  4.97.0
    Path:     C:\Users\somed\.docker\cli-plugins\docker-desktop.exe
  dhi: CLI for managing Docker Hardened Images (Docker Inc.)
    Version:  v0.0.9
    Path:     C:\Users\somed\.docker\cli-plugins\docker-dhi.exe
  extension: Manages Docker extensions (Docker Inc.)
    Version:  v0.2.32
    Path:     C:\Users\somed\.docker\cli-plugins\docker-extension.exe
  init: Creates Docker-related starter files for your project (Docker Inc.)
    Version:  v1.4.1
    Path:     C:\Users\somed\.docker\cli-plugins\docker-init.exe
  mcp: Docker MCP Plugin (Docker Inc.)
    Version:  v0.44.2
    Path:     C:\Users\somed\.docker\cli-plugins\docker-mcp.exe
  model: Docker Model Runner (Docker Inc.)
    Version:  v1.2.9
    Path:     C:\Users\somed\.docker\cli-plugins\docker-model.exe
  offload: Docker Offload (Docker Inc.)
    Version:  v0.7.21
    Path:     C:\Users\somed\.docker\cli-plugins\docker-offload.exe
  pass: Docker Pass Secrets Manager Plugin (beta) (Docker Inc.)
    Version:  v0.3.2
    Path:     C:\Users\somed\.docker\cli-plugins\docker-pass.exe
  sandbox: "docker sandbox" is deprecated, use Docker Sandboxes instead (Docker Inc.)
    Version:  v0.13.0
    Path:     C:\Users\somed\.docker\cli-plugins\docker-sandbox.exe
  scout: Docker Scout (Docker Inc.)
    Version:  v1.27.0
    Path:     C:\Users\somed\.docker\cli-plugins\docker-scout.exe

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 1
 Server Version: 29.9.2
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: local
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Discovered Devices:
  cdi: docker.com/gpu=webgpu
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 nvidia runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: b7a25261e029d68978bbf290df0a62fc819b3c51
 runc version: v1.5.2-0-g29dd3dc2
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.18.54.1-microsoft-standard-WSL2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
 CPUs: 8
 Total Memory: 3.685GiB
 Name: docker-desktop
 ID: c797d5c3-af8c-41d8-b1c2-c89e388ad3a8
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 HTTP Proxy: http.docker.internal:3128
 HTTPS Proxy: http.docker.internal:3128
 No Proxy: hubproxy.docker.internal
 Labels:
  com.docker.desktop.address=npipe://\\.\pipe\docker_cli
 Experimental: false
 Insecure Registries:
  hubproxy.docker.internal:5555
  127.0.0.0/8
  ::1/128
 Live Restore Enabled: false
 Firewall Backend: iptables
 ![docker-version](docs/screenshots/docs/screenshots/06_docker-version.png)