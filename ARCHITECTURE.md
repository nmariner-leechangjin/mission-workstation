# Mission Workstation 구조

## 구성과 책임

- `app/main.py`: Python 표준 라이브러리 HTTP 서버. `/`에서 메시지와 방문 횟수를 표시하고 `/health`로 상태를 확인한다.
- `content/message.txt`: 기본 메시지. 호스트 파일을 `/app/content/message.txt`에 바인드 마운트하여 변경 반영을 실습한다.
- `/data/visits.txt`: 방문 횟수 파일. Docker named volume을 `/data`에 연결하여 컨테이너 교체 후 보존을 확인한다.
- `Dockerfile`: 기존 `python:3.11-slim` 이미지를 기반으로 소스와 기본 콘텐츠를 복사하고 포트·환경 변수·헬스체크를 정의한다.
- `compose.yaml`: `web`과 `monitor` 서비스를 같은 Compose 네트워크에서 실행한다. `monitor`는 서비스 이름 `web`으로 `/health`를 호출한다.
- `app/monitor.py`: Compose 내부 네트워크 통신을 주기적으로 확인하는 보조 서비스다.
- `README.md`: 명령과 실제 결과 및 제출 증거의 진입점이다.

새 서비스를 추가할 때는 실행 코드와 보조 모듈을 `app/`, 기본 콘텐츠를 `content/`, Compose 설정을 루트의 `compose.yaml`, 실행 증거를 `docs/` 아래에 둔다. 서비스 간 통신은 Compose 서비스 이름을 사용하고, 인증 정보와 운영 데이터는 저장소 구조에 포함하지 않는다.

## 데이터 흐름

브라우저 또는 `curl` → 호스트 포트 `18080` → 포트 포워딩/NAT → 컨테이너 네트워크 네임스페이스의 포트 `8000` → Python HTTP 서버 → 메시지 파일 읽기 및 방문 횟수 파일 갱신 → HTML 응답. 컨테이너는 별도 네트워크 네임스페이스를 가지므로 호스트 브라우저가 접근하려면 `-p`로 포트를 publish해야 한다.

## 경계

GitHub에는 소스와 증거만 저장한다. 볼륨 데이터와 인증 정보는 저장하지 않는다. Docker Desktop은 로컬 Linux 컨테이너 엔진을 제공한다.
