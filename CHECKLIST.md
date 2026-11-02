# 제출 체크리스트

상태: `VERIFIED`는 명령 출력이나 화면으로 확인한 항목, `IMPLEMENTED`는 작성했지만 실행 검증 전인 항목, `TODO`는 아직 진행하지 않은 항목이다.

| 번호 | 항목 | 상태 | 증거 위치 |
|---|---|---|---|
| 1 | 공개 제출 저장소 | VERIFIED | GitHub 저장소 링크, README |
| 2 | 기술 문서 | IMPLEMENTED | README |
| 3 | 터미널 조작 로그 | VERIFIED | README |
| 4 | 권한 전후 비교 | VERIFIED | README |
| 5 | Docker 설치 및 점검 | VERIFIED | README 및 기존 스크린샷 |
| 6 | Docker 운영 명령 | VERIFIED | README |
| 7 | hello-world 및 Ubuntu | VERIFIED | README |
| 8 | 커스텀 웹 서버 이미지 | VERIFIED | Dockerfile, app/main.py, README |
| 9 | 포트 매핑 HTTP 접속과 브라우저 화면 | VERIFIED | README, docs/screenshots/15-web-port-mapping.png |
| 10 | 바인드 마운트 반영 | VERIFIED | README |
| 11 | 볼륨 영속성 | VERIFIED | README |
| 12 | Git 설정 및 VS Code/GitHub 연동 | VERIFIED | README, docs/screenshots/16-vscode-github-account.jpg |
| 13 | 보안 검토 | VERIFIED | README, .gitignore, .dockerignore, 스크린샷 육안 검토 |
| 보너스 | Compose 단일·다중 서비스, 운영 명령, 환경 변수 | VERIFIED | README, compose.yaml, app/monitor.py |
| 보너스 | GitHub SSH 키 생성·등록 | VERIFIED | README; GitHub 계정 화면, 로컬 키 파일 |
| 보너스 | GitHub SSH 인증 | VERIFIED | README; 사용자 실행 결과 |
| 보너스 | SSH 원격 전환·push | VERIFIED | README; 사용자 `git push origin main` 결과 `Everything up-to-date` |
