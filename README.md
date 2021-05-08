# [SIMADIAN](http://ec2-18-224-181-83.us-east-2.compute.amazonaws.com/users/)  ⚡️ [![GitHub](https://img.shields.io/github/license/jhabarsingh/SIMADIAN)](https://github.com/jhabarsingh/SIMADIAN/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/jhabarsingh/SIMADIAN)](https://github.com/jhabarsingh/SIMADIAN/stargazers)  [![GitHub contributors](https://img.shields.io/github/contributors/jhabarsingh/SIMADIAN.svg)](https://github.com/jhabarsingh/SIMADIAN/graphs/contributors)  [![GitHub issues](https://img.shields.io/github/issues/jhabarsingh/SIMADIAN.svg)](https://github.com/jhabarsingh/SIMADIAN/issues) [![GitHub forks](https://img.shields.io/github/forks/jhabarsingh/SIMADIAN.svg?style=social&label=Fork)](https://GitHub.com/jhabarsingh/SIMADIAN/network/)

<p align="center">
  <img src="https://github.com/jhabarsingh/SIMADIAN/blob/main/doc/logo.png?raw=true" />
</p>
<details>
  <summary>:zap: TECH STACK</summary>
  <br/>
  <div style="display:flex;justify-content:space-around">
  <img  title="Django" src="https://icon-library.com/images/django-icon/django-icon-0.jpg" width="50px" height="50px" style="margin-right:5px;" />
  <img titlt="Vuejs"   src="https://vuejs.org/images/logo.png" width="50px" height="50px"  style="margin-right:5px;"/>
  <img  title="Vuex" src="https://s3.amazonaws.com/coursetro/posts/144-full.png"  height="50px" style="margin-right:5px;"     />
  <img  title="Vuetify" src="https://cdn.worldvectorlogo.com/logos/vuetify.svg" height="50px"  style="margin-right:5px;"/>
  <img title="Netlify" src="https://www.netlify.com/img/press/logos/logomark.png" height="50px" style="margin-right:5px;" />
  <img  title="Docker" src="https://pbs.twimg.com/profile_images/1273307847103635465/lfVWBmiW_400x400.png" height="50px" style="margin-right:5px;" />
</div>
</details>



<details>
  <summary>:zap: AWS SERVICES</summary>
  <br/>
  <div style="display:flex;justify-content:space-around">
    <img  title="AWS EC2" src="https://i0.wp.com/www.sndkcorp.com/wp-content/uploads/2019/09/amazon-ec2.png?fit=360%2C230&ssl=1" height="70px" style="margin-right:5px;" />
    <img titlt="AWS RDS"   src="https://p2zk82o7hr3yb6ge7gzxx4ki-wpengine.netdna-ssl.com/wp-content/uploads/Amazon-RDS-1.png" height="70px"  style="margin-right:5px;"/>
    <img  title="AWS S3 Bucket" src="https://www.drupal.org/files/project-images/1_B9CIOrxdROHvtdmouQA1_A.png"  height="70px" style="margin-right:5px;"     />
  </div>

</details>

## About
  [SIMADIAN](http://ec2-18-224-181-83.us-east-2.compute.amazonaws.com/users/) is a Web app built using Django and Vuejs. It provides many functionalities:-
  1. **Sell** your **stationaries**
  2. **Upload** the books, other stationary item's detail you want to sell.
  3. You can **Buy** the second hand stationaries at an **affordable cost**.

  
## [Django Api End Points](http://ec2-18-224-181-83.us-east-2.compute.amazonaws.com/users/)
![Django Apis](https://github.com/jhabarsingh/SIMADIAN/blob/main/doc/api.png?raw=true)


## Django Backend Setup

### Using venv
```bash
git clone https://github.com/jhabarsingh/SIMADIAN.git 
cd SIMADIAN
python3 -m venv env # Python 3.6.9 or 3.7.0 version 
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver
```

### Using conda
```bash
git clone https://github.com/jhabarsingh/SIMADIAN.git 
cd SIMADIAN
conda create -n codechef python==3.7 
conda activate codechef
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver
```

### Using Docker

```bash
sudo apt-get install docker docker-compose # Install docker, docker-compose on linux
git clone https://github.com/jhabarsingh/SIMADIAN.git
cd SIMADIAN
sudo docker-compose up
```

## Vuejs Setup

<!-- <p align="center" >
  
  [![Watch the video](https://github.com/jhabarsingh/SIMADIAN/blob/main/app/assets/thumbnail.jpg?raw=true)](https://www.youtube.com/watch?v=IRgjNln4s20)
  <i><b align="center">Click On The Above Image To Watch Demo</b></i>

</p> -->

[Install node](https://nodejs.org/en/download/) |
[Install vue/cli](https://cli.vuejs.org/)
```bash
 git clone https://github.com/jhabarsingh/SIMADIAN.git
 cd SIMADIAN
 npm install   # Nodejs should be installed
 npm run start # Vuejs should be installed
 ```


# [Want To Contribute](https://medium.com/mindsdb/contributing-to-an-open-source-project-how-to-get-started-6ba812301738)
### You can contribute to this project in many ways
 1. You can create an issue if you find any bug.
 2. You can work on an existing issue and Send PR.
 3. You can make changes in the design if it is needed.
 4. Even if you find any grammatical or spelling mistakes then also you can create an issue.

> *I would be glad to see a notification saying `User {xyz} created a Pull Request`.
I promise to review it.*
