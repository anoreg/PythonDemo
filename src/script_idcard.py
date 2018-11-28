# -*- coding:utf-8 -*-
#import numpy

import time
from datetime import date
from datetime import timedelta
import random

#districtcode={"state":"河北省","city":"沧州市","district":"运河区","code":"130903"}
DC_PATH='../districtcode.txt'
# 随机生成身份证号
def getdistrictcode():
    with open(DC_PATH) as file:
        data = file.read()
        print(data)
        districtlist = data.split('\n')
    for node in districtlist:
        # print node
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state": state, "city": city, "district": district, "code": code})


# def gennerator():
#     global codelist
#     codelist = []
#     #print(codelist)
#     codelist = []
#     if not codelist:
#         getdistrictcode()
#     id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
#     id = id + str(random.randint(1990, 1992))  # 年份项
#     da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
#     id = id + da.strftime('%m%d')
#     id = id + str(random.randint(100, 300))  # ，顺序号简单处理
#
#     i = 0
#     count = 0
#     weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
#     checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
#                  '10': '2'}  # 校验码映射
#     for i in range(0, len(id)):
#         count = count + int(id[i]) * weight[i]
#         id = id + checkcode[str(count % 11)]  # 算出校验码
#         return id

def gennerator():
    global codelist
    #codelist = [{"state":"河北省","city":"沧州市","district":"运河区","code":"130903"}]
    #print(codelist)
    codelist = []
    if not codelist:
        getdistrictcode()
    id = codelist[random.randint(0,len(codelist))-1]['code']  # 地区项
    id = id + str(random.randint(1960, 2008))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项

    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]

    id = id + checkcode[str(count % 11)]  # 算出校验码
    return id


if __name__ == '__main__':
     f = open('plutus_hq_ware1.sql1','w',encoding='utf-8')
     #print(gennerator())
     for a in range(1000000):

        f.write(
           f"INSERT INTO `loanuat11`.`t_user` VALUES ('46593691879{str(a).zfill(7)}', '1', '1', NULL, '0', '{gennerator()}', NULL, NULL, NULL, '158{str(a).zfill(8)}', '123456', NULL, '压测','158{str(a).zfill(8)}', '0', '2', '70', '0', '0', NULL, '1', '0', '1', '1000', NULL, '0', '0', NULL, NULL, NULL, '', NULL, NULL, now(), '0', '0', NULL, '46593691879{str(a).zfill(7)}');" + "\n")
        f.write(
           f"INSERT INTO `loanuat11`.`t_user_borrower`  VALUES ('46593691879{str(a).zfill(7)}', NULL, '1000', NULL, NULL,'杭州乐到新能源有限公司', NULL, NULL, NULL, '22', '1', '0', NULL, NULL, '压测', NULL, NULL, NULL, '20181031', NULL, now(), NULL, NULL, NULL, NULL, '0');" + "\n")
        f.write(
           f"INSERT INTO `loanuat11`.`t_bankcard_temp` VALUES ('6212261202{str(a).zfill(7)}10');" + "\n") #临时表
        # CREATE TABLE `t_bankcard_temp` (
        #   `bankcard_id` bigint(20) NOT NULL COMMENT '银行卡ID'
        # ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行卡临时表';
        f.write(
           f"INSERT INTO `loanuat11`.`t_user_org`  VALUES ('46593691879{str(a).zfill(7)}', '1001', '0.00', '1', '0', '2018-11-16 10:47:48');" + "\n")
        f.write(
           f"INSERT INTO `loanuat11`.`t_user_borrower_identity` VALUES ('46593691879{str(a).zfill(7)}', 'http://plutus-dev.oss-cn-hzfinance.aliyuncs.com/1542331447952.png?Expires=1857691448&OSSAccessKeyId=LTAIVte00lkdPULh&Signature=x6DwXjFlBBrK5wVIAJmf%2FvLgaqc%3D', 'http://plutus-dev.oss-cn-hzfinance.aliyuncs.com/1542331453035.png?Expires=1857691453&OSSAccessKeyId=LTAIVte00lkdPULh&Signature=%2Fpcu1SjtuZ2hhuZBN9V0K2jGUGg%3D', NULL, NULL, '2018-11-16 10:47:48', '2018-11-16 10:47:48', 'http://plutus-dev.oss-cn-hzfinance.aliyuncs.com/1542331457482.png?Expires=1857691457&OSSAccessKeyId=LTAIVte00lkdPULh&Signature=L9EMJtLitItn30Fm1gXlZLLowRg%3D', 'http://plutus-dev.oss-cn-hzfinance.aliyuncs.com/1542336462146.png?Expires=1857696462&OSSAccessKeyId=LTAIVte00lkdPULh&Signature=mIhdyzhKOM2vEm8I8brribwHqTI%3D');" + "\n")
        f.write(
           f"INSERT INTO `loanuat11`.`t_user_account` VALUES ('46593691879{str(a).zfill(7)}', '46593691879{str(a).zfill(7)}', '2018-08-03 11:08:26');" + "\n")
        f.write(
           f"INSERT INTO `loanuat11`.`t_account`  VALUES ('46593691879{str(a).zfill(7)}', '', '0.000', '0.000', '0.000', '1', '0', '0', NULL, '0', '0', '', '2018-09-13 16:16:29');" + "\n")
#授信审核结果更新数据库 的t_preloan_credit_apply 用户名为压测的客户状态为2
        #  f.write(
        #      f"INSERT INTO `loanuat11`.`plutus_order_temp` VALUES ('51411568802{str(a).zfill(7)}');" + "\n") #临时表  user ID:'46593691879{str(a).zfill(7)}
        #  CREATE TABLE `plutus_order_temp` (
        #          `ORDER_ID` varchar(64) NOT NULL COMMENT '订单编号'
        #          ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单临时表';

        #  f.write(
        #      f"INSERT INTO `loanuat11`.`t_contract` VALUES ('46715220081{str(a).zfill(7)}', '46715220081{str(a).zfill(7)}', NULL, NULL, '1', '46593691879{str(a).zfill(7)}', '1000', '1001', '压测', '0', 'idNo', '0', '114200.000', '20171031', '20201030', '0.012518', '0.015000', '2', '0', '', '0', '0', '2018-11-19 19:16:54', '0', '吉利 帝豪EV 电动 EV450 精英版', '0', '0.000', '0.000', '0.000', '114200.000', '0.000', '0.000', '0.000', '114200.000', NULL, NULL, '36', '1', '1', '1', '46715220094{str(a).zfill(7)}', '0.000', '2', '51411568802{str(a).zfill(7)}', '1', '3960.0000');" + "\n") #造好数据后更新表中的id:update t_contract a,t_preloan_credit_apply b set a.id_no = b.id_no where a.car_order_id = b.car_order_id
        #  f.write(
        #      f"INSERT INTO `loanuat11`.`t_preloan_apply`  VALUES ('46715220094{str(a).zfill(7)}', '46715220094{str(a).zfill(7)}', '1000', '1001', '0', '20171031', '191654', '46593691879{str(a).zfill(7)}', '压测', '0', 'idNo', '0', '吉利 帝豪EV 电动 EV450 精英版', '3', '0', '0', '4', '0', '114200.000', '0.000', '0.000', '0.000', '114200.000', NULL, NULL, '36', '1', '0.012518', '0.015000', '0', '', '2', '1', '46715220081{str(a).zfill(7)}', '51411568802{str(a).zfill(7)}', '2018-11-19 19:16:54', '2018-11-19 19:16:54', '51411568802{str(a).zfill(7)}');" + "\n")  #造好数据后更新表中ID：update t_contract a,t_preloan_apply b set a.id_no = b.id_no where a.car_order_id = b.car_order_id;


#update t_pre update t_preloan_credit_apply_detail set early_repay_periods='2';
# f.write(f"INSERT INTO `loanuat11`.`t_loan_receipt`(`receipt_id`, `receipt_no`, `contract_id`, `contract_no`, `org_id`, `user_id`, `product_id`, `product_name`, `term_number`, `loan_date`, `loan_time`, `loan_amount`, `use_withhold`, `loan_purpose`, `loan_apply_id`, `pf_org_id`, `four_kind`, `five_kind`, `default_status`, `divide_fees`, `repay_status`, `end_date`, `settle_interest_date`, `last_repay_date`, `pay_way_no`, `loan_channel`, `update_version`, `create_time`, `delay_date`, `delay_times`) VALUES (43193334{str(a).zfill(10)}, '43193334{str(a).zfill(10)}', 427955601398702080, '427955601398702080', 1001, 427872277179142144, 20000, '吉利帝豪EV450精英版', 24, 20180814, 144945, 124200.000, NULL, '', 431933347132870656, 1000, '0', '0', '0', 0.000000, '1', 20200814, 20181013, 20181015, '10000', '0', 29, '2018-08-14 14:49:45', 20200814, 0);"+"\n")