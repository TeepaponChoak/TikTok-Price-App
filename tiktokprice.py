import csv

tiktok_charge = 0.06
payment_charge = 0.02
commission = 0.02

List = str(input("รายการ : "))
sell_price = float(input("ราคาขาย : "))
cost_price = float(input("ต้นทุน : "))

result_tc = sell_price - (sell_price * tiktok_charge)
result_pc = result_tc - (result_tc * payment_charge)
result_com = sell_price * commission
result_profit = result_pc - result_com - cost_price
result_profit_percent = (result_profit / cost_price) * 100

print("ค่าธรรมเนียม TikTok : " + str(f'{result_tc:.2f}') + " บาท")
print("ค่าธรรมเนียมชำระเงิน : " + str(f'{result_pc:.2f}') + " บาท")
print("คอมฯจ่าย : " + str(f'{result_com:.2f}') + " บาท")
print("กำไร : " + str(f'{result_profit:.2f}') + " บาท")
print("กำไร% : " + str(f'{result_profit_percent:.2f}') + "%")