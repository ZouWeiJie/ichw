def exchange(currency_from,currency_to,amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    import json
    
    from urllib.request import urlopen
    
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.format(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    dic = json.loads(jstr)
    
    suc1='{success}'.format(**dic)
    to1='{to}'.format(**dic)
    error1='{error}'.format(**dic)
    if suc1=='True': 
        to2=to1.split(' ')
        re=float(to2[0])
        return re
    else:

        return error1

def test_currency_from():
    """verify that the exchange currency code is valid  """
    assert(9.182905 == exchange('USD','AED',2.5))
    assert(10.633666794431== exchange('EUR','AED',2.5))
    assert('Exchange currency code is invalid.' == exchange('AED','wrong',2.5))

def test_currency_to(): 
    """verify that the source currecy code is valid"""
    assert('Source currency code is invalid.'==exchange('wrong','AED',2.5))
    
def test_amount_from():
    """verify that the currency amount is valid"""
    assert('Currency amount is invalid.'==exchange('USD','AED','wrong'))

def testAll():
    """test all cases"""
    
    test_currency_from()
    test_currency_to()
    test_amount_from()
    print("All tests passed")

testAll()
