# Papers

### 💡 배경
HuggingFace에서 운영하는 Daily Paper에서는 매일 새로운 기술에 관련한 paper를 소개하지만,
10개 이상 paper의 모든 내용을 매일 확인하기에는 어려움<br><br>

### ✨ 서비스
그래서, Daily Paper의 초록(Abstract)을 **한 줄로 요약하고 한글로 번역해** 메일로 전송하는 서비스<br>
📅 **기간** : 평일 (월요일-금요일) <br>
⏰ **시간** : 한국 시간(KST) 기준 매일 오전 10시<br>

##### ⚙️ 주요 기능
- 논문 크롤링 자동화 : [HuggingFace Daily Paper](https://huggingface.co/papers) 에서 최신 논문 자동 수집
- LLM 요약 및 번역 : 논문 초록을 간결하고 자연스러운 한국어로 요약 및 번역
- 이메일 알림 : 요약된 논문을 이메일 주소로 편리하게 제공
- 간편한 배포 및 관리 : GitHub Action의 스케줄링으로 별도의 서버 관리없이 자동 실행<br>

##### 🔄 전체 워크플로우
<img width="581" height="61" alt="제목 없는 다이어그램 drawio" src="https://github.com/user-attachments/assets/007cfad0-48f6-4528-9ab8-585294c01e2c" />
<br><br>

### 개발 스택
- 🐍**언어** : Python
- 🤖**모델** : Qwen/Qwen3-1.7B
- ⏱️**스케줄링** : Git Hub Action
