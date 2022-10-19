```
CREATE TABLE member(id BIGINT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255) NOT NULL,username  VARCHAR(255) NOT NULL,password  VARCHAR(255) NOT NULL,follower_count INT UNSIGNED NOT NULL DEFAULT 0,time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
INSERT INTO member(id,name,username,password,follower_count) VALUES(1,'小一','test','test',1);
INSERT INTO member(id,name,username,password,follower_count) VALUES(2,'小二','two','two',2);
INSERT INTO member(id,name,username,password,follower_count) VALUES(3,'小三','three','three',3);
INSERT INTO member(id,name,username,password,follower_count) VALUES(4,'小四','four','four',4);
INSERT INTO member(id,name,username,password,follower_count) VALUES(5,'小五','five','fieve',5);
SELECT * FROM member;
```
![image](https://user-images.githubusercontent.com/113079404/196691586-253b1fab-f035-4828-9e1e-04ae84a3cb87.png)

```
SELECT * FROM member ORDER BY time DESC;
```
![image](https://user-images.githubusercontent.com/113079404/196691754-7281f67b-f18e-4def-909a-30c13999399c.png)

```
SELECT * FROM member ORDER BY time DESC LIMIT 1,3;
```
![image](https://user-images.githubusercontent.com/113079404/196691882-8433531a-1dd2-4ccc-b5ee-d3fae00f0e1b.png)

```
SELECT * FROM member WHERE username='test';
```
![image](https://user-images.githubusercontent.com/113079404/196691995-2fd5db76-e2ad-4bd8-b8dd-1b3488888f6d.png)

```
SELECT * FROM member WHERE username='test' and password='test';
```
![image](https://user-images.githubusercontent.com/113079404/196692097-fc1d3e20-b1b5-4987-99b3-35f51fc7ae89.png)

```
UPDATE member SET name='test2' WHERE username='test';
SELECT * FROM member;
```
![image](https://user-images.githubusercontent.com/113079404/196692330-6e7abf51-e7a5-4bd6-874a-5062b2614460.png)

```
SELECT COUNT( * ) AS 總共幾筆資料 FROM member;
```
![image](https://user-images.githubusercontent.com/113079404/196692542-432b62d3-6888-457b-bf28-8e0b5ff26a43.png)

```
SELECT SUM(follower_count) AS 總和 FROM member;
```
![image](https://user-images.githubusercontent.com/113079404/196693342-b06877b5-2bf9-413d-83be-847cffdf8a26.png)

```
SELECT AVG(follower_count) AS 平均數 FROM member;
```
![image](https://user-images.githubusercontent.com/113079404/196693585-7e8f2255-124e-409b-b924-ecbf45490d58.png)

```
CREATE TABLE message(id BIGINT PRIMARY KEY AUTO_INCREMENT,member_id BIGINT NOT NULL,content  VARCHAR(255) NOT NULL,like_count INT UNSIGNED NOT NULL DEFAULT 0 ,time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);

INSERT INTO member(member_id,content,like_count) VALUES(1,'你好你好',5);
INSERT INTO member(member_id,content,like_count) VALUES(1,'早安早安',10);
INSERT INTO member(member_id,content,like_count) VALUES(2,'午安午安',15);
INSERT INTO member(member_id,content,like_count) VALUES(2,'哈哈哈哈',20);
INSERT INTO member(member_id,content,like_count) VALUES(3,'晚安晚安',25);

SELECT member.name,message.content FROM member 
INNER JOIN message ON member.id=message.member_id;
```
![image](https://user-images.githubusercontent.com/113079404/196694030-b2907701-9209-4368-9f08-48aed321805b.png)

```
SELECT member.name,message.content FROM member 
INNER JOIN message ON member.id=message.member_id WHERE username='test';
```
![image](https://user-images.githubusercontent.com/113079404/196694156-14c0cf23-3122-4db3-a572-4b664765ea68.png)

```
SELECT AVG(like_count) AS 平均數 FROM member 
INNER JOIN message ON member.id=message.member_id WHERE username='test';
```
![image](https://user-images.githubusercontent.com/113079404/196694245-f661ebac-c437-4555-a2ef-b3e789f3a1e0.png)

