import requests,json
#数据格式要注意
session=requests.session()
cicd='open.kadev-cicd.statusfeishu.cn'

url_all_dep="https://{}/open-apis/contact/v3/departments/0/children".format(cicd)
data={
                "i18n_name": {
                    "en_us": "",
                    "ja_jp": "",
                    "zh_cn": "十二部门-2"
                },
                "name": "十二部门-2",
                "order": "2000",
                "parent_department_id": "0"
        }
header={"Authorization":"Bearer t-g101b19gJH3XKP6UCJI7LBK2KSKPKOXFSJCFK7B7","Content-Type":"application/json; charset=utf-8"}
params={'page_size':50}
resp=session.request(url=url_all_dep,method='get',headers=header,params=params)
bodyjson=resp.json()
num=0
depid_ls=[]
for  item in bodyjson['data']['items'][4:]:
    print(item['name'])
    depid_ls.append(item['department_id'])
    num+=1
print(num)

if len(depid_ls)%2!=0:
    depid_ls.pop(0)

father=depid_ls[:len(depid_ls)//2]
son=depid_ls[len(depid_ls)//2:]

depbody_data= {"i18n_name": {
                    "en_us": "",
                    "ja_jp": "",
                    "zh_cn": "十二部门-2"
                },
                "name": "十二部门-2",
                "order": "10000",
                "parent_department_id": "0" }
params={'department_id_type':"department_id"}
urltest='http://httpbin.org/'
for i in range(len(father)):
    url="https://{0}/open-apis/contact/v3/departments/{1}".format(cicd,son[i])
    depbody_data['i18n_name']['zh_cn']=str(son[i])
    depbody_data['name']=str(son[i])
    depbody_data['parent_department_id']=str(father[i])
    session=requests.session()
    resp=session.request(url=url,method='patch',headers=header,json=depbody_data,params=params)
    print(type(resp.request.body),resp.request.body,resp.request.url,resp.request.headers,resp.request.method)
    print(resp.status_code,resp.json())