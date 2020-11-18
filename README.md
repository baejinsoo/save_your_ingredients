# Save_your_ingredient

### 프로젝트 개요

- *COVID-19* 상황으로 집에서 요리를 해먹는 빈도수가 많아짐

- 냉장고에서 버려지는 재료를 관리하고, 레시피를 추천해주는 사이트 제작

### 프로젝트 구조

![image-20201118111156069](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201118111156069.png)

- 백엔드와 프론트엔드를 분리한 RESTful API 구조
- Backend
  - Requests, BeautifulSoup를 통한 데이터 크롤링 (만개의 레시피 사이트)
  - Django-RestFramework에 내장된 Serializer를 사용해 api 서버 구축
  - amazon-EC2
- Frontend
  - html, css, JS로 웹 사이트 구축
  - XMLHttpRequest를 통한 post, get 등의 json형식 데이터 활용
  - amazon S3 정적 웹 호스팅