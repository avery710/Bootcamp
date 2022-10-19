# WEEK-5 - MySQL

### 要求三：SQL CRUD 
### 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令

* 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。 <br>
![Markdown Logo](/week-5/screenshot/3-1.png)

* 使用 SELECT 指令取得所有在 member 資料表中的會員資料。![Markdown Logo](/week-5//screenshot/3-2.png)

* 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。![Markdown Logo](/week-5//screenshot/3-3.png)

* 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )![Markdown Logo](/week-5//screenshot/3-4.png)

* 使用 SELECT 指令取得欄位 username 是 test 的會員資料。![Markdown Logo](/week-5//screenshot/3-5.png)

* 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。![Markdown Logo](/week-5//screenshot/3-6.png)

* 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。 ![Markdown Logo](/week-5//screenshot/3-7-1.png)![Markdown Logo](/week-5//screenshot/3-7-2.png)

<br>

### 要求四：SQL CRUD 
### 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令

* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。![Markdown Logo](/week-5//screenshot/4-1.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。![Markdown Logo](/week-5//screenshot/4-2.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。![Markdown Logo](/week-5//screenshot/4-3.png) 

<br>

### 要求五：SQL JOIN (Optional)

* 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。![Markdown Logo](/week-5//screenshot/5-1.png)

* 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。![Markdown Logo](/week-5//screenshot/5-2.png)

* 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。 ![Markdown Logo](/week-5//screenshot/5-3.png) 
