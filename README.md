 

# 2022-shaved ice project๐จ

DRF๋ฅผ ์ด์ฉํ ์ฌ๋ฆ๋๊ธฐ ๋น์ ์ผํ๋ชฐ ํ๋ก์ ํธ์๋๋ค.

			
			

## ํ๋ก์ ํธ Description

> 1. ํ๋ก์ ํธ๋ช
>
>      :์ธ๋จธ ๋น์ 
>
 >2. ํ๋ก์ ํธ ๊ณ๊ธฐ
 >
>      : **DRF** ๋ฅผ ๊ณต๋ถํ๋ฉฐ ํ๋ก์ ํธ๋ฅผ ๊ณํํ๋ ์ค 6-7์ ๋์ด ์ฌ๋ฆ์ ์ง์  ๊ฐ์ ๋จน๋ ๊ฒ ๋์  ๋ฐฐ๋ฌํด์ ๋จน๋ ๋น์ ๊ตฌ๋งค ์ผํ๋ชฐ์ ๊ตฌ์ํ๊ฒ ๋จ
>
>3. ํ๋ก์ ํธ ์ค๋ช
 >  ์๋น์ค์ฌ์ฉ์: ๋น์ ๊ตฌ๋งค์, ๋น์ ํ๋งค์
  >    - ๊ตฌ๋งค์์ผ๊ฒฝ์ฐ ๋น์ ์กฐํ, ๊ตฌ๋งค
  >    - ํ๋งค์์ผ๊ฒฝ์ฐ ํ๋งคํ  ๋น์๋ฅผ ์กฐํ, ์ถ๊ฐ, ์์ , ์ญ์ ํ๋ฉฐ ๊ด๋ฆฌ
  >    - ํ๋งค์๊ฐ ๊ฒ์ํ ๋ ์ง๋์ ๋น์ ๊ตฌ๋งค๊ฐ๋ฅ
  > Django Rest Framework์ Serializer๋ฅผ ์ฌ์ฉํ ํ๋ก์ ํธ


  
## ๊ธฐ์  ์คํ

 <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=yellow"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/Mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
 <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
 <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
 <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
  <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">


## ๊ตฌํ๊ธฐ๋ฅ

> 1. ๋ก๊ทธ์ธ ๊ธฐ๋ฅ
> 2. ํ์๊ฐ์ ๊ธฐ๋ฅ
> 3. ๋ง์ดํ์ด์ง ๊ธฐ๋ฅ
> 4. ๋น์ ์ํ ๊ธฐ๋ฅ
>    -  ์ ์ฒด ๋น์ ์กฐํ 
>    -  ๋น์ ์ถ๊ฐ 
>    - ์์ธ ๋น์ ์กฐํ 
>    - ๋น์ ์์ 
>    - ๋น์ ์ญ์ 
>5. ๋น์ ๋ฆฌ๋ทฐ ๊ธฐ๋ฅ
>    -  ์ ์ฒด ๋ฆฌ๋ทฐ ์กฐํ
>    -  ๋ฆฌ๋ทฐ ์ถ๊ฐ
>    - ์ํ๋ณ ๋ฆฌ๋ทฐ ํํฐ
>    - ๋ฆฌ๋ทฐ์์ 
>    -  ๋ฆฌ๋ทฐ์ญ์ 
>6. ๋น์ ์ฅ๋ฐ๊ตฌ๋ ๊ธฐ๋ฅ
>    - ์ฅ๋ฐ๊ตฌ๋ ์ถ๊ฐ
>    - ์ฅ๋ฐ๊ตฌ๋ ์์ 
>    - ์ฅ๋ฐ๊ตฌ๋ ์ญ์ 
>7. ๋น์ ๊ตฌ๋งค ๊ธฐ๋ฅ
	

## ๋ชจ๋ธ

User: ์ฌ์ฉ์์ ํ์์ ๋ณด ๋ชจ๋ธ
> id(PK), username, password, email, nickname, created_at, is_active, is_admin, is_seller

UserProfile: ์ฌ์ฉ์์ ์๊ฐ๊ธ
> id(PK), user(FK), introduction

Product
>id(PK), user(FK), product_name, product_img, price, created_at, started_at, ended_at

Review
>id(PK), author(FK), product(FK), contents, grade, created_at, update_check

Cart
>id(PK), user(FK), product(FK), count

## API ์ค๊ณ

