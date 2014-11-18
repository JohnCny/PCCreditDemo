# coding:utf-8

from flask import Module,request, render_template,flash,redirect

from pccredit import app
# 登陆
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template("welcome.html")
    else:
        return render_template("login.html")

# 注销
@app.route('/change_password')
def change_password():
    return render_template("change_password.html")
	
# 修改密码
@app.route('/logout')
def logout():
    return render_template("login1.html")
	    
# 登录
@app.route('/login1', methods=['GET'])
def login1():
    return render_template("login1.html")
    
# 欢迎界面——主管
@app.route('/welcome_zg', methods=['GET'])
def welcome_zg():
    return render_template("welcome_zg.html")
	
# 欢迎界面——客户经理
@app.route('/welcome_khjl', methods=['GET'])
def welcome_khjl():
    return render_template("welcome_khjl.html")
	
# 欢迎界面——管理员
@app.route('/welcome_gly', methods=['GET'])
def welcome_gly():
    return render_template("welcome_gly.html")

# 进件管理——客户经理
@app.route('/jjgl_khjl', methods=['GET'])
def jjgl_khjl():
    return render_template("index_khjl.html",menu = 'jjgl_khjl')

# 营销管理——客户经理
@app.route('/yxgl_khjl', methods=['GET'])
def yxgl_khjl():
    return render_template("index_khjl.html",menu = 'yxgl_khjl')
	
# 客户管理——客户经理
@app.route('/khgl_khjl', methods=['GET'])
def khgl_khjl():
    return render_template("index_khjl.html",menu = 'khgl_khjl')	
	
# 综合风控管理——客户经理
@app.route('/zhfkgl_khjl', methods=['GET'])
def zhfkgl_khjl():
    return render_template("index_khjl.html",menu = 'zhfkgl_khjl')
	
# 客户经理管理——客户经理
@app.route('/khjlgl_khjl', methods=['GET'])
def khjlgl_khjl():
    return render_template("index_khjl.html",menu = 'khjlgl_khjl')
	
# 系统管理——客户经理
@app.route('/xtgl_khjl', methods=['GET'])
def xtgl_khjl():
    return render_template("index_khjl.html",menu = 'xtgl_khjl')
	

# 进件管理——主管
@app.route('/jjgl_zg', methods=['GET'])
def jjgl_zg():
    return render_template("index_zg.html",menu = 'jjgl_zg')	

# 营销管理——主管
@app.route('/yxgl_zg', methods=['GET'])
def yxgl_zg():
    return render_template("index_zg.html",menu = 'yxgl_zg')
	
# 客户管理——主管
@app.route('/khgl_zg', methods=['GET'])
def khgl_zg():
    return render_template("index_zg.html",menu = 'khgl_zg')	
	
# 综合风控管理——主管
@app.route('/zhfkgl_zg', methods=['GET'])
def zhfkgl_zg():
    return render_template("index_zg.html",menu = 'zhfkgl_zg')	
	
# 客户经理管理——主管
@app.route('/khjlgl_zg', methods=['GET'])
def khjlgl_zg():
    return render_template("index_zg.html",menu = 'khjlgl_zg')	
				
# 系统管理——主管
@app.route('/xtgl_zg', methods=['GET'])
def xtgl_zg():
    return render_template("index_zg.html",menu = 'xtgl_zg')	
	

# 产品管理——管理员
@app.route('/cpgl_gly', methods=['GET'])
def cpgl_gly():
    return render_template("index_gly.html",menu = 'cpgl_gly')

# 统计报表——管理员
@app.route('/tjbb_gly', methods=['GET'])
def tjbb_gly():
    return render_template("index_gly.html",menu = 'tjbb_gly')
	
# 系统管理——管理员
@app.route('/xtgl_gly', methods=['GET'])
def xtgl_gly():
    return render_template("index_gly.html",menu = 'xtgl_gly')
	
###############################进件管理##########################################	
######################进件信息#####################	
# 进件查询
@app.route('/Jjgl/jjxx/jjcx', methods=['GET'])
def jjcx():
    return render_template("Jjgl/jjxx/jjcx.html")	
	
# 进件查询-客户资料
@app.route('/Jjgl/jjxx/khzl', methods=['GET'])
def khzl():
    return render_template("Jjgl/jjxx/khzl.html")	
	
# 进件查询-客户资料(客户申请信息)
@app.route('/Jjgl/jjxx/khsqxx', methods=['GET'])
def khsqxx():
    return render_template("Jjgl/jjxx/khsqxx.html")
	
# 进件查询-客户资料(客户原始信息)
@app.route('/Jjgl/jjxx/khysxx', methods=['GET'])
def khysxx():
    return render_template("Jjgl/jjxx/khysxx.html")
	
# 进件查询-客户资料(影像附件)
@app.route('/Jjgl/jjxx/yxfj', methods=['GET'])
def yxfj():
    return render_template("Jjgl/jjxx/yxfj.html")
	
# 进件查询-客户资料(资信信息)
@app.route('/Jjgl/jjxx/zxxx', methods=['GET'])
def zxxx():
    return render_template("Jjgl/jjxx/zxxx.html")
	
# 进件调查
@app.route('/Jjgl/jjxx/jjdc', methods=['GET'])
def jjdc():
    return render_template("Jjgl/jjxx/jjdc.html")	

# 录入客户调查信息
@app.route('/Jjgl/jjxx/lrkhdcxx', methods=['GET'])
def lrkhdcxx():
    return render_template("Jjgl/jjxx/lrkhdcxx.html")	
	
# 机构内提交进件
@app.route('/Jjgl/jjxx/jgntjjj', methods=['GET'])
def jgntjjj():
    return render_template("Jjgl/jjxx/jgntjjj.html")
	
# 向卡中心提交进件
@app.route('/Jjgl/jjxx/kzxtjjj', methods=['GET'])
def kzxtjjj():
    return render_template("Jjgl/jjxx/kzxtjjj.html")
	
# 分配进件
@app.route('/Jjgl/jjxx/fpjj', methods=['GET'])
def fpjj():
    return render_template("Jjgl/jjxx/fpjj.html")
	
######################客户筛选#####################	
# 客户筛选
@app.route('/Jjgl/khsx/khsx', methods=['GET'])
def khsx():
    return render_template("Jjgl/khsx/khsx.html")
######################多渠道数据采集#####################	
# 客户资料数据录入
@app.route('/Jjgl/dqdsjcj/khzlsjlr', methods=['GET'])
def khzlsjlr():
    return render_template("Jjgl/dqdsjcj/khzlsjlr.html")
	
# 批量客户数据录入
@app.route('/Jjgl/dqdsjcj/plkhsjlr', methods=['GET'])
def plkhsjlr():
    return render_template("Jjgl/dqdsjcj/plkhsjlr.html")
######################客户营销管理#####################		
# 营销规则管理
@app.route('/Jjgl/khyxgl/yxgzgl', methods=['GET'])
def yxgzgl():
    return render_template("Jjgl/khyxgl/yxgzgl.html")
	
# 营销规则管理-新增
@app.route('/Jjgl/khyxgl/new_yxfa', methods=['GET'])
def new_yxfa():
    return render_template("Jjgl/khyxgl/new_yxfa.html")	
	
# 营销规则管理-编辑
@app.route('/Jjgl/khyxgl/edit_yxfa', methods=['GET'])
def edit_yxfa():
    return render_template("Jjgl/khyxgl/edit_yxfa.html")
	
# 营销台账管理
@app.route('/Jjgl/khyxgl/yxtzgl', methods=['GET'])
def yxtzgl():
    return render_template("Jjgl/khyxgl/yxtzgl.html")
	
# 营销台账信息
@app.route('/Jjgl/khyxgl/yxtzxx', methods=['GET'])
def yxtzxx():
    return render_template("Jjgl/khyxgl/yxtzxx.html")
	
# 营销计划查询
@app.route('/Jjgl/khyxgl/yxjhcx', methods=['GET'])
def yxjhcx():
    return render_template("Jjgl/khyxgl/yxjhcx.html")
	
# 营销计划实施
@app.route('/Jjgl/khyxgl/yxjhss', methods=['GET'])
def yxjhss():
    return render_template("Jjgl/khyxgl/yxjhss.html")
	
# 营销计划实施-新增
@app.route('/Jjgl/khyxgl/new_yxjhss', methods=['GET'])
def new_yxjhss():
    return render_template("Jjgl/khyxgl/new_yxjhss.html")		
	
# 营销计划管理
@app.route('/Jjgl/khyxgl/yxjhgl', methods=['GET'])
def yxjhgl():
    return render_template("Jjgl/khyxgl/yxjhgl.html")	
	
# 营销计划管理-新增
@app.route('/Jjgl/khyxgl/new_yxjh', methods=['GET'])
def new_yxjh():
    return render_template("Jjgl/khyxgl/new_yxjh.html")
	
# 营销计划管理-录入营销计划
@app.route('/Jjgl/khyxgl/lryxjh', methods=['GET'])
def lryxjh():
    return render_template("Jjgl/khyxgl/lryxjh.html")
	
# 营销计划管理-营销计划信息
@app.route('/Jjgl/khyxgl/yxjhxx', methods=['GET'])
def yxjhxx():
    return render_template("Jjgl/khyxgl/yxjhxx.html")
######################审核审批#####################		
# 待审批进件
@app.route('/Jjgl/shsp/dspjj', methods=['GET'])
def dspjj():
    return render_template("Jjgl/shsp/dspjj.html")
	
# 进件审批
@app.route('/Jjgl/shsp/jjsp', methods=['GET'])
def jjsp():
    return render_template("Jjgl/shsp/jjsp.html")
######################当前贷款信息查询#####################		
# 申请进度查询
@app.route('/Jjgl/dqdkxxcx/sqjdcx', methods=['GET'])
def sqjdcx():
    return render_template("Jjgl/dqdkxxcx/sqjdcx.html")
######################风险客户管理#####################		
# 上报风险客户
@app.route('/Jjgl/fxkhgl/sbfxkh', methods=['GET'])
def sbfxkh():
    return render_template("Jjgl/fxkhgl/sbfxkh.html")
	
# 上报风险客户-新增
@app.route('/Jjgl/fxkhgl/new_sbfxkh', methods=['GET'])
def new_sbfxkh():
    return render_template("Jjgl/fxkhgl/new_sbfxkh.html")
	
# 风险客户审核
@app.route('/Jjgl/fxkhgl/fxkhsh', methods=['GET'])
def fxkhsh():
    return render_template("Jjgl/fxkhgl/fxkhsh.html")
	
# 风险审核信息
@app.route('/Jjgl/fxkhgl/fxshxx', methods=['GET'])
def fxshxx():
    return render_template("Jjgl/fxkhgl/fxshxx.html")
	

###############################客户管理##########################################	
######################客户原始资料管理#####################	
# 客户原始资料录入
@app.route('/Khgl/khyszlgl/yszllr', methods=['GET'])
def yszllr():
    return render_template("Khgl/khyszlgl/yszllr.html")	
	
# 客户原始资料查询
@app.route('/Khgl/khyszlgl/yszlcx', methods=['GET'])
def yszlcx():
    return render_template("Khgl/khyszlgl/yszlcx.html")
	
# 客户原始资料信息
@app.route('/Khgl/khyszlgl/yszlxx', methods=['GET'])
def yszlxx():
    return render_template("Khgl/khyszlgl/yszlxx.html")	
	
######################客户预评估#####################			
# 客户资信状况评估
@app.route('/Khgl/khypg/khzxzkpg', methods=['GET'])
def khzxzkpg():
    return render_template("Khgl/khypg/khzxzkpg.html")
	
# 客户授信评估报告
@app.route('/Khgl/khypg/sxpgbg', methods=['GET'])
def sxpgbg():
    return render_template("Khgl/khypg/sxpgbg.html")
	
# 客户资信评估报告
@app.route('/Khgl/khypg/zxpgbg', methods=['GET'])
def zxpgbg():
    return render_template("Khgl/khypg/zxpgbg.html")
	
# 客户资信评估报告-人行征信
@app.route('/Khgl/khypg/zxbg_rhzx', methods=['GET'])
def zxbg_rhzx():
    return render_template("Khgl/khypg/zxbg_rhzx.html")
	
# 客户资信评估报告-公安征信
@app.route('/Khgl/khypg/zxbg_gazx', methods=['GET'])
def zxbg_gazx():
    return render_template("Khgl/khypg/zxbg_gazx.html")
	
# 客户资信评估报告-内部征信
@app.route('/Khgl/khypg/zxbg_nbzx', methods=['GET'])
def zxbg_nbzx():
    return render_template("Khgl/khypg/zxbg_nbzx.html")
	
# 客户资信评估报告-申请信息交叉检验规则
@app.route('/Khgl/khypg/zxbg_sqxxjcjy', methods=['GET'])
def zxbg_sqxxjcjy():
    return render_template("Khgl/khypg/zxbg_sqxxjcjy.html")
	
# 客户资信评估报告-申请交叉检验
@app.route('/Khgl/khypg/sqjcjy', methods=['GET'])
def sqjcjy():
    return render_template("Khgl/khypg/sqjcjy.html")
######################客户分案#####################		
# 营销客户分案
@app.route('/Khgl/khfa/yxkhfa', methods=['GET'])
def yxkhfa():
    return render_template("Khgl/khfa/yxkhfa.html")	
	
# 存量客户分案
@app.route('/Khgl/khfa/clkhfa', methods=['GET'])
def clkhfa():
    return render_template("Khgl/khfa/clkhfa.html")	
	
# 强制分案
@app.route('/Khgl/khfa/qzfa', methods=['GET'])
def qzfa():
    return render_template("Khgl/khfa/qzfa.html")	
######################客户维护信息管理#####################	
# 客户维护信息录入
@app.route('/Khgl/khwhxxgl/whxxlr', methods=['GET'])
def whxxlr():
    return render_template("Khgl/khwhxxgl/whxxlr.html")	
	
# 录入维护信息
@app.route('/Khgl/khwhxxgl/lrwhxx', methods=['GET'])
def lrwhxx():
    return render_template("Khgl/khwhxxgl/lrwhxx.html")	
	
# 录入维护信息-新增
@app.route('/Khgl/khwhxxgl/new_whxx', methods=['GET'])
def new_whxx():
    return render_template("Khgl/khwhxxgl/new_whxx.html")	
	
# 录入维护信息-编辑
@app.route('/Khgl/khwhxxgl/edit_whxx', methods=['GET'])
def edit_whxx():
    return render_template("Khgl/khwhxxgl/edit_whxx.html")	
	
# 维护信息查询
@app.route('/Khgl/khwhxxgl/whxxcx', methods=['GET'])
def whxxcx():
    return render_template("Khgl/khwhxxgl/whxxcx.html")	
	
# 维护信息
@app.route('/Khgl/khwhxxgl/whxx', methods=['GET'])
def whxx():
    return render_template("Khgl/khwhxxgl/whxx.html")	
	
# 客户维护报告
@app.route('/Khgl/khwhxxgl/khwhbg', methods=['GET'])
def khwhbg():
    return render_template("Khgl/khwhxxgl/khwhbg.html")	
	
# 录入维护报告
@app.route('/Khgl/khwhxxgl/lrwhbg', methods=['GET'])
def lrwhbg():
    return render_template("Khgl/khwhxxgl/lrwhbg.html")		
	
# 录入维护报告-基本情况
@app.route('/Khgl/khwhxxgl/lrwhbg_jbqk', methods=['GET'])
def lrwhbg_jbqk():
    return render_template("Khgl/khwhxxgl/lrwhbg_jbqk.html")	
	
# 录入维护报告-资产负债表
@app.route('/Khgl/khwhxxgl/lrwhbg_zcfzb', methods=['GET'])
def lrwhbg_zcfzb():
    return render_template("Khgl/khwhxxgl/lrwhbg_zcfzb.html")
	
# 录入维护报告-交叉检验
@app.route('/Khgl/khwhxxgl/lrwhbg_jcjy', methods=['GET'])
def lrwhbg_jcjy():
    return render_template("Khgl/khwhxxgl/lrwhbg_jcjy.html")	
	
# 录入维护报告-损益表
@app.route('/Khgl/khwhxxgl/lrwhbg_syb', methods=['GET'])
def lrwhbg_syb():
    return render_template("Khgl/khwhxxgl/lrwhbg_syb.html")	
	
# 录入维护报告-库存
@app.route('/Khgl/khwhxxgl/lrwhbg_kc', methods=['GET'])
def lrwhbg_kc():
    return render_template("Khgl/khwhxxgl/lrwhbg_kc.html")
	
# 录入维护报告-固定资产清单
@app.route('/Khgl/khwhxxgl/lrwhbg_gdzcqd', methods=['GET'])
def lrwhbg_gdzcqd():
    return render_template("Khgl/khwhxxgl/lrwhbg_gdzcqd.html")
	
# 录入维护报告-账款清单
@app.route('/Khgl/khwhxxgl/lrwhbg_zkqd', methods=['GET'])
def lrwhbg_zkqd():
    return render_template("Khgl/khwhxxgl/lrwhbg_zkqd.html")
	
# 客户维护报告查询
@app.route('/Khgl/khwhxxgl/khwhbgcx', methods=['GET'])
def khwhbgcx():
    return render_template("Khgl/khwhxxgl/khwhbgcx.html")	
	
# 客户维护报告信息
@app.route('/Khgl/khwhxxgl/khwhbgxx', methods=['GET'])
def khwhbgxx():
    return render_template("Khgl/khwhxxgl/khwhbgxx.html")	
	
# 授信额度管理
@app.route('/Khgl/khwhxxgl/sxedgl', methods=['GET'])
def sxedgl():
    return render_template("Khgl/khwhxxgl/sxedgl.html")	
	
# 额度审核
@app.route('/Khgl/khwhxxgl/edsh', methods=['GET'])
def edsh():
    return render_template("Khgl/khwhxxgl/edsh.html")	
			
######################客户评估信息管理#####################	
# 客户评估信息查询
@app.route('/Khgl/khpgxxgl/khpgxxcx', methods=['GET'])
def khpgxxcx():
    return render_template("Khgl/khpgxxgl/khpgxxcx.html")
	
# 客户评估信息查询——Tab
@app.route('/Khgl/khpgxxgl/pgbgTab', methods=['GET'])
def pgbgTab():
    return render_template("Khgl/khpgxxgl/pgbgTab.html")	
	
# 评估报告
@app.route('/Khgl/khpgxxgl/Pgbg', methods=['GET'])
def Pgbg():
    return render_template("Khgl/khpgxxgl/pgbg.html")
	
# 人行征信报告
@app.route('/Khgl/khpgxxgl/rhzxbg', methods=['GET'])
def rhzxbg():
    return render_template("Khgl/khpgxxgl/rhzxbg.html")
	
# 人行征信报告
@app.route('/Khgl/khpgxxgl/gazx', methods=['GET'])
def gazx():
    return render_template("Khgl/khpgxxgl/gazx.html")
######################客户维护管理#####################	
# 客户维护台账
@app.route('/Khgl/khwhgl/khwhtz', methods=['GET'])
def khwhtz():
    return render_template("Khgl/khwhgl/khwhtz.html")
	
# 客户维护记录
@app.route('/Khgl/khwhgl/khwhjl', methods=['GET'])
def khwhjl():
    return render_template("Khgl/khwhgl/khwhjl.html")	
	
# 客户维护计划
@app.route('/Khgl/khwhgl/khwhjh', methods=['GET'])
def khwhjh():
    return render_template("Khgl/khwhgl/khwhjh.html")
	
# 客户维护计划规则
@app.route('/Khgl/khwhgl/khwhjhgz', methods=['GET'])
def khwhjhgz():
    return render_template("Khgl/khwhgl/khwhjhgz.html")
	
# 客户维护计划规则——新增
@app.route('/Khgl/khwhgl/new_khwhjhgz', methods=['GET'])
def new_khwhjhgz():
    return render_template("Khgl/khwhgl/new_khwhjhgz.html")
	
# 客户维护计划规则——编辑
@app.route('/Khgl/khwhgl/edit_khwhjhgz', methods=['GET'])
def edit_khwhjhgz():
    return render_template("Khgl/khwhgl/edit_khwhjhgz.html")
	
# 客户维护计划维护
@app.route('/Khgl/khwhgl/khwhjhwh', methods=['GET'])
def khwhjhwh():
    return render_template("Khgl/khwhgl/khwhjhwh.html")
	
# 客户维护计划维护-新增
@app.route('/Khgl/khwhgl/new_khwhjh', methods=['GET'])
def new_khwhjh():
    return render_template("Khgl/khwhgl/new_khwhjh.html")
	
# 客户维护计划维护-编辑
@app.route('/Khgl/khwhgl/edit_khwhjh', methods=['GET'])
def edit_khwhjh():
    return render_template("Khgl/khwhgl/edit_khwhjh.html")
######################渠道管理#####################	
# 客户信息渠道查询
@app.route('/Khgl/qdgl/khxxqdcx', methods=['GET'])
def khxxqdcx():
    return render_template("Khgl/qdgl/khxxqdcx.html")
	
# 客户信息渠道信息
@app.route('/Khgl/qdgl/khxxqdxx', methods=['GET'])
def khxxqdxx():
    return render_template("Khgl/qdgl/khxxqdxx.html")
	
# 信息员评价查询
@app.route('/Khgl/qdgl/xxypjcx', methods=['GET'])
def xxypjcx():
    return render_template("Khgl/qdgl/xxypjcx.html")
	
# 信息员评价列表（暂无）
@app.route('/Khgl/qdgl/xxypjList', methods=['GET'])
def xxypjList():
    return render_template("Khgl/qdgl/xxypjList.html")
	
# 信息员评价信息
@app.route('/Khgl/qdgl/xxypjxx', methods=['GET'])
def xxypjxx():
    return render_template("Khgl/qdgl/xxypjxx.html")
	
# 信息员渠道
@app.route('/Khgl/qdgl/xxyqd', methods=['GET'])
def xxyqd():
    return render_template("Khgl/qdgl/xxyqd.html")
	
# 修改信息员信息
@app.route('/Khgl/qdgl/edit_xxyxx', methods=['GET'])
def edit_xxyxx():
    return render_template("Khgl/qdgl/edit_xxyxx.html")
	
# 添加负责客户
@app.route('/Khgl/qdgl/tjfzkh', methods=['GET'])
def tjfzkh():
    return render_template("Khgl/qdgl/tjfzkh.html")
	
# 其他渠道
@app.route('/Khgl/qdgl/qtqd', methods=['GET'])
def qtqd():
    return render_template("Khgl/qdgl/qtqd.html")
	
# 修改渠道信息
@app.route('/Khgl/qdgl/edit_qtqdxx', methods=['GET'])
def edit_qtqdxx():
    return render_template("Khgl/qdgl/edit_qtqdxx.html")
######################客户交易信息管理#####################	
# 风险交易分析规则管理
@app.route('/Khgl/khjyxxgl/fxjyfxgzgl', methods=['GET'])
def fxjyfxgzgl():
    return render_template("Khgl/khjyxxgl/fxjyfxgzgl.html")
	
# 交易风险数据分析
@app.route('/Khgl/khjyxxgl/jyfxsjfx', methods=['GET'])
def jyfxsjfx():
    return render_template("Khgl/khjyxxgl/jyfxsjfx.html")
	
# 贡献度数据分析
@app.route('/Khgl/khjyxxgl/gxdsjfx', methods=['GET'])
def gxdsjfx():
    return render_template("Khgl/khjyxxgl/gxdsjfx.html")
	
# 费用列表
@app.route('/Khgl/khjyxxgl/fylb', methods=['GET'])
def fylb():
    return render_template("Khgl/khjyxxgl/fylb.html")
	
###############################客户经理管理##########################################	
######################客户经理信息管理#####################	
# 客户经理基本信息
@app.route('/Khjlgl/khjlxxgl/khjljbxx', methods=['GET'])
def khjljbxx():
    return render_template("Khjlgl/khjlxxgl/khjljbxx.html")	
	
# 客户经理日常管理信息
@app.route('/Khjlgl/khjlxxgl/rcglxx', methods=['GET'])
def rcglxx():
    return render_template("Khjlgl/khjlxxgl/rcglxx.html")	
	
# 客户经理日常管理详情
@app.route('/Khjlgl/khjlxxgl/rcglxq', methods=['GET'])
def rcglxq():
    return render_template("Khjlgl/khjlxxgl/rcglxq.html")
	
# 客户经理属性管理信息
@app.route('/Khjlgl/khjlxxgl/sxglxx', methods=['GET'])
def sxglxx():
    return render_template("Khjlgl/khjlxxgl/sxglxx.html")	
	
# 客户经理属性管理详情
@app.route('/Khjlgl/khjlxxgl/sxglxq', methods=['GET'])
def sxglxq():
    return render_template("Khjlgl/khjlxxgl/sxglxq.html")
	
# 所辖团队管理
@app.route('/Khjlgl/khjlxxgl/sxtdgl', methods=['GET'])
def sxtdgl():
    return render_template("Khjlgl/khjlxxgl/sxtdgl.html")
	
# 所辖团队管理-新增
@app.route('/Khjlgl/khjlxxgl/new_sxtdgl', methods=['GET'])
def new_sxtdgl():
    return render_template("Khjlgl/khjlxxgl/new_sxtdgl.html")
	
# 所辖团队管理-编辑
@app.route('/Khjlgl/khjlxxgl/edit_sxtdgl', methods=['GET'])
def edit_sxtdgl():
    return render_template("Khjlgl/khjlxxgl/edit_sxtdgl.html")	
	
# 客户经理信息
@app.route('/Khjlgl/khjlxxgl/khjlList', methods=['GET'])
def khjlList():
    return render_template("Khjlgl/khjlxxgl/khjlList.html")
	
# 个人信息
@app.route('/Khjlgl/khjlxxgl/grxx', methods=['GET'])
def grxx():
    return render_template("Khjlgl/khjlxxgl/grxx.html")
	
# 客户额度管理
@app.route('/Khjlgl/khjlxxgl/khedgl', methods=['GET'])
def khedgl1():
    return render_template("Khjlgl/khjlxxgl/khedgl.html")
	
# 客户额度信息
@app.route('/Khjlgl/khjlxxgl/khedxx', methods=['GET'])
def khedxx():
    return render_template("Khjlgl/khjlxxgl/khedxx.html")
	
######################员工评估考核#####################	
# 培训期评估
@app.route('/Khjlgl/ygpgkh/pxqpglist', methods=['GET'])
def pxqpglist():
    return render_template("Khjlgl/ygpgkh/pxqpglist.html")	
	
# 课堂培训评估
@app.route('/Khjlgl/ygpgkh/ktpxpg', methods=['GET'])
def ktpxpg():
    return render_template("Khjlgl/ygpgkh/ktpxpg.html")	
	
# 实际操作评估
@app.route('/Khjlgl/ygpgkh/sjczpg', methods=['GET'])
def sjczpg():
    return render_template("Khjlgl/ygpgkh/sjczpg.html")	
	
# 最终评估
@app.route('/Khjlgl/ygpgkh/zzpg', methods=['GET'])
def zzpg():
    return render_template("Khjlgl/ygpgkh/zzpg.html")	
	
# 在岗评估
@app.route('/Khjlgl/ygpgkh/zgpglist', methods=['GET'])
def zgpglist():
    return render_template("Khjlgl/ygpgkh/zgpglist.html")	
	
# 在岗评估-客户经理KPI
@app.route('/Khjlgl/ygpgkh/khjlKPI', methods=['GET'])
def khjlKPI():
    return render_template("Khjlgl/ygpgkh/khjlKPI.html")
	
# 在岗评估-后台岗KPI
@app.route('/Khjlgl/ygpgkh/htgKPI', methods=['GET'])
def htgKPI():
    return render_template("Khjlgl/ygpgkh/htgKPI.html")
	
######################客户经理管理参数维护#####################	
# 参数维护
@app.route('/Khjlgl/khjlglcswh/cswh', methods=['GET'])
def cswh():
    return render_template("Khjlgl/khjlglcswh/cswh.html")	
	
# 参数维护——编辑
@app.route('/Khjlgl/khjlglcswh/edit_cswh', methods=['GET'])
def edit_cswh():
    return render_template("Khjlgl/khjlglcswh/edit_cswh.html")	
	
# 客户经理层级管理
@app.route('/Khjlgl/khjlglcswh/khjlcjgl', methods=['GET'])
def khjlcjgl():
    return render_template("Khjlgl/khjlglcswh/khjlcjgl.html")
	
# 客户经理层级管理——编辑
@app.route('/Khjlgl/khjlglcswh/edit_khjlcjgl', methods=['GET'])
def edit_khjlcjgl():
    return render_template("Khjlgl/khjlglcswh/edit_khjlcjgl.html")
	
# 客户经理评价规则管理
@app.route('/Khjlgl/khjlglcswh/pjgzgl', methods=['GET'])
def pjgzgl():
    return render_template("Khjlgl/khjlglcswh/pjgzgl.html")
	
# 客户经理评价规则管理——基础业绩考核规则
@app.route('/Khjlgl/khjlglcswh/jcyjkhgz', methods=['GET'])
def jcyjkhgz():
    return render_template("Khjlgl/khjlglcswh/jcyjkhgz.html")	
	
# 客户经理评价规则管理——客户经理保护期指标规则
@app.route('/Khjlgl/khjlglcswh/khjlbhqzbgz', methods=['GET'])
def khjlbhqzbgz():
    return render_template("Khjlgl/khjlglcswh/khjlbhqzbgz.html")
	
# 客户经理评价规则管理——综合评估标准
@app.route('/Khjlgl/khjlglcswh/zhpgbz', methods=['GET'])
def zhpgbz():
    return render_template("Khjlgl/khjlglcswh/zhpgbz.html")	
	
# 客户经理晋级审核规则
@app.route('/Khjlgl/khjlglcswh/khjljjshgz', methods=['GET'])
def khjljjshgz():
    return render_template("Khjlgl/khjlglcswh/khjljjshgz.html")
	
# 晋级评估规则
@app.route('/Khjlgl/khjlglcswh/jjpggz', methods=['GET'])
def jjpggz():
    return render_template("Khjlgl/khjlglcswh/jjpggz.html")
	
# 降级评估规则
@app.route('/Khjlgl/khjlglcswh/jjpggz2', methods=['GET'])
def jjpggz2():
    return render_template("Khjlgl/khjlglcswh/jjpggz2.html")
######################客户经理日常维护#####################	
# 客户经理资料
@app.route('/Khjlgl/khjlrcwh/khjlzlwh', methods=['GET'])
def khjlzlwh():
    return render_template("Khjlgl/khjlrcwh/khjlzlwh.html")	
	
# 客户经理资料-新增
@app.route('/Khjlgl/khjlrcwh/new_khjl', methods=['GET'])
def new_khjl():
    return render_template("Khjlgl/khjlrcwh/new_khjl.html")	
	
# 客户经理资料-编辑
@app.route('/Khjlgl/khjlrcwh/edit_khjl', methods=['GET'])
def edit_khjl():
    return render_template("Khjlgl/khjlrcwh/edit_khjl.html")	
	
	
# 维护台账查询
@app.route('/Khjlgl/khjlrcwh/whtzcx', methods=['GET'])
def whtzcx():
    return render_template("Khjlgl/khjlrcwh/whtzcx.html")	
	
# 维护台账信息
@app.route('/Khjlgl/khjlrcwh/whtzxx', methods=['GET'])
def whtzxx():
    return render_template("Khjlgl/khjlrcwh/whtzxx.html")	
	
# 客户经理管理台帐
@app.route('/Khjlgl/khjlrcwh/khjlgltz', methods=['GET'])
def khjlgltz():
    return render_template("Khjlgl/khjlrcwh/khjlgltz.html")	
	
# 客户经理管理台帐-详情列表
@app.route('/Khjlgl/khjlrcwh/khjlgltz_xqList', methods=['GET'])
def khjlgltz_xqList():
    return render_template("Khjlgl/khjlrcwh/khjlgltz_xqList.html")	
	
# 客户经理管理台帐-台账明细
@app.route('/Khjlgl/khjlrcwh/khjlgltz_tzmx', methods=['GET'])
def khjlgltz_tzmx():
    return render_template("Khjlgl/khjlrcwh/khjlgltz_tzmx.html")
	
# 客户经理再培训管理
@app.route('/Khjlgl/khjlrcwh/khjlzpxgl', methods=['GET'])
def khjlzpxgl():
    return render_template("Khjlgl/khjlrcwh/khjlzpxgl.html")	
	
# 客户经理再培训管理
@app.route('/Khjlgl/khjlrcwh/new_khjlzpx', methods=['GET'])
def new_khjlzpx():
    return render_template("Khjlgl/khjlrcwh/new_khjlzpx.html")	
	
# 客户经理再培训管理——客户经理培训计划
@app.route('/Khjlgl/khjlrcwh/khjlpxjh', methods=['GET'])
def khjlpxjh():
    return render_template("Khjlgl/khjlrcwh/khjlpxjh.html")	
	
# 风险警示书
@app.route('/Khjlgl/khjlrcwh/fxjss', methods=['GET'])
def fxjss():
    return render_template("Khjlgl/khjlrcwh/fxjss.html")		
	
# 问责管理
@app.route('/Khjlgl/khjlrcwh/wzgl', methods=['GET'])
def wzgl():
    return render_template("Khjlgl/khjlrcwh/wzgl.html")		
	
# 问责管理-新增
@app.route('/Khjlgl/khjlrcwh/new_wzgl', methods=['GET'])
def new_wzgl():
    return render_template("Khjlgl/khjlrcwh/new_wzgl.html")	
###############################综合风险管理##########################################	
######################催收管理#####################	
# 逾期客户查询
@app.route('/Zhfxgl/csgl/yqkhcx', methods=['GET'])
def yqkhcx():
    return render_template("Zhfxgl/csgl/yqkhcx.html")
	
# 逾期客户催收
@app.route('/Zhfxgl/csgl/yqkhcs', methods=['GET'])
def yqkhcs():
    return render_template("Zhfxgl/csgl/yqkhcs.html")
	
# 逾期客户资料查询
@app.route('/Zhfxgl/csgl/yqkhzlcx', methods=['GET'])
def yqkhzlcx():
    return render_template("Zhfxgl/csgl/yqkhzlcx.html")
	
# 逾期客户信息
@app.route('/Zhfxgl/csgl/yqkhxx', methods=['GET'])
def yqkhxx():
    return render_template("Zhfxgl/csgl/yqkhxx.html")	
	
# 客户催收计划维护
@app.route('/Zhfxgl/csgl/khcsjhwh', methods=['GET'])
def khcsjhwh():
    return render_template("Zhfxgl/csgl/khcsjhwh.html")
	
# 客户催收计划维护信息
@app.route('/Zhfxgl/csgl/khcsjhwhxx', methods=['GET'])
def khcsjhwhxx():
    return render_template("Zhfxgl/csgl/khcsjhwhxx.html")
	
# 客户催收台账查询
@app.route('/Zhfxgl/csgl/khcstzcx', methods=['GET'])
def khcstzcx():
    return render_template("Zhfxgl/csgl/khcstzcx.html")
	
# 客户催收台账维护
@app.route('/Zhfxgl/csgl/khcstzwh', methods=['GET'])
def khcstzwh():
    return render_template("Zhfxgl/csgl/khcstzwh.html")
	
# 客户催收台账维护信息
@app.route('/Zhfxgl/csgl/khcstzwhxx', methods=['GET'])
def khcstzwhxx():
    return render_template("Zhfxgl/csgl/khcstzwhxx.html")
	
# 客户催收计划
@app.route('/Zhfxgl/csgl/csjh', methods=['GET'])
def csjh():
    return render_template("Zhfxgl/csgl/csjh.html")
	
# 客户催收计划信息
@app.route('/Zhfxgl/csgl/khcsjhxx', methods=['GET'])
def khcsjhxx():
    return render_template("Zhfxgl/csgl/khcsjhxx.html")
	
# 催收计划实施
@app.route('/Zhfxgl/csgl/csjhss', methods=['GET'])
def csjhss():
    return render_template("Zhfxgl/csgl/csjhss.html")
	
# 催收计划主动移交
@app.route('/Zhfxgl/csgl/csjhzdyj', methods=['GET'])
def csjhzdyj():
    return render_template("Zhfxgl/csgl/csjhzdyj.html")
	
# 催收案件强制移交（机构内）
@app.route('/Zhfxgl/csgl/csjhqzyj', methods=['GET'])
def csjhqzyj():
    return render_template("Zhfxgl/csgl/csjhqzyj.html")
	
# 催收案件移交（卡中心）
@app.route('/Zhfxgl/csgl/csajyj', methods=['GET'])
def csajyj():
    return render_template("Zhfxgl/csgl/csajyj.html")
######################风险事项管理#####################	
# 风险事项查询
@app.route('/Zhfxgl/fxsxgl/fxsxcx', methods=['GET'])
def fxsxcx():
    return render_template("Zhfxgl/fxsxgl/fxsxcx.html")
	
# 风险事项上传
@app.route('/Zhfxgl/fxsxgl/fxsxsc', methods=['GET'])
def fxsxsc():
    return render_template("Zhfxgl/fxsxgl/fxsxsc.html")
	
# 风险事项上传-新增
@app.route('/Zhfxgl/fxsxgl/new_fxsxsc', methods=['GET'])
def new_fxsxsc():
    return render_template("Zhfxgl/fxsxgl/new_fxsxsc.html")	
	
# 风险事项上传-新增
@app.route('/Zhfxgl/fxsxgl/edit_fxsxsc', methods=['GET'])
def edit_fxsxsc():
    return render_template("Zhfxgl/fxsxgl/edit_fxsxsc.html")	
	
# 存量风险客户维护
@app.route('/Zhfxgl/fxsxgl/clfxkhwh', methods=['GET'])
def clfxkhwh():
    return render_template("Zhfxgl/fxsxgl/clfxkhwh.html")	
	
# 风险信息管理
@app.route('/Zhfxgl/fxsxgl/fxxxgl', methods=['GET'])
def fxxxgl():
    return render_template("Zhfxgl/fxsxgl/fxxxgl.html")
	
# 风险事项审批
@app.route('/Zhfxgl/fxsxgl/fxsxsp', methods=['GET'])
def fxsxsp():
    return render_template("Zhfxgl/fxsxgl/fxsxsp.html")
	
# 风险事项通过
@app.route('/Zhfxgl/fxsxgl/fxsxtg', methods=['GET'])
def fxsxtg():
    return render_template("Zhfxgl/fxsxgl/fxsxtg.html")
	
######################高风险名单管理#####################	
# 提交风险名单
@app.route('/Zhfxgl/gfxmdgl/tjfxmd', methods=['GET'])
def tjfxmd():
    return render_template("Zhfxgl/gfxmdgl/tjfxmd.html") 
	
# 风险名单审批维护
@app.route('/Zhfxgl/gfxmdgl/fxmdspwh', methods=['GET'])
def fxmdspwh():
    return render_template("Zhfxgl/gfxmdgl/fxmdspwh.html") 
	
# 银联黑名单
@app.route('/Zhfxgl/gfxmdgl/ylhmd', methods=['GET'])
def ylhmd():
    return render_template("Zhfxgl/gfxmdgl/ylhmd.html")	
	
# 内部高风险名单
@app.route('/Zhfxgl/gfxmdgl/nbgfxmd', methods=['GET'])
def nbgfxmd():
    return render_template("Zhfxgl/gfxmdgl/nbgfxmd.html")	
	
# 自定义分析规则
@app.route('/Zhfxgl/gfxmdgl/zdyfxgz', methods=['GET'])
def zdyfxgz():
    return render_template("Zhfxgl/gfxmdgl/zdyfxgz.html")
	
# 自定义分析规则-新增
@app.route('/Zhfxgl/gfxmdgl/new_zdyfxgz', methods=['GET'])
def new_zdyfxgz():
    return render_template("Zhfxgl/gfxmdgl/new_zdyfxgz.html")	
	
# 自定义分析规则-编辑
@app.route('/Zhfxgl/gfxmdgl/edit_zdyfxgz', methods=['GET'])
def edit_zdyfxgz():
    return render_template("Zhfxgl/gfxmdgl/edit_zdyfxgz.html")	
	
# 风险交易查询
@app.route('/Zhfxgl/gfxmdgl/fxjycx', methods=['GET'])
def fxjycx():
    return render_template("Zhfxgl/gfxmdgl/fxjycx.html")
	
# 风险交易维护计划
@app.route('/Zhfxgl/gfxmdgl/fxjywhjh', methods=['GET'])
def fxjywhjh():
    return render_template("Zhfxgl/gfxmdgl/fxjywhjh.html")
	
# 风险交易维护计划-新增
@app.route('/Zhfxgl/gfxmdgl/new_fxjywhjh', methods=['GET'])
def new_fxjywhjh():
    return render_template("Zhfxgl/gfxmdgl/new_fxjywhjh.html")
	
# 风险交易维护计划-编辑
@app.route('/Zhfxgl/gfxmdgl/edit_fxjywhjh', methods=['GET'])
def edit_fxjywhjh():
    return render_template("Zhfxgl/gfxmdgl/edit_fxjywhjh.html")
	
# 风险交易维护台账
@app.route('/Zhfxgl/gfxmdgl/fxjywhtz', methods=['GET'])
def fxjywhtz():
    return render_template("Zhfxgl/gfxmdgl/fxjywhtz.html")
	
# 风险交易维护台账信息
@app.route('/Zhfxgl/gfxmdgl/fxjywhtzxx', methods=['GET'])
def fxjywhtzxx():
    return render_template("Zhfxgl/gfxmdgl/fxjywhtzxx.html")
######################不良资产管理#####################	
# 核销流程管理
@app.route('/Zhfxgl/blzcgl/hxlcgl', methods=['GET'])
def hxlcgl():
    return render_template("Zhfxgl/blzcgl/hxlcgl.html")
	
# 不良资产核销发起
@app.route('/Zhfxgl/blzcgl/blzchxfq', methods=['GET'])
def blzchxfq():
    return render_template("Zhfxgl/blzcgl/blzchxfq.html")
	
# 不良资产核销信息
@app.route('/Zhfxgl/blzcgl/blzchxxx', methods=['GET'])
def blzchxxx():
    return render_template("Zhfxgl/blzcgl/blzchxxx.html")
	
# 不良资产核销规则维护
@app.route('/Zhfxgl/blzcgl/blzchxgzwh', methods=['GET'])
def blzchxgzwh():
    return render_template("Zhfxgl/blzcgl/blzchxgzwh.html")
	
# 自定义分析规则
@app.route('/Zhfxgl/blzcgl/zdyfxgz', methods=['GET'])
def zdyfxgz2():
    return render_template("Zhfxgl/blzcgl/zdyfxgz.html")
	
# 不良资产管理
@app.route('/Zhfxgl/blzcgl/blzcgl', methods=['GET'])
def blzcgl():
    return render_template("Zhfxgl/blzcgl/blzcgl.html")	
	
	

###############################产品管理##########################################	
######################产品属性管理#####################	
# 产品属性
#@app.route('/Cpgl/cpsxgl/cpsx', methods=['GET'])
#def cpsx():
    #return render_template("Cpgl/cpsxgl/cpsx.html")	
	
# 产品属性——产品类别
#@app.route('/Cpgl/cpsxgl/cpsx_cplb', methods=['GET'])
#def cpsx_cplb():
 #   return render_template("Cpgl/cpsxgl/cpsx_cplb.html")	
	
# 产品属性——产品性质
#@app.route('/Cpgl/cpsxgl/cpsx_cpxz', methods=['GET'])
#def cpsx_cpxz():
 #   return render_template("Cpgl/cpsxgl/cpsx_cpxz.html")
	
# 产品列表
@app.route('/Cpgl/cpsxgl/cplb', methods=['GET'])
def cplb():
    return render_template("Cpgl/cpsxgl/cplb.html")
	
# 产品类别——新增
@app.route('/Cpgl/cpsxgl/new_cplb', methods=['GET'])
def new_cplb():
    return render_template("Cpgl/cpsxgl/new_cplb.html")	
	
# 产品类别—编辑
@app.route('/Cpgl/cpsxgl/edit_cplb', methods=['GET'])
def edit_cplb():
    return render_template("Cpgl/cpsxgl/edit_cplb.html")
	
# 产品发布
@app.route('/Cpgl/cpsxgl/cpfb', methods=['GET'])
def cpfb():
    return render_template("Cpgl/cpsxgl/cpfb.html")
	
# 产品类别——新增
@app.route('/Cpgl/cpsxgl/new_cpfb', methods=['GET'])
def new_cpfb():
    return render_template("Cpgl/cpsxgl/new_cpfb.html")	
	
# 产品类别——编辑
@app.route('/Cpgl/cpsxgl/edit_cpfb', methods=['GET'])
def edit_cpfb():
    return render_template("Cpgl/cpsxgl/edit_cpfb.html")	
	
	

###############################系统管理##########################################		
# 评估规则维护
@app.route('/Xtgl/pggzwh', methods=['GET'])
def pggzwh():
    return render_template("Xtgl/pggzwh.html")		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

