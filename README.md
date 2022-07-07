 

# 2022-shaved ice project🍨

DRF를 이용한 여름나기 빙수 쇼핑몰 프로젝트입니다.

			
			

## 프로젝트 Description

> 1. 프로젝트명
>
>      :썸머 빙수 
>
 >2. 프로젝트 계기
 >
>      : **DRF** 를 공부하며 프로젝트를 계획하던 중 6-7월 더운 여름에 직접 가서 먹는 것 대신 배달해서 먹는 빙수 구매 쇼핑몰을 구상하게 됨
>
>3. 프로젝트 설명
 >  서비스사용자: 빙수 구매자, 빙수 판매자
  >    - 구매자일경우 빙수 조회, 구매
  >    - 판매자일경우 판매할 빙수를 조회, 추가, 수정, 삭제하며 관리
  >    - 판매자가 게시한 날짜동안 빙수 구매가능

> 
  
## 기술 스택

 <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=yellow"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/Mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
 <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
 <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
 <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
  <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">


## 구현기능

> 1. 로그인 기능
> 2. 회원가입 기능
> 3. 마이페이지 기능
> 4. 빙수 상품 기능
>    -  전체 빙수 조회 
>    -  빙수 추가 
>    - 상세 빙수 조회 
>    - 빙수 수정
>    - 빙수 삭제
>5. 빙수 리뷰 기능
>    -  전체 리뷰 조회
>    -  리뷰 추가
>    - 상품별 리뷰 필터
>    - 리뷰수정
>    -  리뷰삭제
>6. 빙수 장바구니 기능
>    - 장바구니 추가
>    - 장바구니 수정
>    - 장바구니 삭제
>7. 빙수 구매 기능
	

## 모델

User: 사용자의 회원정보 모델
> id(PK), username, password, email, nickname, created_at, is_active, is_admin, is_seller

UserProfile: 사용자의 소개글
> id(PK), user(FK), introduction

Product
>id(PK), user(FK), product_name, product_img, price, created_at, started_at, ended_at

Review
>id(PK), author(FK), product(FK), contents, grade, created_at, update_check

Cart
>id(PK), user(FK), product(FK), count
