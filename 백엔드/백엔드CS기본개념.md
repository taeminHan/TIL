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


## URI
