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

