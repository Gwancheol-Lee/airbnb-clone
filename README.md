# Airbnb Clone

노마드코더 에어비엔비 Cloning with Python, Django, Tailwind 등등 ... 💻👀❤

## D+1 Python3 버블(가상환경) 세팅 및 Django 설치 후 프로젝트 생성

### Python3 버블(가상환경) 세팅 (python3 설치 및 환경설정 필수)

#### Pipenv 설치 (package.json이 있는 npm)

```bash
$ pip install --user pipenv # For Windows
$ brew upgrade pipenv # For MacOs or Linux
$ pipenv # pipenv 설치완료 확인
```

#### 프로젝트 생성 후 이동

```bash
$ mkdir airbnb-clone
$ cd airbnb-clone
```

#### pipenv 사용하여 python3 가상환경 생성

```bash
$ pipenv --three
```

#### 해당 버블(가상환경) 안으로 이동

```bash
$ pipenv shell
```

#### 버블 안에서 장고 설치

```bash
$ pipenv install Django==2.2.5 # 2.2.5 버전으로 설치
$ django-admin # 장고 해당 버블 설치완료 확인
$ which django-admin # django-admin 경로
```

### Django 프로젝트 생성

#### 가상환경 안에서 config 프로젝트 생성

```bash
$ pipenv shell
$ django-admin startproject config
```

#### config 안에 있는 디렉토리를 최상위 경로로 이동

#### Python VSCode Extension 설치

#### VSCode 우측 하단 Python 버전 선택

#### 인터프리터 선택 화면에서 PipEnv 버전으로 선택

#### Pylint VSCode Extension 설치

#### F1 눌러서 Python: Select Linter → flake8 → 미설치시 flake8설치(pipenv install flake8 --dev)

#### .vscode > settins.json 세팅

```bash
$ pipenv shell # 가상환경 내부 접근
$ python -c "import os, sys; print(os.path.dirname(sys.executable))" # python 경로 2번라인
```

```json
{
  "python.defaultInterpreterPath": "python -c 명령어로 확인된 python 경로",
  "python.linting.flake8Enabled": true
}
```

## D+2 Lint, Formatter 세팅 + Django 서버 실행 및 관리자 계정 생성

### Lint, Formatter 세팅

#### PyLint 및 BlackFormatter 설치

```bash
$ pipenv install pylint --dev # pylint 설치
$ pipenv install black --dev --pre # formatter black 설치
```

### Django 서버 실행 및 관리자 계정 생성

#### Django 서버 실행

```bash
$ pipenv shell # 버블 안으로 이동
$ python manage.py runserver # django 서버 실행
```

#### Django 서버 종료 후 migration 진행

```bash
$ python manage.py migrate # django migration
$ python manage.py runserver # django 서버 실행
```

##### http://127.0.0.1:8000/admin 접근 시 관리자 패널 확인 가능

#### 슈퍼어드민 계정 생성

```bash
$ python manage.py createsuperuser # create superuser
```

#### 서버 실행 후 관리자 패널 로그인

```bash
$ python manage.py runserver # django 서버 실행
```

#### 현재 유저 목록 조회 가능. 기본적인 CRUD 제공.
