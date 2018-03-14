import requests
from lxml import html


loginpage = "https://lms.mrt.ac.lk/login.php"
params = {'LearnOrgUsername' : '140106T', 'LearnOrgPassword' : 'GAY@kavi?2013', 'LearnOrgLogin' : 'Login'}
response = requests.post(loginpage,data= params);

tree = html.fromstring(response.content)

print(response.content)
