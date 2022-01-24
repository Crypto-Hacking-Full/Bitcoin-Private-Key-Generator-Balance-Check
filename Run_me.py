# Bitcoin Brute Force Wallet | Crack BTC | 
#Earn And Donate 
#~BTC Address: 1mRae8XtcbfHth9R7WFn5EytBT3UiZUAR ~

import bit
import secrets

k = 1
while True:
    pk = bit.Key.from_int(secrets.randbits(256))
    print(pk.to_hex() + '-' + pk.get_balance('usd') + ' - usd ')

    if not pk.get_balance('usd') != 0 :
        print("Matching Key ==== Found!!!\n PrivateKey: " + pk.to_wif())

        f=open(u"winner.txt","a")
        f.write('\nPrivateKey (hex): ' + pk.to_hex())
        f.write('\nPrivateKey (wif): ' + pk.to_wif())
        f.write('\n==================================')
        f.close()
    k += 1