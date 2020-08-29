import re
f = open('report.txt', 'r', encoding='UTF-8')
lines = f.readlines()
ssns = list()
addrs = list()

ssn_front_re_list = list()

years = ['[9][8]', '[9][9]', '[0][1]']
for year in years:
    for month in range(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            regex = ('[%d][%d]'%((month//10),(month%10))) + '([0-2][0-9]|[3][0-1])'
            ssn_front_re_list.append(year+regex)
        elif month == 2:
            regex = '[0][2]' + '([0-1][0-9]|[2][0-8])'
            ssn_front_re_list.append(year + regex)
        else:
            regex = ('[%d][%d]'%((month//10),(month%10))) + '([0-2][0-9]|[3][0])'
            ssn_front_re_list.append(year + regex)

leap_year = '[0][0]'
for month in range(1, 13):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        regex = ('[%d][%d]'%((month//10),(month%10))) + '([0-2][0-9]|[3][0-1])'
        ssn_front_re_list.append(leap_year+regex)
    elif month == 2:
        regex = '[0][2]' + '[0-2][0-9]'
        ssn_front_re_list.append(leap_year + regex)
    else:
        regex = ('[%d][%d]'%((month//10),(month%10))) + '([0-2][0-9]|[3][0])'
        ssn_front_re_list.append(leap_year + regex)

ssn_back_re = '[1-4][0-9]{6}'

ssn_re_list = list()
for ssn_front_re in ssn_front_re_list:
    ssn_re_list.append(ssn_front_re + '[-]' + ssn_back_re)

email_address_re = ['[a-zA-Z0-9]+[@][a-zA-Z]+[.][a][c][.][k][r]']
re_list = ssn_re_list + email_address_re


ssn_sum = 0
ea_sum = 0
modify = list()
for line in lines:
    words = re.split('\s', line)
    for word in words:
        w = ' '+word+' '
        for detect in re_list:
            r = re.compile('\s%s\s'%(detect))
            m = bool(r.match(w))
            if m == True:
                if detect == email_address_re[0]:
                    modify.append(re.sub('[@][a-zA-Z]+', '@XXXX', word))
                    ea_sum = ea_sum + 1
                else:
                    temp = list(word)
                    modify.append(re.sub('[-]\d{1}[0-9]{6}', '-%dXXXXXX' % (int(temp[7])), word))
                    ssn_sum = ssn_sum + 1


pn_sum = 0
cr_sum = 0
for line in lines:
    words = re.split('\s', line)
    for word in words:
        w = ' '+word+' '
        phone_num = re.compile('\s[0][1][0][-]\d{4}[-]\d{4}\s')
        credit_num = re.compile('\s\d{4}[-]\d{4}[-]\d{4}[-]\d{4}\s')
        p = bool(phone_num.match(w))
        c = bool(credit_num.match(w))
        if p == True:
            pn_sum = pn_sum + 1
        elif c == True:
            cr_sum = cr_sum + 1

print("-------------------------")
print(ssn_sum)
print(ea_sum)
print("-------------------------")
print("-------------------------")
for i in range(len(modify)):
    print(modify[i])
print("-------------------------")
print("-------------------------")
print(pn_sum)
print(cr_sum)
print("-------------------------")













