# dnspod-python api


## 这里脚本主要实现的功能：

* 查询二级域名ID

	###### id = getDomainID('dnspod.com')
* 查询二级域名解析列表
	###### getRecordList(id)
* 获取某条解析ID
	###### getRecordID(id,'cml','10=1')
* 添加域名解析
	###### createRecord(id,'cml','A','0','126.40.109.48')
* 修改域名解析
	###### updateRecordLine(id,'cml','A','10=1','10=1','126.40.109.48')
* 改变域名解析状态
	###### statusRecord(id,'cml','10=1','enabled')
* 删除域名解析
	###### deleteRecord(id,'cml','10=1')



### 在dnspod上申请AccessKey
* 然后按步骤走会生成AccessKeyId与AccessKeySecret（请自己保管好！）
* 修改dnspod_python.py脚本文件里面的Token_ID与Token_key
* 修改自己账号拥有的二级域名

### 执行脚本
```
python dnspod_python.py
```




