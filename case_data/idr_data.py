data = (100119, 2023, "IDR", 10000, "97fa79f073c7c5e3c97b00b50b156eaa")

pay_channels = (1,3, 4, 5, 6, 8, 9, 12, 15, 16, 17, 18, 19, 38)
xendit = (1,2)
oy = list(pay_channels[1:-1])
faspay =  list(pay_channels[1:-1])
print(xendit)
xendit1_data = [
    {

            'merchantId': str(data[0]),
            'productId': str(data[1]),
            'currency': data[2],
            'amount': str(data[3]),
            'payerPhone':  "0888888881",
            'payChannel': str(channel),
            'privateKey': data[4]

    } for channel in xendit
]
print(xendit1_data)
xendit2_data = [
    {
        'data': {
            'merchantId': str(data[0]),
            'productId': str(data[1]),
            'currency': data[2],
            'amount': str(data[3]),
            'payerPhone':  "0888888885",
            'payChannel': str(channel),
            'privateKey': data[4]
        },
        'result': 'success'
    } for channel in list(pay_channels[1:-1])
]
