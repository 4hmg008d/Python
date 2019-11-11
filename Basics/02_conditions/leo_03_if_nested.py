has_ticket = True
knife_length = 20

if has_ticket:
    print('Has ticket, go to safety check...')

    if knife_length <= 20:
        print("Passed safety check, have a pleasant trip!")
    else:
        print('Your knife is %dcm, which is too long to be carried' % knife_length)

else:
    print('Please buy a ticket first!')
