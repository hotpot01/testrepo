import requests

#循环创建1000个部门
#上一个部门的depid,是下一个部门的父部门
cicd='open.kadev-cicd.statusfeishu.cn'
url_creat_dep="https://{}/open-apis/contact/v3/departments".format(cicd)
params={"department_id_type":"department_id"}
header={"Authorization":"Bearer t-g101b1bCL6UJZKXH3MFTCHQCA4AARKNRVBPMJYMI","Content-Type":"application/json; charset=utf-8"}

#创建部门
bodydata={
    "name": "起始部门",
    "i18n_name": {
        "zh_cn": "Dem-1",
        "ja_jp": "名",
        "en_us": "De"
    },
    "parent_department_id":"0",
    "department_id": "1",
    "order": "100"
}
# session=requests.session()
# resp=session.request(url=url_creat_dep,json=bodydata,params=params,headers=header,method='post')
# bodyjson=resp.json()
# print(resp.status_code,resp.url)
# print(type(bodyjson),bodyjson)
# print(bodyjson['data']['department']['department_id'])

for i in range(20,1007):
    bodydata['name']=str(i)
    bodydata['i18n_name']['zh_cn']=str(i)
    bodydata['i18n_name']['ja_jp'] = str(i)
    bodydata['i18n_name']['en_us'] = str(i)
    bodydata['department_id']=str(i)
    bodydata['parent_department_id']=str(i-1)
    resp=requests.post(url=url_creat_dep,json=bodydata,params=params,headers=header)
    if resp.status_code!=200:
        print(resp.json())
        print(i)
        break

