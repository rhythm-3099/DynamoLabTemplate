# Lab 3 - Hands on DynamoDB

[DynamoDB Lab Template](https://github.com/sanket143/DynamoDB-Lab): Here is the boilerplate you'll be using.

Your Directory Tree

```
.
├── data
│   ├── books
│   │   └── books.json
│   ├── devhub
│   │   ├── commits.json
│   │   ├── issues.json
│   │   ├── repositories.json
│   │   └── users.json
│   └── logs
│       └── web_access_log.json
├── finish.py
├── README.md
├── setup.py
└── soln
    ├── task1
    │   ├── q1.py
    │   ├── q2.py
    │   ├── q3.py
    │   ├── q4.py
    │   ├── q5.py
    │   ├── q6.py
    │   └── q7.py
    ├── task2
    │   ├── q1.py
    │   ├── q2.py
    │   ├── q3.py
    │   └── q4.py
    └── task3
        ├── q1.py
        ├── q2.py
        ├── q3.py
        ├── q4.py
        └── q5.py

8 directories, 25 files
```

You'll be writing all your code in `q#.py` files and are suppose to submit compressed `soln/`

<div style="page-break-after: always;"></div>

## Task 1

**1. Create table `Books` for <span style="color: crimson !important">data/books/books.json</span> with following inputs**
  - Partition Key: Publisher
  - Sort Key: Title
  - Global Secondary Index: ISBN

**2. Add a book using `put item`**

**3. Add all the rest of the books using `batch write`**

**4. Get book <span style="color: crimson !important">Learning JavaScript Design Patterns</span> published by <span style="color: crimson !important">O'Reilly Media</span>**

**5. Get book with ISBN number <span style="color: crimson !important">9781491904244</span>**

**6. Update pages of book <span style="color: crimson !important">Git Pocket Guide</span> published by <span style="color: crimson !important">O'Reilly Media</span> to <span style="color: crimson !important">268</span>**

**7. List out book `titles` with `pages` with more than <span style="color: crimson !important">300</span> pages**

[DynamoDB Reference Codes](https://github.com/sanket143/DynamoDB-Lab/wiki/DynamoDB-Reference-Codes)

---

## Task 2

**1. Create a table `WebAccessLog` for <span style="color: crimson">data/logs/web_access_log.json</span> with following constraints:**

- Partition Key: `ip_addr`
- Sort Key: `req_no`


**2. Write script to perform batch writes with batch size of 25 items for all log items ( i.e 201 entries )**

**3. For IP address `188.45.108.168`, count number of non `200` status requests**

**4. For IP address `191.182.199.16`, give daily count of request, total size of data downloaded**

---

<div style="page-break-after: always;"></div>

## Task 3

Setup Database
```shell
$ python setup.py # will do required changes
```

**Table Definitions**

**Users** <br>
- Primary Key: `email`

**Repositories**
- Partition Key: `name`
- Sort Key: `owner`
- Global Secondary Index: `repo_id-index`
  - Primary Key: `repo_id`

**Commits**
- Primary Key: `project_id`
- Sort Key: `sha`

**Issues**
- Partition Key: `title`
- Sort Key: `repo_id`
- Local Secondary Index: `reporter-index`
  - Partition Key: `title`
  - Sort Key: `reporter`

**1. List all the resolved issues reported by `janet` and `drew`**

**2. Print contributors of the repo `pdf.js`**

**3. Delete users with `0` commits. [`deleted` is an attribute]**

**4. List commits done by the members of the `mozilla` organization**

**5. Get `email ids` of the users who are assigned to atleast one issue**

**6. Update issues that are assigned to the users which no longer exists ( i.e unset `assignee` attribute )**

At last, destroy all your tables so that others could have a cold start.

```shell
$ python finish.py
```