#!/bin/python3 
#
# Generate a JWT Token with a secret and a csv value

import jwt, argparse, datetime

parser = argparse.ArgumentParser(description="Generate JWT token with secret, expiration, and csv values")
parser.add_argument('secret', help="The verification signature")
parser.add_argument('data', help="Data within the payload of the Token. CSV format Ex: username=user,password=pass (if emtpy string leave empty ex username=,password=pass)")
parser.add_argument('-e', '--expire', '--e', help="Expire time. Format: mon/day/year 24hour:min:sec - 10/10/2021 18:36:00", default="")
args = parser.parse_args()

def csvToJson(data, exp=""):
    output = {}
    for x in data.split(","):
        output[ x.split('=')[0] ] = x.split('=')[1]
    if exp!="":
        try:
            output['exp'] = datetime.datetime.strptime(exp, "%m/%d/%Y %H:%M:%S")
        except:
            print( "[!] [Error] :: Something is wrong with the expiry time..." )
            exit()
    return output

encoded_jwt = jwt.encode( csvToJson(args.data, args.expire), args.secret, algorithm="HS256")
print( "[+] [Token] :: {}".format( encoded_jwt ) )
