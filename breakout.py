import zrd_login
from pprint import pprint
import time
kite = zrd_login.kite
import pdb
import support_file as sp
import xlwings as xw
import datetime
import pandas as pd

def init():
	global watchlist_fno , zrd_watchlist,temp,wb,status,sht,capital_per_trade,start_time,end_time

	watchlist_fno = ['AARTIIND','ABB','ABBOTINDIA','ABCAPITAL','ABFRL','ACC','ADANIENT','ADANIPORTS','ALKEM','AMARAJABAT','AMBUJACEM','APOLLOHOSP','APOLLOTYRE','ASHOKLEY','ASIANPAINT','ASTRAL','ATUL','AUBANK','AUROPHARMA','AXISBANK','BAJAJ-AUTO','BAJAJFINSV','BAJFINANCE','BALKRISIND','BALRAMCHIN','BANDHANBNK','BANKBARODA','BATAINDIA','BEL','BERGEPAINT','BHARATFORG','BHARTIARTL','BHEL','BIOCON','BOSCHLTD','BPCL','BRITANNIA','BSOFT','CANBK','CANFINHOME','CHAMBLFERT','CHOLAFIN','CIPLA','COALINDIA','COFORGE','COLPAL','CONCOR','COROMANDEL','CROMPTON','CUB','CUMMINSIND','DABUR','DALBHARAT','DEEPAKNTR','DELTACORP','DIVISLAB','DIXON','DLF','DRREDDY','EICHERMOT','ESCORTS','EXIDEIND','FEDERALBNK','FSL','GAIL','GLENMARK','GMRINFRA','GNFC','GODREJCP','GODREJPROP','GRANULES','GRASIM','GUJGASLTD','HAL','HAVELLS','HCLTECH','HDFC','HDFCAMC','HDFCBANK','HDFCLIFE','HEROMOTOCO','HINDALCO','HINDCOPPER','HINDPETRO','HINDUNILVR','HONAUT','IBULHSGFIN','ICICIBANK','ICICIGI','ICICIPRULI','IDEA','IDFC','IDFCFIRSTB','IEX','IGL','INDHOTEL','INDIACEM','INDIAMART','INDIGO','INDUSINDBK','INDUSTOWER','INFY','INTELLECT','IOC','IPCALAB','IRCTC','ITC','JINDALSTEL','JKCEMENT','JSWSTEEL','JUBLFOOD','KOTAKBANK','L&TFH','LALPATHLAB','LAURUSLABS','LICHSGFIN','LT','LTI','LTTS','LUPIN','M&M','M&MFIN','MANAPPURAM','MARICO','MARUTI','MCDOWELL-N','MCX','METROPOLIS','MFSL','MGL','MOTHERSON','MPHASIS','MRF','MUTHOOTFIN','NATIONALUM','NAUKRI','NAVINFLUOR','NESTLEIND','NMDC','NTPC','OBEROIRLTY','OFSS','ONGC','PAGEIND','PEL','PERSISTENT','PETRONET','PFC','PIDILITIND','PIIND','PNB','POLYCAB','POWERGRID','PVR','RAIN','RAMCOCEM','RBLBANK','RECLTD','RELIANCE','SAIL','SBICARD','SBILIFE','SBIN','SHREECEM','SIEMENS','SRF','SRTRANSFIN','SUNPHARMA','SUNTV','SYNGENE','TATACHEM','TATACOMM','TATACONSUM','TATAMOTORS','TATAPOWER','TATASTEEL','TCS','TECHM','TITAN','TORNTPHARM','TORNTPOWER','TRENT','TVSMOTOR','UBL','ULTRACEMCO','UPL','VEDL','VOLTAS','WHIRLPOOL','WIPRO','ZEEL','ZYDUSLIFE']
	zrd_watchlist = []
	temp = {'Name' : None,'ctime' : None,'Sell_price': None,'Buy_price': None, 'LTP': None,'Entry_time' : None,'Target' : None,'Stoploss' : None,'PNL' : None,'Remark' : None,'Remark_2' : None,'Traded' : None}
	status = {}

	for name in watchlist_fno:
		status[name] = temp.copy()

	for name in watchlist_fno:
		zrd_watchlist.append('NSE:' + name)


	wb = xw.Book('live_status_orb.xlsx')
	sht = wb.sheets['console']

	capital_per_trade = 20000

	start_time = datetime.time(9,25)
	end_time = datetime.time(15,15)








init()


while True:

	ctime = datetime.datetime.now().time()

	data = kite.ohlc(zrd_watchlist)

	sht.range('A1').value = pd.DataFrame(status).T


	for name in watchlist_fno:
		openn = data['NSE:'+ name]['ohlc']['open']
		High = data['NSE:'+ name]['ohlc']['high']
		Low = data['NSE:'+ name]['ohlc']['low']


		if ctime > start_time

		pdb.set_trace()

# while True:




# 	data = kite.ltp(zrd_watchlist)


# for name in watchlist_fno:
# 	zrd_name = 'NSE:'+name


# 	# trd = data['NSE:' + name]['last_price']
# 	pdb.set_trace()
# 	ltp,openn,high,low,close,volume  = sp.l_ohlc_v(name)

# 	if openn == high:
# 		print(name , openn , high ,ltp)
# 		print('this is open equals to high' )

# 		# pdb.set_trace()

# 	if openn == low:
# 		print(name, openn , low ,ltp)
# 		print('this is open equals to low' )




# 	# print(name , price)
# 	# pdb.set_trace()

# 	# time.sleep(0.5)

