# private_lesson

### 1 - 1 로컬 환경에서 테스트 하는방법
make install - <패키지 의존성 설치해줌>

brew install direnv

-- 버전확인 -- <br>
direnv version

---
<h5> BASH -> ~/.bashrc에 아래 내용 추가 </h5>
eval "$(direnv hook bash)"

---
<h5> ZSH -> ~/.zshrc에 아래 내용 추가 </h5>
eval "$(direnv hook zsh)"

---
direnv allow

make run - <장고 프로젝트 실행>