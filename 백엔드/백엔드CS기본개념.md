# 백엔드 기본 개념

## REST

REST(Representational State Transfer)
자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.

- 자원의 표현에 의한 상태 전달

    - 자원: 해당 소프트웨어가 관리하는 모든 것 ex) 문서, 그림, 데이터, 소프트웨어

    - 자원의 표현: 자원을 표현하기 위한 이름 ex) DB의 학생 정보가 자원일 때, 'students'를 자원의 표현으로 정함.

- 상태 전달
    - 데이터가 요청되어지는 시점에서 자원의 상태(정보)를 전달한다.
    - JSON 혹은 XML 등을 통해 데이터를 주고 받는 것이 일반적

- 장점
    - HTTP 프로토콜의 인프라를 그래도 사용하므로 REST API 사용을 위한 별도의 인프라 구축이 필요 없음
- 단점
    - 표준이 존재하지 않음
    - 사용할 수 있는 메소드가 4가지 밖에 없다.
        - GET
        - POST
        - PUT
        - DELETE

## HTTP

HTTP(HyperText Transfer Protocol)

W3 상에서 정보를 주고 받을 수 있는 프로토콜(프로토콜이란 상호 간에 정의한 규칙)이다.

- 특징
    - Stateless Protocol 데이터를 주고 받기 위한 각각의 데이터 요청이 서로 독립적으로 관리된다.

    - 데이터를 주고 받는 행위를 Request, Response 라 한다.

    - 보통 TCP/IP 통신 위에서 동작, 기본 포트는 80.
- 메소드
    - **GET**
    - **POST**
    - **PUT**
    - **DELETE**
    - PATCH
    - HEAD
    - OPTIONS
    - ...여러가지가 있지만 GET, POST, PUT, DELETE만 알아두자


## WEB, WAS

### Web Server

- Web Server 개념
    - 소프트웨어와 하드웨어로 구분
        - 하드웨어
            - Web 서버가 설치되어 있는 컴퓨터
        - 소프트웨어
            - 웹 브라우저 클라이언트로부터 HTTP 요청을 받아 정적인 컨텐츠(.html, jpeg, .css 등)를 제공하는 컴퓨터 프로그램

- Web Server 기능
    - HTTP 프로토콜을 기반으로 하여 클라이언트(웹 브라우저 또는 웹 크롤러)의 요청을 서비스하는 기능을 담당한다.
    1) 기능1
        - 정적인 컨턴츠 제공
        - WAS를 거치지 않고 바로 자원을 제공
    2) 기능2
        - 동적인 컨텐츠 제공을 위한 요청 전달
        - 클라이언트의 요청(Request)을 WAS에 보내고, WAS가 처리한 결과를 클라이언트에게 전달(응답, Response)한다.
- Web Server
    - Apache Server, Nginx, IIS




### WAS (Web Application Server)

웹서버 + 웹 컨테이너

- WAS 개념
    - DB 조회나 다양한 로직 처리를 요구하는 **동적인 컨텐츠**를 제공하기 위해 만들어진 Application Server
    - HTTP를 통해 컴퓨터나 장치에 애플리케이션을 수행해주는 미들웨어(소프트웨어 엔진)이다.
- WAS 주요 기능
    - 프로그램 실행 환경과 DB 접속 기능 제공
    - 여러 개의 트랜잭션 관리 기능
    - 업무를 처리하는 비즈니스 로직 수핵
- WAS
    - Tomcat, JBoss